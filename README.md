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

| Rank | Word          | TF-IDF Score        |
|------|---------------|---------------------|
| 1    | gough         | 0.14783080151679642 |
| 2    | cave          | 0.13590949822372375 |
| 3    | museum        | 0.16023458460963863 |
| 4    | human         | 0.17585076404130193 |
| 5    | evidence      | 0.17723715908277887 |
| 6    | points        | 0.2467815284976994  |
| 7    | sophisticated | 0.2467815284976994  |
| 8    | culture       | 0.214732324323041   |
| 9    | butchering    | 0.2467815284976994  |
| 10   | carving       | 0.22803394587756834 |
| 11   | remains       | 0.19598474170290997 |
| 12   | says          | 0.19598474170290997 |
| 13   | dr            | 0.214732324323041   |
| 14   | silvia        | 0.16393553752825157 |
| 15   | bello         | 0.22803394587756834 |
| 16   | scientist     | 0.2467815284976994  |
| 17   | investigates  | 0.2467815284976994  |
| 18   | evolution     | 0.17723715908277887 |
| 19   | behaviour     | 0.19598474170290997 |
| 20   | including     | 0.19598474170290997 |

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
* Requests
    * Tests
    * Metrics
* Soup
    * ~~div article container~~
    * ~~h1, h2, p~~
    * for loop
* NLTK (stopwords) > TF-IDF (possibly good enough alone?)