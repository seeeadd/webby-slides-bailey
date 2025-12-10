#!/usr/bin/env python3
import asyncio
import sys
import os
from pathlib import Path
from playwright.async_api import async_playwright

async def convert_html_to_pdf(html_path, pdf_path):
    """Convert HTML to PDF using Playwright with exact rendering."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path='/root/.cache/ms-playwright/chromium_headless_shell-1194/chrome-linux/headless_shell',
            args=['--no-sandbox']
        )
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Load the HTML file
        file_url = f'file://{os.path.abspath(html_path)}'
        await page.goto(file_url, wait_until='networkidle')

        # Wait for fonts to load
        await page.wait_for_timeout(2000)

        # Print to PDF with exact dimensions (1920x1080 = 508mm x 286mm at 96 DPI)
        await page.pdf(
            path=pdf_path,
            width='508mm',
            height='286mm',
            print_background=True,
            margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
        )

        await browser.close()
        print(f"Converted: {html_path} -> {pdf_path}")

async def main():
    if len(sys.argv) > 1:
        # Convert specific file
        html_path = sys.argv[1]
        pdf_path = html_path.replace('.html', '.pdf')
        await convert_html_to_pdf(html_path, pdf_path)
    else:
        # Convert all DAY 2 HTML files
        base_dir = Path('/home/user/webby-slides-bailey')
        html_files = sorted(base_dir.glob('DAY 2 slides *.html'))

        for html_file in html_files:
            pdf_path = str(html_file).replace('.html', '.pdf')
            await convert_html_to_pdf(str(html_file), pdf_path)

if __name__ == '__main__':
    asyncio.run(main())
