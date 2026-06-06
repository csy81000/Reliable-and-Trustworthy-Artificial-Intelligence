
import torch
import torch.nn as nn

class AssignmentModel(nn.Module):
    def __init__(self):
        super(AssignmentModel, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 32)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(32, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
