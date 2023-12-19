# News Articles Generator

## Overview
The News Articles Generator is a command-line interface (CLI) utility designed for fetching,, processing, and organizing news articles from various publishers. Utilizing the News API, it offers functionalities such as retrieving publishers, fetching the latest nes articles, appending articles fo a file, and generating markdown files with a curated list of articles.

## Features
#### 1. Retrieve Top News Publishers ("-p" or "--publishers"):
- Fetch a list of top new publishers.
- Filter available for category, country, and language.
- Display publishers with details such as name, description, and website URL

#### 2. Fetch Latest News Articles ("-a" or "--articles"):
- Retrieve the latest news articles based on various filters including keyword, sort order (by published date, relevancy, popularity), domain, category, country, language, start and end dates.
- Display articles details like title, author, publication date, and URL.

#### 3. Append Articles to a file ("-ap" or "--append"):
- Append the latest news articles to a specified file with valid file path ("--file" option)
- Each article include details such as title, author, publication date, and URL.

#### 4. Generate Markdown 'To-Read' Lists ("-g" or "--generate"):
- Generate a markdown file containing a list of articles to read.
- The list includes up to 20 articles with formatted links and details.
- The file is saved in a specified directory ("--directory" option).

#### 5. Automated Daily Markdown 'To-Read' List Generation
- Create a script calling the <b><i> Generate Markdown 'To-Read' List</i></b> with various optional arguments such as keywords or published dates in the specified directory.
- Schedule a crontab file to make it execute the script daily at 7:00AM.

## Installation
```commandline
git clone https://github.com/quynhnle135/news-articles-generator-cli-tool.git

cd news-articles-generator-cli-tool
```

## Usage
- For program's instruction and command-lines: ```python3 main.py -h```
- What it looks like after running the <i>help</i> command-line:

``` 
News Articles Generator

options:
  -h, --help            show this help message and exit
  -p, --publishers      Retrieve a list of top news publishers. Can be filtered by category, country, and language.
  -a, --articles        Fetch the latest news articles. Filters like keyword, sortby, domain, category, country, and language can be applied.
  -ap, --append         Enable this option to append the latest news articles to a specified file. Requires a valid file path to be provided with the '--file' option.
  -g, --generate        Enable this option to generate a 'to-read' list in Markdown format. The list will be created in the directory specified by the '--directory' option. Ensure the specified directory
                        exists and is writable.
  -ca CATEGORY, --category CATEGORY
                        Filter publishers/articles by a specific news category (e.g., 'business', 'sports'). Applies to both publishers and articles.
  -co COUNTRY, --country COUNTRY
                        Filter publishers/articles by country using ISO country codes (e.g., 'us' for the United States, 'gb' for Great Britain). Applies to both publishers and articles.
  -la LANGUAGE, --language LANGUAGE
                        Filter publishers/articles by language using ISO language codes (e.g., 'en' for English, 'es' for Spanish). Applies to both publishers and articles.
  -q QUERY, --query QUERY
                        Search articles with multiple keywords
  -k KEYWORD, --keyword KEYWORD
                        Search articles with a specific keyword in the title.
  -do DOMAIN, --domain DOMAIN
                        Search articles in a specific domain.
  -so {publishedAt,relevancy,popularity}, --sortby {publishedAt,relevancy,popularity}
                        Sort retrieved articles by 'publishedAt', 'relevancy', or 'popularity'. Applicable only for articles.
  -fd FROMDATE, --fromdate FROMDATE
                        Specify the start date for filtering articles. Format: YYYY-MM-DD. Articles from this date onwards will be included.
  -td TODATE, --todate TODATE
                        Specify the end date for filtering articles. Format: YYYY-MM-DD. Only articles up to this date will be included.
  -f FILE, --file FILE  Provide the file path where the articles will be appended. Ensure the file path is accessible and writable.
  -dir DIRECTORY, --directory DIRECTORY
                        Specify the directory path where the news articles will be saved. Ensure that the directory exists and has write permissions.

```

---

