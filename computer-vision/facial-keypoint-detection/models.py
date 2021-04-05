import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.pool = nn.MaxPool2d(2, 2)
        self.conv1 = nn.Conv2d(1, 32, 5)  # W = 224 -> (32, 220, 220) -> (32, 110, 110)
        self.conv2 = nn.Conv2d(32, 64, 3)  # W = 110 -> (64, 108, 108) -> (64, 54, 54)
        self.conv3 = nn.Conv2d(64, 128, 2)  # W = 54 -> (128, 53, 53) -> (128, 26, 26)
        self.conv4 = nn.Conv2d(128, 256, 1)  # W = 26 -> (256, 26, 26) -> (256, 13, 13)

        self.fc1 = nn.Linear(256 * 13 * 13, 1024)
        self.fc2 = nn.Linear(1024, 136)

        self.drop1 = nn.Dropout(p=0.1)
        self.drop2 = nn.Dropout(p=0.2)
        self.drop3 = nn.Dropout(p=0.25)
        self.drop4 = nn.Dropout(p=0.3)
        self.drop5 = nn.Dropout(p=0.4)

    def forward(self, x):
        # [conv -> activation -> maxpooling -> dropout] * 4
        x = self.pool(F.relu(self.conv1(x)))
        x = self.drop1(x)
        x = self.pool(F.relu(self.conv2(x)))
        x = self.drop2(x)
        x = self.pool(F.relu(self.conv3(x)))
        x = self.drop3(x)
        x = self.pool(F.relu(self.conv4(x)))
        x = self.drop4(x)

        # flatten
        x = x.view(x.size(0), -1)

        # fully connected -> dropout
        x = F.relu(self.fc1(x))
        x = self.drop5(x)
        x = self.fc2(x)

        return x
