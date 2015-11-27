import collections
import nltk
import string
import os
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
        # stemmed.append(item)
    # print stemmed
    return stemmed


def tokenize(text):
    stemmer = PorterStemmer()
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems


def sort_dict(tup):
    print tup
    return tup[1]


def sort_file_name(filename):
    return int(filename[3:])


def generate_word_freq(path):
    token_dict = collections.OrderedDict()

    for subdir, dirs, files in os.walk(path):
        for file in sorted(files, key=sort_file_name):
            file_path = subdir + os.path.sep + file
            shakes = open(file_path, 'r')
            text = shakes.read()
            lowers = text.lower()
            no_punctuation = lowers.translate(None, string.punctuation)
            token_dict[file] = no_punctuation

    count_vector = CountVectorizer(tokenizer=tokenize, stop_words='english', min_df=1, max_features=300)
    count_matrix = count_vector.fit_transform(token_dict.values()).toarray()
    words = np.array(count_vector.get_feature_names())

    # print (words)
    # exit(0)
    # print (count_matrix[0])

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

    sorted_dict = sorted(word_freq_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True)

    cloud_words = []
    for tup in sorted_dict:
        if len(tup[0]) >= 3:
            cloud_words.append(tup)

    return cloud_words
