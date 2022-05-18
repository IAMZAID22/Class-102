import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(1,1000)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while camera is on
        ret,frame = videoCaptureObject.read()
        #cv2 imwrite is used to save an image
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False

    return img_name
    print("Snapshot taken")
    #releases camera
    videoCaptureObject.release()
    #closes al window
    cv2.destroyAllWindows()

def  upload_file(img_name):
    access_token = "sl.BH1F6wazmpQc7Hx_4GY-KBP0l9GzW3GnuCCUBs04810YLnk_L2_CjKU8NDrVUYYldAMxHMrQ2J55q1Q0BxccryN2T3sXv2kxAwnEzYgAZKpPrEBzShmXS518xuVW7cB3Q0fDqlfM4-kn"
    file = img_name
    file_from = file
    file_to = "/Image Folders/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
            upload_file(name)

main() 

