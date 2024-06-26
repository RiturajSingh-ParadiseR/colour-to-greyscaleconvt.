import cv2

img= input('Enter image location: ')
img1= cv2.imread(img)
img2= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('original image', img1)
cv2.imshow('Greyscale image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

