import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torch import FloatTensor
from torch.utils.data import DataLoader
from torchvision import transforms

from data_load import FacialKeypointsDataset, Rescale, RandomCrop, Normalize, ToTensor
from models import Net

net = Net()
print(net)

criterion = nn.SmoothL1Loss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

""" Load data """
# define the data transform
data_transform = transforms.Compose([Rescale(250),
                                     RandomCrop(224),
                                     Normalize(),
                                     ToTensor()])

# create the transformed dataset
transformed_dataset = FacialKeypointsDataset(csv_file='data/training_frames_keypoints.csv',
                                             root_dir='data/training/',
                                             transform=data_transform)

# load training data in batches
batch_size = 50
train_loader = DataLoader(transformed_dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)


def train_net(n_epochs):
    # prepare the net for training
    net.train()
    loss_over_time = []

    for epoch in range(n_epochs):  # loop over the dataset multiple times

        running_loss = 0.0

        # train on batches of data, assumes you already have train_loader
        for batch_i, data in enumerate(train_loader):
            # get the input images and their corresponding labels
            images = data['image']
            key_pts = data['keypoints']

            # flatten pts
            key_pts = key_pts.view(key_pts.size(0), -1)

            # convert variables to floats for regression loss
            key_pts = key_pts.type(FloatTensor)
            images = images.type(FloatTensor)

            # forward pass to get outputs
            output_pts = net(images)

            # calculate the loss between predicted and target keypoints
            loss = criterion(output_pts, key_pts)

            # zero the parameter (weight) gradients
            optimizer.zero_grad()

            # backward pass to calculate the weight gradients
            loss.backward()

            # update the weights
            optimizer.step()

            # print loss statistics
            # to convert loss into a scalar and add it to the running_loss, use .item()
            running_loss += loss.item()
            if batch_i % 10 == 9:  # print every 10 batches
                print('Epoch: {}, Batch: {}, Avg. Loss: {}'.format(epoch + 1, batch_i + 1, running_loss / 10))
                loss_over_time.append(running_loss / 10)
                running_loss = 0.0

    print('Finished Training')
    return loss_over_time


# train
n_epochs = 30

losses = train_net(n_epochs)

plt.figure(figsize=(20, 10))
plt.plot(losses[1:])

# save model
model_dir = 'saved_models/'
model_name = 'keypoints_model.pt'
torch.save(net.state_dict(), model_dir + model_name)
