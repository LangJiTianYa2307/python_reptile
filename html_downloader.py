import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        #print(response.read().decode('UTF-8'))
        return response.read()
