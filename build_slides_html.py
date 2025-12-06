"""
Bailey Vann - The 2026 Etsy Reset
HTML-BASED SLIDE BUILDER with WeasyPrint PDF Export

Benefits:
- Exact font rendering (embedded OGG fonts)
- Smooth SVG organic shapes
- What you see = what you get
- No font substitution
"""

import os
import base64
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# =============================================================================
# DESIGN SYSTEM
# =============================================================================

COLORS = {
    'teal_deep': '#1B8A8A',
    'teal': '#2BA5A3',
    'teal_light': '#5BBCB3',
    'coral': '#E07B6C',
    'coral_soft': '#F4A89A',
    'coral_pale': '#FDD5CC',
    'cream': '#FDF8F3',
    'cream_dark': '#F5EEE6',
    'blush': '#FEF0EA',
    'blush_soft': '#FEE5E0',
    'mint': '#E8F5F3',
    'gold': '#D4AF37',
    'gold_soft': '#F7E19C',
    'dark': '#2D3436',
    'muted': '#636E72',
    'light': '#9CA3A8',
    'white': '#FFFFFF',
}

# Slide dimensions (16:9 at 1920x1080)
SLIDE_WIDTH = 1920
SLIDE_HEIGHT = 1080

# =============================================================================
# FONT EMBEDDING
# =============================================================================

