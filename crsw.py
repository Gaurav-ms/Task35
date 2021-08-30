import cv2
import numpy as np
# read the first photo
photo1 = cv2.imread("image_name1")

# read the second photo
photo2 = cv2.imread("image_name2")
width, height = 280, 250
photo2 = cv2.resize(photo2, (width, height))

photo2.shape

(280, 250, 3)

photo = np.hstack((photo1,photo2))
cv2.imshow("Before Photo1",photo)
cv2.waitKey()
cv2.destroyAllWindows()

# shape of the photo
photo1.shape

(280, 250, 3)

# shape of the photo
photo2.shape

(280, 250, 3)

photo1.shape == photo2.shape

True


# crop second photo
crop_photo2 = photo2[5:150, 55:190]
photo1[5:150, 55:190]= crop_photo2

final_photo1 = photo1

# reading 1st image
photo1 = cv2.imread("pokemon.png")

# crop 1st photo
crop_photo1= photo1[5:150, 55:190]

# swapping
photo2[5:150, 55:190] = crop_photo1

final_photo2 = photo2

# shape of final photos
final_photo1.shape, final_photo2.shape

((250, 280, 3), (250, 280, 3))

# Attach final swap photo
photo = np.hstack((final_photo1,final_photo2))

cv2.imshow("After swapping",photo)
cv2.waitKey()
cv2.destroyAllWindows()
