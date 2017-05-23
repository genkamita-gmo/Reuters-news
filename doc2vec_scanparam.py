# coding: utf-8
import gensim
from gensim.models.doc2vec import Doc2Vec
import os
import collections
import smart_open
import random
import sys
import multiprocessing

# Set file names for train and test data
test_data_dir = '.'
my_train_file = test_data_dir + os.sep + sys.argv[1]
my_test_file = test_data_dir + os.sep + sys.argv[2]
my_iter = int(sys.argv[3])
my_mincount = int(sys.argv[4])
my_size = int(sys.argv[5])  # doc vector size
my_window = int(sys.argv[6])
my_workers = int(sys.argv[7])

print "\n\niter:", my_iter, "\nmincount:", my_mincount, "\nsize:", my_size, "\nwindow:", my_window, "\nworkers:", my_workers 

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

train_corpus = list(read_corpus(my_train_file))
test_corpus = list(read_corpus(my_test_file, tokens_only=True))


model = gensim.models.doc2vec.Doc2Vec(size=my_size, min_count=my_mincount, iter=my_iter, window = my_window, workers=my_workers)
model.build_vocab(train_corpus)  # takes roughly 1-2 minutes
model.train(train_corpus, total_examples=model.corpus_count)
