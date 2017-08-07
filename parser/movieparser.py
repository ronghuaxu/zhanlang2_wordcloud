# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


def get_douban_comments(res):
    comments_list = []  # 评论列表
    soup = BeautifulSoup(res)
    comment_nodes = soup.select('.comment > p')
    for node in comment_nodes:
        comments_list.append(node.get_text().strip().replace("\n", "") + u'\n')
    return comments_list
