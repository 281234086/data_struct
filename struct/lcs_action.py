# 最大公共子串
# 判断两个字符串相同的开始和结束节点，以及最大长度

def lscUseDirectIterator(str1, str2):

    if str1 == '' and str2 == '':
        return ''
    max_length = 0  # 公共子串最大长度
    max_end = 0  # 最后一个公共字符的index
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                index1 = i  # m为迭代str1的临时index
                index2 = j  # n为迭代str2的临时index
                temp_length = 0  # 最大公共子串长度
                while index1 < len(str1) and index2 <len(str2) and str1[index1] == str2[index2]:
                    temp_length += 1
                    index2 += 1
                    index1 += 1
                if temp_length > max_length:
                    max_length = temp_length
                    max_end = index1
    if max_length == 0:
        return ''
    else:
        start_index = int(max_end-max_length)
        end_index = int(max_end)
        result = str1[start_index:end_index]  # 列表获取
        return result

if __name__ == '__main__':
    lscUseDirectIterator('hello', 'lloppop')
    print(lscUseDirectIterator('hello', 'lloppop'))