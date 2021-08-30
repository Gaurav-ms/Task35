import numpy as np
import cv2

# Read 1st Image
img1 = cv2.imread("pokemon.png")

# Read 2nd Image
img2 = cv2.imread("cubon.png")

# Display 1st image
cv2.imshow("pokemon", img1)

cv2.imshow("cubon", img2)

cv2.waitKey()
cv2.destroyAllWindows()

img1.shape

(250, 280, 3)

img2.shape

(643, 625, 3)
width, height = 280, 250
img2 = cv2.resize(img2, (width, height))

img2.shape

(250, 280, 3)

combine = np.hstack((img1,img2))

cv2.imshow("Combine images", combine)
cv2.waitKey()
cv2.destroyAllWindows()
