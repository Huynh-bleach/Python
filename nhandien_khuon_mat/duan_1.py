import os
import face_recognition
import numpy
import cv2

imgElon = face_recognition.load_image_file("E:/python3.8/nhandien_khuon_mat/pictures/huynh_3.jpg")

imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)


imgCheck = face_recognition.load_image_file("E:/python3.8/nhandien_khuon_mat/pictures/huynh_2.jpg")

imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)


faceLoc = face_recognition.face_locations(imgElon)[0]

print(faceLoc) #(y1, x2, y2, x1)

# ma hao hinh anh

encodeElon = face_recognition.face_encodings(imgElon)[0]

cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1], faceLoc[2]) ,(255,0,255), 3)


faceCheck = face_recognition.face_locations(imgCheck)[0] #xacs dinh vi tri khuon mat
encodeCheck = face_recognition.face_encodings(imgCheck)[0]
cv2.rectangle(imgCheck,(faceCheck[3],faceCheck[0]),(faceCheck[1], faceCheck[2]) ,(0,255,0), 3)

results = face_recognition.compare_faces([encodeElon], encodeCheck)
print(results)

faceDis = face_recognition.face_distance([encodeElon], encodeCheck)
print(faceDis)

cv2.putText(imgCheck,f"{results}{round(faceDis[0],2)}",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow("Elon", imgElon)
cv2.imshow("check", imgCheck)
cv2.waitKey()

