import cv2
from ffpyplayer.player import MediaPlayer
import keyboard

video_pathA="vineA.mp4"
video_pathB="vine B.mp4"
video_pathC="vine C.mp4"
video_pathD="vine D.mp4"
video_pathE="vine E.mp4"
video_pathF="vine F.mp4"
video_pathG="vine G.mp4"
video_pathH="vine H.mp4"
video_pathI="vine I.mp4"
video_pathJ="vine J.mp4"
video_pathK="vine K.mp4"
video_pathL="vine L.mp4"
video_pathM="vine M.mp4"
video_pathN="vine N.mp4"
video_pathO="vine O.mp4"
video_pathP="vine P.mp4"
video_pathQ="vine Q.mp4"
video_pathR="vine R.mp4"
video_pathS="vine S.mp4"
video_pathT="vine T.mp4"
video_pathU="vine U.mp4"
video_pathV="vine V.mp4"
video_pathW="vine W.mp4"
video_pathX="vine X.mp4"
video_pathY="vine Y.mp4"
video_pathZ="vine Z.mp4"


def PlayVideoA(video_pathA):
    videoA=cv2.VideoCapture(video_pathA)
    player = MediaPlayer(video_pathA)
    while True:
        grabbed, frame=videoA.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoA

def PlayVideoB(video_pathB):
    videoB=cv2.VideoCapture(video_pathB)
    player = MediaPlayer(video_pathB)
    while True:
        grabbed, frame=videoB.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoB

def PlayVideoC(video_pathC):
    videoC=cv2.VideoCapture(video_pathC)
    player = MediaPlayer(video_pathC)
    while True:
        grabbed, frame=videoC.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoC

def PlayVideoD(video_pathD):
    videoD=cv2.VideoCapture(video_pathD)
    player = MediaPlayer(video_pathD)
    while True:
        grabbed, frame=videoD.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoD

def PlayVideoE(video_pathE):
    videoE=cv2.VideoCapture(video_pathE)
    player = MediaPlayer(video_pathE)
    while True:
        grabbed, frame=videoE.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoE

def PlayVideoF(video_pathF):
    videoF=cv2.VideoCapture(video_pathF)
    player = MediaPlayer(video_pathF)
    while True:
        grabbed, frame=videoF.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoF

def PlayVideoG(video_pathG):
    videoG=cv2.VideoCapture(video_pathG)
    player = MediaPlayer(video_pathG)
    while True:
        grabbed, frame=videoG.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoG  

def PlayVideoH(video_pathH):
    videoH=cv2.VideoCapture(video_pathH)
    player = MediaPlayer(video_pathH)
    while True:
        grabbed, frame=videoH.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoH

def PlayVideoI(video_pathI):
    videoI=cv2.VideoCapture(video_pathI)
    player = MediaPlayer(video_pathI)
    while True:
        grabbed, frame=videoI.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoI

def PlayVideoJ(video_pathJ):
    videoJ=cv2.VideoCapture(video_pathJ)
    player = MediaPlayer(video_pathJ)
    while True:
        grabbed, frame=videoJ.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoJ

def PlayVideoK(video_pathK):
    videoK=cv2.VideoCapture(video_pathK)
    player = MediaPlayer(video_pathK)
    while True:
        grabbed, frame=videoK.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoK

def PlayVideoL(video_pathL):
    videoL=cv2.VideoCapture(video_pathL)
    player = MediaPlayer(video_pathL)
    while True:
        grabbed, frame=videoL.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoL

def PlayVideoM(video_pathM):
    videoM=cv2.VideoCapture(video_pathM)
    player = MediaPlayer(video_pathM)
    while True:
        grabbed, frame=videoM.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoM

def PlayVideoN(video_pathM):
    videoM=cv2.VideoCapture(video_pathM)
    player = MediaPlayer(video_pathM)
    while True:
        grabbed, frame=videoM.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoM


def PlayVideoL(video_pathL):
    videoL=cv2.VideoCapture(video_pathL)
    player = MediaPlayer(video_pathL)
    while True:
        grabbed, frame=videoL.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoL

def PlayVideoM(video_pathM):
    videoM=cv2.VideoCapture(video_pathM)
    player = MediaPlayer(video_pathM)
    while True:
        grabbed, frame=videoM.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoM

def PlayVideoN(video_pathN):
    videoN=cv2.VideoCapture(video_pathN)
    player = MediaPlayer(video_pathN)
    while True:
        grabbed, frame=videoN.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoN  

def PlayVideoO(video_pathO):
    videoO=cv2.VideoCapture(video_pathO)
    player = MediaPlayer(video_pathO)
    while True:
        grabbed, frame=videoO.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoO

def PlayVideoP(video_pathP):
    videoP=cv2.VideoCapture(video_pathP)
    player = MediaPlayer(video_pathP)
    while True:
        grabbed, frame=videoP.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoP


def PlayVideoQ(video_pathQ):
    videoQ=cv2.VideoCapture(video_pathQ)
    player = MediaPlayer(video_pathQ)
    while True:
        grabbed, frame=videoQ.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoQ


