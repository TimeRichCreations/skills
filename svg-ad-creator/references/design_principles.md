# Design Principles for SVG Ad Creation

This document outlines the core design principles, typography system, spacing rules, and composition guidelines for generating high-quality SVG advertisements.

---

## Typography System

### Font Pairing Matrix

Each pairing includes a heading font and body font that work well together.

#### Pairing 1: Modern Professional
- **Heading**: Inter (700-800 weight)
- **Body**: Inter (400-500 weight)
- **Use**: Corporate, tech, SaaS, professional services
- **Mood**: Clean, trustworthy, modern

#### Pairing 2: Classic Elegance
- **Heading**: Playfair Display (700 weight)
- **Body**: Source Sans Pro (400 weight)
- **Use**: Luxury, fashion, beauty, premium products
- **Mood**: Sophisticated, timeless, elegant

#### Pairing 3: Bold Impact
- **Heading**: Montserrat (800-900 weight)
- **Body**: Montserrat (400-500 weight)
- **Use**: Sales, promotions, energetic brands
- **Mood**: Strong, confident, attention-grabbing

#### Pairing 4: Friendly Approachable
- **Heading**: Poppins (600-700 weight)
- **Body**: Poppins (400 weight)
- **Use**: Lifestyle, wellness, consumer goods
- **Mood**: Warm, inviting, accessible

#### Pairing 5: Tech Modern
- **Heading**: Space Grotesk (700 weight)
- **Body**: IBM Plex Sans (400 weight)
- **Use**: Startups, apps, innovation
- **Mood**: Forward-thinking, digital, contemporary

#### Pairing 6: Editorial
- **Heading**: Merriweather (700-900 weight)
- **Body**: Lato (400 weight)
- **Use**: Content, publishing, storytelling
- **Mood**: Readable, authoritative, journalistic

#### Pairing 7: Geometric Clean
- **Heading**: Raleway (700-800 weight)
- **Body**: Raleway (400 weight)
- **Use**: Minimalist, design-focused, portfolios
- **Mood**: Precise, balanced, modern

#### Pairing 8: Playful Creative
- **Heading**: Fredoka One (400 weight)
- **Body**: Nunito (400 weight)
- **Use**: Kids, fun products, casual brands
- **Mood**: Energetic, youthful, creative

### Font Selection Logic

```
Template Type → Mood → Font Pairing

Product Hero → Professional → Modern Professional
Product Hero → Luxury → Classic Elegance
Multi-Product Grid → Energetic → Bold Impact
Text-Heavy Promo → Strong → Bold Impact
Lifestyle Story → Warm → Friendly Approachable
Minimalist Luxury → Elegant → Classic Elegance
Event Announcement → Modern → Tech Modern
Split Feature → Clean → Geometric Clean
Magazine Layout → Editorial → Editorial
```

### Typography Scale

Base unit: 16px (body text)

**Modular Scale** (1.250 - Major Third):
- Display: 64px (4.000rem)
- H1: 51px (3.200rem)
- H2: 41px (2.560rem)
- H3: 33px (2.050rem)
- H4: 26px (1.640rem)
- H5: 21px (1.310rem)
- Body Large: 20px (1.250rem)
- Body: 16px (1.000rem)
- Body Small: 13px (0.800rem)
- Caption: 10px (0.640rem)

**Line Height**:
- Headings: 1.2-1.3
- Body text: 1.5-1.6
- Short text (CTAs): 1.0-1.2

**Letter Spacing**:
- Large headings: -0.02em to -0.03em (tighter)
- Body text: 0 (default)
- All caps: 0.05em to 0.10em (wider)
- Small text: 0.01em

### Text Hierarchy Rules

1. **Maximum 3 text sizes** per ad (exceptions for magazine layout)
2. **Weight contrast**: Minimum 300 weight difference (e.g., 400 body + 700 heading)
3. **Color contrast**: WCAG AA minimum (4.5:1 for body, 3:1 for headings)
4. **Alignment**: Consistent within template (centered, left, or right)

---

## Spacing System

### Grid System

**8-Point Grid**: All spacing in multiples of 8px

