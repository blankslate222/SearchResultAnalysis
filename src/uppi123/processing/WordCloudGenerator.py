import collections
import os
import string
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer


class WordCloudGenerator:
    """
    uses nltk and sci-kit's sklearn libraries to vectorize the documents
    calls functions that return word cloud
    """
    def __init__(self):
        self

    def stem_tokens(self, tokens, stemmer):
        stemmed = []
        for item in tokens:
            stemmed.append(stemmer.stem(item))
            # stemmed.append(item)
        # print stemmed
        return stemmed

    def tokenize(self, text):
        stemmer = PorterStemmer()
        tokens = nltk.word_tokenize(text)
        stems = self.stem_tokens(tokens, stemmer)
        return stems

    def sort_dict(self, tup):
        print tup
        return tup[1]

    def sort_file_name(self, filename):
        return int(filename[3:])

    def get_token_dictionary(self, path):
        """

        :param path:
        :return:
        """
        token_dict = collections.OrderedDict()
        for subdir, dirs, files in os.walk(path):
            for file in sorted(files, key=self.sort_file_name):
                file_path = subdir + os.path.sep + file
                shakes = open(file_path, 'r')
                text = shakes.read()
                lowers = text.lower()
                no_punctuation = lowers.translate(None, string.punctuation)
                token_dict[file] = no_punctuation
        return token_dict

    def generate_word_freq(self, path, t_d=None):
        """

        :param path:
        :param t_d:
        :return:
        """
        # for testing and overloading
        if t_d is None:
            token_dict = self.get_token_dictionary(path)
        else:
            token_dict = t_d

        vectorizer = CountVectorizer(tokenizer=self.tokenize, stop_words='english', min_df=1, max_features=300)
        count_matrix = vectorizer.fit_transform(token_dict.values()).toarray()
        words = np.array(vectorizer.get_feature_names())

        word_freq_dict = collections.OrderedDict()

        for i in range(len(count_matrix)):
            for j in range(len(words)):  # can also be count_matrix[i] or count_matrix[0]
                if count_matrix[i][j] != 0:
                    # print "doc_num = %s word = %s, freq = %s" % (str(i), words[j], count_matrix[i][j])
                    if words[j] in word_freq_dict:
                        word_freq_dict[words[j]] += count_matrix[i][j]
                    else:
                        word_freq_dict[words[j]] = count_matrix[i][j]
                        # map name of doc and generated doc name and use that mapping here

        sorted_dict = sorted(word_freq_dict.iteritems(), key=lambda (k, v): (v, k), reverse=True)

        cloud_words = []
        for tup in sorted_dict:
            if len(tup[0]) >= 3:
                cloud_words.append(tup)

        return cloud_words
