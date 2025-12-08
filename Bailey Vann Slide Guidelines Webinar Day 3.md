# Bailey Vann Webinar Slides — Claude Code Design System
## VERSION 2.0 — WITH COPYABLE PATTERNS

---

## ⚠️ CRITICAL: FONTS ARE ON GITHUB — USE THEM

**STOP using fallback fonts. The actual OGG Bold and Satoshi fonts are hosted on GitHub.**

### OPTION 1: USE BASE64 EMBEDDED FONTS (MOST RELIABLE)

Extract the base64 font data from the working Day 1 slides file:
`/mnt/user-data/uploads/Day_1_Slides_194-242__4_.html`

**HOW TO EXTRACT:**

1. Open the Day 1 HTML file
2. Find the `@font-face` declarations in the `<style>` block
3. Copy the ENTIRE @font-face blocks including the base64 data
4. Paste into your new HTML file

The base64 format looks like this:
```css
@font-face {
    font-family: 'Ogg Bold';
    src: url(data:font/woff2;base64,d09GMgABAAAAAC...[very long string]...==) format('woff2');
    font-weight: bold;
    font-style: normal;
    font-display: swap;
}
```

**CRITICAL:** The base64 string will be VERY long (thousands of characters). Copy ALL of it.

### OPTION 2: USE GITHUB URLS (IF BASE64 NOT AVAILABLE)

```css
@font-face {
    font-family: 'Ogg Bold';
    src: url('https://seanthea.github.io/bailey-fonts/Ogg-Bold.woff2') format('woff2'),
         url('https://seanthea.github.io/bailey-fonts/Ogg-Bold.woff') format('woff');
    font-weight: bold;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'Satoshi';
    src: url('https://seanthea.github.io/bailey-fonts/Satoshi-Variable.woff2') format('woff2'),
         url('https://seanthea.github.io/bailey-fonts/Satoshi-Variable.woff') format('woff');
    font-weight: 100 900;
    font-style: normal;
    font-display: swap;
}
```

### ⚠️ FONT USAGE MUST MATCH EXACTLY

When USING the fonts, the font-family name MUST match the @font-face declaration EXACTLY:

```css
/* ✅ CORRECT — matches @font-face declaration exactly */
font-family: 'Ogg Bold', serif;
font-family: 'Satoshi', sans-serif;

/* ❌ WRONG — these will NOT work */
font-family: 'OGG Bold', serif;      /* wrong case */
font-family: 'Ogg', serif;           /* missing 'Bold' */
font-family: 'ogg bold', serif;      /* wrong case */
font-family: Ogg Bold, serif;        /* missing quotes */
font-family: 'Satoshi Variable', sans-serif;  /* wrong name */
```

### IF FONTS DON'T RENDER

1. Use base64 embedded fonts from Day 1 slides (most reliable)
2. Check browser console for 404 errors on font URLs
3. Ensure font-family in usage EXACTLY matches @font-face declaration (case-sensitive)

### SLIDE DIMENSIONS

```css
.slide {
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    page-break-after: always;
}
```

---

## REQUIRED CSS CLASSES (Include in every HTML file)

```css
/* === BASE === */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* === SLIDE CONTAINER === */
.slide {
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    page-break-after: always;
}

/* === BACKGROUNDS === */
.bg-cream { background: #FDF8F3; }
.bg-blush { background: #FEF0EA; }
.bg-teal { background: linear-gradient(135deg, #1B8A8A, #2BA5A3); }
.bg-coral { background: linear-gradient(135deg, #E07B6C, #F4A89A); }
.bg-dark { background: #2D3436; }
.bg-dark-deep { background: linear-gradient(145deg, #1E1E26 0%, #141418 100%); }

/* === TYPOGRAPHY === */
.display {
    font-family: 'Ogg Bold', serif;
    font-weight: bold;
    line-height: 1.2;
}

.body {
    font-family: 'Satoshi', sans-serif;
    font-weight: 500;
    line-height: 1.6;
}

/* === TEXT COLORS === */
.text-dark { color: #2D3436; }
.text-muted { color: #636E72; }
.text-light { color: #FFFFFF; }
.text-teal { color: #1B8A8A; }
.text-coral { color: #E07B6C; }
.text-gold { color: #D4AF37; }

/* === LAYOUT HELPERS === */
.flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.content {
    position: relative;
    z-index: 1;
    padding: 60px 80px;
    height: 100%;
}

.text-center { text-align: center; }

/* === BACKGROUND SHAPES CONTAINER === */
.bg-shapes {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}
```

