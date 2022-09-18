#!/bin/sh

# Get script directory
if [ -L $0 ] ; then
    ME=$(readlink $0)
else
    ME=$0
fi
DIR=$(dirname $ME)

cd $DIR

python -m pip install -q --disable-pip-version-check -r scraper/requirements.txt
python scraper/scrape.py
