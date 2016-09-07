from bs4 import BeautifulSoup as bs
import re
import os.path
import urllib.parse
import html_downloader


class HtmlParser():

    def _get_new_urls(self,page_url,soup):
        urls = set()
        links = soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))
        
        for link in links:
            new_url  = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            urls.add(new_full_url)

        return urls

    def _get_data(self,page_url,soup):
        res_data={}

        #url
        res_data['url'] = page_url

        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1').get_text()

        res_data['title']  = title_node

        summary_node = soup.find('div',class_ ='lemma-summary' ).get_text()

        res_data['summary'] = summary_node

        return res_data



    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return 

        soup = bs(html_cont,'html.parser',from_encoding='utf-8')

        urls = self._get_new_urls(page_url,soup)

        data = self._get_data(page_url,soup)
        return (urls,data)

if __name__ == "__main__":
    url = "http://baike.baidu.com/view/21087.htm"
    u = '/view/1111.html'
    p  = HtmlParser()
    d = html_downloader.HtmlDownloader()

    html = d.download(url)
    



    urls,data=p.parse(url,html)

    print(urls)
    print("*"*50)
    print(data)