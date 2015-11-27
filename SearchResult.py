from flask import Flask, request
import search_results
import word_cloud

app = Flask(__name__)


@app.route('/freq_word_cloud')
def freq_based_word_cloud():
    return app.send_static_file('f_word_cloud.html')


@app.route('/')
def home():
    return app.send_static_file('home.html')


@app.route('/search')
def search_handler():
    search_term = request.values.get('term')
    print search_term
    word_freq_dict = search_results.process_term(search_term)
    generated_word_cloud_html = word_cloud.generate_cloud(word_freq_dict)
    return generated_word_cloud_html


if __name__ == '__main__':
    app.run()
