from bs4 import BeautifulSoup

async def fetch_content(client, url):
    try:
        print(f"Fetching: {url}")

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/95.0.4638.69 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;"
                "q=0.9,image/avif,image/webp,image/apng,*/*;"
                "q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
        }

        response = await client.get(url, headers=headers, timeout=30.0)
        response.raise_for_status()
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'lxml')

        # Remove script and style elements
        for script_or_style in soup(['script', 'style', 'noscript']):
            script_or_style.extract()

        # Get the text
        text = soup.get_text(separator='\n')

        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = '\n'.join(chunk for chunk in chunks if chunk)

        # Get the page title
        page_title = soup.title.string if soup.title else 'No Title'

        print(f"Page Title: {page_title}")

        return {
            'url': url,
            'title': page_title,
            'content': text_content
        }

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {
            'url': url,
            'error': str(e)
        }
