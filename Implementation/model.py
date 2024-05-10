import torch
import torch.nn as nn


class CrimeRiskNN(nn.Module):
    def __init__(self, input_size, output_size):
        super(CrimeRiskNN, self).__init__()
        self.layer1 = nn.Linear(input_size, 128)
        self.layer2 = nn.Linear(128, 64)
        self.output_layer = nn.Linear(64, output_size)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = self.output_layer(x)
        return x