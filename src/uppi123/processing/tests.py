import word_freq_generator
import word_cloud as pc
import time

start = time.clock()
path = "G:\Nikhil\MS\MS_SEM3\\239\project\data"
word_dict = word_freq_generator.generate_word_freq(path)
print len(word_dict)
html = pc.generate_cloud(word_dict)
print html
print time.clock() - start
