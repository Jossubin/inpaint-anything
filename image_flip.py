from PIL import Image
import argparse
import sys

def mirror_image(input_image_path, output_image_path):
    """
    이미지를 좌우 반전하는 함수
    :param input_image_path: 원본 이미지 파일 경로
    :param output_image_path: 반전된 이미지 저장 경로
    """
    try:
        # 이미지 열기
        image = Image.open(input_image_path)
        
        # 이미지 좌우 반전
        mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        # 반전된 이미지 저장
        mirrored_image.save(output_image_path)
        print(f"Mirrored image saved to {output_image_path}")
    
    except Exception as e:
        print(f"Error: {e}")

def process_image_file():
    """
    사용자로부터 입력받은 파일 경로로 이미지를 좌우 반전하는 함수
    """
    # 사용자로부터 입력 파일 경로와 출력 파일 경로 받기
    input_image_path = f'{args.input}'
    output_image_path = f'{args.output}'
    
    # 좌우 반전 함수 호출
    mirror_image(input_image_path, output_image_path)

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
  

    # 입력 파일에서 좌표 읽고, 좌우 대칭 후 출력 파일로 저장
    process_image_file()