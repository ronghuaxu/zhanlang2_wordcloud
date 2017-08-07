# -*- coding:utf-8 -*-
import codecs
from os import path

import jieba
from scipy.misc import imread
from wordcloud import WordCloud
import pandas as pd

# 这个函数暂时没有用到
def get_all_keywords(file_name):
    word_lists = []  # 关键词列表
    jieba.enable_parallel(8)
    with codecs.open(file_name, 'r', encoding='utf-8') as f:
        Lists = f.readlines()  # 文本列表
        for List in Lists:
            cut_list = list(jieba.cut(List))
            for word in cut_list:
                word_lists.append(word)
    word_lists_set = set(word_lists)  # 去除重复元素
    word_lists_set = list(word_lists_set)
    length = len(word_lists_set)
    print u"共有%d个关键词" % length
    information = pd.read_excel('/Users/huazi/Desktop/zhanlang2.xlsx')
    world_number_list = []
    word_copy=[]
    for w in word_lists_set:
        if (len(w) == 1):
            continue
        if (word_lists.count(w) > 3):
            world_number_list.append(word_lists.count(w))
            word_copy.append(w)
    information['key'] = word_copy
    information['count'] = world_number_list
    information.to_excel('sun_2.xlsx')


# 绘制词云
def save_jieba_result():
    # 设置多线程切割
    jieba.enable_parallel(4)
    dirs = path.join(path.dirname(__file__), '../pjl_comment.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()
    cut_text = " ".join(jieba.cut(comment_text))  # 将jieba分词得到的关键词用空格连接成为字符串
    with codecs.open('pjl_jieba.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)


def draw_wordcloud2():
    dirs = path.join(path.dirname(__file__), 'pjl_jieba.txt')
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()

    color_mask = imread("template.png")  # 读取背景图片

    stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是', u'什么', u'没有', u'这个', u'那个', u'大家', u'比较', u'看到', u'真是',
                 u'除了', u'时候', u'已经', u'可以']
    cloud = WordCloud(font_path="/Users/huazi/Desktop/simsunttc/simsun.ttc", background_color='white',
                      max_words=2000, max_font_size=200, min_font_size=4, mask=color_mask, stopwords=stopwords)
    word_cloud = cloud.generate(comment_text)  # 产生词云
    word_cloud.to_file("pjl_cloud.jpg")


save_jieba_result()
draw_wordcloud2()
