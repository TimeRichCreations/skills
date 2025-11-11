# SVG Ad Template Specifications

This document defines the 8 core template archetypes for SVG ad generation. Each template has specific use cases, layout rules, and design constraints.

## Template Selection Matrix

| Template | Best For | Image Count | Text Priority | Complexity |
|----------|----------|-------------|---------------|------------|
| Product Hero | Single product showcase | 1 | Medium | Low |
| Multi-Product Grid | Multiple items, catalog | 2-6 | Low | Medium |
| Text-Heavy Promo | Sales, discounts, announcements | 0-1 | High | Low |
| Lifestyle Story | Brand storytelling, emotion | 1-2 | Medium | High |
| Minimalist Luxury | Premium products, elegance | 1 | Low | Medium |
| Event Announcement | Concerts, webinars, launches | 0-2 | High | Medium |
| Split Feature | Compare, dual message | 2 | Medium | Medium |
| Magazine Layout | Editorial, content-rich | 2-4 | High | High |

## Standard Canvas Sizes

Default size: **1080x1080px** (Instagram square)

Supported variations:
- Square: 1080x1080px (Instagram, Facebook)
- Story: 1080x1920px (Instagram/Facebook Stories)
- Wide: 1200x628px (Facebook/Twitter link preview)
- Banner: 728x90px (Web banner)

---

## Template 1: Product Hero

**Use Case**: Single product showcase with emphasis on the item itself

**Trigger Keywords**: "product", "showcase", "feature", "highlight", "hero"

**Layout Structure**:
```
┌─────────────────────────┐
│   [Brand/Logo]          │
│                         │
│   ┌───────────────┐     │
│   │               │     │
│   │  PRODUCT IMG  │     │
│   │               │     │
│   └───────────────┘     │
│                         │
│   [Product Name]        │
│   [Short Description]   │
│   [CTA Button]          │
└─────────────────────────┘
```

**Design Specifications**:
- Image size: 60-70% of canvas height
- Image position: Center or slightly above center
- Background: Solid or subtle gradient
- Typography: Bold product name (36-48pt), body text (16-20pt)
- CTA: Bottom third, prominent button or text
- Padding: 5-8% of canvas dimension

**Color Strategy**:
- Extract dominant color from product image
- Use complementary color for CTA
- High contrast background (light or dark based on image)

**Variations**:
1. Floating product (with shadow)
2. Product in geometric frame
3. Product with decorative shapes

---

## Template 2: Multi-Product Grid

**Use Case**: Catalog, collection showcase, multiple items

**Trigger Keywords**: "products", "collection", "catalog", "multiple", "grid", "gallery"

**Layout Structure**:
```
┌─────────────────────────┐
│   [Header Text]         │
├─────────┬───────────────┤
│  IMG 1  │    IMG 2      │
├─────────┼───────────────┤
│  IMG 3  │    IMG 4      │
└─────────┴───────────────┘
│   [CTA]                 │
└─────────────────────────┘
```

**Design Specifications**:
- Grid configurations: 2x2, 3x1, 2x3, 3x2 (based on image count)
- Image sizes: Equal or asymmetric emphasis
- Gutter: 2-3% of canvas width
- Header: Top 15-20% of canvas
- Typography: Bold header (32-44pt), minimal or no descriptions
- Background: Usually solid color or subtle pattern

**Grid Logic**:
- 2 images: 2x1 (side by side) or 1x2 (stacked)
- 3 images: 3x1 or 2+1 asymmetric
- 4 images: 2x2
- 5-6 images: 3x2 or 2x3

**Color Strategy**:
- Unified color scheme across all images
- Monochromatic or analogous palette
- Consistent border treatment

---

## Template 3: Text-Heavy Promo

**Use Case**: Sales, discounts, announcements, text-focused messaging

**Trigger Keywords**: "sale", "discount", "offer", "promo", "announcement", "deal"

**Layout Structure**:
```
┌─────────────────────────┐
│                         │
│   ┌─────────────────┐   │
│   │  LARGE NUMBER   │   │
│   │      50%        │   │
│   │      OFF        │   │
│   └─────────────────┘   │
│                         │
│   Main Message Text     │
│   Supporting Details    │
│   [Small Image/Icon]    │
│   [CTA]                 │
└─────────────────────────┘
```

**Design Specifications**:
- Primary text: 50-80pt, ultra-bold
- Secondary text: 24-36pt
- Body text: 14-18pt
- Image (optional): 20-30% of canvas, supporting role
- Typography hierarchy: Critical - use size/weight/color
- Geometric shapes: Circles, badges, banners for emphasis

**Color Strategy**:
- High contrast (e.g., white text on dark bg)
- Accent color for key numbers/CTAs
- Bold, energetic palettes

**Variations**:
1. Centered proclamation
2. Diagonal emphasis
3. Badge/stamp style
4. Banner ribbon style

---

## Template 4: Lifestyle Story

**Use Case**: Brand storytelling, emotional connection, aspirational content

**Trigger Keywords**: "lifestyle", "story", "inspiration", "moment", "experience"

**Layout Structure**:
```
┌─────────────────────────┐
│ ┌─────────────────────┐ │
│ │                     │ │
│ │   LIFESTYLE IMAGE   │ │
│ │   (Full Bleed or    │ │
│ │    Large Focus)     │ │
│ │                     │ │
│ └─────────────────────┘ │
│                         │
│   [Overlay Text Box]    │
│   Emotive Copy          │
│   [Subtle CTA]          │
└─────────────────────────┘
```

