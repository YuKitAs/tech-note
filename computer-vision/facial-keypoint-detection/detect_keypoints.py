import cv2.cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch.autograd import Variable

from models import Net


def show_keypoints(image, keypoints):
    plt.figure()

    # un-normalize
    keypoints = keypoints.data.numpy()
    keypoints = keypoints * 50.0 + 100
    keypoints = np.reshape(keypoints, (68, -1))

    plt.imshow(image, cmap='gray')
    plt.scatter(keypoints[:, 0], keypoints[:, 1], s=20, marker='.', c='r')


# load in color image for face detection
image = cv2.imread('images/test.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# load in a haar cascade classifier for detecting frontal faces
face_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(image, 1.2, 2)

net = Net()
net.load_state_dict(torch.load('saved_models/keypoints_model.pt'))
net.eval()

image_copy = np.copy(image)

# loop over the detected faces, mark the image where each face is found
for (x, y, w, h) in faces:
    margin = int(w * 0.3)
    roi = image_copy[y - margin:y + h + margin, x - margin:x + w + margin]
    # RGB to grayscale
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
    # normalize
    roi_norm = roi_gray / 255.0
    # rescale
    roi_resize = cv2.resize(roi_norm, (224, 224))
    # reshape
    roi_reshape = roi_resize.reshape(roi_resize.shape[0], roi_resize.shape[1], 1)
    roi_reshape = roi_reshape.transpose((2, 0, 1))
    roi_reshape = np.expand_dims(roi_reshape, 0)
    # to tensor
    roi_torch = Variable(torch.from_numpy(roi_reshape))
    input_image = roi_torch.type(torch.FloatTensor)

    # forward pass to get net output
    output_pts = net(input_image)
    show_keypoints(roi_resize, output_pts)

plt.show()
