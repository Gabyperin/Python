#BORA PERTUBAR ALGUEM NO WHATSAPP??, MANDE MENSAGENS INFINITAS COM ESSE CODIGO"
import random
import pyautogui as pg
import time
#Crie frases abaixo, entre no whatsapp web e antes de rodar o codigo, 
#entre na conversa com a pessoa que deseja enviar as mensagens infinitas :).
words = ('', '', '') #Escreve no mínimo 3 frases
time.sleep(10)

for i in range(100):
    a = random.choice(words)
    pg.write(a)
    pg.press('enter')
    