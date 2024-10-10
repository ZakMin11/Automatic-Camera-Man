'''
Zak Mineiko
Created: 3/1/2021
Modified: 3/9/2021

This is just a testing script for interfacing servo from py script using serial comm.
'''
import serial
import time
import numpy as np
import pyautogui as pag
ser=serial.Serial('/dev/cu.usbmodem143301', 9600)

# Mybe this will help: https://colab.research.google.com/drive/1Ln-Vty7OaQaaxMREEaGYbDnRekclJKts?usp=sharing#scrollTo=8HGKcho0I-BN


def write_read(x):
    ser.write(bytes(x,'utf-8'))
    time.sleep(0.5)
def testingfunc():
    time.sleep(3)
    for i in range(180):
        ser.write(i)
        i = i+10
        print(i)
        time.sleep(2)

boo = 10
while True:
    pos = input("Enter position: ")
    pos = str(pos)
    pos = pos.encode()
    ser.write(pos)
    #
    #if(boo <180):
   #     boo=boo+10
   # else:
  #      boo = 10
 #       time.sleep(3)
    #x,y=pag.position()
    #x = int(x//180)
 #   print(boo)
 #   boo = str(boo)
#    boo =boo.encode()
#    ser.write(boo)
    time.sleep(1)
    #testingfunc()
    
    
    #ßpos = input("Input position: ")
    #if pos == 'q':
    #    break
    
    
    #ser.write(xval.encode())
    
    

