import time
import cv2
import os
import hand as htm
ptime = 0
cap = cv2.VideoCapture(0)

FolderPath = "E:\python\Opencv\demngontay\Fingers"# dan cho thu muc
lst = os.listdir(FolderPath)#doc thu muc
lst_2=[]# khai bao mang
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    print(f"{FolderPath}/{i}")
    lst_2.append(image)# them anh vaof mang
#print(lst_2[0].shape)# in ra gia tri cua anh la chieu cao chieu rong va kenh mau

detector = htm.handDetector(detectionCon=0.55)

while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmlist = detector.findHands(frame,draw=False) #phat hien vi tri
    print(lmlist)

    if len(lmlist) != 0:
        if lmlist[8][2] < lmlist[6][2]:
            print("ngon tro dang mo")




    h, w, c = lst_2[0].shape# gan gia tri chieu cao, chieu rong, kenh mau cua anh cho h, w,c
    frame [0:h,0:w]=lst_2[0] #toa do hien thi anh trong FolderPath
    # code fps
    cTime = time.time()#tra ve so giay
    fps = 1/(cTime-ptime)# tinh fdf
    ptime = cTime
    #show fps leen khung hinh
    cv2.putText(frame,f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,127),3)
#(150,70): toa do viet chu, 3: co chu, 3: do day cua chu

    cv2.imshow("Dem ngon tay", frame)
    if cv2.waitKey(1)== ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

