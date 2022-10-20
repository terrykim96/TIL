import cv2
import cvlib as cv 
from IPython.display import Image, display



img = cv2.imread('images/KakaoTalk_20221020_094302574_02.jpg') # 이미지 파일 불러오기
conf = 0.5 # 사물 인식을 진행할 confidence의 역치 값
model_name = "yolov7" # 사물을 인식할 모델 이름

result = cv.detect_common_objects(img, confidence=conf, model=model_name)

print(result)

result_img = cv.object_detection.draw_bbox(img, *result) # result 결과를 이미지에 반영
cv2.imshow('output', result_img) # 반영된 이미지 파일 저장
cv2.waitKey(0)
