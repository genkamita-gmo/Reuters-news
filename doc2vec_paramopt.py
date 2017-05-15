# coding: utf-8
import gensim
from gensim.models.doc2vec import Doc2Vec
import os
import collections
import smart_open
import random
import sys


# Set file names for train and test data
test_data_dir = '.'
my_train_file = test_data_dir + os.sep + sys.argv[1]
my_test_file = test_data_dir + os.sep + sys.argv[2]
my_iter = int(sys.argv[3])
my_mincount = int(sys.argv[4])
my_size = int(sys.argv[5])  # doc vector size
my_window = int(sys.argv[6])

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

print("check corpus")
print(train_corpus[:2])
print(test_corpus[:2])

pre = Doc2Vec(min_count=0)
pre.scan_vocab(train_corpus)

for num in range(0, 20):
    print('min_count: {}, size of vocab: '.format(num), pre.scale_vocab(min_count=num, dry_run=True)['memory']['vocab']/700)


model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=my_iter)

model.build_vocab(train_corpus)  # takes roughly 1-2 minutes
model.train(train_corpus, total_examples=model.corpus_count)
model.infer_vector(['only', 'you', 'can', 'prevent', 'forrest', 'fires'])


ranks = []
second_ranks = []
for doc_id in range(len(train_corpus)):
    inferred_vector = model.infer_vector(train_corpus[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    rank = [docid for docid, sim in sims].index(doc_id)
    ranks.append(rank)
    
    second_ranks.append(sims[1])

collections.Counter(ranks)  # Results vary due to random seeding and very small corpus


print('Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))
doc_id = random.randint(0, len(train_corpus))

print('Train Document ({}): «{}»\n'.format(doc_id, ' '.join(train_corpus[doc_id].words)))
sim_id = second_ranks[doc_id]
print('Similar Document {}: «{}»\n'.format(sim_id, ' '.join(train_corpus[sim_id[0]].words)))
doc_id = random.randint(0, len(test_corpus))
inferred_vector = model.infer_vector(test_corpus[doc_id])
sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))

print('Test Document ({}): «{}»\n'.format(doc_id, ' '.join(test_corpus[doc_id])))
print(u'SIMILAR/DISSIMILAR DOCS PER MODEL %s:\n' % model)
for label, index in [('MOST', 0), ('MEDIAN', len(sims)//2), ('LEAST', len(sims) - 1)]:
    print(u'%s %s: «%s»\n' % (label, sims[index], ' '.join(train_corpus[sims[index][0]].words)))

