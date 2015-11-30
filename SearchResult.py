import time
import traceback

from flask import Flask, request

from SearchProcessor import SearchProcessor
from TextCluster import TextCluster
from WordFrequencyCloud import WordFrequencyCloud

app = Flask(__name__)


@app.route('/')
def home():
    return app.send_static_file('home.html')


@app.route('/search_results_word_cloud')
def word_cloud_controller():
    search_term = request.values.get('term')
    if search_term is None:
        return 'Search term is a required parameter'
    print search_term
    try:
        processor = SearchProcessor()
        wfc = WordFrequencyCloud()
        start = time.clock()
        word_freq_dict = processor.do_word_frequency_cloud(search_term)
        print 'time to get word_Freq_dict = %s' % (str(time.clock() - start))
        newstart = time.clock()
        generated_word_cloud_html = wfc.generate_cloud(word_freq_dict, search_term)
        print 'time to get html = %s' % (str(time.clock() - newstart))
        print 'total time = %s' % (str(time.clock() - start))
    except Exception, err:
        traceback.print_exc()
    return generated_word_cloud_html


@app.route('/search_cluster')
def cluster_controller():
    search_term = request.values.get('term')
    if search_term is None:
        return 'Search term is a required parameter'
    print search_term
    cluster = TextCluster()
    html_text = cluster.get_clusters(search_term)
    return html_text


if __name__ == '__main__':
    app.run()
