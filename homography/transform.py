import cv2 
import numpy as np 

img = cv2.imread("img1.jpeg")

srcPoints = np.float32([
  [733, 404], 
  [1308, 378], 
  [754, 1016], 
  [1172, 946], 
  [680, 1163], 
  [1207, 1162], 
  [1932, 625], 
  [1914, 829]
  ])
destPoints = np.float32([
  [752, 402], 
  [1294, 432],
  [889, 1067], 
  [1236, 918],
  [847, 1258], 
  [1244, 1100],
  [1439, 623], 
  [1432, 765]
  ])

matrix = np.float32([
  [-3.8968016892830266, -1.4003956823135806, 2681.2873979018877], [-1.3693720627271537,
  -2.8455734484776927, 1858.3128302974615], [-0.0021801694194510564, -0.0011602814566069775,
  1]
])

h, status = cv2.findHomography(srcPoints, destPoints)
# print(h)

result1 = cv2.warpPerspective(img, matrix, (2000, 2000))
result2 = cv2.warpPerspective(img, h, (2000, 2000))

# These are exactly the same. The input data was likely flawed
cv2.imshow("frame1", result1)
cv2.imshow("frame2", result2)

cv2.imwrite("transformed.jpeg", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
