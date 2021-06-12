import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.035,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in faces:
    center_coordinates = x + w // 2, y + h // 2
    radius = w // 2 # or can be h / 2 or can be anything based on your requirements
    cv2.circle(image, center_coordinates, radius, (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)

# k = cv2.waitKey(30) & 0xff
# if k == ord('s'):
#     # break
