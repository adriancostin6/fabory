:: Scrape fabory.com/ro for products
@echo off

python -m pip install scraper\requirements.txt
python scraper\scrape.py
