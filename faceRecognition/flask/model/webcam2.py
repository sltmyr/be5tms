import cv2


import json
import os
import io

# Imports for image procesing
from PIL import Image

# Imports for prediction
from predict import initialize, predict_image, predict_url

initialize()
cam = cv2.VideoCapture(0)

cam.set(3, 1280)
cam.set(4,720)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        pil_im = Image.fromarray(frame)
        results = predict_image(pil_im)

        max = 0
        for i, pred in enumerate(results['predictions']):
            if pred['probability'] > max:
                max_idx = i
        
        name = results['predictions'][i]['tagName']

        print(name)

        cv2.putText(frame, "user " + name, (200,200), cv2.FONT_HERSHEY_PLAIN, 3.0, (255,255,255), thickness=1)
        cv2.imshow("frame",frame)
        
        cv2.waitKey(1000)
        


        print(results)
        print("\n pred:", results['predictions'])


cam.release()

cv2.destroyAllWindows()