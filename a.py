import cv2,configparser
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture('video_2020-10-03_15-34-59.mp4')

# Loop that runs until we reach an end of a video
while(True):
  ret, img=cap.read()
  if ret == True:
    cv2.namedWindow('Video',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Video', 600,600)
    cv2.imshow("Video", img)
    img_cpy=img.copy()
    h,w,c = img.shape
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plt.rcParams['figure.figsize'] = (16,9)
    img=cv2.blur(img,(3,3))
    img = cv2.Canny(img, 10, 150)
    cv2.namedWindow('Canny',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Canny', 600,600)
    cv2.imshow('Canny',img)
    moedas = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT ,0.9,120,param1=50,param2=30,minRadius=40,maxRadius=100)
    count=0
    if moedas is not None:
        moedas_round = np.uint16(np.around(moedas))
        for i in moedas_round[0, :]:
          cv2.circle(img_cpy,(i[0],i[1]),i[2],(0,0,255),5)
          cv2.putText(img_cpy,'+', (i[0],i[1]-2),cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),2)
          count=count+1
        cv2.putText(img_cpy,'Moedas = '+str(count),(20,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4) 
    cv2.namedWindow('Final',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Final', 600,600)
    cv2.imshow("Final",img_cpy)
  # When we press Q on our keyboard to exit video
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
# Release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