def get_font_base64(font_path):
    """Read font file and return base64 encoded string"""
    if os.path.exists(font_path):
        with open(font_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return None

def get_font_css():
    """Generate @font-face CSS with embedded fonts"""
    fonts = [
        ('Ogg Bold', 'Ogg Bold Font.ttf'),
        ('Ogg Medium', 'Ogg Medium Font.ttf'),
        ('Ogg Light', 'Ogg Light Font.ttf'),
        ('Ogg Text', 'Ogg Text Book.ttf'),
        ('Ogg Text Medium', 'Ogg Text Medium.ttf'),
    ]

    css = ""
    base_path = "/home/user/webby-slides-bailey"

    for font_name, font_file in fonts:
        font_path = os.path.join(base_path, font_file)
        if os.path.exists(font_path):
            b64 = get_font_base64(font_path)
            css += f"""
@font-face {{
    font-family: '{font_name}';
    src: url('data:font/truetype;base64,{b64}') format('truetype');
    font-weight: normal;
    font-style: normal;
}}
"""
    return css

# =============================================================================
# SVG ORGANIC SHAPES
# =============================================================================

def svg_blob(cx, cy, rx, ry, color, opacity=0.3, rotation=0):
    """Generate smooth organic blob using SVG ellipse with rotation"""
    return f'''<ellipse
        cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"
        fill="{color}" fill-opacity="{opacity}"
        transform="rotate({rotation} {cx} {cy})"
    />'''

def svg_smooth_blob(cx, cy, size, color, opacity=0.3, seed=0):
    """Generate smooth organic blob using SVG path with bezier curves"""
    import math

    # Generate smooth blob points
    points = 8
    r = size / 2
    path_data = []

    for i in range(points):
        angle = (2 * math.pi * i) / points
        # Subtle variation for organic feel
        variation = 0.15 * math.sin(3 * angle + seed) + 0.1 * math.cos(2 * angle + seed)
        curr_r = r * (0.85 + variation)

        x = cx + curr_r * math.cos(angle)
        y = cy + curr_r * math.sin(angle)

        if i == 0:
            path_data.append(f"M {x:.1f} {y:.1f}")
        else:
            # Use smooth curve
            path_data.append(f"L {x:.1f} {y:.1f}")

    path_data.append("Z")

    return f'<path d="{" ".join(path_data)}" fill="{color}" fill-opacity="{opacity}" />'

# =============================================================================
# BASE CSS
# =============================================================================

def get_base_css():
    return f"""
{get_font_css()}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

@page {{
    size: {SLIDE_WIDTH}px {SLIDE_HEIGHT}px;
    margin: 0;
}}

.slide {{
    width: {SLIDE_WIDTH}px;
    height: {SLIDE_HEIGHT}px;
    position: relative;
    overflow: hidden;
    page-break-after: always;
    font-family: 'Ogg Text', Georgia, serif;
}}

.slide:last-child {{
    page-break-after: auto;
}}

/* Typography */
.display {{
    font-family: 'Ogg Bold', Georgia, serif;
    font-weight: bold;
}}

.body {{
    font-family: 'Ogg Text', Georgia, serif;
}}

.light {{
    font-family: 'Ogg Light', Georgia, serif;
}}

/* Background shapes container */
.bg-shapes {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
}}

/* Content container */
.content {{
    position: relative;
    z-index: 10;
    width: 100%;
    height: 100%;
    padding: 60px 80px;
}}

/* Pill label */
.pill {{
    display: inline-block;
    padding: 12px 28px;
    border-radius: 50px;
    font-size: 18px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
}}

/* Floating card */
.card {{
    background: white;
    border-radius: 24px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.08);
    padding: 60px;
}}

/* Accent card (teal) */
.card-teal {{
    background: {COLORS['teal_deep']};
    color: white;
    border-radius: 16px;
    padding: 24px 40px;
}}

/* Text colors */
.text-dark {{ color: {COLORS['dark']}; }}
.text-muted {{ color: {COLORS['muted']}; }}
.text-light {{ color: {COLORS['light']}; }}
.text-white {{ color: white; }}
.text-teal {{ color: {COLORS['teal_deep']}; }}
.text-coral {{ color: {COLORS['coral']}; }}

/* Background colors */
.bg-cream {{ background: {COLORS['cream']}; }}
.bg-blush {{ background: linear-gradient(135deg, {COLORS['cream']}, {COLORS['blush_soft']}); }}
.bg-teal {{ background: linear-gradient(135deg, {COLORS['teal_deep']}, {COLORS['teal']}); }}
.bg-coral {{ background: linear-gradient(135deg, {COLORS['coral']}, {COLORS['coral_soft']}); }}
.bg-dark {{ background: {COLORS['dark']}; }}

/* Utility */
.text-center {{ text-align: center; }}
.flex-center {{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}}
"""

# =============================================================================
# SLIDE BUILDERS
# =============================================================================

def slide_01_title():
    """Title slide - THE 2026 ETSY RESET"""
    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1600, 200, 400, 350, COLORS['mint'], 0.5, 20)}
        {svg_blob(100, 900, 300, 280, COLORS['blush_soft'], 0.6, -15)}
        {svg_blob(1700, 850, 250, 200, COLORS['gold_soft'], 0.4, 10)}
        {svg_blob(1500, 550, 200, 180, COLORS['coral_soft'], 0.7, 25)}
        {svg_blob(1620, 680, 150, 130, COLORS['gold_soft'], 0.6, -10)}
    </svg>

    <div class="content">
        <div class="pill" style="background: {COLORS['teal_deep']}; color: white; margin-bottom: 20px;">
            Day 1 of 3
        </div>

        <p class="body text-teal" style="font-size: 28px; margin-bottom: 20px;">
            The 2026 Etsy Upgrade Challenge
        </p>

        <h1 class="display text-dark" style="font-size: 200px; line-height: 0.9; margin-bottom: 30px;">
            RESET
        </h1>

        <div class="body text-muted" style="font-size: 32px; line-height: 1.6; margin-bottom: 40px;">
            Delete the Dead Weight.<br>
            Find Your Focus.<br>
            Build a Shop That Actually Works.
        </div>

        <div class="card-teal" style="display: inline-block;">
            <span class="body" style="font-size: 22px;">
                with <strong>Bailey Vann</strong> &bull; Top 0.1% Etsy Seller &bull; $1M+ in Digital Product Sales
            </span>
        </div>
    </div>
</div>
'''

def slide_02_before_begin():
    """Before We Begin - Pop Quiz"""
    return f'''
