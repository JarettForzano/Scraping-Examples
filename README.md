# Scraping Examples

#### httpx
- Handles batch requests of URL's
- Uses `httpx` to fetch the content
- Does not handle javascript

#### pyppeteer
- Handles batch requests of URL's
- Uses `pyppeteer` to handle javascript
- Uses `puppeteer-stealth` to avoid detection by anti-scraping measures


#### Running the server
```bash
python -m venv venv
pip install -r requirements.txt
uvicorn server:app --reload
```

#### Notes
Code is not optimized as they are just examples