import cv2
import face_recognition
import os
import numpy as np

def nhandienkhuonmat():
    path = "E:/python3.8/nhandien_khuon_mat/List_pictures"
    images = []
    className = []
    i = 0
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        print(cl)
        curImg = cv2.imread(f"{path}/{cl}")
        images.append(curImg)
        className.append(os.path.splitext(cl)[0])
    print(len(images))
    print(className)

    # ma hoa buc anh

    def Mahoa(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnow = Mahoa(images)
    print(len(encodeListKnow))

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        framS = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
        framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)

        facecurFrame = face_recognition.face_locations(framS)
        encodecurFrame = face_recognition.face_encodings(framS)

        for encodeFace, faceLoc in zip(encodecurFrame, facecurFrame):
            matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            print(matchIndex)

            if faceDis[matchIndex] < 0.50:
                name = className[matchIndex].upper()
                i = 1
            else:
                name = "Unknow"
                i = 0

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, name, (x1, y2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Nhin phat biet ngay", frame)

        if i == 1:
            #print(name)
            break


        if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
            break

    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ
    return name



