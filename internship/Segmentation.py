import jieba
import jieba.posseg as pseg
import pandas as pd
import os


def processing(path, path_res):
    # 拿数据
    data = pd.read_excel('/Users/mato/Desktop/奶粉/好评/' + path)['评论内容']
    words = []
    flags = []
    for i in range(len(data)):
        comment = data.iloc[i]
        sentence_segment = jieba.posseg.cut(comment)
        for k in sentence_segment:
            words.append(k.word)
            flags.append(k.flag)
    word_data = pd.DataFrame()
    word_data['词'] = words
    word_data['词性'] = flags
    # 分组排序
    word_data = word_data.groupby(['词', '词性']).size().sort_values(ascending=False).reset_index()  # 没有索引无法进行下面的map处理
    word_data.columns = ['词', '词性', 'count']
    # 去除停用词
    word_data = word_data[word_data['词'].map(lambda x: x not in stopwords)]
    # 去除非中文
    word_data = word_data[word_data['词'].map(lambda x: '\u4e00' <= x <= '\u9fff')]
    # 去除单个字
    word_data = word_data[word_data['词'].map(lambda x: len(x) != 1)].reset_index(drop=True)  # 重置索引
    word_data.to_excel(path_res + path)


if __name__ == '__main__':
    path1 = '/Users/mato/Desktop/奶粉/好评'
    path2 = '/Users/mato/Desktop/奶粉/差评'
    path1_res = '/Users/mato/Desktop/奶粉/好评结果/'
    path2_res = '/Users/mato/Desktop/奶粉/差评结果/'

    # 获得顺序的excel名
    path1_list = os.listdir(path1)
    path1_list.sort(key=lambda x: int(x.split('.')[0]))
    path2_list = os.listdir(path1)
    path2_list.sort(key=lambda x: int(x.split('.')[0]))

    # 获得停用词
    stopwords = [i.strip() for i in open('../data_pre-processing/chineseStopWords.txt', 'r', encoding='gbk').readlines()]  # 去掉换行符

    for i in path1_list:
        processing(i, path1_res)
    for i in path2_list:
        processing(i, path2_res)



