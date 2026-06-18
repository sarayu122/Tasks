/* ──────────────────────────────────────────────
   Text Chunker — mimics RecursiveCharacterTextSplitter
   ────────────────────────────────────────────── */
function splitIntoChunks(text, chunkSize = 500, overlap = 50) {
  if (!text || !text.trim()) return [];

  const separators = ["\n\n", "\n", ". ", " ", ""];

  function recursiveSplit(str, seps) {
    if (str.length <= chunkSize) return [str];

    const sep = seps[0];
    const remaining = seps.slice(1);
    const parts = sep === "" ? [...str] : str.split(sep);

    const chunks = [];
    let current = "";

    for (const part of parts) {
      const addition = current ? sep + part : part;
      if ((current + addition).length > chunkSize && current.length > 0) {
        chunks.push(current.trim());
        const overlapText = current.slice(-overlap);
        current = overlapText + (sep ? sep : "") + part;
      } else {
        current = current ? current + sep + part : part;
      }
    }

    if (current.trim()) chunks.push(current.trim());

    if (remaining.length > 0) {
      return chunks.flatMap(c => c.length > chunkSize ? recursiveSplit(c, remaining) : [c]);
    }
    return chunks;
  }

  return recursiveSplit(text, separators).filter(c => c.trim().length > 0);
}

function findRelevantChunks(query, chunks, k = 3) {
  const terms = query.toLowerCase().split(/\s+/).filter(t => t.length > 2);
  const scored = chunks.map((chunk, i) => {
    const lower = chunk.toLowerCase();
    let score = 0;
    for (const term of terms) {
      const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const matches = lower.match(new RegExp(escaped, 'gi'));
      if (matches) score += matches.length;
      if (lower.includes(term)) score += 0.5;
    }
    return { chunk, i, score: terms.length ? score / terms.length : 0 };
  });
  return scored.sort((a, b) => b.score - a.score).slice(0, k).map(s => s.chunk);
}

/* ──────────────────────────────────────────────
   LLM call — uses OpenRouter-compatible endpoint
   Replace API_KEY with your own key
   ─────────────────────────────────────────────── */
const API_KEY = "YOUR_OPENROUTER_API_KEY";  // ← replace this
const LLM_URL = "https://openrouter.ai/api/v1/chat/completions";
const MODEL = "openai/gpt-oss-120b:free";

async function askLLM(prompt) {
  const res = await fetch("/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  const json = await res.json();
  return json.answer;
}

/* ──────────────────────────────────────────────
   App State
   ────────────────────────────────────────────── */
let knowledgeBase = null;
const messages = [];

let chatHistory =
    JSON.parse(localStorage.getItem("chatHistory")) || [];

let currentChatId = null;
const historyList =
    document.getElementById("history-list");


/* ──────────────────────────────────────────────
   Chat History Functions
   ────────────────────────────────────────────── */

function saveHistory() {
    localStorage.setItem(
        "chatHistory",
        JSON.stringify(chatHistory)
    );
}

function renderHistory() {

    const historyList =
        document.getElementById("history-list");

    if (!historyList) return;

    historyList.innerHTML = "";

    chatHistory.forEach(chat => {

        const item =
            document.createElement("div");

        item.className = "history-item";

        item.innerHTML = `
            <span>${chat.title}</span>
            <button class="delete-chat-btn"
                    onclick="deleteChat(${chat.id})">
                🗑
            </button>
        `;

        item.addEventListener("click", () => {
            loadChat(chat.id);
        });

        historyList.appendChild(item);
    });
}

function loadChat(id) {

    const chat =
        chatHistory.find(c => c.id === id);

    if (!chat) return;

    currentChatId = id;

    messages.length = 0;

    chat.messages.forEach(m => {
        messages.push(m);
    });

    renderMessages();
}

function deleteChat(id) {

    chatHistory =
        chatHistory.filter(c => c.id !== id);

    saveHistory();

    renderHistory();
}

window.deleteChat = deleteChat;

/* ──────────────────────────────────────────────
   Page 1 — Input
   ────────────────────────────────────────────── */
const pageInput = document.getElementById("page-input");
const pageChat  = document.getElementById("page-chat");
const textarea  = document.getElementById("kb-text");
const clearTextBtn = document.getElementById("clear-text-btn");
const titleInput = document.getElementById("kb-title");
const analyzeBtn = document.getElementById("analyze-btn");
const statWords  = document.getElementById("stat-words");
const statChars  = document.getElementById("stat-chars");
const chunkDot   = document.getElementById("chunk-dot");
const chunkBadge = document.getElementById("chunk-badge");
const chunkCount = document.getElementById("chunk-count");
const btnText    = document.getElementById("btn-text");
const btnIcon    = document.getElementById("btn-icon");
const btnSpinner = document.getElementById("btn-spinner");

function updateStats() {
  const text = textarea.value;
  const words = text.trim() ? text.trim().split(/\s+/).length : 0;
  statWords.textContent = `${words.toLocaleString()} words`;
  statChars.textContent = `${text.length.toLocaleString()} characters`;
  analyzeBtn.disabled = !text.trim();
}

textarea.addEventListener("input", updateStats);
titleInput.addEventListener("input", updateStats);
clearTextBtn.addEventListener("click", () => {
  textarea.value = "";
  updateStats();
});

/* ── Analyze button ── */
analyzeBtn.addEventListener("click", () => {
  const text = textarea.value.trim();
  if (!text) return;

  messages.length = 0;

  // Show loading
  btnText.style.display = "none";
  btnIcon.style.display = "none";
  btnSpinner.style.display = "block";
  analyzeBtn.disabled = true;

  const chunks = splitIntoChunks(text, 500, 50);
  knowledgeBase = {
    title: titleInput.value.trim() || "Untitled Knowledge Base",
    text,
    chunks,
  };
  currentChatId = Date.now();

chatHistory.push({
    id: currentChatId,
    title: knowledgeBase.title,
    messages: []
});

saveHistory();
renderHistory();

  // Show chunk count
  chunkDot.style.display = "inline";
  chunkBadge.style.display = "inline-flex";
  chunkCount.textContent = chunks.length;

  // Navigate after a brief moment to show chunks
  setTimeout(() => navigateToChat(), 500);
});

/* ──────────────────────────────────────────────
   Page 2 — Chat / Q&A
   ────────────────────────────────────────────── */
const chatArea        = document.getElementById("chat-area");
const chatInner       = document.getElementById("chat-inner");
const messagesEl      = document.getElementById("messages");
const welcomeScreen   = document.getElementById("welcome-screen");
const questionInput   = document.getElementById("question-input");
const sendBtn         = document.getElementById("send-btn");
const chatTitle       = document.getElementById("chat-title");
const chatMeta        = document.getElementById("chat-meta");
const backBtn         = document.getElementById("back-btn");
const clearChatBtn    = document.getElementById("clear-chat-btn");

function navigateToChat() {
  pageInput.style.display = "none";
  pageChat.style.display = "block";
  chatTitle.textContent = knowledgeBase.title;
  chatMeta.innerHTML = `📄 ${knowledgeBase.chunks.length} chunks`;
  welcomeScreen.style.display = messages.length === 0 ? "block" : "none";
  messagesEl.style.display = messages.length === 0 ? "none" : "flex";
  questionInput.focus();

  // Reset analyze button
  btnText.style.display = "inline";
  btnIcon.style.display = "inline";
  btnSpinner.style.display = "none";
  analyzeBtn.disabled = false;
}

backBtn.addEventListener("click", () => {
  pageChat.style.display = "none";
  pageInput.style.display = "block";
});

function scrollToBottom() {
  chatArea.scrollTop = chatArea.scrollHeight;
}

function renderMessages() {
  messagesEl.innerHTML = messages.map((m, i) => {
    const isUser = m.role === "user";
    const cls = isUser ? "msg user" : "msg assistant";
    const avatar = isUser ? "👤" : "✨";
    const escaped = m.content
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\n/g, "<br>");
    return `<div class="${cls}">
      <div class="msg-avatar">${avatar}</div>
      <div class="msg-bubble">${escaped}</div>
    </div>`;
  }).join("");
}

