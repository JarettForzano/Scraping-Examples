from fastapi import FastAPI
from typing import List
import time
import asyncio
import httpx
from examples.html.httpx_batch import fetch_content
from examples.javascript.puppeter_batch import scrape_website
from pyppeteer import launch

app = FastAPI()


@app.post("/scrape/httpx")
async def scrape_urls(urls: List[str]):
    start_time = time.time()
    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        tasks = [fetch_content(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
    end_time = time.time()
    total_time = end_time - start_time
    return {
        'total_time': total_time,
        'results': results
    }

@app.post("/scrape/puppeter")
async def scrape_urls(urls: List[str]):
    start_time = time.time()

    browser = await launch({ # For now we are doing it inside of the request
        'headless': True,
        'args': [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-blink-features=AutomationControlled',
        ]
    })

    try:
        tasks = [scrape_website(browser, url) for url in urls]
        results = await asyncio.gather(*tasks)
    finally:
        await browser.close()

    end_time = time.time()
    total_time = end_time - start_time
    return {
        'total_time': total_time,
        'results': results
    }
