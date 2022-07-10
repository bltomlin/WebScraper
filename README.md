## WebScraper
A program to demonstrate knowledge on sending HTTP-requests and process the responses, working with an external library, library documentation, file system management and parsing website data.

## Installation

```
# clone the repo
$ git clone https://github.com/bltomlin/WebScraper`

# change the working directory to WebScraper
$ cd WebScraper

# install beautifulsoup4
$ pip install beautifulsoup4
```

## Usage

The program will prompt how many pages you would like to scan from nature.com's 2020 articles list.

```
Enter the number of pages you wish to scrape:
```
The program will then prompt 
```
Enter the article type you would like results for:
```
You can enter any of these types:
- Article
- Author Correction
- Book Review
- Career Column
- Comment
- Correspondence
- Editorial
- Futures
- Nature Briefing
- Nature Index
- Nature Podcast
- News
- News & Views
- News Feature
- News Round-Up
- Outlook
- Publisher Correction
- Research Highlight
- Where I Work
- World View 

The program will then scan each page for the desired article type and save the articles to a text file locally in the WebScraper directory.