function addMessage(role, content) {

  messages.push({ role, content });

  if (currentChatId) {

    const chat =
      chatHistory.find(
        c => c.id === currentChatId
      );

    if (chat) {

      chat.messages = [...messages];

      saveHistory();
    }
  }

  welcomeScreen.style.display = "none";
  messagesEl.style.display = "flex";

  renderMessages();

  scrollToBottom();
}

function addTypingBubble() {
  const div = document.createElement("div");
  div.className = "msg assistant";
  div.id = "typing-msg";
  div.innerHTML = `<div class="msg-avatar">✨</div>
    <div class="msg-bubble typing"><div class="typing-dots"><span></span><span></span><span></span></div></div>`;
  messagesEl.appendChild(div);
  scrollToBottom();
}

function removeTypingBubble() {
  const el = document.getElementById("typing-msg");
  if (el) el.remove();
}

/* ── Ask question ── */
async function askQuestion(q) {
  if (!q.trim() || !knowledgeBase) return;

  addMessage("user", q);
  questionInput.value = "";
  sendBtn.disabled = true;
  addTypingBubble();

  const relevant = findRelevantChunks(q, knowledgeBase.chunks, 3);
  const context = relevant.join("\n\n");

  const prompt = `Answer the question only from the provided context. If the answer is not in the context, say "I couldn't find relevant information in the provided text."

Context:
${context}

Question:
${q}

Answer:`;

  let answer;
  try {
    answer = await askLLM(prompt);
  } catch {
    answer = "Sorry, there was an error calling the AI. Check your API key and try again.";
  }

  removeTypingBubble();
  addMessage("assistant", answer);
  sendBtn.disabled = false;
  questionInput.focus();
}

sendBtn.addEventListener("click", () => askQuestion(questionInput.value));
questionInput.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    askQuestion(questionInput.value);
  }
});

/* ── Hint chips ── */
document.querySelectorAll(".hint-chip").forEach(chip => {
  chip.addEventListener("click", () => {
    questionInput.value = chip.dataset.question;
    sendBtn.disabled = false;
    questionInput.focus();
  });
});

/* ── Clear chat ── */
clearChatBtn.addEventListener("click", () => {

  messages.length = 0;

  const currentChat =
      chatHistory.find(
          c => c.id === currentChatId
      );

  if (currentChat) {
      currentChat.messages = [];
  }

  saveHistory();

  welcomeScreen.style.display = "block";

  messagesEl.style.display = "none";

  messagesEl.innerHTML = "";
});

/* ── Question input enable ── */
questionInput.addEventListener("input", () => {
  sendBtn.disabled = !questionInput.value.trim();
});
renderHistory();
updateStats();