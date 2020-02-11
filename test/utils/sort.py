import collections


class SampleQuickSort:
    def partition(self, arr, low, high):
        i = (low - 1)  # 最小元素索引
        pivot = arr[high]

        for j in range(low, high):

            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                print('%s,%s' % (i, j))

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # arr[] --> 排序数组
    # low  --> 起始索引
    # high  --> 结束索引

    # 快速排序函数
    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def test(self):
        arr = [7, 8, 9, 1, 5, 10]
        n = len(arr)
        self.quick_sort(arr, 0, n - 1)
        print("排序后的数组:")
        for i in range(n):
            print("%d" % arr[i])


class TwoQuickSort:
    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        i = low - 1
        # 基准
        pivot = arr[high]

        for j in range(low, high):
            if arr[j][2] < pivot[2]:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[j][2] == pivot[2]:
                if arr[j][1] <= pivot[1]:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def cvt_arr(self, d):
        r_l = list()
        for k, v in d.items():
            l = list()
            l.append(k)
            for i in range(len(v)):
                l.append(v[i])
            r_l.append(l)
        return r_l

    def cvt_order_dict(self, s_l):
        d = collections.OrderedDict()
        element_length = len(s_l[0])
        for i in range(len(s_l)):
            l = list()
            for j in range(1, element_length):
                l.append(s_l[i][j])
            d[s_l[i][0]] = tuple(l)
        return d

    def dict_to_arr(self, d):
        rl = list()
        for k, v in d.items():
            d = collections.OrderedDict()
            d['name'] = k
            d['width'] = v[1]
            d['height'] = v[0]
            rl.append(d)
        return rl

    def arr_to_dict(self, sls):
        d = collections.OrderedDict()
        for sl in sls:
            l = list()
            l.append(sl['width'])
            l.append(sl['height'])
            d[sl['name']] = tuple(l)
        return d

    def test(self):
        d = collections.OrderedDict()
        d["dfsdf"] = (630, 945)
        d["vxcv"] = (34, 1120)
        d["dfsv"] = (999, 34)
        d["dfsv1"] = (234, 34)
        d["dfsv2"] = (123, 34)
        d["dfsv3"] = (1, 34)
        d["dfxv"] = (123, 123)

        # # 排序一
        # l = self.dict_to_arr(d)
        # print(l)
        # l = sorted(l, key=lambda x: (x['width'], x['height']))
        # print(l)
        # print("排序前的数组:")
        # print(d)
        # print("排序后的数组:")
        # print(self.arr_to_dict(l))
        # print("\n")
        #
        # # 排序二
        # l = self.cvt_arr(d)
        # print(l)
        # l = sorted(l, key=lambda x: (x[2], x[1]))
        # print(l)
        # print("排序前的数组:")
        # print(d)
        # print("排序后的数组:")
        # print(self.cvt_order_dict(l))

        # 快排
        l = self.cvt_arr(d)
        print(l)
        self.quick_sort(l, 0, len(l) - 1)
        print("排序前的数组:")
        print(d)
        print("\n")
        print("排序后的数组:")
        print(self.cvt_order_dict(l))


class ImgQuickSort:
    def partition(self, arr, low, high):
        i = low - 1
        # 基准
        pivot = arr[high]

        for j in range(low, high):
            if arr[j][2] < pivot[2]:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[j][2] == pivot[2]:
                if arr[j][1] <= pivot[1]:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def cvt_arr(self, ds):
        rl = list()
        for k, v in ds.items():
            l = list()
            l.append(k)
            for n in range(len(v)):
                l.append(v[n])
            rl.append(l)
        return rl

    def cvt_dict(self, ls):
        ds = collections.OrderedDict()
        for l in ls:
            v = list()
            v.append(l[1])
            v.append(l[2])
            ds[l[0]] = tuple(v)
        return ds

    def my_sort(self, d):
        l = self.cvt_arr(d)
        self.quick_sort(l, 0, len(l) - 1)
        return self.cvt_dict(l)

    def test(self):
        d = collections.OrderedDict()
        d["dfsdf"] = (630, 945)
        d["vxcv"] = (34, 1120)
        d["dfsv"] = (999, 34)
        d["dfsv1"] = (234, 34)
        d["dfsv2"] = (123, 34)
        d["dfsv3"] = (1, 34)
        d["dfxv"] = (123, 123)

        # 快排
        l = self.cvt_arr(d)
        print(l)
        self.quick_sort(l, 0, len(l) - 1)
        print("排序前的数组:")
        print(d)
        print("排序后的数组:")
        print(self.cvt_dict(l))


if __name__ == "__main__":
    # s = SampleQuickSort()
    # s.test()
    #
    # t = TwoQuickSort()
    # t.test()

    iqs = ImgQuickSort()
    iqs.test()
