import cv2
import mediapipe as mp
# 使用新版MediaPipe Tasks API
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# 创建手部检测器
options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1)
detector = HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
timestamp = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame,1) # 镜像画面

    # BGR转RGB送入模型
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # 检测
    result = detector.detect_for_video(mp_image, timestamp)
    timestamp += 33

    # 判断是否检测到手
    if result.hand_landmarks:
        for hand in result.hand_landmarks:
            # 食指指尖 index=8
            index_point = hand[8]
            h,w,_ = frame.shape
            x = int(index_point.x * w)
            y = int(index_point.y * h)
            print(f"食指 x:{x}, y:{y}")
            cv2.circle(frame, (x,y), 8, (0,255,0), -1)

    cv2.imshow("Hand", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
detector.close()
