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





if __name__ == '__main__':
    sample_compare_two_img()
