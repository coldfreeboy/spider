#coding:utf-8
# 爬虫调度主程序
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain():

    def __init__(self):
        # 初始化各模块

        # url管理器
        self.urls = url_manager.UrlManager()

        # 下载器
        self.downloader = html_downloader.HtmlDownloader()

        # 解析器
        self.parser = html_parser.HtmlParser()

        # 输出器
        self.outputer = html_outputer.HtmlOutputer()



    def craw(self,root_url):

        
        count = 0
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print("craw %d : %s" %(count,new_url))

                html_cont = self.downloader.download(new_url)

                new_urls,new_data = self.parser.parse(new_url,html_cont)

                self.urls.add_new_urls(new_urls)

                self.outputer.collect_data(new_data)

                count=count+1

                if count == 100:
                    break
            except Exception as e:
                print("craw 失败:%s" % e)

        self.outputer.output_html()
        print(self.urls.get_count())
        

       



if __name__=="__main__":

    # 入口url
    root_url = "http://baike.baidu.com/view/21087.htm"

    # 主类
    obj_spider = SpiderMain()

    # 开爬
    obj_spider.craw(root_url)

# 爬虫构架
# 主程序 程序入口 spider_main.py  入口参数url
# url调度         url_manager.py  负责url存储与提供
# 页面解析        html_parser.py  解析页面 提取url title 简介
# 页面下载        html_downloader.py 根据url下载页面
# 页面输出        html_outputer.py 输出数据
