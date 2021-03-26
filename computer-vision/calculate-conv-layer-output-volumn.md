# Calculate Convolutional Layer Output Volume

Hyperparameters:
* Number of filters: K
* Filter size: F
* Stride number: S
* Amount of zero padding: P

Given input image width W and height H:

```
output_width = (W - F + 2P) / S + 1
output_height = (H - F + 2P) / S + 1
output_volume = output_width * output_height * K
```
