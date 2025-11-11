# Color Theory and Palette Systems

This document provides color palette systems, color extraction strategies, and color combination rules for SVG ad generation.

---

## Pre-Defined Color Palettes

Each palette includes: background, primary, secondary, accent, and text colors.

### Palette 1: Ocean Breeze (Cool, Professional)
```
Background:  #F0F8FF (Alice Blue)
Primary:     #2E5266 (Deep Teal)
Secondary:   #6E8898 (Slate Blue)
Accent:      #D3AF37 (Gold)
Text Dark:   #1A1A1A
Text Light:  #FFFFFF
```
**Use**: Corporate, technology, finance, trust-building
**Mood**: Calm, trustworthy, professional

### Palette 2: Sunset Vibes (Warm, Energetic)
```
Background:  #FFF5EB (Seashell)
Primary:     #FF6B35 (Orange Red)
Secondary:   #F7931E (Orange)
Accent:      #C1292E (Cardinal Red)
Text Dark:   #2A2A2A
Text Light:  #FFFFFF
```
**Use**: Sales, promotions, food, energetic brands
**Mood**: Warm, exciting, appetizing

### Palette 3: Forest Fresh (Natural, Organic)
```
Background:  #F4F7F5 (Mint Cream)
Primary:     #2D6A4F (Hunter Green)
Secondary:   #52B788 (Emerald)
Accent:      #95D5B2 (Celadon)
Text Dark:   #1B4332
Text Light:  #FFFFFF
```
**Use**: Wellness, organic, eco-friendly, health
**Mood**: Fresh, natural, calming

### Palette 4: Midnight Luxury (Dark, Premium)
```
Background:  #1A1A1A (Rich Black)
Primary:     #FFFFFF (White)
Secondary:   #A0A0A0 (Silver)
Accent:      #D4AF37 (Metallic Gold)
Text Dark:   #FFFFFF
Text Light:  #E5E5E5
```
**Use**: Luxury, premium products, high-end events
**Mood**: Sophisticated, exclusive, elegant

### Palette 5: Berry Blast (Vibrant, Playful)
```
Background:  #FFF0F5 (Lavender Blush)
Primary:     #C9184A (Ruby)
Secondary:   #FF4D6D (Watermelon)
Accent:      #FFB3C1 (Cherry Blossom)
Text Dark:   #240115
Text Light:  #FFFFFF
```
**Use**: Beauty, fashion, creative, feminine
**Mood**: Playful, bold, energetic

### Palette 6: Monochrome Modern (Neutral, Minimalist)
```
Background:  #FFFFFF (White)
Primary:     #000000 (Black)
Secondary:   #6C757D (Gray)
Accent:      #343A40 (Charcoal)
Text Dark:   #212529
Text Light:  #F8F9FA
```
**Use**: Minimalist, architecture, design portfolios
**Mood**: Clean, modern, sophisticated

### Palette 7: Lavender Dreams (Soft, Calm)
```
Background:  #FAF9FF (Lavender Mist)
Primary:     #7209B7 (Purple)
Secondary:   #B5A1D6 (Mauve)
Accent:      #F72585 (Pink)
Text Dark:   #3C096C
Text Light:  #FFFFFF
```
**Use**: Wellness, spirituality, creativity, lifestyle
**Mood**: Calming, dreamy, creative

### Palette 8: Coral Reef (Tropical, Fresh)
```
Background:  #FDFBF7 (Cosmic Latte)
Primary:     #FF6F61 (Coral)
Secondary:   #00B4D8 (Cerulean)
Accent:      #FFD23F (Saffron)
Text Dark:   #2B2D42
Text Light:  #FFFFFF
```
**Use**: Travel, lifestyle, summer products, fun
**Mood**: Tropical, energetic, adventurous

### Palette 9: Earth Tones (Grounded, Reliable)
```
Background:  #FAF7F2 (Floral White)
Primary:     #8B4513 (Saddle Brown)
Secondary:   #CD853F (Peru)
Accent:      #DEB887 (Burlywood)
Text Dark:   #3E2723
Text Light:  #FFFFFF
```
**Use**: Artisan, handmade, rustic, traditional
**Mood**: Warm, authentic, grounded

