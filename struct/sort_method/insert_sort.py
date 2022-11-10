# 插入排序，
# 排序思想： 从第一个元素开始，该元素可以认为已经被排序
# 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 将新元素插入到该位置后
# 重复步骤2~5

def insert_sort(list1):
    if len(list1) < 2:
        return list1
    for i in range(1, len(list1)):
        cur = list1[i]  # 指定下一个元素
        k = i  # 下标
        while k > 0 and list1[k-1] > cur:
            list1[k] = list1[k-1]
            k -= 1
        list1[k] = cur
    return list1

if __name__ == '__main__':
    list1 = [2,3,12,11,23,21,22,4]
    print(insert_sort(list1))