```
4px  - Micro spacing (between related elements)
8px  - Tight spacing (icon to text)
16px - Standard spacing (paragraph spacing)
24px - Medium spacing (between sections)
32px - Large spacing (major sections)
48px - XL spacing (canvas padding)
64px - XXL spacing (dramatic separation)
```

### Canvas Padding

Based on canvas size percentage:

- **Small canvas** (<600px): 5-6% padding
- **Medium canvas** (600-1200px): 6-8% padding
- **Large canvas** (>1200px): 8-10% padding

**Minimum absolute padding**: 40px

### Element Spacing

**Text to Image**: 24-32px
**Button to Text**: 16-24px
**Between Product Items**: 16-24px
**Logo to Content**: 32-48px

### Breathing Room

- **Don't fill more than 75%** of available space with content
- **Negative space** is a design feature, not wasted space
- **Clustered elements** should have generous surrounding space

---

## Color Composition

### Contrast Requirements

**Text Readability**:
- Body text on background: ≥ 4.5:1
- Heading text on background: ≥ 3:1
- Text on image overlay: ≥ 4.5:1 (use semi-transparent overlays)

**Visual Hierarchy**:
- Primary CTA: Highest contrast element
- Secondary elements: Medium contrast
- Background elements: Low contrast

### Color Dominance

**60-30-10 Rule**:
- **60%**: Dominant color (usually background)
- **30%**: Secondary color (content areas, images)
- **10%**: Accent color (CTAs, highlights)

### Overlay Techniques

When placing text over images:

1. **Dark overlay**: rgba(0, 0, 0, 0.4-0.6) for light images
2. **Light overlay**: rgba(255, 255, 255, 0.7-0.9) for dark images
3. **Gradient overlay**: Dark at bottom, transparent at top
4. **Blur behind text**: Subtle gaussian blur in text area
5. **Solid box**: Semi-transparent background behind text

---

## Composition Principles

### Visual Hierarchy

1. **Primary element**: Largest, highest contrast (50-60% visual weight)
2. **Secondary elements**: Medium size/contrast (30% visual weight)
3. **Tertiary elements**: Smallest, support primary (10% visual weight)

### Rule of Thirds

Divide canvas into 3×3 grid:
- Place key elements at intersection points
- Avoid dead-center placement (unless intentional symmetry)
- Create visual movement across canvas

### Balance

**Symmetrical Balance**:
- Formal, stable, professional
- Perfect for: Luxury, corporate, formal events
- Center alignment, mirrored elements

**Asymmetrical Balance**:
- Dynamic, modern, interesting
- Perfect for: Lifestyle, creative, energetic brands
- Different sized elements balanced by position

### Visual Flow

Create intentional eye movement path:

**Z-Pattern** (Western reading):
```
Start → → → Top Right
  ↓
Middle Left → → Right
  ↓
Bottom Left → → End
```

**F-Pattern** (Text-heavy):
```
Title → → → →
  ↓
Subhead → →
  ↓
Body
  ↓
CTA
```

### Alignment

**Consistent alignment** creates visual harmony:
- Choose left, center, or right alignment per template
- Align related elements to invisible grid lines
- Break alignment intentionally for emphasis only

---

## Image Treatment

### Image Composition

**Product Images**:
- Center of visual weight
- Clean background or subtle shadow
- 60-70% of canvas maximum

**Lifestyle Images**:
- Can extend to edges (full bleed)
- Consider rule of thirds for subject placement
- Ensure text overlay areas have clean space

**Multiple Images**:
- Consistent aspect ratio (preferred)
- OR intentional size hierarchy
- Equal gutter spacing between all images

### Image Enhancements

**Filters** (apply sparingly):
- Brightness adjustment: ±10-20%
- Contrast adjustment: ±5-15%
- Saturation: -10% to +20%
- Duotone: For artistic effect

**Masks & Shapes**:
- Rounded corners: 8-16px radius
- Circular masks: Perfect circles only
- Custom shapes: Simple geometric only

**Borders**:
- Thickness: 1-3px
- Color: From image or brand color
- Or no border (prefer negative space)

---

## Call-to-Action (CTA) Design

### CTA Prominence

