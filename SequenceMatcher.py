import AcquireData

def Levenshtein(text1, text2):
    """
    Levenshtein编辑距离
    :param text1:字符串1
    :param text2:字符串2
    :return:相似度，float值
    """
    import Levenshtein
    distance = Levenshtein.distance(text1, text2)
    Similarity = 1 - distance * 1.0 / max(len(text1), len(text2))
    return Similarity


def read(path1, path2):
    f1 = open(path1, "r", encoding="utf-8")
    f2 = open(path2, "a", encoding="utf-8")
    i = 0
    lables = [0]
    lines = f1.readlines()
    for line in lines:
        i += 1
        line = line.strip('\n')
        data = line.split('"')
        string1 = data[1].split('"')
        string2 = data[2].split('"')
        flag = Levenshtein(data[5], data[9])
        if flag < 0.4:
            lables.append(1)
        else:
            lables.append(0)
        lable = str(lables[i])
        newline = str(i) + "   "
        newline = newline + '"' + data[5] + '"' + ", " + '"' + data[9] + '"'
        f2.write(newline + "    lable: " + lable + '\n')
    f1.close()
    f2.close()



path = input("数据源：")
txt1 = input("数据文本库:")
txt2 = input("结果文本库:")

AcquireData.Acquiredata(path, txt1)
read(txt1, txt2)




