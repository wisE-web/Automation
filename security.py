import cv2
from cv2 import VideoCapture
from cv2 import destroyAllWindows
import time
import random
starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=VideoCaptureObject.read()
        imgname="img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        starttime=time.time
        result=False
    return imgname
    print("snapshot taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
takesnapshot()