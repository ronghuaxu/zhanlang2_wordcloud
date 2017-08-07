# zhanlang2_wordcloud
《战狼2》电影豆瓣影评，爬取了8万多豆瓣短评。做了词云图。
## 碰到的一些问题：

* 因为评论的数据较多，使用jieba分词工具时，时间消耗很大，提高速度的方法， 设置多线程切割： jieba.enable_parallel(4)
* WordCloud使用时，对stopwords使用中文，一直没有效果，通过修改源代码函数达到目标：
