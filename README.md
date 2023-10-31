# Here is an example for Convolution Layer. 
## Have fun with it!
You can either clone the code or download the code by zip format.   
Clone the code with the command below: (remember to install git first)
```
git clone git@github.com:starrain3/ladder_program_design.git
```
Install the python package using the command :
```
pip install -r requirements.txt
```
Run the code with the command below:
```
python Conv.py
```

## You can change the filter while initializing a new Conv3*3 Object.
Like this:  
```
sobel_filter_vertical = [[ 1,  2,  1],
                         [ 0,  0,  0],
                         [-1, -2, -1]]
my_conv_layer = Conv3x3(sobel_filter_vertical)
```
And doing convolution operation with the conv Obj:
```
img = cv2.imread("./python.png", cv2.IMREAD_GRAYSCALE)
output = my_conv_layer(img)
```
Feel free to change the picture by modifying the path:
```
img = cv2.imread("/the/path/to/your/pic", cv2.IMREAD_GRAYSCALE)
output = my_conv_layer(img)
```
## Remember to read the image in GRAYSCALE mode

