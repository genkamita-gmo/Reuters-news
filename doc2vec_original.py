import gensim
import os
import collections
import smart_open
import random

# Set file names for train and test data
test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data'])
lee_train_file = test_data_dir + os.sep + 'lee_background.cor'
lee_test_file = test_data_dir + os.sep + 'lee.cor'

def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
# For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])

train_corpus = list(read_corpus(lee_train_file))
test_corpus = list(read_corpus(lee_test_file, tokens_only=True))

train_corpus[:2]

print(test_corpus[:2])

model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=55)

model.build_vocab(train_corpus)

model.train(train_corpus, total_examples=model.corpus_count)

model.infer_vector(['only', 'you', 'can', 'prevent', 'forrest', 'fires'])