---

## READ THIS FIRST: THE NORTH STAR

You are creating slides that should make people think:
**"Holy shit, I'm getting THIS for free? What happens when I actually pay her?"**

This is NOT a quick template job. This is $50K design agency quality.

**If a slide looks like it could exist in Canva's template library — DELETE IT AND START OVER.**

---

## PHASE 1: BRAND FOUNDATIONS

### Color System (CSS Variables)
```css
:root {
  /* Primary */
  --bailey-teal: #1B8A8A;
  --bailey-teal-light: #2BA5A3;
  --bailey-coral: #E07B6C;
  --bailey-coral-soft: #F4A89A;
  
  /* Neutrals */
  --bailey-cream: #FDF8F3;
  --bailey-blush: #FEF0EA;
  --bailey-pink-soft: #FADADD;
  
  /* Accents */
  --bailey-gold: #D4AF37;
  --bailey-green: #7CB87C;
  --bailey-yellow: #F7E16C;
  
  /* Text */
  --text-dark: #2D3436;
  --text-muted: #636E72;
  --text-light: #FFFFFF;
  
  /* Day 3 Gold Palette (when applicable) */
  --gold-warm: #C9A227;
  --gold-amber: #B8860B;
  --gold-bronze: #5C4827;
  --gold-honey: #D4A84B;
}
```

### Typography
- **Headers:** OGG Bold
- **Body:** Satoshi Variable
- **NO EMOJIS. EVER.**

### FONT IMPORTS (COPY THIS EXACTLY — FONTS ARE ON GITHUB)

```css
@font-face {
    font-family: 'Ogg Bold';
    src: url('https://seanthea.github.io/bailey-fonts/Ogg-Bold.woff2') format('woff2'),
         url('https://seanthea.github.io/bailey-fonts/Ogg-Bold.woff') format('woff');
    font-weight: bold;
    font-style: normal;
    font-display: swap;
}

@font-face {
    font-family: 'Satoshi';
    src: url('https://seanthea.github.io/bailey-fonts/Satoshi-Variable.woff2') format('woff2'),
         url('https://seanthea.github.io/bailey-fonts/Satoshi-Variable.woff') format('woff');
    font-weight: 100 900;
    font-style: normal;
    font-display: swap;
}
```

**CRITICAL: Always include these @font-face declarations at the TOP of your CSS. Do NOT use fallback fonts. The fonts are hosted and available.**

Usage:
```css
/* Headers */
font-family: 'Ogg Bold', serif;

/* Body text */
font-family: 'Satoshi', sans-serif;
font-weight: 500; /* Medium weight */
```

---

## PHASE 2: THE BANNED LIST (DO NOT DO THESE)

### ❌ NEVER DO THIS:

1. **Generic blob shapes** — No Canva-style organic shapes at high opacity
2. **Plain white cards** — Cards must have tinted backgrounds or gradient
3. **Gray shadows** — Shadows must be color-tinted
4. **Flat solid colors** — Use gradients on key elements
5. **Centered-everything layouts** — Be asymmetric, editorial
6. **Icon library circles** — Build custom SVG graphics
7. **Same-size everything** — Use scale transforms for emphasis
8. **Basic X marks** — Even negative indicators need premium treatment
9. **Obvious decorative elements** — Background shapes should be SUBTLE (opacity 0.03-0.1)

