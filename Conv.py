import numpy as np
import cv2

class Conv3x3:
    # A Convolution layer using 3x3 filters.
 
    def __init__(self, filter):
 
        self.filter =  filter

    def iterate_regions(self, image):
        '''
        Generates all possible 3x3 image regions using valid padding.
        - image is a 2d numpy array
        '''
        h, w = image.shape
 
        for i in range(h - 2):
            for j in range(w - 2):
                im_region = image[i:(i + 3), j:(j + 3)]
                yield im_region, i, j

 
    def forward(self, input):
        '''
        Performs a forward pass of the conv layer using the given input.
        Returns a 3d numpy array with dimensions (h - 2, w - 2).
        - input is a 2d numpy array
        '''
        h, w = input.shape
        output = np.zeros((h - 2, w - 2))
 
        for im_region, i, j in self.iterate_regions(input):
            output[i, j] = np.sum(im_region * self.filter)

        return output
    
    def __call__(self, input) :
        return self.forward(input)


sobel_filter_vertical = [[ 1,  2,  1],
                  [ 0,  0,  0],
                  [-1, -2, -1]]


sobel_filter_horizontal= [[ -1,  0,  1],
                  [ -2,  0,  2],
                  [ -1,  0,  1]]


img = cv2.imread("./python.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", img)

my_conv_layer = Conv3x3(sobel_filter_vertical)
output_1 = my_conv_layer(img)
cv2.imshow("Image After Processing with sobel_filter_vertical", output_1)

my_conv_layer = Conv3x3(sobel_filter_horizontal)
output_2 = my_conv_layer(img)
cv2.imshow("Image After Processing with sobel_filter_horizontal", output_2)

output = (output_1**2 + output_2**2)**(1/2)
cv2.imshow("Image After Processing with sobel_filter ", output)

cv2.waitKey(0)

