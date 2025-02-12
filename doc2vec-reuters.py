# coding: utf-8

import gensim
import os
import collections
import smart_open
import random

# Set file names for train and test data
test_data_dir = '/Users/usr0102377/gitrepo/Reuters-full-data-set'

my_train_file = test_data_dir + os.sep + 'split_titleaa'
my_test_file = test_data_dir + os.sep + 'split_titleab'



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

train_corpus[:2]

print(test_corpus[:2])
model = gensim.models.doc2vec.Doc2Vec(size=50, min_count=2, iter=55)
get_ipython().magic(u'pinfo gensim.models.doc2vec.Doc2Vec')

model.build_vocab(train_corpus)  # takes roughly 1-2 minutes
get_ipython().magic(u'time model.train(train_corpus, total_examples=model.corpus_count)#, epochs=model.iter)')
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