### Palette 10: Electric Neon (Bold, Modern)
```
Background:  #0A0E27 (Dark Navy)
Primary:     #00F5FF (Cyan)
Secondary:   #7B2CBF (Purple)
Accent:      #FF006E (Hot Pink)
Text Dark:   #00F5FF
Text Light:  #FFFFFF
```
**Use**: Tech, gaming, nightlife, modern brands
**Mood**: Edgy, futuristic, bold

---

## Palette Selection Logic

### By Template Type

```
Product Hero          → Based on product image colors or brand
Multi-Product Grid    → Unified neutral (Monochrome, Earth Tones)
Text-Heavy Promo      → High contrast (Sunset Vibes, Electric Neon)
Lifestyle Story       → Mood-matching (Lavender Dreams, Ocean Breeze)
Minimalist Luxury     → Minimal (Monochrome, Midnight Luxury)
Event Announcement    → Event type (Corporate = Ocean, Party = Electric)
Split Feature         → Complementary colors (customize)
Magazine Layout       → Neutral with accents (Monochrome + brand color)
```

### By Keywords in Prompt

```
"luxury", "premium", "elegant"     → Midnight Luxury
"sale", "discount", "promo"        → Sunset Vibes, Berry Blast
"natural", "organic", "eco"        → Forest Fresh, Earth Tones
"modern", "tech", "digital"        → Ocean Breeze, Electric Neon
"calm", "peaceful", "wellness"     → Lavender Dreams, Ocean Breeze
"bold", "energetic", "vibrant"     → Electric Neon, Coral Reef
"professional", "corporate"        → Ocean Breeze, Monochrome
"fun", "playful", "creative"       → Berry Blast, Coral Reef
```

### By Image Content Analysis

When images are provided, analyze described content:

**Dominant colors mentioned**:
- Blues/Greens → Ocean Breeze, Forest Fresh
- Reds/Oranges → Sunset Vibes, Coral Reef
- Purples/Pinks → Berry Blast, Lavender Dreams
- Neutral/Monochrome → Monochrome Modern
- Browns/Tans → Earth Tones

**Content type**:
- Products on white background → Monochrome or complementary
- Nature/outdoor → Forest Fresh, Coral Reef
- Urban/cityscape → Monochrome, Ocean Breeze
- People/lifestyle → Match mood (Lavender Dreams, Sunset Vibes)

---

## Color Extraction from Images

When user provides image descriptions with color information:

### Step 1: Identify Dominant Colors
Parse image descriptions for color keywords:
- "blue sky", "green grass", "red dress", "golden sunset"
- Extract 2-3 primary colors mentioned

### Step 2: Generate Harmonious Palette

**Monochromatic Scheme**:
- Use different shades/tints of dominant color
- Example: Blue → Light blue (bg), Medium blue (primary), Dark blue (accent)

**Complementary Scheme**:
- Dominant color + opposite on color wheel
- Example: Blue → Blue + Orange

**Analogous Scheme**:
- Dominant color + adjacent colors
- Example: Blue → Blue + Cyan + Purple

**Triadic Scheme**:
- Dominant color + two equidistant colors
- Example: Blue → Blue + Red + Yellow

### Step 3: Assign Roles

```
Background:  Lightest color (90-95% lightness) or darkest (5-10%)
Primary:     Dominant image color (medium saturation)
Secondary:   Supporting color (lower saturation than primary)
Accent:      Highest saturation, smallest usage (CTA, highlights)
Text:        High contrast with background (black/white)
```

### Color Extraction Algorithm

```python
def extract_palette_from_description(description):
    # Parse for color keywords
    colors_mentioned = extract_color_keywords(description)

    if not colors_mentioned:
        # No colors mentioned, use context
        return select_by_content_type(description)

    # Get dominant color
    dominant = colors_mentioned[0]

    # Determine mood (bright, muted, dark)
    mood = analyze_mood(description)

    # Generate palette based on dominant + mood
    if mood == "vibrant":
        return create_triadic_palette(dominant)
    elif mood == "calm":
        return create_monochromatic_palette(dominant)
    elif mood == "bold":
        return create_complementary_palette(dominant)
    else:
        return create_analogous_palette(dominant)
```

