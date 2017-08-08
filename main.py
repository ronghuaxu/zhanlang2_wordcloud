# -*- coding:utf-8 -*-
import random
import time

from downloader import download as dd
from zhanlangparser import movieparser as ps
import codecs

if __name__ == '__main__':

    templateurl = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P';
    with codecs.open('pjl_comment.txt', 'a', encoding='utf-8') as f:
        # 4249
        for i in range(4249):
            print ('开始爬取{}页评论...', i)
            targeturl = templateurl.format(i * 20)
            res = dd.download_page(targeturl)
            f.writelines(ps.get_douban_comments(res))
            time.sleep(1 + float(random.randint(1, 20)) / 20)
