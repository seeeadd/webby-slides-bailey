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

def svg_blob(cx, cy, rx, ry, color, opacity=0.3, rotation=0, seed=0, style='organic'):
    """
    Generate smooth organic blob using SVG path with cubic bezier curves.
    Creates truly organic, Pinterest-worthy shapes.

    Styles:
    - 'organic': Natural flowing shape (default)
    - 'amoeba': More irregular, amoeba-like
    - 'cloud': Puffy, cloud-like shape
    - 'wave': Flowing wave-like form
    """
    import math
    import random

    # Set random seed for reproducibility
    rng = random.Random(seed)

    # Different point counts and variation amounts for each style
    style_configs = {
        'organic': {'points': 6, 'var1': 0.22, 'var2': 0.15, 'smooth': 0.25},
        'amoeba': {'points': 8, 'var1': 0.35, 'var2': 0.20, 'smooth': 0.30},
        'cloud': {'points': 10, 'var1': 0.15, 'var2': 0.25, 'smooth': 0.20},
        'wave': {'points': 5, 'var1': 0.30, 'var2': 0.10, 'smooth': 0.35},
    }

    config = style_configs.get(style, style_configs['organic'])
    points = config['points']
    var1 = config['var1']
    var2 = config['var2']
    smooth = config['smooth']

    # Calculate vertices with organic variation
    vertices = []
    for i in range(points):
        angle = (2 * math.pi * i) / points

        # Multi-frequency organic variation
        variation = (
            var1 * math.sin(3 * angle + seed * 0.7) +
            var2 * math.cos(2 * angle + seed * 1.3) +
            0.08 * math.sin(5 * angle + seed * 2.1) +
            rng.uniform(-0.05, 0.05)  # Small random noise
        )

        r_x = rx * (0.85 + variation)
        r_y = ry * (0.85 + variation * 0.9)

        x = cx + r_x * math.cos(angle)
        y = cy + r_y * math.sin(angle)
        vertices.append((x, y))

    # Build smooth bezier path with catmull-rom style control points
    path_parts = [f"M {vertices[0][0]:.1f} {vertices[0][1]:.1f}"]

    for i in range(points):
        curr = vertices[i]
        next_v = vertices[(i + 1) % points]
        prev = vertices[(i - 1) % points]
        next_next = vertices[(i + 2) % points]

        # Catmull-Rom to Bezier control point conversion
        cp1_x = curr[0] + (next_v[0] - prev[0]) * smooth
        cp1_y = curr[1] + (next_v[1] - prev[1]) * smooth
        cp2_x = next_v[0] - (next_next[0] - curr[0]) * smooth
        cp2_y = next_v[1] - (next_next[1] - curr[1]) * smooth

        path_parts.append(f"C {cp1_x:.1f} {cp1_y:.1f}, {cp2_x:.1f} {cp2_y:.1f}, {next_v[0]:.1f} {next_v[1]:.1f}")

    path_parts.append("Z")

    transform = f'transform="rotate({rotation} {cx} {cy})"' if rotation != 0 else ''

    return f'<path d="{" ".join(path_parts)}" fill="{color}" fill-opacity="{opacity}" {transform} />'


def svg_blob_gradient(cx, cy, rx, ry, color1, color2, opacity=0.3, rotation=0, seed=0, gradient_id=None):
    """Create a blob with a gradient fill"""
    import math
    import random

    if gradient_id is None:
        gradient_id = f"grad_{seed}"

    rng = random.Random(seed)
    points = 7

    vertices = []
    for i in range(points):
        angle = (2 * math.pi * i) / points
        variation = 0.25 * math.sin(3 * angle + seed) + 0.15 * math.cos(2 * angle + seed * 0.8)
        r_x = rx * (0.85 + variation)
        r_y = ry * (0.85 + variation * 0.9)
        x = cx + r_x * math.cos(angle)
        y = cy + r_y * math.sin(angle)
        vertices.append((x, y))

    path_parts = [f"M {vertices[0][0]:.1f} {vertices[0][1]:.1f}"]
    for i in range(points):
        curr = vertices[i]
        next_v = vertices[(i + 1) % points]
        prev = vertices[(i - 1) % points]
        next_next = vertices[(i + 2) % points]

        cp1_x = curr[0] + (next_v[0] - prev[0]) * 0.25
        cp1_y = curr[1] + (next_v[1] - prev[1]) * 0.25
        cp2_x = next_v[0] - (next_next[0] - curr[0]) * 0.25
        cp2_y = next_v[1] - (next_next[1] - curr[1]) * 0.25

        path_parts.append(f"C {cp1_x:.1f} {cp1_y:.1f}, {cp2_x:.1f} {cp2_y:.1f}, {next_v[0]:.1f} {next_v[1]:.1f}")

    path_parts.append("Z")

    transform = f'transform="rotate({rotation} {cx} {cy})"' if rotation != 0 else ''

    gradient = f'''<defs>
        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color1};stop-opacity:{opacity}" />
            <stop offset="100%" style="stop-color:{color2};stop-opacity:{opacity * 0.6}" />
        </linearGradient>
    </defs>'''

    return f'{gradient}<path d="{" ".join(path_parts)}" fill="url(#{gradient_id})" {transform} />'


