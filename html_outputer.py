class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def outupt_html(self):
        fout = open('output.html','w',encoding='utf-8')
        fout.write("<html>")
        # fout.write('<head><meta charset="utf-8"></head>')
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<tr>%s</td>"%data['url'])
            fout.write("<tr>%s</td>" % data['title'])
            fout.write("<tr>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")