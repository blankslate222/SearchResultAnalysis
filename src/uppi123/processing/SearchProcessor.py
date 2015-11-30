import codecs
import collections
import os

import webhose

from WordCloudGenerator import WordCloudGenerator


class SearchProcessor:
    """
    Retrieve results from webhose
    Process retrieved results
    Service layer
    """

    def __init__(self):
        self

    def get_query(self, search_term):
        """
        build query object for querying webhose using the sdk
        :param search_term: search term from app home page
        :return: web hose query string
        """
        site_types = ['news']
        webhose.config(token='d72a236b-f6d9-4c52-b2d1-cceb9734579a')
        q = webhose.Query()
        q.__setattr__('body_text', search_term)
        q.__setattr__('language', "english")
        q.__setattr__('site_type', site_types)
        print q.query_string()
        return q

    def search(self, query):
        """
        retrieves result for the searched term from web hose
        uses webhose sdk to construct query object
        :param query:
        :return: search result as a json string
        """
        post = webhose.search(query)
        # print post
        return post

    def process_result(self, post, path=None):
        """
        process retrieved data and put them in files and a dictionary
        :param path: path of directory to store files for further processing
        :param post: json string which is the result of webhose search
        :param to_file: whether to write to a file or not
        :return: dictionary mapping search result url to text
        """
        file_dict = collections.OrderedDict()
        result_list = post.posts

        if path is not None:
            i = 0
            for result in result_list:
                filename = "doc" + str(i)
                filepath = path + os.sep + filename
                result_doc = codecs.open(filepath, mode='w', encoding='utf-8')
                result_doc.write(result.text)
                result_doc.close()
                file_dict[result.url] = result.text
                i += 1
        else:
            print 'direct to dictionary'
            for result in result_list:
                file_dict[result.url] = result.text

        return file_dict

    def get_data(self, term):
        webhose_query = self.get_query(term)
        webhose_data = self.search(webhose_query)
        return webhose_data

    def do_word_frequency_cloud(self, term):
        """
        function to return html for word cloud
        :param term: the search term
        :param test:
        :return: html code as string
        """
        path = 'G:\Nikhil\MS\MS_SEM3\\239\project\data'

        wc_gen = WordCloudGenerator()

        webhose_data = self.get_data(term)
        file_content_dict = self.process_result(webhose_data)
        # file_content_dict = self.process_result(webhose_data, path) # only for testing
        # exit(0)
        # print file_content_dict
        if len(file_content_dict) > 0:
            word_freq_dict = wc_gen.generate_word_freq(path, file_content_dict)
        else:
            word_freq_dict = {}

        return word_freq_dict