## Examples of News Articles Generator features:
- Retrieve top publishers in the category <i>business</i>: ```python3 main.py -p --category business```
- Result:
```commandline
---10  Publishers---
1. Argaam
Description: ارقام موقع متخصص في متابعة سوق الأسهم السعودي تداول - تاسي - مع تغطيه معمقة لشركات واسعار ومنتجات البتروكيماويات , تقارير مالية الاكتتابات الجديده 
Check their website: http://www.argaam.com


2. Australian Financial Review
Description: The Australian Financial Review reports the latest news from business, finance, investment and politics, updated in real time. It has a reputation for independent, award-winning journalism and is essential reading for the business and investor community.
Check their website: http://www.afr.com


3. Bloomberg
Description: Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News.
Check their website: http://www.bloomberg.com


4. Business Insider
Description: Business Insider is a fast-growing business site with deep financial, media, tech, and other industry verticals. Launched in 2007, the site is now the largest business news site on the web.
Check their website: http://www.businessinsider.com


5. Business Insider (UK)
Description: Business Insider is a fast-growing business site with deep financial, media, tech, and other industry verticals. Launched in 2007, the site is now the largest business news site on the web.
Check their website: http://uk.businessinsider.com


6. Die Zeit
Description: Aktuelle Nachrichten, Kommentare, Analysen und Hintergrundberichte aus Politik, Wirtschaft, Gesellschaft, Wissen, Kultur und Sport lesen Sie auf ZEIT ONLINE.
Check their website: http://www.zeit.de/index


7. Financial Post
Description: Find the latest happenings in the Canadian Financial Sector and stay up to date with changing trends in Business Markets. Read trading and investing advice from professionals.
Check their website: http://business.financialpost.com


8. Fortune
Description: Fortune 500 Daily and Breaking Business News
Check their website: http://fortune.com


9. Handelsblatt
Description: Auf Handelsblatt lesen sie Nachrichten über Unternehmen, Finanzen, Politik und Technik. Verwalten Sie Ihre Finanzanlagen mit Hilfe unserer Börsenkurse.
Check their website: http://www.handelsblatt.com


10. Il Sole 24 Ore
Description: Notizie di economia, cronaca italiana ed estera, quotazioni borsa in tempo reale e di finanza, norme e tributi, fondi e obbligazioni, mutui, prestiti e lavoro a cura de Il Sole 24 Ore.
Check their website: https://www.ilsole24ore.com

```

- Retrieve articles without providing any optional arguments: ```python3 main.py -a```
- Result:

```commandline
---10 Articles---
1. Apple Releases Safari Technology Preview 184 With Bug Fixes and Performance Improvements
Written by: Juli Clover
Published at: 2023-12-07T22:21:42Z
Read the full article at: https://www.macrumors.com/2023/12/07/apple-releases-safari-technology-preview-184/


2. Putin says Russia will develop new AI technology to counter the Western monopoly, which he fears could lead to a 'digital abolition' of Russian culture
Written by: lvaranasi@insider.com (Lakshmi Varanasi)
Published at: 2023-11-25T21:11:13Z
Read the full article at: https://www.businessinsider.com/putin-russia-develop-new-ai-technology-to-counter-west-2023-11


3. TSMC Demos Next-Gen Chip Technology to Apple Ahead of 2025 Debut
Written by: Hartley Charlton
Published at: 2023-12-12T15:31:04Z
Read the full article at: https://www.macrumors.com/2023/12/12/tsmc-demos-next-gen-chip-technology/


4. Slow down! As deaths and injuries mount, new calls for technology to reduce speeding
Written by: Joel Rose
Published at: 2023-12-06T10:01:14Z
Read the full article at: https://www.npr.org/2023/12/06/1216557190/car-crash-accident-speeding-technology-slow-down-speed-assistance


5. Technology to stop drunk drivers could be coming to every new car in the nation
Written by: Joe Hernandez
Published at: 2023-12-13T19:56:07Z
Read the full article at: https://www.npr.org/2023/12/13/1219076996/drunk-driving-nhtsa-new-cars


6. Meta Says There's Been No Downside To Sharing AI Technology
Written by: msmash
Published at: 2023-12-01T15:20:00Z
Read the full article at: https://tech.slashdot.org/story/23/12/01/1512232/meta-says-theres-been-no-downside-to-sharing-ai-technology


7. Meta, IBM Create Industrywide AI Alliance To Share Technology
Written by: msmash
Published at: 2023-12-05T13:00:00Z
Read the full article at: https://tech.slashdot.org/story/23/12/05/0726255/meta-ibm-create-industrywide-ai-alliance-to-share-technology


8. Google's new AI technology could be smarter than OpenAI's GPT-4
Written by: Lakshmi Varanasi
Published at: 2023-12-09T16:25:45Z
Read the full article at: https://www.businessinsider.com/gemini-ultra-google-ai-smarter-than-openai-gpt-4-2023-12


9. The rise of AI is fueling a seamless technology evolution called ambient computing. Here's what that could mean for us.
Written by: Sponsor Post
Published at: 2023-11-27T18:13:47Z
Read the full article at: https://www.businessinsider.com/sc/how-arm-is-taking-leading-role-rise-of-ambient-computing


10. A downed Russian Shahed drone was found with a Ukrainian SIM card, suggesting the technology was used to pilot the explosive drone: think tank
Written by: Natalie Musumeci
Published at: 2023-12-01T19:54:38Z
Read the full article at: https://www.businessinsider.com/downed-russian-shahed-drone-found-with-ukrainian-sim-card-2023-12

```

