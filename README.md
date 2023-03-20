# 利用yolov5做区域告警



## 配置：

- yolov5.5
- python和其他的支撑请查阅官方文档要求



## 项目改造

- 主要对detect文件进行结果处理
- 获取视频流原图和copy之后的图进行图像操作
- 获取人与规定的区域是否重合



## detect.py 文件

154行增加了一句代码：

```
frame_area = regional_alarm.draw_warning(im0) # 目的是：绘制一块与视频分辨率大小一致的蒙版
````

183行增加了一段代码

```
foot_box = xyxy2xycenter.xyxy_to_wh(xyxy)
if foot_box:
     print("foot_box", foot_box)
     frame_peo = regional_alarm.point_color(im0.copy(), foot_box)  # 人物脚下区域的返回参数
      result = regional_alarm.area_merge(frame_area, frame_peo)
     if result is True:
          # label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
           label = f" Person Warning "
           annotator.box_label(xyxy, label, color=colors(2, True))
       else:
          label = f" Person Safe "
          annotator.box_label(xyxy, label, color=colors(0, True))
```

## regional_alarm.py 文件

##### draw_warning 模块

将4个点绘制成一个封闭填充满的区域

##### point_color 模块

将出现的人的坐标变成一块封闭的矩形

##### area_merge 模块

将4个点绘制的区域和人的脚下区域进行与操作， 判断蒙版的平均色值



## **xyxy2xycente.py文件**

将目标点坐标获取后，转换成二分之一高度的点位坐标，返回新的坐标点给主程序





