import collections
import os
import shutil

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import mean_squared_error as mse_ski
from skimage.metrics import structural_similarity as ssim

# 比较图片的相似情况
from test.utils.fs import mkdir_loop
from test.utils.sort import ImgQuickSort


def compareImages(a_path, b_path):
    a = plt.imread(a_path)
    b = plt.imread(b_path)
    # 权重计算
    weight = np.array([0.64, 0.35, 0.01])
    a1 = np.dot(a, weight)
    b1 = np.dot(b, weight)

    m2 = mse_ski(a1, b1)  # skimage封装函数
    s = ssim(a1, b1)

    print("MSE With Ski: %.2f, SSIM: %.2f" % (m2, s * 100) + "%")


# 修改图片的大小，以小图为准
def change_size(path_a, path_b):
    a = cv2.imread(path_a)
    b = cv2.imread(path_b)

    a_height_width = a.shape[:2]
    b_height_width = b.shape[:2]
    height = a_height_width[0] if a_height_width[0] < b_height_width[0] else b_height_width[0]
    width = a_height_width[1] if a_height_width[1] < b_height_width[1] else b_height_width[1]

    a_dst = cv2.resize(a, (width, height), interpolation=cv2.INTER_AREA)
    b_dst = cv2.resize(b, (width, height), interpolation=cv2.INTER_AREA)

    # print(a_dst.shape[:2])
    # print(b_dst.shape[:2])
    return a_dst, b_dst


# 保存图片到磁盘
def sample_save_to_disk(a_src_path, b_src_path, a_dst_path, b_dst_path):
    if os.path.exists(a_dst_path) or os.path.exists(b_dst_path):
        a, b = change_size(a_src_path, b_src_path)

        # 将图片写入磁盘
        cv2.imwrite(a_dst_path, a)
        cv2.imwrite(b_dst_path, b)


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


def adjust_imgs(src_path, dst_path):
    pass


def sample_compare_two_img():
    src_base = "/home/john/tmp/images/src/"
    dst_base = "/home/john/tmp/images/dst/"

    a_path = '5e3e4d661ea3649bc2eb86b1.jpg'
    b_path = '5e3e4d681ea3649bc2eb86b4.jpg'

    a_src_path = src_base + a_path
    b_src_path = src_base + b_path
    a_dst_path = dst_base + a_path
    b_dst_path = dst_base + b_path

    sample_save_to_disk(a_src_path, b_src_path, a_dst_path, b_dst_path)

    compareImages(a_dst_path, b_dst_path)


if __name__ == '__main__':
    # sample_compare_two_img()
    classify_imgs('/home/john/tmp/images/src')
