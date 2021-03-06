import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count =1
        print("根网址：",root_url)
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d: %s",count,new_url)
                html_cont = self.downloader.download(new_url)
                # print("下载的网站数据",html_cont)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count ==2:
                    break
                count += 1
            except:
                print("The url is invalide.")
        self.outputer.outupt_html()

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider.craw(root_url)
    obj_spider = SpiderMain()