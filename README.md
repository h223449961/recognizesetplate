python 實現識別車牌![image](https://user-images.githubusercontent.com/31395513/121687499-02573500-caf5-11eb-9694-150fa67f18d2.png)

以下是原始引數：

https://blog.csdn.net/qq_41686130/article/details/81229353

第三張照片引數：

![image](https://user-images.githubusercontent.com/31395513/121689413-26b41100-caf7-11eb-8e57-1266d2df28c3.png)

    k = 27
    '''
    以下開始，直到第二次 dilate 膨脹，是型態學處理
    '''
    gaussian = cv2.GaussianBlur(gray, (k,k), 0, 0, cv2.BORDER_DEFAULT)
    median = cv2.medianBlur(gaussian, 13)
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0,ksize=3)
    ret, binary = cv2.threshold(sobel, 22, 252, cv2.THRESH_BINARY)
    '''
    膨脹 size
    '''
    dilatesize = cv2.getStructuringElement(cv2.MORPH_RECT, (5,10))
    '''
    侵蝕 size
    '''
    erodesize = cv2.getStructuringElement(cv2.MORPH_RECT, (3,33))
    '''
    第一次膨脹
    '''
    dilation = cv2.dilate(binary, dilatesize,iterations=13)
    '''
    第一次侵蝕
    '''
    erosion = cv2.erode(dilation, erodesize,iterations=1)
    '''
    第二次膨脹
    '''
    dilation2 = cv2.dilate(erosion, dilatesize,iterations=3)

第十二張照片引數：

![image](https://user-images.githubusercontent.com/31395513/121690421-67f8f080-caf8-11eb-9065-db70a371262d.png)

    k = 3
    '''
    以下開始，直到第二次 dilate 膨脹，是型態學處理
    '''
    gaussian = cv2.GaussianBlur(gray, (k,k), 0, 0, cv2.BORDER_DEFAULT)
    median = cv2.medianBlur(gaussian, 5)
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0,ksize=3)
    ret, binary = cv2.threshold(sobel,170,255,cv2.THRESH_BINARY)
    '''
    膨脹 size
    '''
    dilatesize = cv2.getStructuringElement(cv2.MORPH_RECT, (9,7))
    '''
    侵蝕 size
    '''
    erodesize = cv2.getStructuringElement(cv2.MORPH_RECT, (9,1))
    '''
    第一次膨脹
    '''
    dilation = cv2.dilate(binary, dilatesize,iterations=1)
    '''
    第一次侵蝕
    '''
    erosion = cv2.erode(dilation, erodesize,iterations=1)
    '''
    第二次膨脹
    '''
    dilation2 = cv2.dilate(erosion, dilatesize,iterations=3)
