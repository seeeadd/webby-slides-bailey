#!/bin/bash

# Read base64 encoded fonts
OGG_BOLD_BASE64=$(cat /tmp/ogg-bold-base64.txt)
SATOSHI_BASE64=$(cat /tmp/satoshi-base64.txt)

# Read original HTML and extract slides
HTML_FILE="/home/user/webby-slides-bailey/Day 2 Revised Slides.html"

# Slide names for output files
declare -a SLIDE_NAMES=(
    "Slide 91 - Persona"
    "Slide 92 - Context"
    "Slide 93 - Goal"
    "Slide 118 - 4Ms Summary"
    "Slide 222 - I Made Something For You"
    "Slide 227 - Your Homework"
    "Slide 229 - Instructions"
    "Slide 237 - Day 3 Preview"
)

# Create a Node script to extract and convert slides
cat > /tmp/extract-slides.js << 'NODESCRIPT'
const fs = require('fs');

// Read fonts
const oggBoldBase64 = fs.readFileSync('/tmp/ogg-bold-base64.txt', 'utf8').trim();
const satoshiBase64 = fs.readFileSync('/tmp/satoshi-base64.txt', 'utf8').trim();

// Read HTML
let html = fs.readFileSync('/home/user/webby-slides-bailey/Day 2 Revised Slides.html', 'utf8');

// Font face declarations with base64
const fontFaces = `
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

const slideNames = [
    "Slide 91 - Persona",
    "Slide 92 - Context",
    "Slide 93 - Goal",
    "Slide 118 - 4Ms Summary",
    "Slide 222 - I Made Something For You",
    "Slide 227 - Your Homework",
    "Slide 229 - Instructions",
    "Slide 237 - Day 3 Preview"
];

// Extract slides using regex
const slideRegex = /<div class="slide"[^>]*>[\s\S]*?(?=<div class="slide"|<\/body>)/g;
const slides = html.match(slideRegex) || [];

console.log(`Found ${slides.length} slides`);

// Base styles (without slide labels and shadows)
const baseStyles = `
${fontFaces}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Satoshi', Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.slide {
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    margin: 0;
    padding: 0;
}

.bg-shapes {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}

.slide-label {
    display: none !important;
}
`;

slides.forEach((slide, i) => {
    // Remove slide label from this slide
    let cleanSlide = slide.replace(/<div class="slide-label">[^<]*<\/div>/g, '');
    // Remove box-shadow
    cleanSlide = cleanSlide.replace(/box-shadow:\s*[^;]+;/g, '');

    const slideHtml = `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>${baseStyles}</style>
</head>
<body>
${cleanSlide}
</body>
</html>`;

    const filename = `/tmp/slide_${i}.html`;
    fs.writeFileSync(filename, slideHtml);
    console.log(`Created: ${filename} -> ${slideNames[i] || 'Unknown'}`);
});
NODESCRIPT

# Run Node script to extract slides
node /tmp/extract-slides.js

# Convert each slide to PDF using wkhtmltopdf
for i in {0..7}; do
    INPUT="/tmp/slide_${i}.html"
    OUTPUT="/home/user/webby-slides-bailey/Day 2 - ${SLIDE_NAMES[$i]}.pdf"

    if [ -f "$INPUT" ]; then
        echo "Converting: ${SLIDE_NAMES[$i]}"
        wkhtmltopdf --page-width 1920px --page-height 1080px \
            --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 \
            --no-outline --enable-local-file-access \
            --print-media-type --disable-smart-shrinking \
            "$INPUT" "$OUTPUT" 2>/dev/null

        if [ $? -eq 0 ]; then
            echo "Created: $OUTPUT"
        else
            echo "Failed: $OUTPUT"
        fi
    fi
done

echo "Done!"
