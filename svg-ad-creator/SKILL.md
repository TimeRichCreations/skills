---
name: svg-ad-creator
description: Create professional SVG advertisements with customizable layouts, typography, and color schemes. This skill should be used when users request ad creation, promotional graphics, marketing materials, social media posts, or any visual advertisement in SVG format. Supports multiple templates (product showcase, promotions, events, lifestyle, minimalist, grid layouts), automatic template selection based on content and intent, and generates unique designs through intelligent color palette selection, font pairing, and layout variations.
---

# SVG Ad Creator

Create professional, unique SVG advertisements with intelligent template selection, sophisticated design systems, and automated layout optimization.

## Overview

This skill generates complete SVG ad code with:
- **8 template archetypes** (Product Hero, Multi-Product Grid, Text-Heavy Promo, Lifestyle Story, Minimalist Luxury, Event Announcement, Split Feature, Magazine Layout)
- **10 pre-defined color palettes** with automatic keyword-based selection
- **8 professional font pairings** matched to template and mood
- **Automated layout calculations** using design principles (rule of thirds, golden ratio, 8-point grid)
- **Uniqueness through variation** while maintaining professional quality

## Workflow Decision Tree

Follow this decision tree to determine how to approach SVG ad generation:

```
START
  │
  ├─ User provides explicit template name?
  │  └─ YES → Use specified template → Continue to customization
  │  └─ NO → Continue to analysis
  │
  ├─ Analyze user prompt for:
  │  ├─ Number of images (0, 1, 2-6, 7+)
  │  ├─ Keywords (sale, luxury, event, product, etc.)
  │  ├─ Tone/mood (professional, playful, elegant, bold)
  │  └─ Content type (product, lifestyle, text-heavy, mixed)
  │
  ├─ SELECT TEMPLATE:
  │  ├─ 0 images + sale/promo keywords → Text-Heavy Promo
  │  ├─ 1 image + luxury/minimal keywords → Minimalist Luxury
  │  ├─ 1 image + lifestyle content → Lifestyle Story
  │  ├─ 1 image (default) → Product Hero
  │  ├─ 2 images + comparison intent → Split Feature
  │  ├─ 2-6 images → Multi-Product Grid
  │  ├─ 2-4 images + editorial tone → Magazine Layout
  │  └─ Event keywords → Event Announcement
  │
  ├─ SELECT COLOR PALETTE:
  │  ├─ Check for color keywords in prompt or image descriptions
  │  ├─ Check for mood/brand keywords (luxury, eco, tech, etc.)
  │  └─ Use template default if no matches
  │
  ├─ SELECT FONT PAIRING:
  │  └─ Match to template type and detected mood
  │
  ├─ GENERATE SVG:
  │  ├─ Use scripts/generate_svg_ad.py for base structure
  │  ├─ Apply color palette from assets/palettes.json
  │  ├─ Apply typography from assets/fonts.json
  │  └─ Add icons from assets/icons.svg if appropriate
  │
  └─ OUTPUT complete SVG code
```

## Core Capabilities

### 1. Template Selection

Automatically select or use specified template based on content analysis.

**Template Overview:**

| Template | Trigger | Image Count | Best For |
|----------|---------|-------------|----------|
| Product Hero | "product", "showcase", "feature" | 1 | Single product focus |
| Multi-Product Grid | "products", "collection", "catalog" | 2-6 | Multiple items |
| Text-Heavy Promo | "sale", "discount", "offer" | 0-1 | Promotions, deals |
| Lifestyle Story | "lifestyle", "story", "inspiration" | 1-2 | Brand storytelling |
| Minimalist Luxury | "luxury", "premium", "elegant" | 1 | High-end products |
| Event Announcement | "event", "concert", "webinar" | 0-2 | Events, launches |
| Split Feature | "compare", "vs", "options" | 2 | Comparisons, choices |
| Magazine Layout | "editorial", "magazine", "article" | 2-4 | Content-rich ads |

**Selection Logic:**
1. Check for explicit template request
2. Count images from user input
3. Parse keywords using template_specs.md mappings
4. Analyze tone and content type
5. Apply selection priority rules

**Reference:** See `references/template_specs.md` for complete specifications, layout structures, and design rules for each template.

### 2. Color Palette Management

Select harmonious color palettes that match the ad's purpose and mood.

