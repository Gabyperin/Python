#Tira foto de uma pessoa linda (se tiver WebCam)

import cv2 
cam = cv2.VideoCapture(0) 

resultado, imagem = cam.read() 

if resultado:
    cv2.imshow("Foto", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()