import codecs
import os
from string import Template

from pytagcloud import create_html_data, make_tags, LAYOUT_HORIZONTAL


class WordFrequencyCloud:
    """
    uses pytagcloud library to generate word cloud html code
    """

    def __init__(self):
        self

    def generate_cloud(self, cloud_words, search_term):
        generated_html = self.generate_html(cloud_words, search_term)
        return generated_html

    def generate_html(self, word_freq_tup_list, search_term):
        """
        this function generates html file depicting word cloud word_freq_tup is passed by the caller
        :param word_freq_tup_list:
        :return: generated word cloud html text
        """
        tags = make_tags(word_freq_tup_list)
        # print tags

        cloud_html = create_html_data(tags[:100], (500, 500), layout=LAYOUT_HORIZONTAL, fontname='PT Sans Regular')
        temp_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..', 'templates', 'template.html'))
        template_file = codecs.open(temp_path, mode='r', encoding='utf-8')
        html_template = Template(template_file.read())
        context = {}

        # TODO: change href attribute in a tag to give link to data display
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
        context['mycss'] = "\
            #word_f { \
            height: 300px; \
            -webkit-column-count: 5; \
            -moz-column-count: 5; \
            column-count: 5; \
            } \
            #word_f li { \
            display: block; \
            }\
            #word_f li a { \
            color: rgb(0, 162, 232); \
            }"

        context['word_freq'] = "".join(
            "<li> %(key)s => %(val)s </li>" % {'key': t[0], 'val': str(t[1])} for t in word_freq_tup_list)

        context['page_title'] = 'Search Term : %s - Frequency Based Word Cloud - Top 100 words from search \
            results (length(word) >= 3)' % search_term
        context['list_title'] = '300 features extracted and their corresponding frequencies'
        html_text = html_template.substitute(context)
        return html_text
