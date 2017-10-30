## Books of Sorrow Scraper

A one-off script for scraping the Books of Sorrow from the Ishtar Collective website.

Usage:

```bash
# Dowwnload the Books of Sorrow as HTML
./scrape.sh
# Parse them into text (Note that the Calcified Fragements will be out of order)
./parse.py > out.txt
