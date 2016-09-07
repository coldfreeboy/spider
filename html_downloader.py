# 下载模块
# from urllib import request as rq
import urllib.request as rq

class HtmlDownloader():

    def download(self,url):
        if url is None:
            return

        obj_rq = rq.Request(url)

        # 释放gc资源
        with rq.urlopen(obj_rq,timeout=20) as response:
            if response.code != 200:
                return None

            return response.read()


if __name__ == "__main__":
    # print(type(HtmlDownloader().download("http://www.baidu.com")))
    print(dir(rq))

        