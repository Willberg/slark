import collections
import os
import shutil

import cv2

# 比较图片的相似情况
from test.utils.fs import mkdir_loop
from test.utils.sort import ImgQuickSort


# 归类图片
def classify_imgs(src_path):
    dir_names = set()

    # 扫描所有文件，获得路径
    ds = os.listdir(src_path)
    dis = collections.OrderedDict()
    for d in ds:
        f = os.path.join(src_path, d)
        if os.path.isfile(f):
            # 获取图片高度和宽度，形成dict
            img = cv2.imread(f)
            img_height_width = img.shape[:2]
            dis[d] = img_height_width
        elif os.path.isdir(f):
            title = f.title().split('/')[-1].lower()
            if 'x' in title:
                dir_names.add(title)

    # 分别以长和宽进行排序
    iqs = ImgQuickSort()
    dis = iqs.my_sort(dis)

    # 以最小长宽为目录名建立目录，划分依据长宽比例不得大于1%，并移动文件
    for k, v in dis.items():
        width, height = v[1], v[0]
        dst_path = None
        for dir_name in dir_names:
            # 基准宽度，高度比较
            p_w, p_h = dir_name.split('x')
            p_w = int(p_w)
            p_h = int(p_h)
            if p_w * 99 <= width * 100 <= p_w * 101 and p_h * 99 <= height * 100 <= p_h * 101:
                dst_path = src_path + "/" + dir_name
                break

        # 找不到路径说明不存在
        if not dst_path:
            dir_name = str(width) + 'x' + str(height)
            dst_path = src_path + "/" + dir_name
            mkdir_loop(dst_path)
            dir_names.add(dir_name)

        if not os.path.exists(dst_path + '/' + k):
            shutil.move(src_path + '/' + k, dst_path)
        else:
            img_name = src_path + '/' + k
            os.remove(img_name)
            print(img_name)


# 调整图片
def adjust_imgs(src_path, dst_path):
    dir_names = set()
    # 扫描所有文件，获得路径
    ds = os.listdir(src_path)
    for d in ds:
        f = os.path.join(src_path, d)
        if os.path.isdir(f):
            title = f.title().split('/')[-1].lower()
            if 'x' in title:
                dir_names.add(title)

    # 构造存放路径和修改尺寸
    for dir_name in dir_names:
        width, height = dir_name.split("x")
        width = int(width)
        height = int(height)
        save_path = dst_path + '/' + dir_name
        if not os.path.exists(save_path):
            mkdir_loop(save_path)

        # 调整图片并保存
        ds = os.listdir(src_path + "/" + dir_name)
        for d in ds:
            f = os.path.join(src_path, dir_name, d)
            if os.path.isfile(f):
                title = f.title().split('/')[-1].lower()
                if not os.path.exists(save_path + "/" + title):
                    img = cv2.imread(f)
                    cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
                    cv2.imwrite(save_path + "/" + title, img)


if __name__ == '__main__':
    classify_imgs('/home/john/tmp/images/src')
    adjust_imgs('/home/john/tmp/images/src', '/home/john/tmp/images/dst')
