# Bailey Vann Webinar Slides — Claude Code Design System
## DAY 2: WINNER HYPOTHESIS (Pink/Blush Palette)

---

## ⚠️ CRITICAL: READ BEFORE WRITING ANY CODE

### FONTS — USE BASE64 EMBEDDED (EXTRACTED FROM DAY 1 SLIDES)

**DO NOT use external GitHub URLs for fonts. They don't load reliably.**

Instead, extract the base64 font data from the working Day 1 slides file:
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

### FONT USAGE MUST MATCH EXACTLY

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

### SLIDE DIMENSIONS

```css
.slide {
    width: 1920px;
    height: 1080px;
    position: relative;
    overflow: hidden;
}
```

### THE NORTH STAR

Make attendees think: **"Holy shit, I'm getting THIS for free?"**

If a slide looks like Canva — DELETE IT AND START OVER.

---

## PHASE 1: DAY 2 COLOR SYSTEM

### ⚠️ IMPORTANT: LIGHT BACKGROUNDS, PINK ON ELEMENTS

Day 2 uses pinks, blushes, and rose tones — but NOT as heavy backgrounds.

**DO:** Light/cream backgrounds with pink on text, cards, icons, accents
**DON'T:** Pink-tinted backgrounds everywhere (looks cheap)

```css
:root {
    /* === BACKGROUNDS (Keep these LIGHT) === */
    --bg-cream: #FDF8F6;              /* Primary - warm cream with blush undertone */
    --bg-blush-white: #FFFBFA;        /* Secondary - almost white with pink warmth */
    --bg-soft: #FAF5F3;               /* Subtle warmth */
    --bg-card: #FFFFFF;               /* Cards start white, add tints */
    
    /* === DARK BACKGROUNDS (Section headers only) === */
    --bg-rose-dark: #8B4D5C;          /* Deep rose for section headers */
    --bg-rose-deeper: #5C3341;        /* Gradient end - wine/burgundy */
    --bg-mauve-dark: #6B4F5C;         /* Alternative dark */
    
    /* === PINK/BLUSH ACCENT COLORS (Use on ELEMENTS) === */
    --pink-primary: #D4727A;          /* Main pink - headers, emphasis */
    --pink-rose: #C76B73;             /* Deeper rose - secondary */
    --pink-blush: #E8A5AB;            /* Softer blush - highlights */
    --pink-dusty: #B8848B;            /* Muted dusty rose - subtle accents */
    --pink-coral: #E07B6C;            /* Coral crossover (Day 1 callback) */
    
    /* === SUPPORTING ACCENTS === */
    --sage-success: #7CB87C;          /* Checkmarks, wins, positive */
    --sage-muted: #8BA88B;            /* Softer success */
    --coral-warning: #D4685A;         /* X marks, warnings */
    --teal-callback: #1B8A8A;         /* Day 1 callbacks */
    --gold-premium: #C9A227;          /* Premium/value moments */
    
    /* === TEXT === */
    --text-dark: #2D3436;             /* Primary body */
    --text-rose: #5C3341;             /* Warm dark with rose undertone */
    --text-muted: #636E72;            /* Secondary */
    --text-light: #FFFBFA;            /* On dark backgrounds */
    
    /* === TINTED CARD BACKGROUNDS === */
    --card-blush-tint: #FEF5F4;       /* White + hint of blush */
    --card-rose-tint: #FDF0EE;        /* White + hint of rose */
    --card-sage-tint: #F5F9F5;        /* White + hint of sage */
    --card-warm-tint: #FAF6F4;        /* White + warm undertone */
}
```

---

## PHASE 2: THE BANNED LIST

### ❌ NEVER DO THESE:

1. **Pink/blush backgrounds on content slides** — Backgrounds stay cream/white
2. **Generic blob shapes at high opacity** — Use SVG gradients at 0.03-0.08 opacity
3. **Plain white cards** — Add subtle tint or gradient
4. **Gray shadows** — Shadows must be color-tinted (rose/pink tones)
5. **Flat solid colors on buttons/badges** — Use gradients
6. **Icon library graphics** — Build custom SVG
7. **Centered-everything layouts** — Be asymmetric, editorial
8. **Fallback fonts** — Use the base64-embedded OGG and Satoshi
9. **Obvious decorative elements** — Subtlety is premium
10. **"Millennial pink" overload** — Pink is an accent, not the whole palette