**Design Specifications**:
- Image treatment: Full bleed or 80%+ of canvas
- Text overlay: Semi-transparent box or gradient overlay
- Typography: Elegant, readable serif or modern sans
- Mood: Aspirational, calm, inviting
- Negative space: Strategic for text readability

**Color Strategy**:
- Extract from lifestyle image
- Muted, sophisticated palettes
- Overlay colors: Black/white with opacity

**Variations**:
1. Full bleed with bottom text overlay
2. Framed image with external text
3. Duotone image effect

---

## Template 5: Minimalist Luxury

**Use Case**: Premium products, high-end brands, elegance

**Trigger Keywords**: "luxury", "premium", "elegant", "minimalist", "sophisticated"

**Layout Structure**:
```
┌─────────────────────────┐
│                         │
│                         │
│       [PRODUCT]         │
│                         │
│                         │
│   Product Name          │
│                         │
│                         │
└─────────────────────────┘
```

**Design Specifications**:
- Maximum negative space: 50-70% empty
- Centered composition
- Minimal text: Product name only or + one line
- Typography: Refined serif or geometric sans (24-36pt)
- No borders, minimal decoration
- Subtle shadows or elevation

**Color Strategy**:
- Monochromatic or limited palette (2-3 colors max)
- Neutral backgrounds: White, cream, black, grey
- Metallic accents: Gold, silver, bronze tones

**Variations**:
1. Pure centered
2. Golden ratio placement
3. Asymmetric balance

---

## Template 6: Event Announcement

**Use Case**: Concerts, webinars, launches, conferences, parties

**Trigger Keywords**: "event", "concert", "webinar", "launch", "conference", "party", "show"

**Layout Structure**:
```
┌─────────────────────────┐
│   EVENT NAME            │
│   ════════════          │
│                         │
│   [Key Visual/Img]      │
│                         │
│   DATE & TIME           │
│   LOCATION/PLATFORM     │
│                         │
│   [Additional Details]  │
│   [Register/RSVP CTA]   │
└─────────────────────────┘
```

**Design Specifications**:
- Event name: Top, large (40-56pt), bold
- Date/time: Prominent, easily scannable (28-36pt)
- Location: Clear, with icon if possible
- Key visual: 30-50% of canvas
- Decorative elements: Lines, shapes, borders
- CTA: Strong, action-oriented

**Color Strategy**:
- Energetic, attention-grabbing
- Event type matching (corporate = professional, party = vibrant)
- High readability for date/time

**Variations**:
1. Poster style (bold graphics)
2. Ticket style (perforated look)
3. Clean corporate (professional)

---

## Template 7: Split Feature

**Use Case**: Comparisons, dual messages, before/after, two products

**Trigger Keywords**: "compare", "vs", "choose", "options", "before after", "both"

**Layout Structure**:
```
┌────────────┬────────────┐
│            │            │
│   IMAGE 1  │  IMAGE 2   │
│            │            │
├────────────┼────────────┤
│  Feature A │ Feature B  │
│            │            │
│  [Detail]  │ [Detail]   │
└────────────┴────────────┘
```

**Design Specifications**:
- Perfect vertical split: 50/50
- Mirrored or contrasting design
- Central divider line or no line
- Balanced typography on both sides
- Equal weight to both sides

**Color Strategy**:
- Complementary colors for each side
- Shared accent color for unity
- Or mirrored monochrome

**Variations**:
1. Contrasting colors (blue vs orange)
2. Light vs dark split
3. Gradient transition

---

## Template 8: Magazine Layout

**Use Case**: Editorial content, content-rich ads, storytelling with multiple elements

**Trigger Keywords**: "editorial", "magazine", "article", "content", "feature story"

**Layout Structure**:
```
┌─────────────────────────┐
│ ┌──────┐  HEADLINE      │
│ │ IMG1 │  Subheadline   │
│ └──────┘                │
├─────────────────────────┤
│  Body text in columns   │
│  with visual flow       │
│  ┌─────┐  continuing    │
│  │IMG2 │  around images │
│  └─────┘  naturally     │
│                         │
│  [Pull Quote or CTA]    │
└─────────────────────────┘
```

**Design Specifications**:
- Complex grid system
- Multiple text blocks
- 2-4 images integrated into layout
- Typography variation: Headlines, subheads, body
- Strong visual hierarchy
- Whitespace management critical

**Color Strategy**:
- Editorial palette: Black text, selective color accents
- Image-driven color scheme
- Professional, readable

---

## Responsive Considerations

When adapting templates to different canvas sizes:

**Story (Vertical)**:
- Stack elements vertically
- Increase text size proportionally
- Reduce horizontal padding

**Wide (Horizontal)**:
- Horizontal layouts preferred
- Side-by-side elements
- Watch text wrapping

**Banner**:
- Single row layout
- Minimal text
- Clear CTA

## Selection Priority Logic

1. **Explicit user request** (e.g., "use minimalist style") → Direct template match
2. **Image count** → Narrow to appropriate templates
3. **Keyword analysis** → Best semantic match
4. **Tone detection** → Final selection
5. **Default** → Product Hero (1 image) or Multi-Product Grid (2+ images)
