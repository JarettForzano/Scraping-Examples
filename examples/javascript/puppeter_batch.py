import asyncio
from pyppeteer_stealth import stealth

async def scrape_website(browser, url):
    page = await browser.newPage()
    await stealth(page)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/95.0.4638.69 Safari/537.36'
    )
    await page.setViewport({'width': 1280, 'height': 800})
    await page.setExtraHTTPHeaders({
        'Accept-Language': 'en-US,en;q=0.9',
    })

    # Enable request interception
    await page.setRequestInterception(True)

    async def intercept_request(request):
        if request.resourceType in ['image', 'stylesheet', 'font', 'media']:
            await request.abort()
        else:
            await request.continue_()

    # Attach the interception handler properly
    page.on('request', lambda req: asyncio.ensure_future(intercept_request(req)))

    print(f"Navigating to: {url}")
    await page.goto(url, {'waitUntil': 'domcontentloaded'})

    page_title = await page.title()
    print(f"Page Title: {page_title}")

    page_content = await page.evaluate('() => document.body.innerText')
    await page.close()

    # Return the scraped content instead
    return {
        'url': url,
        'title': page_title,
        'content': page_content
    }

