class HtmlOutputer():
    def __init__(self):
        self.data = []

    def collect_data(self,new_data):
        if new_data is None:
            return 
        self.data.append(new_data)


    def output_html(self):
        s=""
        for i in self.data:
            s="%s%s"%(s,("<tr><td>%s</td><td>%s</td><td>%s</td></tr>\n"% (i["title"],i["url"],i['summary'])))

        html="""
<html>
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
        <table>
            <tr>
            <th>title</th>
            <th>url</th>
            <th>简介</th>
            </tr>
            %s
        </table>
    </body>

</html>
        """% s

        # print(html,type(html))
       

        with open("output.html",'wb') as f:
            f.write(html.encode('utf-8'))





        

        