<div class="slide bg-blush">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 180, 320, 280, COLORS['mint'], 0.45, 15)}
        {svg_blob(100, 850, 280, 250, COLORS['coral_pale'], 0.5, -20)}
    </svg>

    <div class="content flex-center">
        <div class="card text-center" style="max-width: 900px;">
            <h1 class="display text-dark" style="font-size: 80px; margin-bottom: 30px;">
                Before We Begin...
            </h1>

            <div style="width: 120px; height: 6px; background: {COLORS['teal']}; margin: 0 auto 30px;"></div>

            <div class="pill" style="background: {COLORS['coral']}; color: white; margin-bottom: 40px;">
                Quick Pop Quiz
            </div>

            <p class="body text-muted" style="font-size: 28px; line-height: 1.6;">
                I want to show you something that might change<br>
                how you think about Etsy in 2026...
            </p>
        </div>
    </div>
</div>
'''

def slide_03_get_ready():
    """Get ready to type in the chat"""
    return f'''
<div class="slide bg-blush">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(150, 200, 280, 250, COLORS['coral_pale'], 0.5, -10)}
        {svg_blob(1700, 750, 250, 220, COLORS['muted'], 0.2, 15)}
    </svg>

    <div class="content flex-center">
        <div class="card text-center" style="max-width: 800px; position: relative;">
            <h1 class="display text-dark" style="font-size: 72px; margin-bottom: 40px;">
                Get ready to type<br>in the chat!
            </h1>

            <div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 30px;">
                <div style="width: 24px; height: 24px; background: {COLORS['teal']}; border-radius: 50%;"></div>
                <div style="width: 24px; height: 24px; background: {COLORS['teal']}; border-radius: 50%; opacity: 0.7;"></div>
                <div style="width: 24px; height: 24px; background: {COLORS['teal']}; border-radius: 50%; opacity: 0.4;"></div>
            </div>

            <!-- Speech bubble pointer -->
            <div style="position: absolute; bottom: -30px; left: 50%; transform: translateX(-50%);
                        width: 0; height: 0; border-left: 25px solid transparent;
                        border-right: 25px solid transparent; border-top: 30px solid white;"></div>
        </div>

        <p class="body text-muted" style="font-size: 24px; margin-top: 60px;">
            This is interactive &mdash; your answers matter
        </p>
    </div>
</div>
'''

def slide_04_quiz_ab():
    """Which design was made by professional artist?"""
    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 150, 350, 300, COLORS['mint'], 0.4, 20)}
        {svg_blob(80, 900, 280, 250, COLORS['blush_soft'], 0.5, -15)}
        {svg_blob(1650, 900, 280, 220, COLORS['gold_soft'], 0.35, 10)}
    </svg>

    <div class="content">
        <h1 class="display text-dark text-center" style="font-size: 56px; margin-bottom: 50px;">
            Which design was made by a professional artist?
        </h1>

        <div style="display: flex; gap: 60px; justify-content: center; align-items: center;">
            <!-- Option A -->
            <div class="card" style="width: 500px; height: 380px; padding: 20px;">
                <div style="width: 100%; height: 280px; background: linear-gradient(135deg, {COLORS['mint']}, {COLORS['cream']});
                            border-radius: 16px; display: flex; align-items: center; justify-content: center;">
                    <span class="text-light" style="font-size: 24px;">[ Image A ]</span>
                </div>
                <div style="text-align: center; margin-top: 20px;">
                    <div style="width: 60px; height: 60px; background: {COLORS['teal_deep']}; border-radius: 50%;
                                display: inline-flex; align-items: center; justify-content: center;">
                        <span class="display text-white" style="font-size: 28px;">A</span>
                    </div>
                </div>
            </div>

            <span class="body text-muted" style="font-size: 32px;">vs</span>

            <!-- Option B -->
            <div class="card" style="width: 500px; height: 380px; padding: 20px;">
                <div style="width: 100%; height: 280px; background: linear-gradient(135deg, {COLORS['coral_pale']}, {COLORS['cream']});
                            border-radius: 16px; display: flex; align-items: center; justify-content: center;">
                    <span class="text-light" style="font-size: 24px;">[ Image B ]</span>
                </div>
                <div style="text-align: center; margin-top: 20px;">
                    <div style="width: 60px; height: 60px; background: {COLORS['coral']}; border-radius: 50%;
                                display: inline-flex; align-items: center; justify-content: center;">
                        <span class="display text-white" style="font-size: 28px;">B</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
'''

