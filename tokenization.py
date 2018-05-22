from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
# from scipy.sparse.csr import csr_matrix
# csr matrix for saving the tfidf matrix if wanted

def get_tfidf(vect):
    tf = TfidfVectorizer(input='content', analyzer='word', ngram_range=(1, 1),
                         min_df=0, stop_words='english', sublinear_tf=True)
    tfidf_matrix = tf.fit_transform(vect)
    print(tfidf_matrix)
    feature_array = tf.get_feature_names()

    doc = 2
    feature_index = tfidf_matrix[doc, :].nonzero()[1]
    print(feature_index)
    tfidf_scores = zip(feature_index, [tfidf_matrix[doc, x] for x in feature_index])

    for w, s in [(feature_array[i], s) for (i, s) in tfidf_scores]:
        print(w, s)
