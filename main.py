import cv2
import numpy as np
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)
access = ['Sairam', 'jhon']
while True:
    success,img = cap.read()
    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,(255,0,255),3)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0]+10,pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(32,128,255),2)
        if myData in access:
            cv2.putText(img, 'access granted', (pts2[0], pts2[3]), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,128,0), 2)
        else:
            cv2.putText(img, 'access denied', (pts2[0], pts2[3]), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255), 2)
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