**Available Palettes:**
- **Ocean Breeze** - Professional, trustworthy (corporate, tech)
- **Sunset Vibes** - Warm, energetic (sales, food)
- **Forest Fresh** - Natural, organic (wellness, eco)
- **Midnight Luxury** - Dark, premium (luxury, high-end)
- **Berry Blast** - Vibrant, playful (beauty, fashion)
- **Monochrome Modern** - Neutral, minimalist (design, architecture)
- **Lavender Dreams** - Soft, calm (wellness, creativity)
- **Coral Reef** - Tropical, fresh (travel, summer)
- **Earth Tones** - Grounded, authentic (artisan, traditional)
- **Electric Neon** - Bold, modern (tech, gaming)

**Selection Process:**
1. Check prompt for color-related keywords (luxury → Midnight Luxury, sale → Sunset Vibes, etc.)
2. Check image descriptions for dominant colors
3. Use template defaults if no specific indicators
4. Load from `assets/palettes.json`

**Custom Palette Generation:**
When image descriptions include specific colors:
1. Extract dominant color using `scripts/color_utils.py`
2. Generate harmonious palette based on mood:
   - Vibrant → Triadic scheme
   - Calm → Monochromatic scheme
   - Bold → Complementary scheme
   - Neutral → Analogous scheme

**Reference:** See `references/color_theory.md` for color psychology, contrast requirements, and palette generation algorithms.

### 3. Typography System

Apply professional font pairings that match the template and brand personality.

**Font Pairings:**
1. **Modern Professional** (Inter) - Corporate, tech, SaaS
2. **Classic Elegance** (Playfair Display + Source Sans) - Luxury, fashion
3. **Bold Impact** (Montserrat) - Sales, promotions
4. **Friendly Approachable** (Poppins) - Lifestyle, wellness
5. **Tech Modern** (Space Grotesk + IBM Plex) - Startups, apps
6. **Editorial** (Merriweather + Lato) - Content, publishing
7. **Geometric Clean** (Raleway) - Minimalist, design
8. **Playful Creative** (Fredoka + Nunito) - Kids, fun products

**Typography Scale:**
Use modular scale from `assets/fonts.json`:
- Display: 64px (hero headlines)
- H1: 51px (main headlines)
- H2: 41px (subheadings)
- H3: 33px (section headers)
- Body Large: 20px (emphasis)
- Body: 16px (standard text)
- Caption: 10px (fine print)

**Application Rules:**
- Maximum 3 text sizes per ad (exceptions: Magazine Layout)
- Minimum 300 weight difference between heading and body
- Line height: 1.2 for headings, 1.5 for body text
- Letter spacing: -0.02em for large headings, 0em for body

**Reference:** See `references/design_principles.md` for complete typography system and hierarchy rules.

### 4. Layout Calculation

Calculate optimal layouts using design principles and mathematical precision.

**8-Point Grid System:**
All spacing in multiples of 8px for visual harmony:
- 8px: Tight spacing (icon to text)
- 16px: Standard spacing (paragraphs)
- 24px: Medium spacing (sections)
- 32px: Large spacing (major divisions)
- 48px: Canvas padding

**Layout Techniques:**
- **Rule of Thirds**: Position key elements at intersection points
- **Golden Ratio** (1.618): For asymmetric balance in Minimalist templates
- **60-30-10 Color Rule**: 60% background, 30% content, 10% accent
- **Vertical Rhythm**: Typography-based spacing calculations
- **Grid Configurations**: Automatic for multi-image layouts (2x2, 3x1, etc.)

**Use `scripts/layout_engine.py` for:**
- Grid calculations: `calculate_grid(num_images)`
- Centered positioning: `calculate_centered_box(width, height)`
- Button sizing: `calculate_button_size(text_length, size)`
- Rule of thirds points: `calculate_rule_of_thirds_points()`
- Golden ratio placement: `calculate_golden_ratio_position()`

**Reference:** See `references/design_principles.md` for spacing systems, composition principles, and visual hierarchy rules.

### 5. Generating SVG Code

Create complete, valid SVG code using the generation scripts and design principles.

**Generation Process:**

1. **Import utilities:**
```python
from scripts.generate_svg_ad import SVGAdGenerator
from scripts.color_utils import select_palette_by_keywords, ColorPalette
from scripts.layout_engine import LayoutEngine
```

2. **Initialize generator:**
```python
# Create generator with canvas size and seed for reproducibility
generator = SVGAdGenerator(1080, 1080, seed=user_prompt_hash)
```

3. **Select palette:**
```python
# Select based on keywords in prompt
palette = select_palette_by_keywords(user_prompt, template_type)
```

