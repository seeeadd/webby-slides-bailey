const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const files = [
  'DAY 1 slides 1-41.html',
  'DAY 1 slides 42-84.html',
  'DAY 1 slides 85-101.html',
  'DAY 1 slides 102-115.html',
  'DAY 1 slides 145-170.html',
  'DAY 1 slides 171-189.html',
  'DAY 1 slides 190-193.html',
  'DAY 1 slides 194-242.html'
];

const workDir = __dirname;

for (const file of files) {
  const htmlPath = path.resolve(workDir, file);
  const pdfPath = htmlPath.replace('.html', '.pdf');

  console.log(`Converting: ${file}`);

  try {
    // Use wkhtmltopdf with landscape orientation for slides
    execSync(`wkhtmltopdf --orientation Landscape --page-size A4 --no-background --enable-local-file-access "${htmlPath}" "${pdfPath}"`, {
      stdio: 'inherit'
    });
    console.log(`Created: ${path.basename(pdfPath)}`);
  } catch (err) {
    console.error(`Error converting ${file}:`, err.message);
  }
}

console.log('All conversions complete!');
