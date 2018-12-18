import threading
import time
import cv2
import sys
import numpy as np
import datetime
import cognitive_face as CF
from io import BytesIO
from multiprocessing import Process
import os
import json


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

GROUP_FACE_API="video_test"

FACE_API_TOKEN_MICROSOFT="8f7bc585b4bf42dd883ed1dde0111aa4"
CF.Key.set(FACE_API_TOKEN_MICROSOFT)

FACE_API_BASE_URL = "https://eastus2.api.cognitive.microsoft.com/face/v1.0/"
CF.BaseUrl.set(FACE_API_BASE_URL)

PERSON_GROUP_ID="grupo-video-prueba"

PERSON_ID="1353d255-27c2-456b-8ef2-65d43fd4161a"
PERSON_ID2="2334a349-2d0d-499e-80c0-67807897063a"
PERSON_ID3="4ca5786f-7fa3-4518-893d-82bf7bc45366"
img_url='/home/luciozolezzi/Documentos/FaceSnoop/video/tmp/'
img_Prueba="/home/luciozolezzi/Documentos/FaceSnoop/video/tmp/faceIoT2018-10-31-12-01-09.png"
img_Prueba2="/home/luciozolezzi/Documentos/FaceSnoop/video/tmp/faceIoT2018-10-31-10-45-41.png"
img_Prueba3="/home/luciozolezzi/Documentos/FaceSnoop/video/tmp/faceIoT2018-10-31-15-01-15.png"
img_name='faceIoT'
rostro_detectado={}
nombre='Lucio Zolezzi'

##############################################################################################

def getFechaAhoraStr():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d-%H-%M-%S")

def tomarFoto(camara,path,frame,ext='.png'):
    fname=path+getFechaAhoraStr()+ext
    camara.imwrite(fname,frame)
    print('Se guardo la imagen: '+fname)
    return fname

def crearPersona(grupo,usuario):
    response = CF.person.create(grupo,usuario)
    id_persona=response['personId']
    return id_persona

def entrenarCara(path,grupo,personId):
    CF.person.add_face(path,grupo,personId)
    status=CF.person_group.train(grupo)
    return status

def procesamientoVideo(video_capture):
    umbral = 101   #Cuadros estables
    sizeFrame=110
    lenAct=0
    lenAnt=0
    count=0

    font                   = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    bottomLeftCornerOfText = (500,400)
    fontScale              = 2
    fontColor              = (0,255,0)
    lineType               = 4
    while True:
        # Captura cuadro por cuadro
        lenAnt=lenAct

        ret, frame = video_capture.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(sizeFrame, sizeFrame)
        )

        #len(faces) es la cantidad de caras encontradas
        cont=1
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+h, y+h), (0, 255, 0), 2)

        lenAct=len(faces)
        cv2.putText(frame,str(count),bottomLeftCornerOfText,font, fontScale,fontColor,lineType)
        cv2.imshow("Deteccion de caras en tiempo real", frame)


        k = cv2.waitKey(1)

        if k%256 == 27:
            #ESC presionado
            break
        elif k%256 == 32:   #Toma foto
            # SPACE presionado
            if (count==umbral):
                imgPath=tomarFoto(cv2,img_url+img_name,frame)

        if(lenAct==lenAnt and lenAct!=0):
            count+=1
        else:
            count=0

        if (count==umbral and lenAct!=0):
            imgPath=tomarFoto(cv2,img_url+img_name,frame)
            count=0
            video_capture.release()
            cv2.destroyAllWindows()
            rostro_detectado = CF.face.detect(imgPath)
            face_ids = [d['faceId'] for d in rostro_detectado]
            identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
            aux=json.dumps(identified_faces)
            carasId=json.loads(aux)
            print(carasId)
            if(carasId[0]['candidates'][0]['personId']=="1353d255-27c2-456b-8ef2-65d43fd4161a"):
                print("Lucio Zolezzi")
                cv2.putText(frame,"Lucio Zolezzi",(200,100),font, fontScale,fontColor,lineType)
                imgPath=tomarFoto(cv2,img_url+img_name+"RECON",frame)
            break
            #Redirigir a otra url

        count%=umbral

##############################################################################################

if len(sys.argv) < 2:
    video_cap = cv2.VideoCapture(0)
else:
    video_cap = cv2.VideoCapture(sys.argv[1])

threads=[]






























##
