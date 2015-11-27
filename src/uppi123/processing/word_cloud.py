import codecs
from pytagcloud import create_html_data, make_tags, LAYOUT_HORIZONTAL
from string import Template
"""
word_freq_tup_list = []
word_freq_tup_list.append(('nikhil', 5))
word_freq_tup_list.append(('rocky', 8))
word_freq_tup_list.append(('arnold', 10))
word_freq_tup_list.append(('ranbir', 1))
# tags = make_tags(word_freq_tup_list)

# print tags

# exit(0)
"""


def generate_cloud(cloud_words):
    generated_html = generate_html(cloud_words)
    return generated_html


def generate_html(word_freq_tup_list):
    """
    this function generates html file depicting word cloud word_freq_tup is passed by the caller
    :param word_freq_tup_list:
    :return: generated word cloud html text
    """

    tags = make_tags(word_freq_tup_list)
    print tags

    cloud_html = create_html_data(tags[:100], (500, 600), layout=LAYOUT_HORIZONTAL, fontname='PT Sans Regular')

    template_file = codecs.open('G:\\Nikhil\\MS\\MS_SEM3\\239\\project\\files\\template.html', mode='r',
                                encoding='utf-8')
    html_template = Template(template_file.read())
    context = {}

    # change href attribute in a tag to give link to data display
    tags_template = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; height: %(height)dpx;">' \
                    '<a class="tag %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
        left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; line-height:%(lh)dpx;">%(tag)s</a></li>'

    context['tags'] = ''.join([tags_template % link for link in cloud_html['links']])
    context['width'] = cloud_html['size'][0]
    context['height'] = cloud_html['size'][1]
    context['css'] = "".join("a.%(cname)s{color:%(normal)s;}\
        a.%(cname)s:hover{color:%(hover)s;}" %
                             {'cname': k,
                              'normal': v[0],
                              'hover': v[1]}
                             for k, v in cloud_html['css'].items())

    html_text = html_template.substitute(context)
    return html_text

# print generate_cloud(word_freq_tup_list)