def slide_05_type_ab():
    """Type A or B in the chat"""
    return f'''
<div class="slide bg-teal">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1550, 200, 400, 350, COLORS['teal_light'], 0.25, 15)}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-white" style="font-size: 90px; margin-bottom: 60px;">
            Type A or B<br>in the chat!
        </h1>

        <div style="display: flex; gap: 80px; align-items: center;">
            <div style="width: 180px; height: 160px; background: white; border-radius: 50%;
                        display: flex; align-items: center; justify-content: center;">
                <span class="display text-teal" style="font-size: 72px;">A</span>
            </div>

            <span class="body text-white" style="font-size: 36px; opacity: 0.8;">or</span>

            <div style="width: 180px; height: 160px; background: {COLORS['coral']}; border-radius: 50%;
                        display: flex; align-items: center; justify-content: center;">
                <span class="display text-white" style="font-size: 72px;">B</span>
            </div>
        </div>
    </div>
</div>
'''

def slide_06_answer_is():
    """The Answer Is..."""
    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1600, 200, 400, 350, COLORS['mint'], 0.45, 25)}
        {svg_blob(100, 800, 300, 280, COLORS['blush_soft'], 0.5, -15)}
        {svg_blob(1650, 850, 280, 220, COLORS['gold_soft'], 0.4, 10)}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-dark" style="font-size: 120px;">
            The Answer Is...
        </h1>

        <div style="display: flex; gap: 20px; margin-top: 60px;">
            <div style="width: 20px; height: 20px; background: {COLORS['teal']}; border-radius: 50%;"></div>
            <div style="width: 20px; height: 20px; background: {COLORS['teal']}; border-radius: 50%; opacity: 0.6;"></div>
            <div style="width: 20px; height: 20px; background: {COLORS['teal']}; border-radius: 50%; opacity: 0.3;"></div>
        </div>
    </div>
</div>
'''

def slide_07_both_ai():
    """Both Were Made by AI"""
    return f'''
<div class="slide bg-coral">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1500, 200, 400, 350, COLORS['coral_pale'], 0.3, 15)}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-white" style="font-size: 100px; margin-bottom: 50px;">
            Both Were Made by AI.
        </h1>

        <div class="card text-center" style="padding: 50px 80px;">
            <p class="body text-dark" style="font-size: 36px; line-height: 1.6;">
                In less than 30 seconds.<br>
                For free.
            </p>
        </div>
    </div>
</div>
'''

def slide_08_ai_nowadays():
    """Yes we all use AI nowadays"""
    return f'''
<div class="slide bg-blush">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 200, 320, 280, COLORS['muted'], 0.2, 20)}
        {svg_blob(100, 850, 280, 250, COLORS['coral_pale'], 0.4, -15)}
    </svg>

    <div class="content flex-center">
        <div class="card" style="max-width: 1000px; padding: 70px;">
            <p class="body text-muted" style="font-size: 28px; margin-bottom: 20px;">
                Yes, we all use AI nowadays...
            </p>

            <div style="width: 200px; height: 5px; background: {COLORS['teal']}; margin-bottom: 40px;"></div>

            <h2 class="display text-dark" style="font-size: 48px; line-height: 1.4; margin-bottom: 40px;">
                But in 2026, they've gotten so good that hiring someone REAL is starting to become just an option...
            </h2>

            <div class="pill" style="background: {COLORS['coral_pale']}; color: {COLORS['coral']};">
                Just an option
            </div>
        </div>
    </div>
</div>
'''

def slide_09_sink_in():
    """Let that sink in"""
    return f'''
<div class="slide" style="background: linear-gradient(135deg, {COLORS['cream']}, {COLORS['mint']});">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(150, 150, 350, 300, COLORS['gold_soft'], 0.4, -10)}
        {svg_blob(1600, 800, 350, 300, COLORS['mint'], 0.5, 20)}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-teal" style="font-size: 90px; text-align: center;">
            Let that sink in<br>for a second.
        </h1>
    </div>
</div>
'''

def slide_10_uncomfortable():
    """Now let me ask you something uncomfortable"""
    return f'''
