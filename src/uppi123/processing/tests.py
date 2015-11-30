import os
import time

import WordFrequencyCloud as pc
from TextCluster import TextCluster

tc = TextCluster()

tc.do_kMeans("G:\\Nikhil\\MS\\MS_SEM3\\239\\project\\data")
exit(0)
"""

sp = SearchProcessor()
sp.do_word_frequency_cloud('jaguar')
exit(0)
word_freq_tup_list = []
word_freq_tup_list.append(('nikhil', 5))
word_freq_tup_list.append(('rocky', 8))
word_freq_tup_list.append(('arnold', 10))
word_freq_tup_list.append(('ranbir', 1))
# tags = make_tags(word_freq_tup_list)

# print tags

# exit(0)
"""

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'templates', 'template.html'))
f = file(path)
print f.name
list_template = '<li>%(item)s</li>'

start = time.clock()
# path = "G:\Nikhil\MS\MS_SEM3\\239\project\data"
# word_dict = word_freq_generator.generate_word_freq(path)
# print len(word_dict)
# html = pc.generate_cloud(word_dict)
# print html
word_freq_tup_list = []
word_freq_tup_list.append(('nikhil', 5))
word_freq_tup_list.append(('rocky', 8))
word_freq_tup_list.append(('arnold', 10))
word_freq_tup_list.append(('ranbir', 1))

mylst = "".join("<li> %(key)s => %(val)s </li>" % {'key': t[0], 'val': str(t[1])} for t in word_freq_tup_list)
print mylst
html = pc.generate_html(word_freq_tup_list)
print time.clock() - start
