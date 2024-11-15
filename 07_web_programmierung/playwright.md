
# Web Scraping

### Exercise 1: Download

Use the `httpx` module to download a Wikipedia page and save it to a file.

    import httpx
    p = httpx.get("http://localhost:8000")
    print(p.status_code)
    print(p.text)

### Exercise 2: Parse HTML

Read the saved HTML page and parse it using Beautiful Soup.
Use the code in `example_bs4.py` as a starting point.

Discuss how to use documentation of Python modules.

### Exercise 3: Web front-end testing

Remote-control your browser. Run from the command line:

    pip install playwright
    playwright install

Generate test code with

    playwright codegen www.wikipedia.org

Before closing the browser, copy the generated code.
To run it, add imports:

    import playwright
    from playwright.sync_api import sync_playwright, Playwright

before closing the context, add:

    page.screenshot(path="screenshot.png")

Execute the code with Python.

Also see: [https://playwright.dev/python/](https://playwright.dev/python/)
