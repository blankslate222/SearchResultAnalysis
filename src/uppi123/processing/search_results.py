import webhose
import codecs
import word_freq_generator


def get_query(search_term):
    """
    build query object for querying webhose using the sdk
    :param search_term: search term from app home page
    :return: web hose query string
    """
    site_types = ['blogs', 'news']
    webhose.config(token='d72a236b-f6d9-4c52-b2d1-cceb9734579a')
    q = webhose.Query()
    q.__setattr__('body_text', search_term)
    q.__setattr__('language', "english")
    q.__setattr__('site_type', site_types)
    print q.query_string()
    return q


def search(query):
    """
    retrieves result for the searched term from web hose
    uses webhose sdk to construct query object
    :param query:
    :return: search result as a json string
    """
    post = webhose.search(query)
    print post
    return post


def process_result(path, post):
    """
    process retrieved data and put them in files and a dictionary
    :param path: path of directory to store files for further processing
    :param post: json string which is the result of webhose search
    :return:
    """
    file_dict = {}
    result_list = post.posts
    i = 0
    for result in result_list:
        filename = "doc" + str(i)
        filepath = path + '\\' + filename
        result_doc = codecs.open(filepath, mode='w', encoding='utf-8')
        result_doc.write(result.text)
        result_doc.close()
        file_dict[result.url] = result.text
        i += 1
    return file_dict


def get_search_result(term):
    path = 'G:\Nikhil\MS\MS_SEM3\\239\project\data'
    webhose_query = get_query(term)
    webhose_data = search(webhose_query)
    file_content_dict = process_result(path, webhose_data)
    print file_content_dict
    word_freq_dict = word_freq_generator.generate_word_freq(path)
    return word_freq_dict
