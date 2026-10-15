# My First Web Scraper: Book Catalog

Hey! I'm currently studying AI at university, and this is one of my first hands-on data engineering projects. It's a foundational web scraper I built to practice extracting structured data from the web.

Sure, the target site (books.toscrape.com) is a sandbox, but the mechanics I used here are totally real. 

## What it does
- Scrapes all 1,000 books across 50 paginated pages.
- Pulls the Title, Price, and Stock Availability.
- Uses `pandas` to structure everything cleanly instead of just dumping raw text.

## The Stack
- **Python** 
- **BeautifulSoup4** (for parsing HTML)
- **Requests** (for navigating pages)
- **Pandas** (for building the dataset)

## What I learned
The biggest takeaway for me was leveling up how I handle data. Instead of just printing raw text or using basic string writing, I learned how to use pandas to store everything in a structured DataFrame before exporting it to a clean CSV. I also got comfortable handling pagination—writing logic to automatically find the "Next" button and crawl through all 50 pages autonomously.

Next up: building a more complex parser for real-world sites