---

## PHASE 3: REQUIRED CSS CLASSES

Include these in every HTML file:

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
.bg-cream { background: #FDF8F6; }
.bg-blush-white { background: #FFFBFA; }
.bg-soft { background: linear-gradient(180deg, #FFFBFA 0%, #FAF5F3 100%); }

.bg-rose-dark { 
    background: linear-gradient(145deg, #8B4D5C 0%, #5C3341 100%); 
}
.bg-mauve { 
    background: linear-gradient(145deg, #6B4F5C 0%, #4A3541 100%); 
}

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
.text-rose { color: #5C3341; }
.text-muted { color: #636E72; }
.text-light { color: #FFFBFA; }
.text-pink { color: #D4727A; }
.text-coral { color: #E07B6C; }
.text-sage { color: #7CB87C; }

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

## PHASE 4: COPYABLE PATTERNS

### Background Shapes (SUBTLE — 0.03-0.08 opacity)

**❌ WRONG:**
```css
.blob { background: #D4727A; opacity: 0.3; }
```

**✅ CORRECT:**
```html
<svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
    <defs>
        <linearGradient id="blushGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#D4727A;stop-opacity:0.06" />
            <stop offset="100%" style="stop-color:#FDF8F6;stop-opacity:0.01" />
        </linearGradient>
    </defs>
    <ellipse cx="1550" cy="350" rx="500" ry="400" fill="url(#blushGrad1)"/>
</svg>
```

**For dark (rose) backgrounds:**
```html
<svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
    <defs>
        <linearGradient id="pinkGradDark" x1="30%" y1="0%" x2="70%" y2="100%">
            <stop offset="0%" style="stop-color:#E8A5AB;stop-opacity:0.1" />
            <stop offset="100%" style="stop-color:#8B4D5C;stop-opacity:0.02" />
        </linearGradient>
    </defs>
    <ellipse cx="1100" cy="300" rx="600" ry="450" fill="url(#pinkGradDark)"/>
    <ellipse cx="400" cy="850" rx="400" ry="300" fill="url(#pinkGradDark)"/>
</svg>
```

---

### Shadows (COLOR-TINTED with rose/pink)

```css
/* Pink/rose elements */
box-shadow: 0 8px 30px rgba(212, 114, 122, 0.15);
box-shadow: 0 15px 50px rgba(212, 114, 122, 0.12);

/* Blush elements */
box-shadow: 0 8px 30px rgba(232, 165, 171, 0.18);

/* Sage/success elements */
box-shadow: 0 8px 30px rgba(124, 184, 124, 0.15);

/* Coral/warning elements */
box-shadow: 0 8px 30px rgba(212, 104, 90, 0.15);

/* Subtle cards on cream */
box-shadow: 0 10px 40px rgba(139, 77, 92, 0.06);

/* Dark/rose cards */
box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
```

---

### Card Backgrounds (TINTED, not plain white)

```css
/* Blush-tinted card */
background: linear-gradient(145deg, #FFFFFF 0%, #FEF5F4 100%);
border: 1px solid rgba(212, 114, 122, 0.1);

/* Rose-tinted card */
background: linear-gradient(145deg, #FFFFFF 0%, #FDF0EE 100%);
border: 1px solid rgba(199, 107, 115, 0.1);

/* Sage-tinted card (for success/positive) */
background: linear-gradient(145deg, #FFFFFF 0%, #F5F9F5 100%);
border: 1px solid rgba(124, 184, 124, 0.1);

/* Neutral premium card */
background: linear-gradient(145deg, #FFFFFF 0%, #FAF6F4 100%);
border: 1px solid rgba(45, 52, 54, 0.05);
```

---

### Pink Elements (Gradients, not flat)

```css
/* Primary pink button/badge */
background: linear-gradient(135deg, #D4727A 0%, #E8A5AB 100%);
box-shadow: 0 8px 25px rgba(212, 114, 122, 0.3);

/* Rose accent */
background: linear-gradient(135deg, #C76B73 0%, #D4727A 100%);

/* Dark rose element */
background: linear-gradient(135deg, #8B4D5C 0%, #5C3341 100%);

/* Blush soft element */
background: linear-gradient(135deg, #E8A5AB 0%, #F0C4C8 100%);
```

---

### Premium X Marks and Checkmarks

**Coral X Mark (for warnings/mistakes):**
```html
<div style="width: 45px; height: 45px; 
            background: linear-gradient(135deg, #D4685A 0%, #C05A4D 100%); 
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 6px 20px rgba(212, 104, 90, 0.35);
            flex-shrink: 0;">
    <svg width="22" height="22" viewBox="0 0 22 22">
        <path d="M5 5 L17 17 M17 5 L5 17" stroke="white" stroke-width="2.5" stroke-linecap="round"/>
    </svg>
</div>
```

**Sage Checkmark (for success/wins):**
```html
<div style="width: 45px; height: 45px; 
            background: linear-gradient(135deg, #7CB87C 0%, #6BA86B 100%); 
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 6px 20px rgba(124, 184, 124, 0.35);
            flex-shrink: 0;">
    <svg width="22" height="22" viewBox="0 0 22 22">
        <path d="M4 11 L9 16 L18 6" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
```

**Pink Checkmark (for general positive):**
```html
<div style="width: 45px; height: 45px; 
            background: linear-gradient(135deg, #D4727A 0%, #E8A5AB 100%); 
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 6px 20px rgba(212, 114, 122, 0.35);
            flex-shrink: 0;">
    <svg width="22" height="22" viewBox="0 0 22 22">
        <path d="M4 11 L9 16 L18 6" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
```

---

### Premium List Card (Complete Pattern)

```html
<div style="background: linear-gradient(145deg, #FFFFFF 0%, #FEF5F4 100%); 
            border-radius: 16px; 
            padding: 22px 28px;
            box-shadow: 0 8px 30px rgba(212, 114, 122, 0.08);
            display: flex; 
            align-items: center; 
            gap: 20px;
            border: 1px solid rgba(212, 114, 122, 0.1);">
    
    <!-- Icon -->
    <div style="width: 45px; height: 45px; 
                background: linear-gradient(135deg, #D4727A 0%, #E8A5AB 100%); 
                border-radius: 12px;
                display: flex; align-items: center; justify-content: center;
                box-shadow: 0 6px 20px rgba(212, 114, 122, 0.3);
                flex-shrink: 0;">
        <svg width="22" height="22" viewBox="0 0 22 22">
            <path d="M4 11 L9 16 L18 6" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
    </div>
    
    <!-- Text -->
    <span style="font-family: 'Satoshi', sans-serif; 
                 font-size: 20px; 
                 font-weight: 500; 
                 color: #2D3436;">
        Your list item text here
    </span>
</div>
```

---

## PHASE 5: SLIDE TEMPLATES

### Section Header (Dark Rose Background)

```html
<div class="slide bg-rose-dark">
    <!-- Subtle blush gradient shapes -->
    <svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="sectionBlush" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#E8A5AB;stop-opacity:0.12" />
                <stop offset="100%" style="stop-color:#8B4D5C;stop-opacity:0" />
            </linearGradient>
        </defs>
        <ellipse cx="1500" cy="350" rx="550" ry="420" fill="url(#sectionBlush)"/>
        <ellipse cx="300" cy="800" rx="400" ry="300" fill="url(#sectionBlush)"/>
    </svg>
    
    <div class="content flex-center">
        <div style="text-align: center;">
            <p style="font-family: 'Satoshi', sans-serif; 
                      font-size: 18px; 
                      text-transform: uppercase;
                      letter-spacing: 4px; 
                      color: #E8A5AB; 
                      margin-bottom: 25px;">
                SECTION LABEL
            </p>
            <h1 style="font-family: 'Ogg Bold', serif; 
                       font-size: 72px; 
                       color: #FFFBFA;
                       margin-bottom: 20px;">
                THE MAIN TITLE
            </h1>
            <p style="font-family: 'Satoshi', sans-serif; 
                      font-size: 26px; 
                      color: #E8A5AB;
                      opacity: 0.9;">
                Supporting subtitle text here
            </p>
        </div>
    </div>
</div>
```

### Content Slide (Light Cream Background)

```html
<div class="slide bg-cream">
    <!-- Very subtle pink accent in corner -->
    <svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="contentPink" x1="100%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#D4727A;stop-opacity:0.05" />
                <stop offset="100%" style="stop-color:#FDF8F6;stop-opacity:0" />
            </linearGradient>
        </defs>
        <ellipse cx="1700" cy="200" rx="400" ry="350" fill="url(#contentPink)"/>
    </svg>
    
    <div class="content">
        <div style="max-width: 1000px;">
            <!-- Header with pink accent -->
            <h2 style="font-family: 'Ogg Bold', serif; 
                       font-size: 52px; 
                       color: #2D3436;
                       margin-bottom: 15px;">
                Main Headline with <span style="color: #D4727A;">Pink Emphasis</span>
            </h2>
            <p style="font-family: 'Satoshi', sans-serif; 
                      font-size: 22px; 
                      color: #636E72;
                      margin-bottom: 45px;">
                Supporting description text goes here.
            </p>
            
            <!-- Content cards -->
            <div style="display: flex; flex-direction: column; gap: 18px;">
                <!-- Card 1 -->
                <div style="background: linear-gradient(145deg, #FFFFFF 0%, #FEF5F4 100%); 
                            border-radius: 16px; padding: 22px 28px;
                            box-shadow: 0 8px 30px rgba(212, 114, 122, 0.08);
                            display: flex; align-items: center; gap: 20px;
                            border: 1px solid rgba(212, 114, 122, 0.1);">
                    <div style="width: 45px; height: 45px; 
                                background: linear-gradient(135deg, #D4727A 0%, #E8A5AB 100%); 
                                border-radius: 12px;
                                display: flex; align-items: center; justify-content: center;
                                box-shadow: 0 6px 20px rgba(212, 114, 122, 0.3);
                                flex-shrink: 0;">
                        <span style="color: white; font-family: 'Ogg Bold', serif; font-size: 20px;">1</span>
                    </div>
                    <span style="font-family: 'Satoshi', sans-serif; font-size: 20px; 
                                 font-weight: 500; color: #2D3436;">
                        First point goes here
                    </span>
                </div>
                <!-- Repeat for other cards -->
            </div>
        </div>
    </div>
</div>
```

### Quote Slide (Dark Rose with Light Text)

```html
<div class="slide" style="background: linear-gradient(145deg, #8B4D5C 0%, #5C3341 100%);">
    <svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="quoteBlush" x1="30%" y1="0%" x2="70%" y2="100%">
                <stop offset="0%" style="stop-color:#E8A5AB;stop-opacity:0.08" />
                <stop offset="100%" style="stop-color:#8B4D5C;stop-opacity:0.01" />
            </linearGradient>
        </defs>
        <ellipse cx="1200" cy="400" rx="600" ry="500" fill="url(#quoteBlush)"/>
        <ellipse cx="300" cy="750" rx="350" ry="280" fill="url(#quoteBlush)"/>
    </svg>
    
    <div class="content flex-center">
        <div style="text-align: center; max-width: 1200px;">
            <h1 style="font-family: 'Ogg Bold', serif; 
                       font-size: 56px; 
                       color: #FFFBFA;
                       line-height: 1.3;
                       margin-bottom: 20px;">
                The best ideas come from
            </h1>
            <h1 style="font-family: 'Ogg Bold', serif; 
                       font-size: 56px; 
                       color: #E8A5AB;
                       line-height: 1.3;">
                observing what's already working.
            </h1>
        </div>
    </div>
</div>
```

### Split Layout (Asymmetric)

```html
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">
        <defs>
            <linearGradient id="splitPink" x1="0%" y1="100%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#D4727A;stop-opacity:0.04" />
                <stop offset="100%" style="stop-color:#FDF8F6;stop-opacity:0" />
            </linearGradient>
        </defs>
        <ellipse cx="150" cy="900" rx="350" ry="280" fill="url(#splitPink)"/>
    </svg>
    
    <div class="content" style="display: flex; align-items: center; gap: 100px;">
        <!-- Left: Text -->
        <div style="flex: 1;">
            <h2 style="font-family: 'Ogg Bold', serif; font-size: 56px; color: #D4727A;
                       line-height: 1.1; margin-bottom: 10px;">
                Winner
            </h2>
            <h2 style="font-family: 'Ogg Bold', serif; font-size: 56px; color: #2D3436;
                       margin-bottom: 25px;">
                Hypothesis
            </h2>
            <p style="font-family: 'Satoshi', sans-serif; font-size: 22px; color: #636E72;">
                Research before you create.<br>Validate before you invest.
            </p>
        </div>
        
        <!-- Right: Cards -->
        <div style="flex: 1; display: flex; flex-direction: column; gap: 16px;">
            <!-- Card with checkmark -->
            <div style="background: linear-gradient(145deg, #FFFFFF 0%, #FEF5F4 100%); 
                        border-radius: 16px; padding: 22px 28px;
                        box-shadow: 0 8px 30px rgba(212, 114, 122, 0.08);
                        display: flex; align-items: center; gap: 18px;
                        border: 1px solid rgba(212, 114, 122, 0.1);">
                <div style="width: 42px; height: 42px; 
                            background: linear-gradient(135deg, #7CB87C 0%, #6BA86B 100%); 
                            border-radius: 10px;
                            display: flex; align-items: center; justify-content: center;
                            box-shadow: 0 4px 15px rgba(124, 184, 124, 0.3);
                            flex-shrink: 0;">
                    <svg width="20" height="20" viewBox="0 0 20 20">
                        <path d="M4 10 L8 14 L16 5" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <span style="font-family: 'Satoshi', sans-serif; font-size: 20px; 
                             font-weight: 500; color: #2D3436;">Data-backed decision</span>
            </div>
            <!-- Repeat for other cards -->
        </div>
    </div>
</div>
```

---

## PHASE 6: CUSTOM SVG GRAPHICS

### Arrow (Pink)
```html
<svg width="80" height="40" viewBox="0 0 80 40">
    <path d="M0 20 L55 20 M45 10 L60 20 L45 30" 
          stroke="#D4727A" stroke-width="4" fill="none" 
          stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Heart/Love Icon
```html
<svg width="28" height="28" viewBox="0 0 28 28">
    <path d="M14 24 C5 17 2 12 2 8 C2 4 5 2 8 2 C11 2 14 5 14 8 C14 5 17 2 20 2 C23 2 26 4 26 8 C26 12 23 17 14 24Z" 
          fill="#D4727A"/>
</svg>
```

### Lightbulb/Idea Icon
```html
<svg width="50" height="50" viewBox="0 0 50 50">
    <circle cx="25" cy="20" r="14" fill="none" stroke="#D4727A" stroke-width="3"/>
    <path d="M20 34 L30 34 M21 38 L29 38 M22 42 L28 42" stroke="#D4727A" stroke-width="3" stroke-linecap="round"/>
    <path d="M25 10 L25 6" stroke="#E8A5AB" stroke-width="2" stroke-linecap="round"/>
    <path d="M18 12 L15 9" stroke="#E8A5AB" stroke-width="2" stroke-linecap="round"/>
    <path d="M32 12 L35 9" stroke="#E8A5AB" stroke-width="2" stroke-linecap="round"/>
</svg>
```

### Target/Bullseye Icon
```html
<svg width="50" height="50" viewBox="0 0 50 50">
    <circle cx="25" cy="25" r="20" fill="none" stroke="#D4727A" stroke-width="3"/>
    <circle cx="25" cy="25" r="12" fill="none" stroke="#D4727A" stroke-width="3"/>
    <circle cx="25" cy="25" r="4" fill="#D4727A"/>
</svg>
```

### Magnifying Glass (Research)
```html
<svg width="50" height="50" viewBox="0 0 50 50">
    <circle cx="22" cy="22" r="14" fill="none" stroke="#D4727A" stroke-width="3"/>
    <path d="M32 32 L44 44" stroke="#D4727A" stroke-width="4" stroke-linecap="round"/>
</svg>
```

---

## PHASE 7: ANIMATION VIA SLIDE DUPLICATION

PowerPoint animations can't be coded, so we duplicate slides:

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

Keep layouts IDENTICAL between duplicates — only content visibility changes.

---

## PHASE 8: FINAL CHECKLIST

Before ANY slide is done:

- [ ] **@font-face with BASE64** — Extract from Day 1 slides (`/mnt/user-data/uploads/Day_1_Slides_194-242__4_.html`)
- [ ] **Font-family EXACT match** — `'Ogg Bold'` and `'Satoshi'` (case-sensitive, with quotes)
- [ ] **Background is LIGHT** — Cream/white, NOT pink-tinted
- [ ] **Pink is on ELEMENTS** — Headers, cards, icons, badges — not backgrounds
- [ ] **Background shapes are SUBTLE** — SVG gradients at 0.03-0.08 opacity
- [ ] **Shadows are COLOR-TINTED** — Rose/pink tones, not gray
- [ ] **Cards have GRADIENT backgrounds** — White → blush tint, not plain white
- [ ] **Cards have SUBTLE borders** — 1px with low-opacity pink
- [ ] **Icons are CUSTOM SVG** — No icon libraries
- [ ] **Buttons/badges use GRADIENTS** — Not flat colors
- [ ] **Layout is ASYMMETRIC** — Not centered-everything
- [ ] **Would someone pay $2K for this?** — If not, redesign

---

## QUICK REFERENCE: DAY 2 vs DAY 1 vs DAY 3

| Element | Day 1 (Teal/Coral) | Day 2 (Pink/Blush) | Day 3 (Gold/Bronze) |
|---------|-------------------|-------------------|---------------------|
| Primary accent | #1B8A8A (teal) | #D4727A (pink) | #C9A227 (gold) |
| Secondary accent | #E07B6C (coral) | #E8A5AB (blush) | #B8860B (amber) |
| Dark background | #2D3436 | #8B4D5C (rose) | #5C4827 (bronze) |
| Success color | #7CB87C | #7CB87C (same) | #6B8E6B (sage) |
| Warning color | #E07B6C | #D4685A (coral) | #E07B6C (coral) |
| Light background | #FDF8F3 | #FDF8F6 | #FDF8F3 |
| Card tint | Cool white | Blush white | Warm gold white |
| Vibe | Professional, fresh | Warm, feminine, soft | Premium, closing energy |

---

## DAY 2 SPECIFIC NOTES

Day 2 is the **validation/research** day. The pink/blush palette should feel:

✅ **Warm and approachable** — Not clinical or cold
✅ **Feminine but professional** — Not "girly" or juvenile
✅ **Soft but confident** — The blush tones convey expertise without harshness
✅ **Research energy** — Curiosity, discovery, insight

The pink should enhance the "aha moment" energy of learning to validate product ideas.

**Key visual moments for Day 2:**
- Winner Hypothesis Framework reveal
- Research tool demonstrations
- "Green flags" validation criteria
- Before/after transformation moments

---

## REMEMBER

Day 2 should feel **warm and insightful** like a supportive mentor — but keep backgrounds LIGHT.

The pink should appear on:
- Headers and emphasized text
- Card icons and badges
- Section dividers and accents
- Buttons and CTAs
- Key framework reveals

The pink should NOT appear on:
- Full slide backgrounds (keep cream/white)
- Large areas that make it look "too pink"
- Every single element (use restraint)

When in doubt: **Light background, pink elements, rose-tinted shadows, gradient everything.**
