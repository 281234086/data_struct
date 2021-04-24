# 选择排序
# 选择排序思想：找到最小(大)的元素，将该元素放在列表的最前(后)端
def select_sort(list1):
    new_list = []
    while list1:
        max_item = list1[0]
        for i in range(1, len(list1)):
            if max_item < list1[i]:
                max_item = list1[i]
        list1.remove(max_item)
        new_list.insert(0, max_item)
    return new_list

if __name__ == '__main__':
    list_test = [1,2,3,12,11,14,13]
    print(select_sort(list_test))
