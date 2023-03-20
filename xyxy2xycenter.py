# 根据xyxy坐标，返回脚步foot的坐标集
def xyxy_to_wh(xyxy):
    left_top_x = xyxy[0].item()
    left_top_y = xyxy[1].item()
    re_bottom_x = xyxy[2].item()
    re_bottom_y = xyxy[3].item()

    w = re_bottom_x - left_top_x
    h = re_bottom_y - left_top_y

    left_foot_box_x = int(left_top_x)
    left_foot_box_y = int(re_bottom_y - w / 2)

    foot_box = [[left_foot_box_x, left_foot_box_y], [int(re_bottom_x), int(re_bottom_y)]]
    return foot_box