<div class="slide bg-dark">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(960, 540, 500, 400, COLORS['coral'], 0.15, -10)}
    </svg>

    <div class="content flex-center">
        <p class="body text-white" style="font-size: 40px; margin-bottom: 30px; opacity: 0.9;">
            Now let me ask you
        </p>

        <h1 class="display text-coral" style="font-size: 100px; text-align: center;">
            something<br>uncomfortable...
        </h1>
    </div>
</div>
'''

# Continue with more slides...
def slide_11_what_happens():
    """What happens to YOUR Etsy shop in 2026?"""
    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1600, 200, 380, 330, COLORS['mint'], 0.45, 20)}
        {svg_blob(100, 750, 300, 280, COLORS['blush_soft'], 0.5, -15)}
        {svg_blob(1550, 750, 250, 200, COLORS['coral_pale'], 0.5, 10)}
        {svg_blob(1650, 850, 200, 160, COLORS['gold_soft'], 0.4, -5)}
    </svg>

    <div class="content">
        <p class="body text-muted text-center" style="font-size: 28px; margin-bottom: 40px; margin-top: 60px;">
            If anyone can create designs like this in seconds...
        </p>

        <h1 class="display text-dark text-center" style="font-size: 90px; line-height: 1.1;">
            What happens to<br>YOUR Etsy shop<br>in 2026?
        </h1>

        <div style="position: absolute; right: 200px; bottom: 200px;">
            <span class="display text-coral" style="font-size: 120px; opacity: 0.6;">?</span>
        </div>
    </div>
</div>
'''

def slide_12_survey_intro():
    """The numbers I'm about to show you"""
    return f'''
<div class="slide bg-blush">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 200, 350, 300, COLORS['muted'], 0.15, 20)}
        {svg_blob(100, 850, 300, 270, COLORS['coral_pale'], 0.4, -15)}
    </svg>

    <div class="content">
        <h1 class="display text-dark text-center" style="font-size: 72px; margin-top: 80px; margin-bottom: 60px;">
            The numbers I'm about<br>to show you aren't random...
        </h1>

        <div class="card-teal text-center" style="max-width: 800px; margin: 0 auto; padding: 50px;">
            <p class="body text-white" style="font-size: 28px; margin-bottom: 20px;">
                These are from YOUR OWN ANSWERS
            </p>
            <p class="body" style="font-size: 22px; opacity: 0.8; margin-bottom: 30px;">
                after I asked 160+ of you last week
            </p>
            <div class="pill" style="background: {COLORS['coral']}; color: white;">
                160+ Sellers Surveyed
            </div>
        </div>
    </div>
</div>
'''

# =============================================================================
# BUILD ALL SLIDES
# =============================================================================

def build_all_slides():
    """Generate all slides as HTML"""
    slides = [
        slide_01_title(),
        slide_02_before_begin(),
        slide_03_get_ready(),
        slide_04_quiz_ab(),
        slide_05_type_ab(),
        slide_06_answer_is(),
        slide_07_both_ai(),
        slide_08_ai_nowadays(),
        slide_09_sink_in(),
        slide_10_uncomfortable(),
        slide_11_what_happens(),
        slide_12_survey_intro(),
    ]

    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        {get_base_css()}
    </style>
</head>
<body>
    {"".join(slides)}
</body>
</html>
'''
    return html

def main():
    print("=" * 60)
    print("BAILEY VANN - THE 2026 ETSY RESET")
    print("HTML Slide Builder with WeasyPrint")
    print("=" * 60)

    # Generate HTML
    html_content = build_all_slides()

    # Save HTML for preview
    html_path = "/home/user/webby-slides-bailey/slides_preview.html"
    with open(html_path, 'w') as f:
        f.write(html_content)
    print(f"  HTML saved: {html_path}")

    # Convert to PDF
    print("  Converting to PDF...")
    font_config = FontConfiguration()

    pdf_path = "/home/user/webby-slides-bailey/Bailey_Etsy_Reset_HTML.pdf"
    HTML(string=html_content).write_pdf(
        pdf_path,
        font_config=font_config
    )

    print(f"  PDF saved: {pdf_path}")
    print("=" * 60)
    print("DONE!")

if __name__ == "__main__":
    main()