def PlayVideoR(video_pathR):
    videoR=cv2.VideoCapture(video_pathR)
    player = MediaPlayer(video_pathR)
    while True:
        grabbed, frame=videoR.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoR

def PlayVideoS(video_pathS):
    videoS=cv2.VideoCapture(video_pathS)
    player = MediaPlayer(video_pathS)
    while True:
        grabbed, frame=videoS.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoS

def PlayVideoT(video_pathT):
    videoT=cv2.VideoCapture(video_pathT)
    player = MediaPlayer(video_pathT)
    while True:
        grabbed, frame=videoT.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoT


def PlayVideoU(video_pathU):
    videoU=cv2.VideoCapture(video_pathU)
    player = MediaPlayer(video_pathU)
    while True:
        grabbed, frame=videoU.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoU

def PlayVideoV(video_pathV):
    videoV=cv2.VideoCapture(video_pathV)
    player = MediaPlayer(video_pathV)
    while True:
        grabbed, frame=videoV.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoV

def PlayVideoW(video_pathW):
    videoW=cv2.VideoCapture(video_pathW)
    player = MediaPlayer(video_pathW)
    while True:
        grabbed, frame=videoW.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoW

def PlayVideoX(video_pathX):
    videoX=cv2.VideoCapture(video_pathX)
    player = MediaPlayer(video_pathX)
    while True:
        grabbed, frame=videoX.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoX

def PlayVideoY(video_pathY):
    videoY=cv2.VideoCapture(video_pathY)
    player = MediaPlayer(video_pathY)
    while True:
        grabbed, frame=videoY.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoY

def PlayVideoZ(video_pathZ):
    videoZ=cv2.VideoCapture(video_pathZ)
    player = MediaPlayer(video_pathZ)
    while True:
        grabbed, frame=videoZ.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    return videoZ

while True:
    if keyboard.is_pressed('a') == True:
        videoA = PlayVideoA(video_pathA)
        videoA.release()

    if keyboard.is_pressed('b') == True:
        videoB = PlayVideoA(video_pathB)
        videoB.release()

    if keyboard.is_pressed('c') == True:
        videoC = PlayVideoC(video_pathC)
        videoC.release()

    if keyboard.is_pressed('d') == True:
        videoD = PlayVideoC(video_pathD)
        videoD.release()

    if keyboard.is_pressed('e') == True:
        videoE = PlayVideoE(video_pathE)
        videoE.release()

    if keyboard.is_pressed('f') == True:
        videoF = PlayVideoE(video_pathF)
        videoF.release()

    if keyboard.is_pressed('g') == True:
        videoG = PlayVideoG(video_pathG)
        videoG.release()

    if keyboard.is_pressed('h') == True:
        videoH = PlayVideoG(video_pathH)
        videoH.release()

    if keyboard.is_pressed('i') == True:
        videoI = PlayVideoG(video_pathI)
        videoI.release()

    if keyboard.is_pressed('j') == True:
        videoJ = PlayVideoG(video_pathJ)
        videoJ.release()

    if keyboard.is_pressed('k') == True:
        videoK = PlayVideoK(video_pathK)
        videoK.release()

    if keyboard.is_pressed('l') == True:
        videoL = PlayVideoL(video_pathL)
        videoL.release()

    if keyboard.is_pressed('m') == True:
        videoM = PlayVideoM(video_pathM)
        videoM.release()

    if keyboard.is_pressed('n') == True:
        videoN = PlayVideoN(video_pathN)
        videoN.release()

    if keyboard.is_pressed('o') == True:
        videoO = PlayVideoO(video_pathO)
        videoO.release()

    if keyboard.is_pressed('p') == True:
        videoP = PlayVideoP(video_pathP)
        videoP.release()

    if keyboard.is_pressed('q') == True:
        videoQ = PlayVideoQ(video_pathQ)
        videoQ.release()

    if keyboard.is_pressed('r') == True:
        videoR = PlayVideoR(video_pathR)
        videoR.release()

    if keyboard.is_pressed('s') == True:
        videoS = PlayVideoS(video_pathS)
        videoS.release()

    if keyboard.is_pressed('t') == True:
        videoT = PlayVideoT(video_pathT)
        videoT.release()

    if keyboard.is_pressed('u') == True:
        videoU = PlayVideoU(video_pathU)
        videoU.release()

    if keyboard.is_pressed('v') == True:
        videoV = PlayVideoV(video_pathV)
        videoV.release()

    if keyboard.is_pressed('w') == True:
        videoW = PlayVideoW(video_pathW)
        videoW.release()

    if keyboard.is_pressed('x') == True:
        videoX = PlayVideoX(video_pathX)
        videoX.release()

    if keyboard.is_pressed('y') == True:
        videoY = PlayVideoY(video_pathY)
        videoY.release()

    if keyboard.is_pressed('z') == True:
        videoZ = PlayVideoZ(video_pathZ)
        videoZ.release()


