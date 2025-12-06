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
        ('Satoshi', 'Satoshi-Variable.ttf'),
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
    font-family: 'Satoshi', 'Ogg Text', sans-serif;
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
    font-family: 'Satoshi', sans-serif;
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
.bg-dark-stat {{ background: linear-gradient(145deg, #2D2D38 0%, #232330 100%); }}
.bg-dark-deep {{ background: linear-gradient(145deg, #1E1E26 0%, #141418 100%); }}
.bg-dark-moody {{ background: linear-gradient(145deg, #2A2A35 0%, #1E1E26 100%); }}

/* Stat slide styles */
.stat-num {{ line-height: 0.85; }}
.stat-num-huge {{ font-size: 360px; }}
.stat-num-large {{ font-size: 200px; margin-bottom: 30px; }}
.stat-text {{ font-size: 42px; color: rgba(255,255,255,0.9); line-height: 1.4; }}
.stat-layout {{ display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 100px; height: 100%; }}
.stat-left {{ text-align: left; max-width: 700px; }}

/* Color utilities */
.c-red {{ color: #C45050; }}
.c-gray {{ color: #6B7280; }}
.c-purple {{ color: #8B7EC8; }}
.c-white {{ color: white; }}
.c-white-60 {{ color: rgba(255,255,255,0.6); }}

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

def svg_shop_mockup_messy():
    """Create SVG for the messy/cluttered Etsy shop - FEELS chaotic and stressful"""
    # Desaturated, slightly sad colors with warning tint
    sad_bg = '#D8D8D8'
    sad_header = '#C4C4C4'

    # Chaotic tilted listing boxes with some dead/faded ones
    listings = []

    # Grid of messy, tilted, overlapping boxes
    box_configs = [
        # (x, y, w, h, color, opacity, rotation, is_dead)
        (12, 58, 46, 42, '#B0B8B8', 0.7, -2, False),
        (62, 55, 44, 40, '#A8B0B0', 0.6, 3, True),   # dead listing
        (110, 60, 48, 44, '#BCC4C4', 0.75, -1, False),
        (162, 56, 42, 38, '#9CA4A4', 0.5, 2, True),  # dead listing
        (14, 104, 44, 40, '#C0C8C8', 0.65, 1, False),
        (60, 100, 46, 42, '#A4ACAC', 0.55, -3, True), # dead listing
        (108, 106, 50, 44, '#B8C0C0', 0.7, 2, False),
        (160, 102, 44, 40, '#B0B8B8', 0.6, -2, False),
        (10, 148, 48, 42, '#9CA4A4', 0.5, 3, True),  # dead listing
        (62, 152, 42, 38, '#C4CCCC', 0.7, -1, False),
        (106, 150, 46, 44, '#ACB4B4', 0.55, 2, True), # dead listing
        (158, 146, 48, 42, '#B4BCBC', 0.65, -2, False),
        (14, 194, 44, 40, '#A0A8A8', 0.6, 1, False),
        (60, 196, 46, 42, '#BCC4C4', 0.7, -3, False),
        (110, 192, 42, 38, '#98A0A0', 0.45, 2, True), # dead listing
        (160, 198, 44, 40, '#B8C0C0', 0.65, -1, False),
        (12, 240, 48, 42, '#C0C8C8', 0.7, 2, False),
        (64, 238, 44, 40, '#A4ACAC', 0.5, -2, True),  # dead listing
        (112, 244, 46, 42, '#B0B8B8', 0.6, 1, False),
        (162, 240, 42, 38, '#ACB4B4', 0.55, -1, False),
    ]

    for x, y, w, h, color, opacity, rot, is_dead in box_configs:
        transform = f'transform="rotate({rot} {x + w/2} {y + h/2})"'
        listings.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{color}" opacity="{opacity}" {transform}/>')
        # Add red X for dead listings
        if is_dead:
            cx, cy = x + w/2, y + h/2
            listings.append(f'<line x1="{cx-8}" y1="{cy-8}" x2="{cx+8}" y2="{cy+8}" stroke="#C45C5C" stroke-width="2.5" opacity="0.7" {transform}/>')
            listings.append(f'<line x1="{cx+8}" y1="{cy-8}" x2="{cx-8}" y2="{cy+8}" stroke="#C45C5C" stroke-width="2.5" opacity="0.7" {transform}/>')

    return f'''
    <g transform="translate(0, 0)">
        <!-- Sad shadow underneath -->
        <ellipse cx="115" cy="320" rx="100" ry="12" fill="#00000" opacity="0.08"/>

        <!-- Shop container - slightly worn look -->
        <rect x="0" y="0" width="230" height="310" rx="10" fill="#F8F6F4"
              style="filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));"/>

        <!-- Dull header bar -->
        <rect x="0" y="0" width="230" height="48" rx="10" fill="{sad_header}"/>
        <rect x="0" y="18" width="230" height="30" fill="{sad_header}"/>

        <!-- Sad shop name -->
        <rect x="12" y="14" width="90" height="10" rx="2" fill="#9CA3A8"/>
        <rect x="12" y="28" width="55" height="7" rx="2" fill="#B0B8B8"/>

        <!-- Wilting plant icon -->
        <g transform="translate(195, 12)">
            <ellipse cx="12" cy="22" rx="10" ry="6" fill="#A8B0B0"/>
            <path d="M12 20 Q8 12 12 5 Q10 10 8 8" stroke="#8A9494" stroke-width="2" fill="none" stroke-linecap="round"/>
            <circle cx="8" cy="6" r="3" fill="#9CA4A4" opacity="0.7"/>
        </g>

        <!-- Messy cluttered thumbnails -->
        {chr(10).join(listings)}

        <!-- Revenue indicator - PAINFUL treatment -->
        <rect x="8" y="285" width="214" height="24" rx="5" fill="#FCE8E8"/>
        <rect x="10" y="287" width="210" height="20" rx="4" fill="#F8DEDE"/>

        <!-- Down arrow - prominent -->
        <g transform="translate(22, 290)">
            <path d="M6 2 L6 12 M2 8 L6 12 L10 8" stroke="#C45050" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        </g>

        <!-- $127 in painful coral/red - BIGGER text -->
        <text x="45" y="302" font-family="Satoshi, sans-serif" font-size="22" fill="#C45050" font-weight="700">$127</text>
        <text x="105" y="302" font-family="Satoshi, sans-serif" font-size="16" fill="#C45050" font-weight="500">this month</text>
    </g>
    '''


def svg_shop_mockup_focused():
    """Create SVG for the focused/successful Etsy shop - FEELS like winning"""
    teal = COLORS['teal_deep']
    coral = COLORS['coral']
    mint = COLORS['mint']
    gold = '#E8C547'

    # Clean, confident listing boxes with depth
    listings = []
    listing_configs = [
        (14, 60, 98, 78, teal, 0.9),
        (118, 60, 98, 78, coral, 0.85),
        (14, 146, 98, 78, mint, 0.95),
        (118, 146, 98, 78, teal, 0.85),
        (14, 232, 98, 78, coral, 0.9),
        (118, 232, 98, 78, mint, 0.9),
    ]

    for x, y, w, h, color, opacity in listing_configs:
        # Soft shadow for each listing
        listings.append(f'<rect x="{x+2}" y="{y+3}" width="{w}" height="{h}" rx="8" fill="#000" opacity="0.06"/>')
        listings.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{color}" opacity="{opacity}"/>')
        # Subtle shine/highlight
        listings.append(f'<rect x="{x+4}" y="{y+4}" width="{w-8}" height="3" rx="1" fill="white" opacity="0.25"/>')

    return f'''
    <g transform="translate(0, 0)">
        <!-- Success glow underneath -->
        <ellipse cx="115" cy="365" rx="120" ry="18" fill="{teal}" opacity="0.12"/>

        <!-- Outer glow ring -->
        <rect x="-6" y="-6" width="242" height="372" rx="18" fill="{teal}" opacity="0.08"/>
        <rect x="-3" y="-3" width="236" height="366" rx="15" fill="{gold}" opacity="0.06"/>

        <!-- Shop container - premium feel -->
        <rect x="0" y="0" width="230" height="360" rx="12" fill="white"
              style="filter: drop-shadow(0 12px 40px rgba(27,138,138,0.2));"/>

        <!-- Branded header bar -->
        <rect x="0" y="0" width="230" height="52" rx="12" fill="{teal}"/>
        <rect x="0" y="20" width="230" height="32" fill="{teal}"/>

        <!-- Shop name - confident branding - BIGGER -->
        <text x="14" y="32" font-family="Ogg Bold, serif" font-size="19" fill="white" font-weight="bold">Focused Shop</text>
        <rect x="14" y="40" width="85" height="5" rx="2" fill="white" opacity="0.5"/>

        <!-- Thriving plant icon -->
        <g transform="translate(185, 10)">
            <ellipse cx="18" cy="30" rx="14" ry="8" fill="{mint}"/>
            <path d="M18 28 Q22 18 18 6 Q24 14 28 10" stroke="{teal}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <circle cx="28" cy="8" r="5" fill="{coral}" opacity="0.9"/>
            <path d="M14 24 Q10 16 14 8" stroke="{teal}" stroke-width="2" fill="none" stroke-linecap="round"/>
            <circle cx="14" cy="6" r="4" fill="{mint}"/>
        </g>

        <!-- Clean, glowing thumbnails -->
        {chr(10).join(listings)}

        <!-- Revenue indicator - WINNING treatment with glow -->
        <rect x="6" y="318" width="218" height="36" rx="10" fill="{teal}" opacity="0.15"/>
        <rect x="8" y="320" width="214" height="32" rx="8" fill="{mint}"/>
        <rect x="10" y="322" width="210" height="28" rx="6" fill="white" opacity="0.5"/>

        <!-- Sparkle near revenue - bigger -->
        <g transform="translate(24, 328)">
            <path d="M7 0 L7 14 M0 7 L14 7" stroke="{gold}" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M2 2 L12 12 M12 2 L2 12" stroke="{gold}" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
        </g>

        <!-- $3,847 - BOLD and prominent - BIGGER text with gap -->
        <text x="42" y="343" font-family="Satoshi, sans-serif" font-size="26" fill="{teal}" font-weight="800">$3,847</text>
        <text x="140" y="343" font-family="Satoshi, sans-serif" font-size="17" fill="{teal}" font-weight="600">this month</text>

        <!-- Up arrow indicator - bigger -->
        <g transform="translate(186, 328)">
            <path d="M9 16 L9 4 M4 9 L9 4 L14 9" stroke="{teal}" stroke-width="3" fill="none" stroke-linecap="round"/>
        </g>

        <!-- Tiny hearts scattered -->
        <path d="M200 75 C200 72 203 70 205 72 C207 70 210 72 210 75 C210 78 205 82 205 82 C205 82 200 78 200 75Z" fill="{coral}" opacity="0.6"/>
        <path d="M22 180 C22 178 24 176.5 25.5 178 C27 176.5 29 178 29 180 C29 182 25.5 185 25.5 185 C25.5 185 22 182 22 180Z" fill="{coral}" opacity="0.5"/>
    </g>
    '''


def svg_sparkle(x, y, size=12, color='#E8C547'):
    """Create a sparkle/star decoration"""
    s = size
    return f'''
    <g transform="translate({x}, {y})">
        <path d="M{s/2} 0 L{s/2} {s} M0 {s/2} L{s} {s/2}" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
        <path d="M{s*0.15} {s*0.15} L{s*0.85} {s*0.85} M{s*0.85} {s*0.15} L{s*0.15} {s*0.85}" stroke="{color}" stroke-width="1.5" stroke-linecap="round" opacity="0.7"/>
    </g>
    '''


def slide_01_title():
    """Title slide - THE 2026 ETSY RESET - MASSIVE typography + transformation visual"""
    gold = '#E8C547'
    success_green = '#2D9B6E'

    return f'''
<div class="slide bg-cream">
    <!-- Subtle background texture/warmth - balanced sparkles -->
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        <!-- Warm organic shapes in background -->
        {svg_blob(1780, 120, 260, 220, COLORS['mint'], 0.18, 15, seed=100, style='cloud')}
        {svg_blob(30, 850, 220, 200, COLORS['blush_soft'], 0.22, -10, seed=101, style='amoeba')}
        {svg_blob(1820, 920, 180, 160, COLORS['coral_pale'], 0.12, 20, seed=102, style='organic')}

        <!-- Balanced floating sparkles - top left, mid right, bottom left -->
        {svg_sparkle(80, 140, 14, gold)}
        {svg_sparkle(1680, 320, 12, COLORS['teal_light'])}
        {svg_sparkle(160, 780, 10, COLORS['coral_soft'])}
        {svg_sparkle(1750, 700, 14, gold)}
    </svg>

    <div class="content" style="display: flex; flex-direction: row; align-items: center; padding: 100px 180px 80px 100px; gap: 80px;">

        <!-- LEFT: Text content - BIGGER -->
        <div style="flex: 0.9; max-width: 700px;">
            <div class="pill" style="background: {COLORS['teal_deep']}; color: white; margin-bottom: 16px; padding: 12px 26px; font-size: 18px;">
                Day 1 of 3
            </div>

            <p class="body text-teal" style="font-size: 26px; margin-bottom: 8px; letter-spacing: 0.5px;">
                The 2026 Etsy Upgrade Challenge
            </p>

            <!-- MASSIVE RESET with hand-drawn underline -->
            <div style="position: relative; margin-bottom: 18px;">
                <h1 class="display text-dark" style="font-size: 190px; line-height: 0.85; letter-spacing: -4px;">
                    RESET
                </h1>
                <!-- Hand-drawn style underline -->
                <svg style="position: absolute; bottom: 8px; left: 5px;" width="400" height="18" viewBox="0 0 400 18">
                    <path d="M5 10 Q70 5 140 12 Q210 4 280 11 Q350 7 395 7" stroke="{COLORS['coral']}" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.75"/>
                </svg>
            </div>

            <!-- Subtitle - SHORT, fits on one line -->
            <p class="body" style="font-size: 22px; margin-bottom: 26px; color: {COLORS['dark']}; font-weight: 500; white-space: nowrap;">
                Delete the Dead Weight <span style="color: {COLORS['coral']}; font-size: 10px;">&#9679;</span> Find Your Focus <span style="color: {COLORS['coral']}; font-size: 10px;">&#9679;</span> Build a Shop That Works
            </p>

            <!-- Credentials badge - clean single line -->
            <div style="background: {COLORS['teal_deep']}; color: white; padding: 16px 32px; border-radius: 14px; display: inline-block;">
                <span class="body" style="font-size: 18px; opacity: 0.85;">with </span><span class="display" style="font-size: 24px; font-weight: bold;">Bailey Vann</span><span class="body" style="font-size: 17px; opacity: 0.7;"> &nbsp;&#8226;&nbsp; Top 0.1% Etsy Seller</span>
            </div>
        </div>

        <!-- RIGHT: Shop Transformation Visual - CENTERED, away from edges -->
        <div style="flex: 1.2; display: flex; align-items: center; justify-content: center; position: relative;">

            <svg width="680" height="580" viewBox="0 0 560 480">
                <!-- BEFORE label -->
                <text x="90" y="42" text-anchor="start" font-family="Satoshi, sans-serif"
                      font-size="11" fill="{COLORS['dark']}" font-weight="700"
                      letter-spacing="2" opacity="0.7">BEFORE</text>

                <!-- Messy Shop (Before) -->
                <g transform="translate(20, 60)">
                    {svg_shop_mockup_messy()}
                </g>

                <!-- AFTER label -->
                <text x="445" y="32" text-anchor="middle" font-family="Satoshi, sans-serif"
                      font-size="11" fill="{COLORS['teal_deep']}" font-weight="700"
                      letter-spacing="2">AFTER</text>

                <!-- Focused Shop (After) - overlapping, in front, glowing -->
                <g transform="translate(320, 45)">
                    {svg_shop_mockup_focused()}
                </g>

                <!-- BIG RESET Arrow Bridge - prominent and dynamic -->
                <g transform="translate(205, 165)">
                    <!-- Glow behind arrow -->
                    <ellipse cx="55" cy="50" rx="65" ry="45" fill="{COLORS['coral']}" opacity="0.12"/>

                    <!-- Dynamic curved arrow -->
                    <path d="M 0 50 Q 40 25 85 50 Q 105 58 120 50" stroke="{COLORS['coral']}" stroke-width="5"
                          fill="none" stroke-linecap="round"/>
                    <polygon points="118,40 138,50 118,60" fill="{COLORS['coral']}"/>

                    <!-- RESET button - bigger and glowing -->
                    <rect x="15" y="70" width="95" height="42" rx="10" fill="{COLORS['coral']}"
                          style="filter: drop-shadow(0 5px 14px rgba(224,123,108,0.45));"/>
                    <text x="62" y="98" text-anchor="middle" font-family="Ogg Bold, serif"
                          font-size="18" fill="white" font-weight="bold">RESET</text>

                    <!-- Sparkle on button -->
                    <circle cx="100" cy="78" r="4" fill="white" opacity="0.6"/>
                </g>

                <!-- Sparkles around success -->
                {svg_sparkle(495, 50, 14, gold)}
                {svg_sparkle(540, 210, 11, COLORS['teal_light'])}
                {svg_sparkle(335, 430, 12, COLORS['coral_soft'])}
            </svg>

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
    """What happens to YOUR Etsy shop in 2026? - DARK/MOODY tension builder"""
    # Dark palette for uncomfortable feeling
    dark_bg = '#2A2A35'
    dark_accent = '#3D3D4A'
    muted_coral = '#C4736A'

    return f'''
<div class="slide" style="background: linear-gradient(145deg, {dark_bg} 0%, #1E1E26 100%);">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        <!-- Dark, moody organic shapes -->
        {svg_blob(1600, 200, 400, 350, dark_accent, 0.3, 25, seed=38, style='amoeba')}
        {svg_blob(100, 750, 350, 300, muted_coral, 0.08, -20, seed=39, style='cloud')}
        {svg_blob(1700, 800, 280, 230, dark_accent, 0.25, 15, seed=40, style='wave')}
        {svg_blob(200, 150, 200, 180, muted_coral, 0.06, 5, seed=42, style='organic')}
    </svg>

    <div class="content flex-center">
        <p class="body text-center" style="font-size: 30px; margin-bottom: 50px; color: rgba(255,255,255,0.6); letter-spacing: 0.5px;">
            If anyone can create designs like this in seconds...
        </p>

        <h1 class="display text-center" style="font-size: 100px; line-height: 1.1; color: white;">
            What happens to<br>
            <span style="color: {COLORS['coral']};">YOUR</span> Etsy shop<br>
            in 2026?
        </h1>
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
# STAT SLIDE HELPERS - Reduce repetition
# =============================================================================

STAT_COLORS = {
    'red': {'main': '#C45050', 'light': '#D4736A', 'shadow': 'rgba(196,80,80,0.3)'},
    'gray': {'main': '#6B7280', 'light': '#9CA3AF', 'shadow': 'rgba(107,114,128,0.3)'},
    'purple': {'main': '#8B7EC8', 'light': '#A89BD4', 'shadow': 'rgba(139,126,200,0.3)'},
}

def stat_slide_number(num, color_key, seed_base):
    """Generate a number-only stat reveal slide"""
    c = STAT_COLORS[color_key]
    return f'''
<div class="slide bg-dark-stat">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 200, 350, 300, c['main'], 0.08, 20, seed=seed_base, style='amoeba')}
        {svg_blob(150, 800, 300, 280, c['main'], 0.06, -15, seed=seed_base+1, style='cloud')}
    </svg>
    <div class="content flex-center">
        <h1 class="display stat-num stat-num-huge" style="color: {c['main']}; text-shadow: 0 20px 60px {c['shadow']};">{num}</h1>
    </div>
</div>
'''

def stat_slide_full(num, color_key, seed_base, text_html, visual_svg):
    """Generate a full stat slide with visualization"""
    c = STAT_COLORS[color_key]
    return f'''
<div class="slide bg-dark-stat">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1650, 200, 350, 300, c['main'], 0.08, 20, seed=seed_base, style='amoeba')}
        {svg_blob(150, 850, 300, 280, c['main'], 0.06, -15, seed=seed_base+1, style='cloud')}
    </svg>
    <div class="content stat-layout">
        <div class="stat-left">
            <h1 class="display stat-num stat-num-large" style="color: {c['main']}; text-shadow: 0 15px 40px {c['shadow'].replace('0.3','0.25')};">{num}</h1>
            <p class="body stat-text">{text_html}</p>
        </div>
        <div>{visual_svg}</div>
    </div>
</div>
'''

def svg_declining_bars():
    """SVG for declining bar chart visualization"""
    return '''<svg width="400" height="350" viewBox="0 0 400 350">
        <rect x="40" y="50" width="60" height="250" rx="8" fill="#3A3A48" opacity="0.5"/>
        <rect x="40" y="80" width="60" height="220" rx="8" fill="#D4736A" opacity="0.7"/>
        <rect x="120" y="50" width="60" height="250" rx="8" fill="#3A3A48" opacity="0.5"/>
        <rect x="120" y="120" width="60" height="180" rx="8" fill="#C45050" opacity="0.8"/>
        <rect x="200" y="50" width="60" height="250" rx="8" fill="#3A3A48" opacity="0.5"/>
        <rect x="200" y="170" width="60" height="130" rx="8" fill="#C45050" opacity="0.9"/>
        <rect x="280" y="50" width="60" height="250" rx="8" fill="#3A3A48" opacity="0.5"/>
        <rect x="280" y="220" width="60" height="80" rx="8" fill="#C45050"/>
        <path d="M 60 40 L 320 280" stroke="#C45050" stroke-width="4" stroke-dasharray="12,6" opacity="0.6"/>
        <polygon points="310,260 340,290 300,290" fill="#C45050" opacity="0.8"/>
        <text x="200" y="335" text-anchor="middle" font-family="Satoshi, sans-serif" font-size="16" fill="rgba(255,255,255,0.5)">SHOP REVENUE TREND</text>
    </svg>'''

def svg_zero_visibility():
    """SVG for zero/empty visualization"""
    return '''<svg width="350" height="350" viewBox="0 0 350 350">
        <circle cx="175" cy="175" r="140" fill="none" stroke="#3A3A48" stroke-width="30" opacity="0.4"/>
        <circle cx="175" cy="175" r="140" fill="none" stroke="#6B7280" stroke-width="8" stroke-dasharray="20,10" opacity="0.6"/>
        <text x="175" y="200" text-anchor="middle" font-family="Ogg Bold, serif" font-size="120" fill="#6B7280" opacity="0.8">0</text>
        <g transform="translate(60, 60)" opacity="0.4"><circle cx="15" cy="15" r="12" fill="#6B7280"/><line x1="5" y1="5" x2="25" y2="25" stroke="#232330" stroke-width="3"/></g>
        <g transform="translate(270, 80)" opacity="0.3"><circle cx="15" cy="15" r="10" fill="#6B7280"/><line x1="7" y1="7" x2="23" y2="23" stroke="#232330" stroke-width="2"/></g>
        <g transform="translate(50, 250)" opacity="0.35"><circle cx="12" cy="12" r="10" fill="#6B7280"/><line x1="4" y1="4" x2="20" y2="20" stroke="#232330" stroke-width="2"/></g>
        <g transform="translate(280, 240)" opacity="0.25"><circle cx="12" cy="12" r="8" fill="#6B7280"/><line x1="5" y1="5" x2="19" y2="19" stroke="#232330" stroke-width="2"/></g>
        <text x="175" y="340" text-anchor="middle" font-family="Satoshi, sans-serif" font-size="14" fill="rgba(255,255,255,0.4)">VISIBILITY</text>
    </svg>'''

def svg_confusion():
    """SVG for confusion/paralysis visualization"""
    return '''<svg width="350" height="350" viewBox="0 0 350 350">
        <text x="80" y="80" font-family="Ogg Bold, serif" font-size="48" fill="#8B7EC8" opacity="0.7" transform="rotate(-15 80 80)">?</text>
        <text x="250" y="100" font-family="Ogg Bold, serif" font-size="36" fill="#A89BD4" opacity="0.5" transform="rotate(20 250 100)">?</text>
        <text x="175" y="180" font-family="Ogg Bold, serif" font-size="72" fill="#8B7EC8" opacity="0.9">?</text>
        <text x="120" y="280" font-family="Ogg Bold, serif" font-size="42" fill="#A89BD4" opacity="0.6" transform="rotate(-10 120 280)">?</text>
        <text x="270" y="260" font-family="Ogg Bold, serif" font-size="54" fill="#8B7EC8" opacity="0.65" transform="rotate(25 270 260)">?</text>
        <text x="60" y="200" font-family="Ogg Bold, serif" font-size="32" fill="#A89BD4" opacity="0.4" transform="rotate(-25 60 200)">?</text>
        <text x="300" y="180" font-family="Ogg Bold, serif" font-size="28" fill="#8B7EC8" opacity="0.35" transform="rotate(15 300 180)">?</text>
        <rect x="50" y="130" width="30" height="30" rx="4" fill="#3A3A48" opacity="0.4" transform="rotate(15 65 145)"/>
        <rect x="280" y="200" width="25" height="25" rx="4" fill="#3A3A48" opacity="0.35" transform="rotate(-20 292 212)"/>
        <rect x="140" y="300" width="35" height="35" rx="4" fill="#3A3A48" opacity="0.3" transform="rotate(30 157 317)"/>
        <text x="175" y="345" text-anchor="middle" font-family="Satoshi, sans-serif" font-size="14" fill="rgba(255,255,255,0.4)">PARALYSIS</text>
    </svg>'''

def slide_13a_stat_75_number():
    return stat_slide_number('75+', 'red', 50)

def slide_13b_stat_75_full():
    return stat_slide_full('75+', 'red', 50,
        'of sellers report their shops <span style="color: #C45050; font-weight: bold;">tanked</span> in the last 2 months...',
        svg_declining_bars())

def slide_14a_stat_58_number():
    return stat_slide_number('58+', 'gray', 52)

def slide_14b_stat_58_full():
    return stat_slide_full('58+', 'gray', 52,
        'sellers said their #1 problem:<br><span style="color: #9CA3AF; font-weight: bold;">"No views anymore"</span>',
        svg_zero_visibility())

def slide_15a_stat_47_number():
    return stat_slide_number('47+', 'purple', 54)

def slide_15b_stat_47_full():
    return stat_slide_full('47+', 'purple', 54,
        'said they have<br><span style="color: #A89BD4; font-weight: bold;">"No idea what to design"</span>',
        svg_confusion())


def slide_16_engagement():
    """Does anyone else feel that way? - Engagement moment with custom chat bubble"""
    return f'''
<div class="slide bg-blush">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1620, 180, 380, 320, COLORS['mint'], 0.35, 25, seed=56, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['coral_pale'], 0.4, -20, seed=57, style='amoeba')}
        {svg_blob(1750, 650, 220, 200, COLORS['teal_light'], 0.2, 10, seed=58, style='wave')}
        {svg_blob(180, 200, 200, 180, COLORS['gold_soft'], 0.25, -5, seed=59, style='organic')}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-dark text-center" style="font-size: 72px; margin-bottom: 50px; line-height: 1.2;">
            Does anyone else<br>feel that way?
        </h1>

        <!-- Custom chat bubble graphic -->
        <div style="position: relative; margin-bottom: 40px;">
            <svg width="500" height="160" viewBox="0 0 500 160">
                <!-- Chat bubble shape -->
                <rect x="0" y="0" width="500" height="120" rx="24" fill="{COLORS['teal_deep']}"/>
                <!-- Bubble tail -->
                <polygon points="100,120 130,120 115,150" fill="{COLORS['teal_deep']}"/>

                <!-- Text inside bubble -->
                <text x="250" y="50" text-anchor="middle" font-family="Satoshi, sans-serif" font-size="26" fill="white" font-weight="500">Type</text>
                <text x="250" y="100" text-anchor="middle" font-family="Ogg Bold, serif" font-size="48" fill="{COLORS['gold']}" font-weight="bold">YES</text>

                <!-- Typing indicator dots -->
                <circle cx="430" cy="60" r="6" fill="white" opacity="0.9"/>
                <circle cx="450" cy="60" r="6" fill="white" opacity="0.6"/>
                <circle cx="470" cy="60" r="6" fill="white" opacity="0.3"/>
            </svg>
        </div>

        <p class="body text-muted text-center" style="font-size: 28px;">
            if you're seeing the same problems
        </p>
    </div>
</div>
'''


def slide_17_reframe_setup():
    """The reframe setup - strikethrough old thinking"""
    wrong_red = '#C45050'

    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1620, 180, 380, 320, COLORS['mint'], 0.35, 25, seed=60, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['blush_soft'], 0.4, -20, seed=61, style='amoeba')}
        {svg_blob(1750, 700, 220, 200, COLORS['coral_pale'], 0.25, 10, seed=62, style='wave')}
    </svg>

    <div class="content flex-center">
        <p class="body text-muted text-center" style="font-size: 32px; margin-bottom: 40px;">
            So the real question isn't:
        </p>

        <!-- Strikethrough treatment -->
        <div style="position: relative; display: inline-block;">
            <h1 class="display text-dark text-center" style="font-size: 64px; opacity: 0.5;">
                "how do I make more listings?"
            </h1>

            <!-- SVG X / Strikethrough overlay -->
            <svg style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);" width="900" height="120" viewBox="0 0 900 120">
                <!-- Big diagonal X lines -->
                <line x1="20" y1="20" x2="880" y2="100" stroke="{wrong_red}" stroke-width="8" stroke-linecap="round" opacity="0.85"/>
                <line x1="20" y1="100" x2="880" y2="20" stroke="{wrong_red}" stroke-width="8" stroke-linecap="round" opacity="0.85"/>
            </svg>
        </div>

        <!-- Visual X marks on sides -->
        <div style="display: flex; gap: 60px; margin-top: 50px; align-items: center;">
            <svg width="60" height="60" viewBox="0 0 60 60">
                <line x1="10" y1="10" x2="50" y2="50" stroke="{wrong_red}" stroke-width="6" stroke-linecap="round"/>
                <line x1="50" y1="10" x2="10" y2="50" stroke="{wrong_red}" stroke-width="6" stroke-linecap="round"/>
            </svg>
            <p class="body" style="font-size: 24px; color: {wrong_red}; text-transform: uppercase; letter-spacing: 3px; font-weight: bold;">
                Wrong Question
            </p>
            <svg width="60" height="60" viewBox="0 0 60 60">
                <line x1="10" y1="10" x2="50" y2="50" stroke="{wrong_red}" stroke-width="6" stroke-linecap="round"/>
                <line x1="50" y1="10" x2="10" y2="50" stroke="{wrong_red}" stroke-width="6" stroke-linecap="round"/>
            </svg>
        </div>
    </div>
</div>
'''


def slide_18_big_question():
    """The Big Question - Is Etsy even worth pursuing in 2026?"""
    dark_bg = '#1E1E26'
    dark_accent = '#2A2A35'

    return f'''
<div class="slide" style="background: linear-gradient(145deg, {dark_bg} 0%, #141418 100%);">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(960, 540, 600, 500, dark_accent, 0.4, 0, seed=63, style='amoeba')}
        {svg_blob(1700, 200, 280, 250, COLORS['coral'], 0.05, 20, seed=64, style='cloud')}
        {svg_blob(150, 850, 250, 220, COLORS['teal_deep'], 0.04, -10, seed=65, style='wave')}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-center" style="font-size: 90px; line-height: 1.15; color: white;">
            Is Etsy even<br>
            <span style="color: {COLORS['coral']};">worth pursuing</span><br>
            in 2026?
        </h1>
    </div>
</div>
'''


def slide_19_promise():
    """The Promise - I'm going to answer that question tonight"""
    return f'''
<div class="slide" style="background: linear-gradient(135deg, {COLORS['cream']}, {COLORS['mint']});">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1620, 180, 380, 320, COLORS['teal_light'], 0.3, 25, seed=66, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['coral_pale'], 0.35, -20, seed=67, style='amoeba')}
        {svg_blob(1750, 700, 220, 200, COLORS['gold_soft'], 0.3, 10, seed=68, style='wave')}
        {svg_blob(180, 200, 200, 180, COLORS['blush_soft'], 0.25, -5, seed=69, style='organic')}
    </svg>

    <div class="content flex-center">
        <h1 class="display text-dark text-center" style="font-size: 64px; margin-bottom: 40px; line-height: 1.3;">
            I'm going to answer that<br>question tonight.
        </h1>

        <div style="display: flex; align-items: center; gap: 30px; margin-bottom: 40px;">
            <div style="width: 100px; height: 4px; background: {COLORS['teal']}; border-radius: 2px;"></div>
            <!-- Subtle reveal/surprise visual element -->
            <svg width="50" height="50" viewBox="0 0 50 50">
                <circle cx="25" cy="25" r="22" fill="{COLORS['teal']}" opacity="0.15"/>
                <circle cx="25" cy="25" r="15" fill="{COLORS['teal']}" opacity="0.3"/>
                <circle cx="25" cy="25" r="8" fill="{COLORS['teal']}"/>
            </svg>
            <div style="width: 100px; height: 4px; background: {COLORS['teal']}; border-radius: 2px;"></div>
        </div>

        <h2 class="display text-teal text-center" style="font-size: 52px; line-height: 1.3;">
            And the answer?<br>
            <span style="color: {COLORS['coral']};">It might honestly surprise you.</span>
        </h2>
    </div>
</div>
'''


def slide_20a_opportunity_part1():
    """The Opportunity Reveal - Part 1: Just the opportunity statement"""
    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1620, 180, 380, 320, COLORS['mint'], 0.4, 25, seed=70, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['blush_soft'], 0.45, -20, seed=71, style='amoeba')}
        {svg_blob(1750, 700, 220, 200, COLORS['teal_light'], 0.25, 10, seed=72, style='wave')}
    </svg>

    <div class="content flex-center">
        <p class="body text-muted text-center" style="font-size: 28px; margin-bottom: 40px;">
            Because what nobody is talking about is this:
        </p>

        <h1 class="display text-dark text-center" style="font-size: 64px; line-height: 1.3;">
            The AI flood actually<br>
            <span style="color: {COLORS['teal_deep']}; font-size: 80px;">CREATES</span> an opportunity<br>
            <span style="font-size: 52px;">for a very specific type of seller...</span>
        </h1>
    </div>
</div>
'''


def slide_20b_opportunity_full():
    """The Opportunity Reveal - Full with the BUT condition"""
    gold = '#D4AF37'

    return f'''
<div class="slide bg-cream">
    <svg class="bg-shapes" viewBox="0 0 {SLIDE_WIDTH} {SLIDE_HEIGHT}" preserveAspectRatio="none">
        {svg_blob(1620, 180, 380, 320, COLORS['mint'], 0.4, 25, seed=70, style='cloud')}
        {svg_blob(80, 830, 320, 290, COLORS['blush_soft'], 0.45, -20, seed=71, style='amoeba')}
        {svg_blob(1750, 700, 220, 200, COLORS['teal_light'], 0.25, 10, seed=72, style='wave')}
        {svg_blob(200, 150, 180, 160, COLORS['gold_soft'], 0.3, 5, seed=73, style='organic')}
    </svg>

    <div class="content" style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; gap: 30px;">
        <p class="body text-muted text-center" style="font-size: 26px;">
            Because what nobody is talking about is this:
        </p>

        <h1 class="display text-dark text-center" style="font-size: 56px; line-height: 1.3; margin-bottom: 10px;">
            The AI flood actually<br>
            <span style="color: {COLORS['teal_deep']}; font-size: 72px;">CREATES</span> an
            <span style="background: linear-gradient(135deg, {COLORS['gold']}, {gold}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">opportunity</span><br>
            <span style="font-size: 46px;">for a very specific type of seller...</span>
        </h1>

        <!-- The BUT condition - visual gate -->
        <div style="background: linear-gradient(135deg, {COLORS['teal_deep']}, {COLORS['teal']}); padding: 30px 60px; border-radius: 20px; margin-top: 20px; box-shadow: 0 15px 40px rgba(27,138,138,0.25);">
            <p class="body text-center" style="font-size: 32px; color: white; line-height: 1.5;">
                <span style="font-weight: bold; font-size: 38px; color: {COLORS['coral_soft']};">BUT</span> only if you understand<br>
                what's <span style="font-weight: bold;">really</span> happening...
            </p>
        </div>

        <!-- Subtle unlock/key visual -->
        <svg width="60" height="60" viewBox="0 0 60 60" style="margin-top: 10px; opacity: 0.4;">
            <circle cx="30" cy="22" r="14" fill="none" stroke="{COLORS['teal_deep']}" stroke-width="4"/>
            <rect x="24" y="32" width="12" height="20" rx="3" fill="{COLORS['teal_deep']}"/>
            <circle cx="30" cy="40" r="3" fill="white"/>
        </svg>
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
        slide_13a_stat_75_number(),
        slide_13b_stat_75_full(),
        slide_14a_stat_58_number(),
        slide_14b_stat_58_full(),
        slide_15a_stat_47_number(),
        slide_15b_stat_47_full(),
        slide_16_engagement(),
        slide_17_reframe_setup(),
        slide_18_big_question(),
        slide_19_promise(),
        slide_20a_opportunity_part1(),
        slide_20b_opportunity_full(),
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
