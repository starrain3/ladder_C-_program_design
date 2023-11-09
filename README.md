# 這是一個有關卷積的簡單範例
## 希望你們喜歡
你可以選擇透過git clone或是下載zip檔的方式來使用。  
若要使用git clone可以透過在你本機的CMD上輸入下面的程式碼 :
```
git clone git@github.com:starrain3/ladder_program_design.git
```
下載完成後，請先透過requirements.txt來安裝所需之套件，輸入以下指令:    
```
pip install -r requirements.txt
```
安裝完所需套件後可以透過下面的指令來執行本範例:  
```
python Conv.py
```

## 客製化卷積的濾波器(filter/kernel)
你可以在建立Conv物件時，傳入你想要拿來進行卷積運算的濾波器，參考以下程式碼:   
```
sobel_filter_vertical = [[ 1,  2,  1],
                         [ 0,  0,  0],
                         [-1, -2, -1]]
my_conv_layer = Conv3x3(sobel_filter_vertical)
```
讀入圖片後，就可以透過該物件進行卷積運算:  
```
img = cv2.imread("./python.png", cv2.IMREAD_GRAYSCALE)
output = my_conv_layer(img)
```
你可以使用自己的圖片來玩玩看(更改影像讀入路徑):  
```
img = cv2.imread("/the/path/to/your/pic", cv2.IMREAD_GRAYSCALE)
output = my_conv_layer(img)
```
## 記得要用cv2.IMREAD_GRAYSCALE以灰階的形式來讀入圖片
## 覺得有幫助的可以幫我按個Star <3 

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

