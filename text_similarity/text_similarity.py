from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import nltk
import numpy


def sim(str1, str2):
    stop_words = set(stopwords.words("english"))
    filtered_sentence1 = []
    filtered_sentence2 = []
    lemm_sentence1 = []
    lemm_sentence2 = []
    sims = []
    temp1 = []
    temp2 = []
    simi = []
    final = []
    same_sent1 = []
    same_sent2 = []
    lemmatizer = WordNetLemmatizer()
    for words1 in word_tokenize(str1):
        if words1 not in stop_words:
            if words1.isalnum():
                filtered_sentence1.append(words1)

    for i in filtered_sentence1:
        lemm_sentence1.append(lemmatizer.lemmatize(i))

    for words2 in word_tokenize(str2):
        if words2 not in stop_words:
            if words2.isalnum():
                filtered_sentence2.append(words2)

    for i in filtered_sentence2:
        lemm_sentence2.append(lemmatizer.lemmatize(i))
    for word1 in lemm_sentence1:
        simi = []
        for word2 in lemm_sentence2:
            sims = []
            syns1 = wordnet.synsets(word1)
            syns2 = wordnet.synsets(word2)
            for sense1, sense2 in product(syns1, syns2):
                d = wordnet.wup_similarity(sense1, sense2)
                if d != None:
                    sims.append(d)

            if sims != []:
                max_sim = max(sims)
                simi.append(max_sim)

        if simi != []:
            max_final = max(simi)
            final.append(max_final)
    similarity_index = numpy.mean(final)
    similarity_index = round(similarity_index, 2)

    if numpy.isnan(similarity_index):
        return 1
    return similarity_index
