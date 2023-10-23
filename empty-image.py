""" 新しくカラー画像を作成・保存 """
import numpy as np
import cv2 as cv


# 作る画像の大きさ（横 W, 縦 H ピクセル）
W, H = (800, 600)

# 黒い画像を作り、保存する
# (縦, 横, 3) の順で大きさを指定する（順序注意）。
# 下の例で (0, 0, 0) と指定するのと同じ
image = np.zeros((H, W, 3), np.uint8)
image[300]=255 # 横一列
image[:,200]=(0,255,255) # 縦一列
image[350:400,:]=(255,0,255)   # image[300:400]でも可
image[:,700:750]=(255,0,255)
image[350:400,700:750]=(255,255,0)
cv.imwrite('black.png', image)

# 色のついた画像を作り、保存する
image = np.full((H, W, 3), (0, 0, 255), np.uint8)
cv.imwrite('red.png', image)

image = np.full((H, W, 3), (0, 255, 0), np.uint8)
cv.imwrite('green.png', image)

image = np.full((H, W, 3), (0, 255, 255), np.uint8)
cv.imwrite('yellow.png', image)

image = np.full((H, W, 3), (255, 0, 0), np.uint8)
cv.imwrite('blue.png', image)

image = np.full((H, W, 3), (255, 0, 255), np.uint8)
cv.imwrite('magenta.png', image)

image = np.full((H, W, 3), (255, 255, 0), np.uint8)
cv.imwrite('cyan.png', image)

image = np.full((H, W, 3), (255, 255, 255), np.uint8)
cv.imwrite('white.png', image)


"""
Note:
    OpenCV では、色のチャンネルは BGR の順なので、
    (B, G, R) のようにタプルで色を与える必要がある。
    各チャンネルは 8bit なので 0 から 255 の間の整数である。
    N.B. 多くの画像形式では RGB を採用している。

    保存する画像の種類は拡張子（ . の後ろの文字）で決まる。
    研究用途では、不可逆圧縮されない png が便利である。
"""

