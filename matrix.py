import numpy as np
import math

def Rotation(r):
  return np.array([[round(math.cos(math.radians(r)), 3), round(-math.sin(math.radians(r)), 3), 0],
                   [round(math.sin(math.radians(r)), 3), round(math.cos(math.radians(r)), 3), 0],
                   [0, 0, 1]])
def Translation(Tx,Ty):
  return np.array([[1, 0, Tx],
                   [0, 1, Ty],
                   [0, 0, 1]])

def Scalation(Sx,Sy):
  return  np.array([[Sx, 0, 0],
                    [0, Sy, 0],
                    [0, 0, 1]])
def Vector(x,y):
  return np.array([[x],
                    [y],
                    [1]])

action = input('choose the operation: RSTV, RTSV, SRTV, STRV, TRSV, TSRV \n')
if action not in ['RSTV','RTSV','SRTV','STRV','TRSV','TSRV']:
    action = input('try again, choose the operation: T, R, S or V \n')
else:
    if action == 'RSTV':
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(R, S),T),V))
    if action == 'RTSV':
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(R, T),S),V))
    if action == 'SRTV':
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(S, R),T),V))
    if action == 'STRV':
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(S, T),R),V))
    if action == 'TRSV':
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(T, R),S),V))
    if action == 'TSRV':
      Tx = float(input('xTranslation: '))
      Ty = float(input('yTranslation: '))
      T = Translation(Tx,Ty)
      #print(T)
      Sx = float(input('xScalation: '))
      Sy = float(input('yScalation: '))
      S = Scalation(Sx,Sy)
      #print(S)
      r = float(input('Angle: '))
      R = Rotation(r)
      #print(R)
      x = float(input('xVector: '))
      y = float(input('xVector: '))
      V = Vector(x,y)
      #print(V)
      print(np.dot(np.dot(np.dot(T, S),R),V))
