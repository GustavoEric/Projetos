import cv2
import face_recognition as fr

rosto=False 
rosto2 =False
img1 = False
webcam = cv2.VideoCapture(0)
if webcam.isOpened():
    validacao, frame = webcam.read()
    while rosto != True:
        validacao, frame = webcam.read()
        imagem = frame
        try:
            faceLocWebCam = fr.face_locations(imagem)[0]
            cv2.rectangle(imagem,(faceLocWebCam[3],faceLocWebCam[0]),(faceLocWebCam[1],faceLocWebCam[2]),(0,255,0),2)
            cv2.imshow('camera',imagem)
        except:
            print('Sem Rosto')
        #print(faceLocWebCam)
        #encodeFrame = fr.face_encodings(imagem)[0]
        #comparacao = fr.compare_faces([encodeMarcus],encodeFrame)
        #print(comparacao)
        if cv2.waitKey(1) == 27:
            cv2.imwrite("reconhecimento_facial/imagens/marcus.jpg", frame)
            imgMarcus = fr.load_image_file('reconhecimento_facial\imagens\marcus.jpg')
            imgMarcus = cv2.cvtColor(imgMarcus,cv2.COLOR_BGR2RGB)

            faceLoc = fr.face_locations(imgMarcus)[0]
            cv2.rectangle(imgMarcus,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),2)
            print(faceLoc)
            encodeMarcus = fr.face_encodings(imgMarcus)[0]
            print(encodeMarcus)
            print('Primeira Foto OK')
            cv2.imshow('camera2',imgMarcus)
            img1 = True
            rosto = True

if img1 == True:
    validacao, frame = webcam.read()
    while rosto2 != True:
        validacao, frame = webcam.read()
        imagem = frame
        try:
            faceLocWebCam = fr.face_locations(imagem)[0]
            cv2.rectangle(imagem,(faceLocWebCam[3],faceLocWebCam[0]),(faceLocWebCam[1],faceLocWebCam[2]),(0,255,0),2)
            cv2.imshow('camera',imagem)
        except:
            print('Sem Rosto')
        #print(faceLocWebCam)
        #encodeFrame = fr.face_encodings(imagem)[0]
        #comparacao = fr.compare_faces([encodeMarcus],encodeFrame)
        #print(comparacao)
        if cv2.waitKey(1) == 27:
            cv2.imwrite("reconhecimento_facial/imagens/FotoGus.jpg", frame)
            imgGus = fr.load_image_file('reconhecimento_facial\imagens\FotoGus.jpg')
            imgGus = cv2.cvtColor(imgGus,cv2.COLOR_BGR2RGB)
            faceLocGus = fr.face_locations(imgGus)[0]
            cv2.rectangle(imgGus,(faceLocGus[3],faceLocGus[0]),(faceLocGus[1],faceLocGus[2]),(0,255,0),2)
            print('Segunda Foto OK')
            cv2.imshow('camera3',imgGus)
            encodeGus = fr.face_encodings(imgGus)[0]
            print(encodeGus)
            comparacao = fr.compare_faces([encodeMarcus],encodeGus[0])
            print(comparacao)
webcam.release()

cv2.waitKey(0)