---

## Color Combination Rules

### Contrast Ratios

**WCAG Compliance**:
- AAA (ideal): 7:1 for text, 4.5:1 for large text
- AA (minimum): 4.5:1 for text, 3:1 for large text

**Testing combinations**:
```
White (#FFFFFF) on Black (#000000)     = 21:1 ✓
Black (#000000) on White (#FFFFFF)     = 21:1 ✓
Dark Gray (#333) on White              = 12.6:1 ✓
Light Gray (#CCC) on White             = 1.6:1 ✗
Blue (#0066CC) on White                = 4.7:1 ✓
```

### 60-30-10 Distribution

**60%**: Background/Dominant
- Large areas, canvas background
- Low saturation, high lightness (or very dark for dark mode)

**30%**: Secondary/Content Areas
- Images, content blocks, secondary elements
- Medium saturation and lightness

**10%**: Accent/CTA
- Buttons, highlights, important text
- High saturation, attention-grabbing

### Color Temperature

**Warm colors** (Red, Orange, Yellow):
- Energetic, exciting, appetite-stimulating
- Advance visually (appear closer)
- Use for CTAs and emphasis

**Cool colors** (Blue, Green, Purple):
- Calming, trustworthy, professional
- Recede visually (appear farther)
- Use for backgrounds and large areas

**Mixing warm + cool**:
- Creates dynamic tension
- Cool background + warm CTA (common)
- Warm background + cool content (less common)

### Saturation Harmony

**High saturation** (80-100%):
- Energetic, youthful, bold
- Use sparingly (accent only)
- Maximum 10-15% of canvas

**Medium saturation** (40-60%):
- Balanced, professional
- Primary and secondary colors
- Most of colored content

**Low saturation** (10-30%):
- Subtle, sophisticated, calming
- Backgrounds, neutral areas
- 60-70% of canvas

### Lightness Distribution

**For light backgrounds** (90%+ lightness):
```
Background:  95% lightness
Content:     60-80% lightness
Text/Icons:  10-20% lightness (dark)
Accent:      40-60% lightness (medium)
```

**For dark backgrounds** (10% lightness):
```
Background:  5-10% lightness
Content:     20-40% lightness
Text/Icons:  90-100% lightness (light)
Accent:      60-80% lightness (bright)
```

---

## Gradient Techniques

### Linear Gradients

**Two-color gradients**:
```svg
<linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
</linearGradient>
```

**Directions**:
- Top to bottom: 0°, 180° (most common)
- Diagonal: 45°, 135° (dynamic)
- Left to right: 90°, 270° (horizontal)

**Color stops**:
- Two stops: Simple blend
- Three stops: Middle accent
- Multiple stops: Complex, use sparingly

### Radial Gradients

**Center focus**:
```svg
<radialGradient id="grad2" cx="50%" cy="50%" r="50%">
  <stop offset="0%" style="stop-color:#fff;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#4facfe;stop-opacity:1" />
</radialGradient>
```

**Use cases**:
- Spotlight effect
- Vignette (dark edges)
- Depth illusion

### Gradient Best Practices

1. **Same hue**: Most harmonious (blue to light blue)
2. **Analogous hues**: Smooth transition (blue to purple)
3. **Complementary hues**: Bold (blue to orange) - use carefully
4. **Opacity gradients**: Fade to transparent for overlays

**Avoid**:
- Muddy middle (happens with complementary colors)
- Too many color stops (>3)
- Gradients on text (readability issues)

---

## Overlay Strategies

### Text Over Images

**Dark overlay** (for light images):
```
Background: rgba(0, 0, 0, 0.4-0.6)
Text: White (#FFFFFF)
```

**Light overlay** (for dark images):
```
Background: rgba(255, 255, 255, 0.8-0.9)
Text: Black (#000000)
```