4. **Generate template:**
```python
# Example: Product Hero
svg_code = generator.generate_product_hero(
    product_name="Premium Headphones",
    description="Experience crystal-clear audio",
    cta_text="Shop Now",
    palette=palette,
    brand_text="AudioBrand"
)
```

5. **Output SVG:**
Return complete SVG code to user, ready to save as .svg file.

**Available Generation Methods:**
- `generate_product_hero()` - Single product showcase
- `generate_multi_product_grid()` - Grid of multiple products
- `generate_text_heavy_promo()` - Promotion with large text
- `generate_minimalist_luxury()` - Minimal, elegant design
- More methods available in `scripts/generate_svg_ad.py`

**Custom Elements:**
- Text: `create_text_element(text, x, y, size, weight, color)`
- Rectangles: `create_rect(x, y, width, height, fill, stroke)`
- Circles: `create_circle(cx, cy, r, fill, stroke)`
- Images: `create_image_placeholder(x, y, width, height, label)`
- CTAs: `create_cta_button(x, y, width, height, text, colors)`

### 6. Ensuring Uniqueness

Each generated ad should feel unique while maintaining professional quality.

**Variation Points:**
1. **Color palette selection** - Choose from 10 palettes or generate custom
2. **Font pairing** - Rotate through appropriate options
3. **Layout micro-variations** - Adjust spacing by ±10-20%
4. **Decorative elements** - Vary shapes, positions, styles
5. **Image treatment** - Different borders, shadows, masks
6. **Gradient directions** - Rotate angles
7. **Accent placement** - Reposition emphasis elements

**Seeded Randomness:**
Use hash of user prompt as seed for reproducibility:
```python
import hashlib
seed = hashlib.md5(user_prompt.encode()).hexdigest()
generator = SVGAdGenerator(width, height, seed=seed)
```

This ensures:
- Same input → Same output (reproducible)
- Different inputs → Different outputs (unique)
- Deterministic but varied choices

**Quality Constraints:**
Do not randomize:
- Template selection (must be intentional)
- Core visual hierarchy
- Readability and contrast
- Essential structure

### 7. Accessibility & Quality Assurance

Ensure all generated ads meet accessibility standards and quality benchmarks.

**Accessibility Checklist:**
- [ ] Text contrast ≥ 4.5:1 for body text (WCAG AA)
- [ ] Text contrast ≥ 3:1 for large text (24px+)
- [ ] CTA buttons ≥ 44x44px (touch targets)
- [ ] Minimum font size 14px for body text
- [ ] No color-only information (use text/icons too)
- [ ] High contrast for critical information

**Use `scripts/color_utils.py` for:**
```python
# Check contrast ratio
ratio = get_contrast_ratio(text_color, bg_color)
# Ensure sufficient contrast
safe_color = ensure_sufficient_contrast(text_color, bg_color, min_ratio=4.5)
```

**Design Quality Checklist:**
- [ ] Clear visual hierarchy (primary element obvious)
- [ ] Consistent spacing (8px grid alignment)
- [ ] Maximum 3 text sizes (exceptions: Magazine)
- [ ] Adequate padding (minimum 5% of canvas)
- [ ] CTA clearly visible and actionable
- [ ] Balanced composition (not too crowded)
- [ ] Color harmony (60-30-10 rule applied)

### 8. Handling User Requests

Interpret user requests and extract necessary information for ad generation.

**Information to Extract:**
- **Template preference** - "minimalist style", "grid layout", explicit template name
- **Content type** - Product name, event details, promotional offer
- **Number of images** - "one product photo", "gallery of 4 images"
- **Image descriptions** - Parse for colors, subjects, mood
- **Brand elements** - Logo text, brand name, brand colors
- **Call-to-action** - "Shop Now", "Learn More", "Register Today"
- **Tone/mood** - "professional", "playful", "luxurious", "bold"
- **Size requirements** - Default 1080x1080px, or specify custom

**Example Request Parsing:**

**User:** "Create a promotional ad for 50% off summer sale, bright and energetic"

**Parse:**
- Template: Text-Heavy Promo (keywords: "promotional", "sale")
- Content: "50% OFF", "Summer Sale"
- Images: 0 (text-focused)
- Palette: Sunset Vibes (keywords: "bright", "energetic")
- Font: Bold Impact (matches promo template)
- CTA: "Shop Now" (default for sales)

**User:** "Make an elegant ad showcasing our luxury watch"

**Parse:**
- Template: Minimalist Luxury (keywords: "elegant", "luxury")
- Content: "Luxury Watch" (product name)
- Images: 1 (single product)
- Palette: Midnight Luxury (keywords: "elegant", "luxury")
- Font: Classic Elegance (matches luxury template)
- CTA: "Discover More" (subtle for luxury)

