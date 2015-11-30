import json
from string import Template

import requests
from yattag import Doc


class TextCluster:
    def __init__(self):
        self

    def get_clusters(self, term):
        json_response = self.get_carrot_results(term)
        html_string = self.parse_json_response(json_response, term)
        return html_string

    def get_carrot_results(self, term):
        url = 'http://localhost:8080/Carrot/search_cluster?term=%s' % term
        response = requests.get(url=url)
        print response.status_code
        body = response.content
        return body

    def parse_json_response(self, result, term):
        html_template = "<html> \
        <head> \
        <title> Uppi123 Clusters </title>\
        <style> body {background-color:whitesmoke;} </style>\
        </head>\
        <body> \
        <h2> Search Results Cluster List -> Search Keyword: %s </h2> <a href='http://127.0.0.1:5000/'>Search Again</a>\
         $result \
        </body> \
        </html>" % (term)
        template = Template(html_template)
        context = {}
        context['result'] = self.generate_html_table(result)
        html_text = template.substitute(context)
        return html_text

    def generate_html_table(self, result_json):
        jsonobj = json.loads(result_json)
        doc = Doc()
        tag = doc.tag
        text = doc.text

        textarea = '<li><a href="%(link)s">%(title)s</a></li>'

        for cluster in jsonobj:
            # print cluster['clusterLabel']
            with tag(tag_name='div', id=cluster['clusterLabel']):
                with tag('h3'):
                    text(cluster['clusterLabel'])
                for result in cluster['results']:
                    with tag(tag_name='ul'):
                        txt = "".join(textarea % {'link': result['url'], 'title': result['title']})
                        doc.asis(txt)
                        # print txt
                        # text(txt)
        print doc.getvalue()
        htmlcode = doc.getvalue()
        # print htmlcode
        return htmlcode
