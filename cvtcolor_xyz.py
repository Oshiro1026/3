# cvtcolor_xyz.py
import numpy as np
import cv2 as cv

FN_INPUT = 'space-cat.jpg'

# 画像を読み込む
image = cv.imread(FN_INPUT)

# HSV 変換
image_xyz = cv.cvtColor(image, cv.COLOR_BGR2XYZ)    # BGR -> XYZ(CIE 1931 色空間)
image_x = image_xyz[:, :, 0]
image_y = image_xyz[:, :, 1]
image_z = image_xyz[:, :, 2]

cv.imwrite(FN_INPUT + '_x.png', image_x)
cv.imwrite(FN_INPUT + '_y.png', image_y)
cv.imwrite(FN_INPUT + '_z.png', image_z)
