const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Read fonts as base64
const oggBoldBase64 = fs.readFileSync('/tmp/ogg-bold-base64.txt', 'utf8');
const satoshiBase64 = fs.readFileSync('/tmp/satoshi-base64.txt', 'utf8');

// Read original HTML
let html = fs.readFileSync('/home/user/webby-slides-bailey/Day 2 Revised Slides.html', 'utf8');

// Replace font-face declarations with base64 embedded versions
const newFontFaces = `
@font-face {
    font-family: 'Ogg Bold';
    src: url(data:font/truetype;base64,${oggBoldBase64}) format('truetype');
    font-weight: bold;
}

@font-face {
    font-family: 'Satoshi';
    src: url(data:font/truetype;base64,${satoshiBase64}) format('truetype');
    font-weight: 500;
}
`;

// Replace the existing font-face declarations
html = html.replace(/@font-face \{[^}]*font-family: 'Ogg Bold'[^}]*\}/g, '');
html = html.replace(/@font-face \{[^}]*font-family: 'Satoshi'[^}]*\}/g, '');
html = html.replace('/* ============================================', newFontFaces + '\n/* ============================================');

// Remove slide-label elements
html = html.replace(/<div class="slide-label">[^<]*<\/div>/g, '');

// Remove box-shadow from .slide
html = html.replace(/box-shadow: 0 10px 40px rgba\(0,0,0,0\.3\);/g, '');

// Remove margin from slides for PDF
html = html.replace(/margin: 20px auto;/g, 'margin: 0;');

// Change body background to white for individual slides
html = html.replace(/background: #1a1a1a;/g, 'background: white;');

// Save cleaned HTML
fs.writeFileSync('/home/user/webby-slides-bailey/Day 2 Revised Slides - Clean.html', html);

async function convertToPDF() {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    
    // Set viewport to slide dimensions
    await page.setViewportSize({ width: 1920, height: 1080 });
    
    // Load the HTML file
    await page.goto('file:///home/user/webby-slides-bailey/Day 2 Revised Slides - Clean.html', {
        waitUntil: 'networkidle'
    });
    
    // Wait for fonts to load
    await page.waitForTimeout(2000);
    
    // Get all slides
    const slides = await page.$$('.slide');
    
    const slideNames = [
        'Slide 91 - Persona',
        'Slide 92 - Context', 
        'Slide 93 - Goal',
        'Slide 118 - 4Ms Summary',
        'Slide 222 - I Made Something For You',
        'Slide 227 - Your Homework',
        'Slide 229 - Instructions',
        'Slide 237 - Day 3 Preview'
    ];
    
    console.log(`Found ${slides.length} slides`);
    
    for (let i = 0; i < slides.length; i++) {
        const slide = slides[i];
        
        // Take screenshot of just this slide as PDF
        const boundingBox = await slide.boundingBox();
        
        // Create a new page for each slide
        const slidePage = await browser.newPage();
        await slidePage.setViewportSize({ width: 1920, height: 1080 });
        
        // Create HTML for just this slide
        const slideHtml = await page.evaluate((index) => {
            const slides = document.querySelectorAll('.slide');
            const slide = slides[index];
            const styles = document.querySelector('style').outerHTML;
            return `<!DOCTYPE html><html><head><meta charset="UTF-8">${styles}<style>body{margin:0;padding:0;background:transparent;}.slide{margin:0;}</style></head><body>${slide.outerHTML}</body></html>`;
        }, i);
        
        await slidePage.setContent(slideHtml, { waitUntil: 'networkidle' });
        await slidePage.waitForTimeout(1000);
        
        const pdfPath = `/home/user/webby-slides-bailey/Day 2 - ${slideNames[i]}.pdf`;
        
        await slidePage.pdf({
            path: pdfPath,
            width: '1920px',
            height: '1080px',
            printBackground: true,
            margin: { top: 0, right: 0, bottom: 0, left: 0 }
        });
        
        console.log(`Created: ${pdfPath}`);
        await slidePage.close();
    }
    
    await browser.close();
    console.log('Done!');
}

convertToPDF().catch(console.error);
