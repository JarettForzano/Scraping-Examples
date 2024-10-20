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
uvicorn server:app
```

#### Example request using postman
```bash
POST http://localhost:8000/scrape/httpx
Body:
[
  "https://www.google.com",
  "https://www.yahoo.com"
]
```

#### Possible bugs
If you can for some reason not close the server and start it up again or the port is still under use after you kill the process you can manually kill the process using `kill -9 <pid>` after finding the pid with `lsof -i :8000`

#### Notes
Code is not optimized as they are just examples