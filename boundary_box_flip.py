import argparse
import sys

def read_bounding_boxes(input_file):
    """
    파일에서 YOLO 형식의 Bounding Box를 읽는 함수
    파일 형식: [class, x_center, y_center, width, height]
    """
    bounding_boxes = []
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            # 각 값을 float로 변환
            bbox = [int(parts[0])] + [float(x) for x in parts[1:]]
            bounding_boxes.append(bbox)
    return bounding_boxes

def write_bounding_boxes(output_file, bounding_boxes):
    """
    YOLO 형식의 Bounding Box를 파일로 쓰는 함수
    """
    with open(output_file, 'w') as file:
        for bbox in bounding_boxes:
            bbox_str = ' '.join(map(str, bbox))
            file.write(f"{bbox_str}\n")

def mirror_bounding_box_yolo(bbox):
    """
    주어진 YOLO 형식의 Bounding Box를 좌우 대칭하는 함수
    bbox: [class, x_center, y_center, width, height]
    """
    cls, x_center, y_center, width, height = bbox
    
    # x_center 좌우 대칭 계산
    x_center_sym = 1 - x_center
    
    # 대칭된 Bounding Box 반환 (class는 변하지 않음)
    return [cls, x_center_sym, y_center, width, height]

def process_bounding_boxes(input_file, output_file):
    """
    입력 파일에서 Bounding Box를 읽어 좌우 대칭 변환 후 출력 파일로 저장하는 함수
    """
    # Bounding Box 읽기
    bounding_boxes = read_bounding_boxes(input_file)
    
    # 좌우 대칭 변환
    mirrored_boxes = [mirror_bounding_box_yolo(bbox) for bbox in bounding_boxes]
    
    # 변환된 Bounding Box 저장
    write_bounding_boxes(output_file, mirrored_boxes)

def setup_args(parser):
    parser.add_argument(
        "--input", type=str, required=True,
        help="input Path",
    )
    parser.add_argument(
        "--output", type=str, required=True,
        help="output Path"
    )

if __name__=="__main__":

    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])
    # 파일 입출력 실행 예시
    input_file = f'{args.input}'
    output_file = f'{args.output}'

    # 입력 파일에서 좌표 읽고, 좌우 대칭 후 출력 파일로 저장
    process_bounding_boxes(input_file, output_file)
