import json

from yattag import Doc

doc = Doc()
tag = doc.tag
text = doc.text
list = ['a', 'b']

jsonstr = '[{"clusterLabel":"Detroit Lions", \
"results":[{"url":"http://omgili.com/r/jHIAmI4hxg_Onobag4zFn.hBe6y2DYjgjsOWUHMfSbd.iepZGe4ufBzN12.L9XLorD1_i0CSMQO0NCjYcoiutL4NoMDHzzPUFFA6ZmNi5hV0LWGjhJEPG9p7wAH1ZDJEkUn2W30FkIwCqLYR8vFoZgXsyWI7e50N", \
"title":"Patriots-Broncos missing a key cast member: Peyton Manning"},\
{"url":"abc",\
"title":"abc"}]\
}]'

textarea = '<li><a href="%(link)s">%(title)s</a></li>'
jsonobj = json.loads(jsonstr)
doc = Doc()
tag = doc.tag
text = doc.text

for cluster in jsonobj:
    # print cluster['clusterLabel']
    with tag(tag_name='div', id=cluster['clusterLabel']):
        with tag('h3'):
            text(cluster['clusterLabel'])
        for result in cluster['results']:
            with tag(tag_name='ul'):
                txt = "".join(textarea % {'link': res['url'], 'title': res['title']} for res in cluster['results'])
                doc.asis(txt)
                # print txt
                # text(txt)
print doc.getvalue()