### IF YOU SEE YOURSELF DOING ANY OF THESE, STOP AND REDESIGN.

---

## PHASE 3: COPYABLE CSS PATTERNS

### Background Shapes (The RIGHT Way)

**❌ WRONG (What you're doing now):**
```css
/* This looks like Canva */
.blob {
  background: #C9A227;
  opacity: 0.3;
  border-radius: 50%;
}
```

**✅ CORRECT (What Day 1 does):**
```html
<svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
    <defs>
        <linearGradient id="uniqueGradId" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#1B8A8A;stop-opacity:0.06" />
            <stop offset="100%" style="stop-color:#FDF8F3;stop-opacity:0.02" />
        </linearGradient>
    </defs>
    <ellipse cx="1600" cy="400" rx="500" ry="400" fill="url(#uniqueGradId)"/>
</svg>
```

**Key differences:**
- Uses SVG gradient, not solid color
- Opacity is **0.02-0.1**, not 0.3+
- Positioned OFF-CENTER (cx="1600" not centered)
- Uses ellipse with different rx/ry, not perfect circle

---

### Card Shadows (The RIGHT Way)

**❌ WRONG:**
```css
box-shadow: 0 4px 6px rgba(0,0,0,0.1);
```

**✅ CORRECT (Color-tinted shadows):**
```css
/* For coral/warning elements */
box-shadow: 0 8px 30px rgba(224, 123, 108, 0.15);

/* For teal/positive elements */
box-shadow: 0 15px 50px rgba(27, 138, 138, 0.3);

/* For gold/premium elements */
box-shadow: 0 15px 50px rgba(212, 175, 55, 0.12);

/* For dark stat cards */
box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);

/* For subtle white cards */
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
```

**Rule: Shadows should ALWAYS pick up the element's primary color at low opacity.**

---

### Card Backgrounds (The RIGHT Way)

**❌ WRONG:**
```css
background: white;
```

**✅ CORRECT (Tinted backgrounds):**
```css
/* Teal-tinted for positive/teal contexts */
background: #E8F5F3;

/* Coral-tinted for warning contexts */
background: #FEF0EA;

/* Gold-tinted for premium contexts */
background: #FAF3E0;

/* Cream base for general cards */
background: #FDF8F3;

/* Soft gradient for elevated cards */
background: linear-gradient(145deg, #FFFFFF 0%, #FDF8F3 100%);
```

---

### Gradient Buttons/Elements (The RIGHT Way)

**❌ WRONG:**
```css
background: #1B8A8A;
```

**✅ CORRECT:**
```css
/* Teal gradient */
background: linear-gradient(135deg, #1B8A8A, #2BA5A3);

/* Coral gradient */
background: linear-gradient(135deg, #E07B6C, #F4A89A);

/* Gold gradient */
background: linear-gradient(135deg, #C9A227, #D4A84B);

/* Dark stat gradient */
background: linear-gradient(145deg, #2D2D38 0%, #232330 100%);
```

---

### Emphasis with Scale (The RIGHT Way)

When you want something to stand out:
```css
/* Make the "winner" element pop */
.highlighted-element {
  transform: scale(1.1);
}

/* Make "before" or "wrong" elements recede */
.de-emphasized {
  opacity: 0.5;
}
```

---

### Custom X Marks / Checkmarks (The RIGHT Way)

**❌ WRONG:**
```html
<div style="color: red;">✗</div>
```

**✅ CORRECT:**
```html
<!-- Coral X mark with proper styling -->
<div style="width: 45px; height: 45px; background: #E07B6C; border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 4px 15px rgba(224, 123, 108, 0.25);">
    <svg width="24" height="24" viewBox="0 0 24 24">
        <path d="M6 6 L18 18 M18 6 L6 18" stroke="white" stroke-width="3" stroke-linecap="round"/>
    </svg>
</div>

<!-- Teal checkmark with proper styling -->
<div style="width: 45px; height: 45px; background: linear-gradient(135deg, #1B8A8A, #2BA5A3); 
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 4px 15px rgba(27, 138, 138, 0.25);">
    <svg width="24" height="24" viewBox="0 0 24 24">
        <path d="M5 12 L10 17 L19 7" stroke="white" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
```

---

### List Cards (The RIGHT Way)

**❌ WRONG (What Image 2 looks like):**
```html
<div style="background: white; border-radius: 12px; padding: 20px;">
    <span style="color: red;">✗</span> Niche selection
</div>
```

**✅ CORRECT:**
```html
<div style="background: linear-gradient(145deg, #FFFFFF 0%, #FEF0EA 100%); 
            border-radius: 16px; padding: 22px 28px;
            box-shadow: 0 8px 30px rgba(224, 123, 108, 0.08);
            display: flex; align-items: center; gap: 18px;
            border: 1px solid rgba(224, 123, 108, 0.1);">
    
    <!-- Proper X mark -->
    <div style="width: 42px; height: 42px; background: #E07B6C; border-radius: 10px;
                display: flex; align-items: center; justify-content: center;
                box-shadow: 0 4px 12px rgba(224, 123, 108, 0.3); flex-shrink: 0;">
        <svg width="20" height="20" viewBox="0 0 20 20">
            <path d="M5 5 L15 15 M15 5 L5 15" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
        </svg>
    </div>
    
    <span style="font-family: 'Satoshi', sans-serif; font-size: 20px; font-weight: 500;
                 color: #2D3436;">Niche selection</span>
</div>
```

**Key differences:**
- Gradient background (white → tinted)
- Color-tinted shadow
- Subtle border with color tint
- Proper padding and gap
- Premium icon treatment
- Correct typography

---

### Quote Slides (The RIGHT Way)

**❌ WRONG (What Image 1 looks like):**
```html
<div style="background: #5C4827;">
    <div class="blob" style="background: #C9A227; opacity: 0.3;"></div>
    <h1>When your time creates money...</h1>
</div>
```

**✅ CORRECT:**
```html
<div class="slide" style="background: linear-gradient(145deg, #5C4827 0%, #3D2B1F 100%); position: relative;">
    
    <!-- Subtle gradient shape, NOT a blob -->
    <svg style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
         viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="quoteGrad" x1="30%" y1="0%" x2="70%" y2="100%">
                <stop offset="0%" style="stop-color:#C9A227;stop-opacity:0.08" />
                <stop offset="100%" style="stop-color:#5C4827;stop-opacity:0.02" />
            </linearGradient>
        </defs>
        <ellipse cx="1100" cy="300" rx="600" ry="450" fill="url(#quoteGrad)"/>
        <ellipse cx="400" cy="800" rx="400" ry="350" fill="url(#quoteGrad)"/>
    </svg>
    
    <!-- Content with proper treatment -->
    <div style="position: relative; z-index: 1; text-align: center; padding: 60px;">
        <h1 style="font-family: 'OGG-Bold', Georgia, serif; font-size: 52px; 
                   color: #FFFEF5; line-height: 1.3; margin-bottom: 20px;">
            When your time creates money,
        </h1>
        <h1 style="font-family: 'OGG-Bold', Georgia, serif; font-size: 52px; 
                   color: #C9A227; line-height: 1.3;">
            money's job is to buy back your time.
        </h1>
    </div>
</div>
```

**Key differences:**
- Background is a GRADIENT, not flat
- Shape uses SVG gradient ellipse at 0.08 opacity, not solid blob
- Multiple subtle shapes for depth
- Typography has proper font stack

---

## PHASE 4: SLIDE TYPE PATTERNS

### Title/Section Headers
```html
<div class="slide" style="background: linear-gradient(145deg, #5C4827 0%, #3D2B1F 100%);">
    <!-- Subtle background treatment -->
    <svg style="position: absolute; inset: 0; width: 100%; height: 100%;" 
         viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="sectionGrad" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#C9A227;stop-opacity:0.1" />
                <stop offset="100%" style="stop-color:#5C4827;stop-opacity:0" />
            </linearGradient>
        </defs>
        <ellipse cx="1500" cy="350" rx="550" ry="420" fill="url(#sectionGrad)"/>
    </svg>
    
    <div style="position: relative; z-index: 1; display: flex; flex-direction: column;
                align-items: center; justify-content: center; height: 100%; text-align: center;">
        <p style="font-family: 'Satoshi', sans-serif; font-size: 18px; text-transform: uppercase;
                  letter-spacing: 3px; color: #C9A227; margin-bottom: 20px;">
            SECTION LABEL
        </p>
        <h1 style="font-family: 'OGG-Bold', Georgia, serif; font-size: 64px; color: #C9A227;">
            THE MAIN TITLE
        </h1>
        <p style="font-family: 'Satoshi', sans-serif; font-size: 24px; color: #FFFEF5;
                  margin-top: 25px; opacity: 0.9;">
            Supporting subtitle text
        </p>
    </div>
</div>
```

### Content Cards Layout
```html
<div class="slide" style="background: #FDF8F3;">
    <!-- Gradient accent -->
    <svg style="position: absolute; inset: 0;" viewBox="0 0 1920 1080">
        <defs>
            <linearGradient id="contentGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#E07B6C;stop-opacity:0.05" />
                <stop offset="100%" style="stop-color:#FDF8F3;stop-opacity:0" />
            </linearGradient>
        </defs>
        <ellipse cx="200" cy="900" rx="400" ry="300" fill="url(#contentGrad)"/>
    </svg>
    
    <div style="position: relative; z-index: 1; padding: 60px 80px;">
        <!-- Header -->
        <div style="margin-bottom: 50px;">
            <h2 style="font-family: 'OGG-Bold', Georgia, serif; font-size: 48px; color: #2D3436;">
                <span style="color: #E07B6C;">Never</span> Delegate
            </h2>
            <p style="font-family: 'Satoshi', sans-serif; font-size: 20px; color: #636E72;
                      margin-top: 12px;">
                You are the vision. A VA can't be you.
            </p>
        </div>
        
        <!-- Cards grid -->
        <div style="display: flex; flex-direction: column; gap: 16px; max-width: 500px; margin-left: auto;">
            <!-- Card 1 -->
            <div style="background: linear-gradient(145deg, #FFFFFF 0%, #FEF0EA 100%); 
                        border-radius: 16px; padding: 22px 28px;
                        box-shadow: 0 8px 30px rgba(224, 123, 108, 0.08);
                        display: flex; align-items: center; gap: 18px;
                        border: 1px solid rgba(224, 123, 108, 0.1);">
                <div style="width: 42px; height: 42px; background: #E07B6C; border-radius: 10px;
                            display: flex; align-items: center; justify-content: center;
                            box-shadow: 0 4px 12px rgba(224, 123, 108, 0.3); flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 20 20">
                        <path d="M5 5 L15 15 M15 5 L5 15" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
                    </svg>
                </div>
                <span style="font-family: 'Satoshi', sans-serif; font-size: 20px; 
                             font-weight: 500; color: #2D3436;">Niche selection</span>
            </div>
            <!-- Repeat for other cards -->
        </div>
    </div>
</div>
```

---

## PHASE 5: CUSTOM GRAPHICS (BUILD THESE)

Don't use icon libraries. Build custom SVG graphics for:

### Custom Arrow
```html
<svg width="80" height="40" viewBox="0 0 80 40">
    <path d="M0 20 L60 20 M50 10 L65 20 L50 30" 
          stroke="#1B8A8A" stroke-width="4" fill="none" 
          stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Building Blocks Icon
```html
<svg width="60" height="60" viewBox="0 0 60 60">
    <rect x="10" y="35" width="40" height="15" rx="3" fill="#1B8A8A"/>
    <rect x="15" y="22" width="30" height="12" rx="2" fill="#2BA5A3"/>
    <rect x="20" y="12" width="20" height="9" rx="2" fill="#D4AF37"/>
</svg>
```

### Star/Sparkle
```html
<svg width="24" height="24" viewBox="0 0 24 24">
    <path d="M12 2 L14 9 L21 9 L15 14 L17 21 L12 17 L7 21 L9 14 L3 9 L10 9 Z" 
          fill="#D4AF37"/>
</svg>
```

---

## PHASE 6: THE FINAL CHECKLIST

Before you consider ANY slide done:

- [ ] **Fonts are BASE64 embedded** — Extract from Day 1 slides, or use GitHub URLs as fallback
- [ ] **Font-family EXACT match** — `'Ogg Bold'` and `'Satoshi'` (case-sensitive, with quotes)
- [ ] **No generic blobs** — Background shapes use SVG gradients at 0.02-0.1 opacity
- [ ] **No gray shadows** — All shadows are color-tinted
- [ ] **No plain white cards** — Cards have tinted backgrounds or gradients
- [ ] **No flat colors on key elements** — Buttons/badges use gradients
- [ ] **No icon library graphics** — Custom SVG for every icon
- [ ] **No same-size everything** — Scale transforms for emphasis
- [ ] **No centered-everything** — Asymmetric, editorial layouts
- [ ] **No Canva vibes** — Would someone pay $2K for a course with this slide?

---

## PHASE 7: A/B EXAMPLES

### Quote Slide

**❌ CANVA LOOK:**
- Solid brown background
- Obvious blob shape at 30% opacity
- Flat gold text
- No depth

**✅ PREMIUM LOOK:**
- Gradient background (dark bronze → deeper)
- Multiple SVG gradient ellipses at 5-8% opacity
- Two-tone text (white + gold for emphasis)
- Subtle vignette effect

### List Slide

**❌ CANVA LOOK:**
- Flat cream background
- Obvious decorative blob
- Plain white cards with gray shadows
- Basic circle icons with X

**✅ PREMIUM LOOK:**
- Cream with subtle gradient accent in corner
- Cards with gradient backgrounds (white → tinted)
- Color-tinted shadows matching the icon color
- Premium icon treatment with proper sizing and shadow
- Cards have subtle colored border

---

## PHASE 8: ANIMATION VIA SLIDE DUPLICATION

PowerPoint animations can't be coded directly, so we fake it by duplicating slides.

**When to use:** When Bailey needs to explain something BEFORE the full content appears.

**Example — 3 bullet reveal:**
```
Slide 14a: Headline only (Bailey introduces)
Slide 14b: Headline + bullet 1
Slide 14c: Headline + bullets 1-2  
Slide 14d: Headline + all 3 bullets (complete)
```

**Example — Before/After reveal:**
```
Slide 22a: Only "BEFORE" graphic visible
Slide 22b: Both "BEFORE" and "AFTER" visible
```

**Example — Big number reveal:**
```
Slide 79a: Setup text "After switching to digital products..."
Slide 79b: The big "$1,000,000+" appears
```

**Rules:**
- Keep layouts IDENTICAL between duplicates
- Only content visibility changes
- Creates seamless "animation" when clicking through

---

## REMEMBER

**The difference between "fine" and "premium" is in the DETAILS:**

1. Shadow color matches element color
2. Backgrounds are gradients, not flat
3. Shapes are subtle (0.02-0.1 opacity), not obvious
4. Icons are custom SVG, not library
5. Text has proper hierarchy with color emphasis
6. Cards have subtle tints and proper depth
7. Layout is editorial, not template

**When in doubt:** Look at the Day 1 HTML and copy the pattern exactly, then adapt for your content.
