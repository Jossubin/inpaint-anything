import os
import warnings
import numpy as np
from PIL import Image
from lang_sam import LangSAM
import shutil

# YOLO 포맷 변환 함수
def convert_to_yolo(x1, y1, x2, y2, img_width, img_height):
    # 바운딩 박스 중심 계산
    cx = (x1 + x2) / 2.0
    cy = (y1 + y2) / 2.0
   
    # 바운딩 박스 너비와 높이 계산
    w = x2 - x1
    h = y2 - y1
   
    # YOLO 형식으로 변환 (이미지 크기 대비 상대 좌표)
    cx /= img_width
    cy /= img_height
    w /= img_width
    h /= img_height
   
    return cx, cy, w, h

def convert_boxes_to_yolo_format(boxes, img_width, img_height):
    yolo_boxes = []
   
    # 텐서를 리스트로 변환
    boxes_list = boxes.cpu().numpy().tolist()  # 텐서에서 리스트로 변환
   
    for box in boxes_list:
        x1, y1, x2, y2 = box  # (x_min, y_min, x_max, y_max)
        yolo_box = convert_to_yolo(x1, y1, x2, y2, img_width, img_height)
        yolo_boxes.append(yolo_box)
    return yolo_boxes

def save_yolo_format_to_txt(yolo_boxes, output_txt_path):
    with open(output_txt_path, 'w') as f:
        if yolo_boxes:
            for box in yolo_boxes:
                cx, cy, w, h = box
                # YOLO format: "0 cx cy w h" where 0 is the class label
                f.write(f"0 {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n")
        else:
            # No objects detected, save a "0" in the YOLO format file
            f.write("0\n")

def process_images_from_folder(input_folder, output_folder, temp_folder):
    # 모델 초기화
    model = LangSAM()

    # 입력 폴더에 있는 모든 PNG 파일 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            image_pil = Image.open(image_path).convert("RGB")
            img_width, img_height = image_pil.size

            # 모델을 사용해 바운딩 박스 예측
            masks, boxes, phrases, logits = model.predict(image_pil, text_prompt="person")

            # YOLO 포맷 좌표를 이미지 이름과 동일한 텍스트 파일로 저장할 경로 설정
            output_txt_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            if len(boxes) == 0:
                # No objects detected, print the image filename and save a YOLO file with "0"
                print(f"No objects detected in image: {filename}")

                save_yolo_format_to_txt([], output_txt_path)  # 빈 리스트 전달
                
   
       
                continue

            # YOLO 포맷으로 변환
            yolo_boxes = convert_boxes_to_yolo_format(boxes, img_width, img_height)

            # YOLO 포맷 좌표를 텍스트 파일로 저장
            save_yolo_format_to_txt(yolo_boxes, output_txt_path)
            print(f"Saved YOLO format bounding boxes to: {output_txt_path}")

def main():
    # 경로 설정
    input_folder = '/workspace/Inpaint-Anything/inpainting_dataset/images/train'
    output_folder = '/workspace/Inpaint-Anything/inpainting_dataset/labels/train'
    temp_folder = '/workspace/Inpaint-Amythhomg/results/tmp'

    # 출력 폴더가 존재하지 않으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 경로에서 이미지 처리 및 YOLO 텍스트 파일 저장
    process_images_from_folder(input_folder, output_folder, temp_folder)

if __name__ == "__main__":
    main()