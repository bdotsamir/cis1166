import cv2
import numpy as np

img = cv2.imread("./images/temple_logo.png")

srcPoints = np.float32([
    [0, 0],
    [2506, 0],
    [0, 675],
    [2506, 675]
])
destPoints = np.float32([
    [13, 158],
    [247, 154],
    [13, 252],
    [247, 248]
])

matrix = np.float32([
    [0.09337589784517317, -0.00000000000000042923704781994003, 13.000000000000021],
    [-0.0015961691939330128, 0.1392592592592602, 157.99999999999903],
    [0.000000000000000006736284271475909, -0.0000000000000000021590270586249244, 1]
])

h, status = cv2.findHomography(srcPoints, destPoints)
# print(h)

result1 = cv2.warpPerspective(img, matrix, (2000, 2000))
result2 = cv2.warpPerspective(img, h, (2000, 2000))

# These are exactly the same. The input data was likely flawed
cv2.imshow("frame1", result1)
cv2.imshow("frame2", result2)

cv2.imwrite("transformed.jpeg", result1)

cv2.waitKey(0)
cv2.destroyAllWindows()
