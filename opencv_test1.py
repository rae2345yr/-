import cv2
import sys

# 카메라 열기
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 카메라 열리지 않을 경우 종료
if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

frames = []
frame_count = 0

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임 읽기 실패 시 종료
    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다.")
        break

    # 프레임 화면에 표시
    cv2.imshow('Video display', frame)

    # 키 입력 대기
    key = cv2.waitKey(1)
    
    # 'c' 키를 눌러서 프레임 캡처
    if key == ord('c'):
        frame_count += 1
        frames.append(frame)
        print(f'Captured frame {frame_count}')
        
        # 3개의 프레임 캡처하면 루프 종료
        if frame_count == 3:
            break

    # 'q' 키를 눌러서 루프 종료
    elif key == ord('q'):
        break

# 카메라 자원 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()

# 캡처한 프레임 저장
for i, frame in enumerate(frames):
    cv2.imwrite(f'captured_frame_{i + 1}.png', frame)
    print(f'Frame {i + 1} saved as captured_frame_{i + 1}.png')

