# nhm-scraper

## The Task
Extract the paragraph and header (H1 & H2) text from the following articles and present the top 20 keywords (excluding stop words) from the aggregated dataset. 

http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html

http://www.nhm.ac.uk/discover/how-we-became-human.html

http://www.nhm.ac.uk/discover/the-origin-of-our-species.html

###Hint: 

There are many ways to perform the text extraction, one would be using an XPath expression. If you wanted to extract just the paragraph and H1 text within the URL’s you could use the following XPath (it will need amending to include H2 text as well).

```/html/body//div[contains(@class,'article--container')]//p|//h1```

# Results

| Rank | word        | score |
|------|-------------|-------|
| 1    | visitors    | 0.129 |
| 2    | africa      | 0.126 |
| 3    | ancient     | 0.111 |
| 4    | homo        | 0.109 |
| 5    | neanderthal | 0.106 |
| 6    | relatives   | 0.105 |
| 7    | gallery     | 0.103 |
| 8    | dna         | 0.099 |
| 9    | species     | 0.096 |
| 10   | like        | 0.091 |
| 11   | evolved     | 0.091 |
| 12   | recently    | 0.091 |
| 13   | human       | 0.090 |
| 14   | million     | 0.089 |
| 15   | years       | 0.086 |
| 16   | skull       | 0.085 |
| 17   | lived       | 0.085 |
| 18   | fossil      | 0.085 |
| 19   | scientists  | 0.081 |
| 20   | lineage     | 0.080 |

## Running the Code
### Setup Virtual Environment
Using venvwrapper or venvwrapper-win
```bash
cd WORKINGDIRECTORY
git clone git@github.com:aSipiere/nhm-scraper.git
cd PROJECTPATH
mkvirtualenv -p python3 -r requirements.txt -a /PROJECTPATH nhmscraper
```
If python3 is the only version on your system then `-p python` is fine too.

## To Do
* ~~Initial spike~~
* ~~Requests~~
    * Metrics
* ~~Soup~~
    * ~~div article container~~
    * ~~h1, h2, p~~
    * ~~loop~~
    * ~~tests~~
* ~~NLTK (stopwords) > TF-IDF (possibly good enough alone?)~~
    * tests
* to csv
* plots