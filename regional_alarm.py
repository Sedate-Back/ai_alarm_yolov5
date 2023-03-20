import numpy as np
import cv2

# 1、获取到了脚步的顶部左点，底部右点  -->  foot_box
# 2、检测区为pts，根据pts绘制size=监控画面的二值化图
# pts = [[34, 232], [95, 394], [371, 208], [253, 97]]
# pts = [[220, 129],[159, 158],[216, 204],[290, 166]]
# pts = [[182, 29],[144, 54],[196, 83],[256, 46]]

# pts 是由前端传递过来的区域
pts = [[214, 365], [321, 353], [394, 572], [228, 572]]
lower = np.array([255, 255, 255])
upper = np.array([256, 256, 256])


# 3、读取视频中的帧画面，将画面中的每一帧都画上矩形
def draw_warning(frame):
    global pts
    frame_shape = frame.shape  #  (576, 704, 3) 监控画面原图的参数
    # print("frame_shape: ", frame_shape)
    x = frame_shape[0]
    y = frame_shape[1]
    frame_ones = np.ones(shape=(x, y), dtype=np.uint8) # 根据原图大小，转化成二值图

    pts = np.array(pts, np.int32)  # 将前端传递给我们的值转化为numpy数组
    cv2.polylines(frame_ones, [pts], True, 255)  # 给二值图画上区域
    cv2.fillPoly(frame_ones, [pts], (255, 255, 255))  # 给二值图的区域填充颜色
    cv2.polylines(frame, [pts], True, (0, 0,255))  # 给原图画上区域边框
    cv2.imshow("frame_ones", frame_ones)
    return frame_ones


# 绘制人的脚下区域
def point_color(frame, foot_box):
    # 左上角坐标
    x_min = foot_box[0][0]
    y_min = foot_box[0][1]
    # 右下角坐标
    x_max = foot_box[1][0]
    y_max = foot_box[1][1]

    # 读取画面尺寸
    frame_shape = frame.shape  #
    x = frame_shape[0]
    y = frame_shape[1]
    # 将图像二值化
    frame_ones = np.ones(shape=(x, y), dtype=np.uint8)

    # 将人物的脚步区域画成一个白色的矩形
    cv2.rectangle(frame_ones, foot_box[0], foot_box[1], 255, -1)
    cv2.imshow("frame_ones_peo", frame_ones)
    return frame_ones


# 将两个区域进行与操作
def area_merge(frame_1, frame_2):
    dst = cv2.bitwise_and(src1=frame_1, src2=frame_2)

    cv2.imshow("dst", dst)
    # 与操作之后，图像没有重叠的话，就全黑
    # 有重叠的话，就有部分是白色
    # 用均值的判断方式判断
    # mean => (1.0, 0.0, 0.0, 0.0)
    mean = cv2.mean(dst)[0]

    if mean <= 1: # 说明区域内没有人在
        print("mean: ", mean)
        return False
    else:
        print("mean: ", mean)
        return True