CTAs must be **immediately obvious**:
- Highest contrast element on canvas
- Sufficient size: Minimum 44x44px touch target
- Clear, action-oriented text

### CTA Button Design

**Anatomy**:
```
┌─────────────────────┐
│   [Icon] Action     │  ← 16-24px padding vertical
└─────────────────────┘    32-48px padding horizontal
```

**Text**:
- Size: 16-20px
- Weight: 600-700 (semibold to bold)
- All caps or sentence case (consistent)
- 1-3 words maximum

**Colors**:
- Background: Brand accent or high contrast
- Text: White or dark (ensure 4.5:1 contrast)
- Hover state: 10-20% darker/lighter

### CTA Placement

**Priority by template**:
1. Bottom third of canvas (most common)
2. Top right (navigation style)
3. Center (hero announcement)
4. After main content (natural flow)

**Spacing around CTA**: Minimum 24px clear space on all sides

---

## Special Effects & Decorative Elements

### When to Use

- **Minimalist templates**: No decorative elements
- **Bold templates**: Geometric shapes, lines, patterns
- **Playful templates**: Illustrations, doodles, icons
- **Professional templates**: Subtle lines, minimal shapes

### Geometric Shapes

**Circles**:
- Background decoration
- Image masks
- Badges for emphasis

**Rectangles/Squares**:
- Frames for content
- Background blocks
- Grid elements

**Lines**:
- Dividers (1-2px)
- Underlines for emphasis (3-5px)
- Decorative accents (45° angles)

**Custom Shapes**:
- Brand-specific shapes
- Abstract organic shapes
- Layered for depth

### Effects Usage

**Shadows**:
- Subtle: 0 2px 8px rgba(0,0,0,0.1)
- Medium: 0 4px 16px rgba(0,0,0,0.15)
- Strong: 0 8px 32px rgba(0,0,0,0.2)

**Gradients**:
- Linear: Top to bottom or diagonal
- Radial: From center outward
- Subtle (within same hue) or bold (complementary)

**Opacity**:
- Full opacity: Main content (100%)
- Semi-transparent: Overlays (40-80%)
- Ghosted: Background elements (10-30%)

---

## Accessibility Guidelines

### Essential Requirements

1. **Text contrast**: Minimum WCAG AA (4.5:1 body, 3:1 headings)
2. **Font size**: Minimum 14px for body text
3. **Touch targets**: Minimum 44x44px for interactive elements
4. **Color independence**: Don't rely solely on color to convey meaning

### Best Practices

- Avoid text on busy image backgrounds without overlay
- Use clear, readable fonts (avoid overly decorative)
- Sufficient line height for readability (1.5 minimum)
- High contrast for primary information

---

## Uniqueness Through Variation

To ensure each ad feels unique while maintaining quality:

### Randomization Points

1. **Color palette**: Choose from 5-7 options per template
2. **Font pairing**: Rotate through appropriate pairings
3. **Layout micro-variations**: Adjust spacing by ±10-20%
4. **Decorative elements**: Different shapes/positions
5. **Image treatment**: Vary masks, borders, effects
6. **Gradient directions**: Rotate angle
7. **Accent placement**: Different positions for emphasis

### Seeded Randomness

Use hash of user prompt + timestamp as seed for:
- Consistent results for same input (reproducible)
- Variation when user wants "another version"
- Deterministic but seemingly random choices

### Prohibited Variations

Don't randomize core structure:
- Template selection must be intentional
- Don't break established hierarchy
- Maintain readability and usability
- Keep brand consistency if specified

---

## Quality Checklist

Before finalizing any SVG ad, verify:

- [ ] Clear visual hierarchy (primary element obvious)
- [ ] Sufficient contrast (text readable, CTA prominent)
- [ ] Consistent spacing (8px grid alignment)
- [ ] Typography properly scaled (max 3 sizes)
- [ ] Adequate padding (minimum 5% canvas size)
- [ ] CTA clearly visible and actionable
- [ ] No text on busy backgrounds without overlay
- [ ] Balanced composition (not too crowded or empty)
- [ ] Color harmony (60-30-10 rule applied)
- [ ] All elements aligned to grid
