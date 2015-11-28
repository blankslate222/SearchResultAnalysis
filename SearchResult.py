import time
from flask import Flask, request
from SearchProcessor import SearchProcessor
from WordFrequencyCloud import WordFrequencyCloud
import traceback

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
    except Exception, err:
        traceback.print_exc()

    start = time.clock()
    word_freq_dict = processor.do_word_frequency_cloud(search_term)
    print 'time to get word_Freq_dict = %s' % (str(time.clock() - start))
    newstart = time.clock()
    generated_word_cloud_html = wfc.generate_cloud(word_freq_dict)
    print 'time to get html = %s' % (str(time.clock() - newstart))
    print 'total time = %s' % (str(time.clock() - start))
    return generated_word_cloud_html


@app.route('/search_results_cluster')
def cluster_controller():
    search_term = request.values.get('term')
    if search_term is None:
        return 'Search term is a required parameter'
    print search_term
    processor = SearchProcessor()
    start = time.clock()
    cluster_dict = processor.do_cluster()
    print 'time to get cluster_dict = %s' % (str(time.clock() - start))
    newstart = time.clock()

    print 'time to generate view = %s' % (str(time.clock() - newstart))
    print 'total time = %s' % (str(time.clock() - start))
    return "generating clusters..."


if __name__ == '__main__':
    app.run()
