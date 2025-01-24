import cv2

img = cv2.imread('gan.jpg',0)
print(img)
status=cv2.imwrite('wp3.jpg',img)
print("image written to file-system: ",status)