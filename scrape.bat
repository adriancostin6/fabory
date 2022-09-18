:: Scrape fabory.com/ro for products
@echo off

pushd "%~dp0"

python -m pip install -q --disable-pip-version-check -r scraper\requirements.txt
python scraper\scrape.py

popd
