# 快速排序
# 思想： 选出一个基准，对基准左侧与右侧的分别排序,直到排序完成
def quickly_sort(list_1):
    if len(list_1) < 2:
        return list_1
    item = list_1[0]
    less = [i for i in list_1[0:] if i < item]
    great = [j for j in list_1[0:] if j > item]
    return quickly_sort(less) + list(item) + quickly_sort(great)

if __name__ == '__main__':
    list1 = [2,3,411,23,4,21,32,1]
    print(quickly_sort(list1))
