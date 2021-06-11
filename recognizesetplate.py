import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread('03.jpeg')
    img = cv2.resize(img,(1000,500))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    '''
    引數必須是正奇數
    '''
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
    regions = []
    contours, hierarchy = cv2.findContours(dilation2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    '''
    找輪廓
    '''
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area < 1800):
            continue
        rect = cv2.minAreaRect(contour)
        '''
        boxPoints() 回傳四個座標的順序：右下→左下→左上→右上
        '''
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        ratio =float(width) / float(height)
        if (ratio < 5 and ratio > 1.8):
            regions.append(box)
    for box in regions:
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
    cv2.imshow('output', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
