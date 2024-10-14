import cv2
import numpy as np
from __MAPS__.site4_ugv import MAP

# 이미지를 그레이스케일로 읽기
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 해리스 코너 검출
corners = cv2.cornerHarris(image, blockSize=2, ksize=3, k=0.04)

# 결과를 시각화하기 위해 코너 위치를 원으로 표시
image[corners > 0.01 * corners.max()] = [255]

# 결과 이미지 보기
cv2.imshow('Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
