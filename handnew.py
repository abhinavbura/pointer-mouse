from unittest import result
import cv2
import mediapipe as mp
import pyautogui as pg

cap=cv2.VideoCapture("http://192.168.0.102:8080/video")
hands = mp.solutions.hands.Hands()
draw=mp.solutions.drawing_utils
while True:
    success , img =cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result= hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c =img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                if id== 8:
                    pg.moveTo(cx-800+330,cy)
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
        draw.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS)
    cv2.circle(img, (330, 1), 25, (255, 0, 255), cv2.FILLED)
    


    cv2.imshow('got my handsss', cv2.flip(img, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
