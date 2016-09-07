# url管理器


class UrlManager():

    def __init__(self):
        self.urls = set()        #排除相同urls库
        self.new_urls = []       #list(set(),set()...)格式 安顺序被查询urls
        self.tmp_urls = []        #当前正在被查询url列表 等于list(new_urls.pop(0))

        # self.new_urls = set()
        # self.old_urls = set()
    def get_count(self):
        return len(self.urls)

    def add_new_url(self,url):
        if url is None:
            return
        d = set()
        d.add(url)

        d = d-self.urls

        if len(d):
            self.urls.update(d)
            self.new_urls.append(d)



    # def add_new_url(self,url):
    #     if url is None:
    #         return
    #     if url not in self.new_urls and url not in self.old_urls:
    #         self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return

        datas = urls - self.urls
        if len(datas):
            self.urls.update(datas)
            self.new_urls.append(datas)

    # def add_new_urls(self,urls):
    #     if urls is None or len(urls) == 0:
    #         return 
    #     for url in urls:
    #         self.add_new_url(url)


    # 查询数据库数据 当前库没有url从new_urls库中提取
    def has_new_url(self):
        if not len(self.tmp_urls):
            if not len(self.new_urls):
                return 0
            else:
                self.tmp_urls=list(self.new_urls.pop(0))
                return True
                # print(self.tmp_urls)
        else:
            return True

        # return len(self.new_urls)!=0

    def get_new_url(self):
        url = self.tmp_urls.pop(0)
        return url

    # def get_new_url(self):

    #     url = self.new_urls.pop()
    #     self.old_urls.add(url)
    #     return url



