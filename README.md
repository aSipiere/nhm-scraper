# nhm-scraper

## The Task
Extract the paragraph and header (H1 & H2) text from the following articles and present the top 20 keywords (excluding stop words) from the aggregated dataset. 

http://www.nhm.ac.uk/discover/the-cannibals-of-goughs-cave.html

http://www.nhm.ac.uk/discover/how-we-became-human.html

http://www.nhm.ac.uk/discover/the-origin-of-our-species.html

#####Hint: 

There are many ways to perform the text extraction, one would be using an XPath expression. If you wanted to extract just the paragraph and H1 text within the URL’s you could use the following XPath (it will need amending to include H2 text as well).
```/html/body//div[contains(@class,'article--container')]//p|//h1```

## Running the Code
### Setup Virtual Environment

```bash
cd WORKINGDIRECTORY
git clone git@github.com:aSipiere/nhm-scraper.git
cd PROJECTPATH
mkvirtualenv -p python3 -r requirements.txt -a /PROJECTPATH nhmscraper
```
If python3 is the only version on your system then `-p python` is fine too.

## To Do
* Requests
    * Tests
    * Metrics
* Soup
* NLTK (stopwords) > TF-IDF (possibly good enough alone?)