**Gradient overlay**:
```
Bottom: rgba(0, 0, 0, 0.7)
Top: rgba(0, 0, 0, 0)
Text: White, positioned in dark area
```

**Colored overlay**:
```
Background: rgba(Primary Color, 0.85)
Text: White or contrasting color
Effect: Duotone, branded look
```

### Scrim Technique

Gradual overlay for text readability:
```
Image: Full brightness
Scrim: Linear gradient from
       rgba(0,0,0,0) to rgba(0,0,0,0.8)
Text: Positioned in dark scrim area
```

---

## Special Color Effects

### Duotone

Convert image to two colors for artistic effect:

**Classic duotone**:
- Shadows: Dark blue (#2E3A59)
- Highlights: Orange (#FF9A56)

**High contrast**:
- Shadows: Black (#000000)
- Highlights: Cyan (#00FFFF)

**Vintage**:
- Shadows: Sepia (#704214)
- Highlights: Cream (#F4E4C1)

### Color Filters

**Brightness**: -20% to +20%
**Contrast**: -10% to +20%
**Saturation**: -30% to +30%
**Hue Rotation**: Shift entire palette (use sparingly)

---

## Accessibility Considerations

### Color Blindness

**Don't rely on color alone**:
- Use text labels in addition to color coding
- Use patterns or shapes alongside color
- Ensure sufficient contrast regardless of hue

**Safe color combinations**:
- Blue + Orange (most accessible contrast)
- Blue + Yellow
- Black + White (always safe)

**Avoid**:
- Red + Green (common color blindness)
- Low contrast pastels

### High Contrast Mode

Design should work with:
- Inverted colors
- Grayscale
- Increased contrast

**Test**: Convert to grayscale - does hierarchy remain clear?

---

## Seasonal & Trend Colors

### Seasonal Palettes

**Spring**:
- Pastels: Soft pink, mint green, lavender, butter yellow
- Fresh, light, optimistic

**Summer**:
- Bright: Coral, turquoise, sunshine yellow, hot pink
- Energetic, vibrant, warm

**Fall**:
- Rich: Burnt orange, burgundy, mustard, forest green
- Cozy, warm, grounding

**Winter**:
- Cool: Navy, ice blue, silver, deep purple
- Crisp, elegant, festive

### Current Trends (2024-2025)

- **Digital Lavender**: #B0A7D5
- **Viva Magenta**: #BE3455 (Pantone 2023)
- **Peach Fuzz**: #FFBE98 (Pantone 2024)
- **Dopamine Brights**: Saturated, joyful colors
- **Neo Mint**: #88D4AB
- **Barely There**: Ultra-pale neutrals

**Use trends carefully**: Timeless > trendy for most ads

---

## Color Psychology Quick Reference

| Color | Associations | Use Cases |
|-------|-------------|-----------|
| Red | Energy, passion, urgency | Sales, food, alerts |
| Orange | Enthusiasm, creativity | CTAs, friendly brands |
| Yellow | Optimism, warmth, caution | Highlights, attention |
| Green | Nature, growth, money | Eco, health, finance |
| Blue | Trust, calm, professional | Corporate, tech |
| Purple | Luxury, creativity, wisdom | Premium, beauty |
| Pink | Feminine, playful, sweet | Beauty, youth, fun |
| Brown | Earthy, reliable, rustic | Organic, traditional |
| Black | Luxury, power, sophistication | High-end, modern |
| White | Purity, simplicity, clean | Minimal, medical |
| Gray | Neutral, professional | Corporate, tech |

---

## Implementation Checklist

When assigning colors:

- [ ] Palette matches template type and mood
- [ ] Background provides sufficient contrast for text
- [ ] CTA has highest visual prominence (color + contrast)
- [ ] 60-30-10 rule applied
- [ ] Text contrast meets WCAG AA minimum (4.5:1)
- [ ] Colors work together (harmonious, not clashing)
- [ ] Accent color used sparingly (<15% of canvas)
- [ ] No color-only information encoding
- [ ] Tested in grayscale (hierarchy remains clear)
