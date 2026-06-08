
import torch
import torch.nn as nn
import torch.optim as optim


torch.manual_seed(42)

X = torch.randn(100, 4)

y = ((X[:, 0] + X[:, 1]) > 0).float().view(-1, 1)



class TwoLayerNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(4, 8),   
            nn.ReLU(),

            nn.Linear(8, 1),  
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)

model = TwoLayerNN()

print("\nModel Architecture:\n")
print(model)

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 100

print("\nTraining Started...\n")

for epoch in range(epochs):

    predictions = model(X)

    loss = criterion(predictions, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}]  Loss: {loss.item():.4f}")


with torch.no_grad():
    final_preds = model(X)

    predicted_classes = (final_preds > 0.5).float()


accuracy = (predicted_classes == y).float().mean()

print(f"\nAccuracy: {accuracy.item() * 100:.2f}%")