def svg_circle(cx, cy, r, color, opacity=1.0):
    """Simple circle for UI elements like buttons"""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" fill-opacity="{opacity}" />'

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
    padding: 100px 120px;
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
    height: 100%;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
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
        {svg_blob(1550, 180, 420, 380, COLORS['mint'], 0.45, 15, seed=1, style='cloud')}
        {svg_blob(80, 880, 320, 300, COLORS['blush_soft'], 0.55, -20, seed=2, style='amoeba')}
        {svg_blob(1720, 820, 280, 230, COLORS['gold_soft'], 0.35, 25, seed=3, style='organic')}
        {svg_blob(1480, 520, 220, 200, COLORS['coral_soft'], 0.6, 30, seed=4, style='wave')}
        {svg_blob(1600, 700, 180, 150, COLORS['gold_soft'], 0.5, -15, seed=5, style='organic')}
        {svg_blob(200, 150, 180, 160, COLORS['mint'], 0.25, 10, seed=6, style='cloud')}
    </svg>

    <div class="content" style="display: flex; flex-direction: column; justify-content: center; padding-left: 150px;">
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
        {svg_blob(1620, 160, 350, 300, COLORS['mint'], 0.4, 20, seed=7, style='cloud')}
        {svg_blob(80, 820, 300, 280, COLORS['coral_pale'], 0.45, -15, seed=8, style='amoeba')}
        {svg_blob(1750, 500, 200, 180, COLORS['gold_soft'], 0.25, 10, seed=9, style='organic')}
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
        {svg_blob(130, 180, 300, 270, COLORS['coral_pale'], 0.45, -15, seed=10, style='amoeba')}
        {svg_blob(1720, 720, 280, 250, COLORS['mint'], 0.3, 20, seed=11, style='cloud')}
        {svg_blob(1600, 150, 200, 180, COLORS['gold_soft'], 0.2, 10, seed=12, style='organic')}
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
        {svg_blob(1620, 130, 380, 320, COLORS['mint'], 0.35, 25, seed=13, style='cloud')}
        {svg_blob(60, 880, 300, 280, COLORS['blush_soft'], 0.4, -20, seed=14, style='amoeba')}
        {svg_blob(1680, 880, 300, 250, COLORS['gold_soft'], 0.3, 15, seed=15, style='wave')}
        {svg_blob(150, 200, 180, 160, COLORS['coral_pale'], 0.2, 5, seed=16, style='organic')}
    </svg>

    <div class="content flex-center">
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
        {svg_blob(1520, 180, 420, 380, COLORS['teal_light'], 0.2, 20, seed=17, style='cloud')}
        {svg_blob(100, 800, 320, 280, COLORS['teal_light'], 0.15, -15, seed=18, style='amoeba')}
        {svg_blob(1650, 750, 250, 220, COLORS['mint'], 0.18, 10, seed=19, style='wave')}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-white" style="font-size: 90px; margin-bottom: 60px;">
            Type A or B<br>in the chat!
        </h1>

        <div style="display: flex; gap: 80px; align-items: center;">
            <div style="width: 180px; min-width: 180px; height: 180px; min-height: 180px;
                        background: white; border-radius: 50%; flex-shrink: 0;
                        display: flex; align-items: center; justify-content: center;">
                <span class="display text-teal" style="font-size: 72px;">A</span>
            </div>

            <span class="body text-white" style="font-size: 36px; opacity: 0.8;">or</span>

            <div style="width: 180px; min-width: 180px; height: 180px; min-height: 180px;
                        background: {COLORS['coral']}; border-radius: 50%; flex-shrink: 0;
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
        {svg_blob(1570, 180, 420, 370, COLORS['mint'], 0.4, 30, seed=20, style='cloud')}
        {svg_blob(80, 780, 320, 300, COLORS['blush_soft'], 0.45, -20, seed=21, style='amoeba')}
        {svg_blob(1680, 830, 300, 250, COLORS['gold_soft'], 0.35, 15, seed=22, style='wave')}
        {svg_blob(200, 200, 180, 160, COLORS['coral_pale'], 0.25, 5, seed=23, style='organic')}
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
        {svg_blob(1480, 180, 420, 380, COLORS['coral_pale'], 0.25, 20, seed=24, style='cloud')}
        {svg_blob(120, 820, 300, 280, COLORS['coral_pale'], 0.2, -15, seed=25, style='amoeba')}
        {svg_blob(1700, 700, 220, 200, COLORS['white'], 0.1, 10, seed=26, style='wave')}
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
        {svg_blob(1620, 180, 350, 300, COLORS['mint'], 0.3, 25, seed=27, style='cloud')}
        {svg_blob(80, 830, 300, 280, COLORS['coral_pale'], 0.35, -20, seed=28, style='amoeba')}
        {svg_blob(1750, 650, 200, 180, COLORS['gold_soft'], 0.2, 10, seed=29, style='organic')}
        {svg_blob(180, 180, 200, 180, COLORS['blush_soft'], 0.25, -5, seed=30, style='wave')}
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
        {svg_blob(130, 130, 380, 330, COLORS['gold_soft'], 0.35, -15, seed=31, style='cloud')}
        {svg_blob(1580, 780, 380, 320, COLORS['teal_light'], 0.4, 25, seed=32, style='amoeba')}
        {svg_blob(1700, 200, 220, 200, COLORS['coral_pale'], 0.25, 10, seed=33, style='wave')}
        {svg_blob(100, 650, 200, 180, COLORS['blush_soft'], 0.3, -5, seed=34, style='organic')}
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
        {svg_blob(960, 540, 520, 420, COLORS['coral'], 0.12, -15, seed=35, style='amoeba')}
        {svg_blob(1700, 200, 280, 250, COLORS['teal_deep'], 0.1, 20, seed=36, style='cloud')}
        {svg_blob(150, 850, 250, 220, COLORS['coral'], 0.08, -10, seed=37, style='wave')}
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
        {svg_blob(1580, 180, 400, 350, COLORS['mint'], 0.4, 25, seed=38, style='cloud')}
        {svg_blob(80, 730, 320, 300, COLORS['blush_soft'], 0.45, -20, seed=39, style='amoeba')}
        {svg_blob(1530, 730, 280, 230, COLORS['coral_pale'], 0.4, 15, seed=40, style='wave')}
        {svg_blob(1670, 870, 220, 180, COLORS['gold_soft'], 0.35, -10, seed=41, style='organic')}
        {svg_blob(180, 180, 180, 160, COLORS['mint'], 0.2, 5, seed=42, style='cloud')}
    </svg>

    <div class="content flex-center">
        <p class="body text-muted text-center" style="font-size: 28px; margin-bottom: 40px;">
            If anyone can create designs like this in seconds...
        </p>

        <h1 class="display text-dark text-center" style="font-size: 90px; line-height: 1.1;">
            What happens to<br>YOUR Etsy shop<br>in 2026?
        </h1>

        <div style="margin-top: 40px;">
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
        {svg_blob(1620, 180, 380, 320, COLORS['mint'], 0.3, 25, seed=43, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['coral_pale'], 0.35, -20, seed=44, style='amoeba')}
        {svg_blob(1750, 600, 220, 200, COLORS['gold_soft'], 0.2, 10, seed=45, style='wave')}
        {svg_blob(180, 200, 200, 180, COLORS['blush_soft'], 0.25, -5, seed=46, style='organic')}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-dark text-center" style="font-size: 72px; margin-bottom: 60px;">
            The numbers I'm about<br>to show you aren't random...
        </h1>

        <div class="card-teal text-center" style="max-width: 800px; padding: 50px;">
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
