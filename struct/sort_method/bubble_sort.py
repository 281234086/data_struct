# 冒泡排序
# 依次比较两个值，若第一个比第二个大，则交换
# 对每一对相邻的元素进行比较，从开始到最后，做完之后，最后的元素为最大的数
def bubble_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    for i in range(len(sort_list)):  # 循环遍历整个列表
        for j in range(1, len(sort_list)-i):  # 每次遍历进行比较
            if sort_list[j-1] > sort_list[j]:
                sort_list[j], sort_list[j-1] = sort_list[j-1], sort_list[j]


li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)