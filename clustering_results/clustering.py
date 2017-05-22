
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pprint as pp
import sys

def corpusNumLines():
    num_lines_in_corpus = get_ipython().getoutput(u'wc -l $corpus_train_file | sed "s/$corpus_train_file//g;"')
    num_lines_in_corpus = int(num_lines_in_corpus.s)
    return num_lines_in_corpus

#  parameters
docvec_file = "docvec60000"
docvec = np.load(docvec_file)
corpus_train_file = "split60000aa"
num_cluster = int(sys.argv[1])
num_randpick = int(sys.argv[2])
dimensionality_reduction = int(sys.argv[3])
num_init = int(sys.argv[4]) 

num_lines_in_corpus = corpusNumLines()

if dimensionality_reduction == 1:
    print("dimensionality reduction before clustering")
    docvec = PCA(n_components=2).fit_transform(docvec)
    kmeans = KMeans(init='k-means++', n_clusters = num_cluster, n_init=num_init)
    fit = kmeans.fit(docvec)
else:
    print("performing clustering of raw docvec")
    X = np.load(docvec_file)
    kmeans = KMeans(init='k-means++', n_clusters = num_cluster, n_init=num_init)
    fit = kmeans.fit(docvec)

news_randpick_index = np.random.randint(0,num_lines_in_corpus-1,num_randpick)
news_randpick_label = fit.labels_[news_randpick_index]
# sort them according to label
news_randpick_label, news_randpick_index = (list(t) for t in zip(*sorted(zip(news_randpick_label, news_randpick_index))))

news_randpick_title = []
for num in news_randpick_index:
    title = get_ipython().getoutput(u'sed -n "$num"p $corpus_train_file')
    news_randpick_title.append(title)

for num in range(num_cluster):
    count = sum(i == num for i in news_randpick_label)
    if count > 2:
        print("cluster " + str(num) + ": ---------------------------------------")
        pp.pprint(news_randpick_title[0:count])
    news_randpick_title = news_randpick_title[count:]

if dimensionality_reduction == 1:
    print("plotting clustering of dimensionality reduced data")
    for num in range(num_cluster):
        condition = fit.labels_ == num
        filtered_docvec_x = docvec[condition,0]
        filtered_docvec_y = docvec[condition,1]
        plt.plot(filtered_docvec_x, filtered_docvec_y, '.', markersize=0.5)

    plt.plot(docvec[news_randpick_index, 0], docvec[news_randpick_index, 1], 'k.')
    plt.show()
