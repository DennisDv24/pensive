import cv2
directory = 'reddit_sub_LiminalSpace/'
output_dir = 'fliped/'
img = cv2.imread(directory+'test.jpg')


flip_img = cv2.flip(img, 0)

cv2.imshow('original', img)
cv2.imshow('flip', flip_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(output_dir+'finalImgTest.jpg', flip_img)

print(directory+'test.jpg')
