# Adjust Contrast and Brightness

A commonly used expression is:

<p align="center">g(i, j) = α * f(i, j) + β</p>

where `f(i, j)` are the source image pixels and `g(i, j)` are the output image pixels; `i` and `j` indicate the pixel located in the *i-th* row and *j-th* column of the image; `α > 0` is called *gain* parameter and said to control contrast, `β` is called *bias* parameter and said to control brightness.

Use the following codes to perform the operation with an RGB source image:

```cpp
double alpha;
int beta;

for (int y = 0; y < src_img.rows; y++) {
    for (int x = 0; x < src_img.cols; x++) {
        for (int c = 0; c < 3; c++) {
            new_img.at<Vec3b>(y, x)[c] = saturate_cast<uchar>(alpha * (src.at<Vec3b>(y,x)[c]) + beta);
        }
    }
}
```

`saturate_cast` is used to make sure the output values are valid.
