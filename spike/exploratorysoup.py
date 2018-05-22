import requests
import time
import requests

page = requests.get("http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html")
print(page.status_code)

soup = bs(page.content, 'html.parser')

for i in soup.find_all("div", class_="article--container"):
    i_descendants = i.descendants
    for d in i_descendants:
        if d.name in ['h1', 'h2', 'p']:
            print(d.text)

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