- Retrieve latest articles when providing <i>Ariana Grander as keyword</i> and <i>publishedAt as sortBy filter</i>: ```python3 main.py -a --keyword "Ariana Grande" --sortby "publishedAt"```
- Result: 
```commandline
---10 Articles---
1. SZA, Ariana Grande and ‘Insecure’: Everyone Wants a Piece of Producer Leon Thomas
Written by: hollywoodreporter.com
Published at: 2023-12-15T17:26:10Z
Read the full article at: https://biztoc.com/x/dffa1902d722d536


2. Ariana Grande – Christmas & Chill (2023)
Written by: Kingman
Published at: 2023-12-13T19:50:23Z
Read the full article at: https://rlsbb.ru/ariana-grande-christmas-chill-2023/


3. Sydney Sweeney, Olivia Rodrigo, & Ariana Grande Confirm the Little Red Dress Is All the Rage This Season — See Photos
Written by: Sandy Aziz
Published at: 2023-12-13T18:59:57Z
Read the full article at: https://www.teenvogue.com/story/little-red-dress-holiday-season-2023


4. Jennifer Hudson Talks Reuniting With ‘Christmas Angels’ Mariah Carey & Ariana Grande
Written by: billboard.com
Published at: 2023-12-12T18:20:52Z
Read the full article at: https://biztoc.com/x/37e3c1813a0be750


5. Jennifer Hudson Recalls Reuniting With Mariah Carey & Ariana Grande
Written by: Hannah Dailey
Published at: 2023-12-12T18:16:35Z
Read the full article at: https://www.billboard.com/music/music-news/jennifer-hudson-reuniting-mariah-carey-ariana-grande-1235552799/


6. Travis Kelce plays 'Kiss Marry Kill' with Taylor Swift, Ariana Grande and Katy Perry... his choices were a shock
Written by: M.C.
Published at: 2023-12-12T15:27:12Z
Read the full article at: https://www.marca.com/en/nfl/kansas-city-chiefs/2023/12/12/65787bb5ca4741983b8b45f4.html


7. Ariana Grande Is Looking To Score A Big Hit This Christmas Season
Written by: Hugh McIntyre, Senior Contributor, 
 Hugh McIntyre, Senior Contributor
 https://www.forbes.com/sites/hughmcintyre/
Published at: 2023-12-12T15:00:00Z
Read the full article at: https://www.forbes.com/sites/hughmcintyre/2023/12/12/ariana-grande-is-looking-to-score-a-big-hit-this-christmas-season/


8. Ariana Grande Gifts Fans With ‘Naughty Version’ of ‘Santa Tell Me’: Stream It Now
Written by: billboard.com
Published at: 2023-12-11T17:42:24Z
Read the full article at: https://biztoc.com/x/e3c5eec83e77435e


9. Ariana Grande Changed 2 Lyrics For "Santa Tell Me (Naughty Version)"
Written by: Dylan Kickham
Published at: 2023-12-11T17:05:11Z
Read the full article at: https://www.elitedaily.com/entertainment/ariana-grande-changed-lyrics-santa-tell-me-naughty-version


10. Ariana Grande Signs With New Management - Billboard
Written by: feedfeeder
Published at: 2023-12-11T05:53:28Z
Read the full article at: https://slashdot.org/firehose.pl?op=view&amp;id=172464629

```