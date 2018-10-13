#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.10.2018 17:07
:Licence GNUv3
Part of DataScienceProject

"""
import itertools
from igraph import Graph, plot
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
import re
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS as stopwords
from threading import Thread

print("Loading stop words")
custom_stop_words = None
with open('customStopWords.txt', 'r') as f:
    custom_stop_words = f.readlines()
custom_stop_words = frozenset(map(lambda x: x.strip(), custom_stop_words))

print("Initializing stemmer")
stemmer = SnowballStemmer('english')


def process_tweets(tweets):
    dt = pd.DataFrame(list(tweets), columns=['text'])


    print('Processing content')
    def _transform_tweet(text: str):
        w = text.strip().lower()
        w = re.sub('http\S+', ' ', w)
        w = re.sub(r'@[a-zA-Z0-9_]+', ' ', w)
        w = re.sub(r'[^a-zA-Z ]', '', w)
        w = ' '.join(w.split())
        w = stemmer.stem(w)
        ws = [x for x in w.split() if x not in stopwords and x not in custom_stop_words]
        return ws
    dt['transformed'] = dt['text'].apply(_transform_tweet)


    print('Finding unique words')
    uniqueWords = dt['transformed'].apply(pd.Series).stack().unique()


    print('Building graph')
    g = Graph()
    g.es["weight"] = 0.0
    g.add_vertices(uniqueWords)
    def _fill_edges(words):
        for i in itertools.combinations(words, 2):
            g[i[0], i[1]] += 1
    dt['transformed'].apply(_fill_edges)
    def _recompute_weight(edge):
        edge['weight'] = 1 / edge['weight']
    pd.Series(list(g.es)).apply(_recompute_weight)


    print("Running community detection")
    dendrogram = g.community_walktrap('weight', 6)


    print("Making clusters")
    clustering = dendrogram.as_clustering()
    subgraphs = clustering.subgraphs()
    interestingClustersIndexes = pd.Series(subgraphs).apply(lambda x: len(x.vs)).sort_values(ascending=False).index[:3]


    print("Printing keywords\n")
    wordsGroups = list()
    for i in interestingClustersIndexes:
        graph = subgraphs[i]
        importantNodes = pd.Series(graph.betweenness(weights='weight'))
        importantNodes.sort_values(ascending=False, inplace=True)
        vertices = pd.Series(importantNodes[:15].index).apply(lambda x: graph.vs[x])
        representativeWords = vertices.apply(lambda x: x.attributes()['name'])
        representativeWords = representativeWords[representativeWords.str.len() > 3][:10]
        words = " ".join(representativeWords.values)
        print(words + "\n")
        wordsGroups.append(words)


    print("\nPlotting")
    Thread(target=lambda: plot(clustering, bbox=(4000, 4000)),
           name="Plotting thread",
           daemon=True).start()

    return wordsGroups
