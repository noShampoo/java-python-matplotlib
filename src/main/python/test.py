import sys
# 评估指标
def MetricsValue(x, y):
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    # p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    plt.figure(figsize=(15, 50))  # 创建绘图对象
    plt.title('Test')
    plt.plot(p, x, color='green', label='Odd number is 0')
    plt.plot(p, y, color='red', label='Even number is 0')
    # plt.plot(p, z, label='score_people')s
    plt.legend()  # 显示图例

    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    plt.savefig("test.png");


if __name__ == '__main__':
    print("=============start-------------")
    # 存放所有的参数 最后一个为第一个列表的长度（分割时用）
    list_str = []
    # 存放字符型list
    list1_str = []
    list2_str = []
    # 字符型转换为int型
    list_int = []
    list1_int = []
    list2_int = []

    for i in range(1, len(sys.argv)):
        list_str.append(sys.argv[i].replace(",", ""))
    # 处理第一个还有最后一个元素的格式
    list_str[0] = list_str[0].replace("[", "")
    list_str[len(sys.argv) - 2] = list_str[len(sys.argv) - 2].replace("]", "")

    # 取出最后一个数作为第一个列表的长度来分割列表
    list1Size = int(list_str[len(list_str) - 1])
    # print("list1Size==", list1Size)
    # 根据size取出第一个列表list[a:b]表示取出下表为a到下标为b-1的值组成一个list
    list1_str = list_str[0:list1Size]
    # print("list1_str==", list1_str)
    # 取出第二个列表
    list2_str = list_str[list1Size:len(list_str) - 1]
    # print("list2_str==", list2_str)
    # 将str转换为int
    list_int = list(map(int, list_str))
    list1_int = list(map(int, list1_str))
    list2_int = list(map(int, list2_str))
    print(MetricsValue(list1_int, list2_int))