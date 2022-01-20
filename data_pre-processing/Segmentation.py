import jieba
import jieba.posseg as pseg  # 判断词性
import pandas as pd
from collections import Counter  # 来统计每个词出现的次数（value_counts：这是panda的）

'''
jieba分词
'''

# anaconda中没有jieba，需要使用：pip install jieba -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
s = '指南者留学线上教育，指南者留学背景提升项目实训营'
# 三种模式
# 1.精确模式：试图将句子最精地切开，适合文本分析
# 2.全搜索：把句子中所有的可以成词的词语都扫描出来，速度非常快，但是不能解决歧义
# 3.搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词

# 精确模式
print(list(jieba.cut(s)))  # cut_all为False
# 全模式
print(list(jieba.cut(s, cut_all=True)))
# 搜索引擎模式
print(list(jieba.cut_for_search(s)))

# 自定义添加词典
jieba.add_word('指南者留学', 5)  # 词频，大概意思可能是词频越高，越把这个词一起分出来
print(list(jieba.cut(s)))


data = pd.read_excel('QQ音乐评论.xlsx')
# 对评论数据进行切词
words = []
for i in range(len(data)):
    # 取出当前评论
    comment = data['评论'].iloc[i]
    # 对评论进行切词
    cut_word = list(jieba.cut(str(comment)))
    # 把切词的结果存入列表
    # 为什么用extend，因为拿到的是list，append的话是把list加进去，extend是把list里的内容加进去
    words.extend(cut_word)
# 转化为dataframe的格式
# 字典转dataframe得加个[]
# <class 'collections.Counter'>;T:转成竖的;reset_index():重置（加个）索引列，0、1、2、3;Counter：计算数量
dfs = pd.DataFrame([dict(Counter(words))]).T.reset_index()
dfs.columns = ['词', '词频']  # 重命名列明
dfs = dfs.sort_values(by='词频', ascending=False)  # 排序
# 导入停用词表(为啥不用pandas：txt不是pd的呢两种数据结构，不过也能用，没必要)
stopwords = [i.strip() for i in open('chineseStopWords.txt', 'r', encoding='gbk').readlines()]  # 去掉换行符
print(stopwords)


words2 = []
flags = []
for x in range(len(data)):
    # 取出当前评论
    comment = data['评论'].iloc[x]
    # 进行切词和词性标注(详细词性：https://github.com/fxsjy/jieba)
    sentence_segment = jieba.posseg.cut(comment)
    for i in sentence_segment:
        words2.append(i.word)
        flags.append(i.flag)
# 将这两列数据存入dataframe
word_data = pd.DataFrame()
word_data['词'] = words2
word_data['词性'] = flags
word_data = word_data.groupby(['词', '词性']).size().sort_values(ascending=False).reset_index()  # 同一个词词性可能不同;这二.size这个值就直接添加到了data里
word_data.columns = ['词', '词性', 'count']
# 去除停用词
word_data = word_data[word_data['词'].map(lambda x: x not in stopwords)]  # 这个写法注意一下，可能是x not in后会返回true，然后这个词会保留下来
# 去除非中文
word_data = word_data[word_data['词'].map(lambda x: '\u4e00' <= x <= '\u9fff')]

# 统计每个词性出现的次数(count这里一个中括号返回series，两个返回dataframe)
new = word_data.groupby('词性')[['count']].sum().reset_index().sort_values(by='count', ascending=False)
print(new)