**Missing Information:**
If critical information is missing, ask clarifying questions:
- "What text should appear on the ad?"
- "How many images will be included?"
- "What should the call-to-action say?"
- "Any specific colors or brand guidelines?"

## Canvas Sizes

**Default:** 1080x1080px (Instagram square)

**Supported Sizes:**
- Square: 1080x1080px (Instagram, Facebook post)
- Story: 1080x1920px (Instagram/Facebook Stories)
- Wide: 1200x628px (Facebook/Twitter link preview)
- Banner: 728x90px (Web banner)
- Custom: Any size (specify width x height)

**Responsive Adaptations:**
- Story (vertical): Stack elements vertically, increase text size
- Wide (horizontal): Horizontal layouts, side-by-side elements
- Banner (small): Single row, minimal text, clear CTA

## Icons and Decorative Elements

Icons available from `assets/icons.svg`:

**Shopping/Commerce:**
- cart, tag, gift, percent, truck (delivery)

**Communication:**
- phone, mail, arrow-right

**Time/Location:**
- clock, calendar, map-pin

**Achievement:**
- star, trophy, award, sparkles

**Action:**
- check, download, zap (lightning), fire

**Usage:**
```svg
<!-- Reference icon in SVG -->
<use href="assets/icons.svg#icon-cart" x="100" y="100" width="32" height="32" fill="#000000"/>
```

Add icons to CTAs, section headers, or as decorative accents (use sparingly).

## Example Usage

### Example 1: Product Showcase

**User Request:** "Create an ad for our new wireless headphones with a clean, professional look"

**Process:**
1. Template: Product Hero (1 product, professional)
2. Palette: Ocean Breeze (professional keyword)
3. Font: Modern Professional
4. Layout: Centered product image, name below, CTA at bottom
5. Generate using `generate_product_hero()`

### Example 2: Flash Sale

**User Request:** "50% off everything! Make it bold and attention-grabbing for our summer sale"

**Process:**
1. Template: Text-Heavy Promo (sale, no images needed)
2. Palette: Sunset Vibes (energetic, sale)
3. Font: Bold Impact
4. Layout: Large "50% OFF" badge, sale details, strong CTA
5. Generate using `generate_text_heavy_promo()`

### Example 3: Product Collection

**User Request:** "Show our 6 new product designs in a grid layout"

**Process:**
1. Template: Multi-Product Grid (6 images)
2. Palette: Monochrome Modern (clean, lets products shine)
3. Font: Modern Professional
4. Layout: 3x2 grid, header at top, CTA at bottom
5. Generate using `generate_multi_product_grid()`

## Tips for Best Results

1. **Be specific about intent** - "luxury", "sale", "professional" guide template and palette selection
2. **Mention image count** - Helps select appropriate template
3. **Describe image content** - Color keywords help palette generation
4. **Specify CTA** - Or accept intelligent defaults
5. **Request variations** - "Show me another version" uses different palette/fonts
6. **Canvas size matters** - Specify if not using Instagram square default
7. **Trust the system** - Templates and palettes are professionally designed

## Resources

### scripts/
- `generate_svg_ad.py` - Main SVG generation engine with template methods
- `color_utils.py` - Color palette selection, extraction, and manipulation
- `layout_engine.py` - Layout calculations, grid systems, positioning

### references/
- `template_specs.md` - Complete specifications for all 8 templates
- `design_principles.md` - Typography, spacing, composition rules
- `color_theory.md` - Color palettes, harmony, and psychology

### assets/
- `palettes.json` - 10 pre-defined color palettes with metadata
- `fonts.json` - 8 font pairings with usage guidelines
- `icons.svg` - Library of 20+ reusable SVG icons

## Limitations

- **Image placeholders only** - Script generates placeholders with labels; actual images would need to be embedded separately
- **Web-safe fonts** - Uses system fonts with fallbacks (no embedded font files)
- **Static output** - SVG code only, no animations or interactivity
- **Manual iteration** - Each request generates one design; request variations explicitly

## Output Format

Always return:
1. **Complete SVG code** - Valid, copy-paste ready
2. **Brief description** - Template used, palette name, key features
3. **Usage instructions** - How to save and use the SVG file
4. **Customization notes** - What can be easily adjusted

```
Generated SVG Ad: [Template Name] with [Palette Name]

[SVG CODE HERE]

To use: Save as filename.svg and open in browser or design tool.
Customization: Colors in palette can be adjusted, text content easily modified.
```
