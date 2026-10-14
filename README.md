# 食指指尖实时跟踪
基于MediaPipe HandLandmarker，调用摄像头实时追踪食指指尖，打印指尖像素坐标。

## 安装依赖
```bash
pip install -r requirements.txt
## 模型准备

手动下载 `hand_landmarker.task` 放到项目根目录
下载地址：
[https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task)

## 运行

```
python text_hand.py
```

- 摄像头画面做镜像处理
- 画面绿色圆圈标记食指指尖
- 控制台输出食指 x、y 像素坐标
- 按键盘 `q` 退出程序

## 项目原理

1. OpenCV 读取摄像头帧，画面水平镜像
2. BGR 图像转为 RGB，送入 HandLandmarker 手部模型
3. VIDEO 视频流模式推理，传入递增时间戳
4. 获取手部关键点，取出食指指尖（id=8）
5. 转换为像素坐标，打印并绘制标记点