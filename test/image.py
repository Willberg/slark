import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import mean_squared_error as mse_ski
from skimage.metrics import structural_similarity as ssim


def compareImages(imageA, imageB):
    # 权重计算
    weight = np.array([0.64, 0.35, 0.01])
    a1 = np.dot(imageA, weight)
    b1 = np.dot(imageB, weight)

    m2 = mse_ski(a1, b1)  # skimage封装函数
    s = ssim(a1, b1)

    print("MSE With Ski: %.2f, SSIM: %.2f" % (m2, s))


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


if __name__ == '__main__':
    src_base = "/home/john/tmp/images/src/"
    dst_base = "/home/john/tmp/images/dst/"

    a_path = '5e3e4d661ea3649bc2eb86b1.jpg'
    b_path = '5e3e4d681ea3649bc2eb86b4.jpg'

    a_dst_path = dst_base + a_path
    b_dst_path = dst_base + b_path

    if os.path.exists(a_dst_path) or os.path.exists(b_dst_path):
        a, b = change_size(src_base + a_path, src_base + b_path)

        # 将图片写入磁盘
        cv2.imwrite(a_dst_path, a)
        cv2.imwrite(b_dst_path, b)

    a = plt.imread(dst_base + a_path)
    b = plt.imread(dst_base + b_path)

    compareImages(a, b)
