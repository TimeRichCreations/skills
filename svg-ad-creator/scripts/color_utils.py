#!/usr/bin/env python3
"""
Color Utilities - Color extraction, manipulation, and palette management

This module provides utilities for working with colors in SVG ad generation,
including palette selection, color extraction from descriptions, contrast
calculation, and color harmony generation.
"""

import re
import colorsys
from typing import List, Tuple, Optional, Dict
from dataclasses import dataclass


@dataclass
class ColorPalette:
    """Color palette with assigned roles"""
    background: str
    primary: str
    secondary: str
    accent: str
    text_dark: str
    text_light: str


# Pre-defined palettes from color_theory.md
PREDEFINED_PALETTES = {
    "ocean_breeze": ColorPalette(
        background="#F0F8FF",
        primary="#2E5266",
        secondary="#6E8898",
        accent="#D3AF37",
        text_dark="#1A1A1A",
        text_light="#FFFFFF"
    ),
    "sunset_vibes": ColorPalette(
        background="#FFF5EB",
        primary="#FF6B35",
        secondary="#F7931E",
        accent="#C1292E",
        text_dark="#2A2A2A",
        text_light="#FFFFFF"
    ),
    "forest_fresh": ColorPalette(
        background="#F4F7F5",
        primary="#2D6A4F",
        secondary="#52B788",
        accent="#95D5B2",
        text_dark="#1B4332",
        text_light="#FFFFFF"
    ),
    "midnight_luxury": ColorPalette(
        background="#1A1A1A",
        primary="#FFFFFF",
        secondary="#A0A0A0",
        accent="#D4AF37",
        text_dark="#FFFFFF",
        text_light="#E5E5E5"
    ),
    "berry_blast": ColorPalette(
        background="#FFF0F5",
        primary="#C9184A",
        secondary="#FF4D6D",
        accent="#FFB3C1",
        text_dark="#240115",
        text_light="#FFFFFF"
    ),
    "monochrome_modern": ColorPalette(
        background="#FFFFFF",
        primary="#000000",
        secondary="#6C757D",
        accent="#343A40",
        text_dark="#212529",
        text_light="#F8F9FA"
    ),
    "lavender_dreams": ColorPalette(
        background="#FAF9FF",
        primary="#7209B7",
        secondary="#B5A1D6",
        accent="#F72585",
        text_dark="#3C096C",
        text_light="#FFFFFF"
    ),
    "coral_reef": ColorPalette(
        background="#FDFBF7",
        primary="#FF6F61",
        secondary="#00B4D8",
        accent="#FFD23F",
        text_dark="#2B2D42",
        text_light="#FFFFFF"
    ),
    "earth_tones": ColorPalette(
        background="#FAF7F2",
        primary="#8B4513",
        secondary="#CD853F",
        accent="#DEB887",
        text_dark="#3E2723",
        text_light="#FFFFFF"
    ),
    "electric_neon": ColorPalette(
        background="#0A0E27",
        primary="#00F5FF",
        secondary="#7B2CBF",
        accent="#FF006E",
        text_dark="#00F5FF",
        text_light="#FFFFFF"
    ),
}


# Keyword to palette mapping
KEYWORD_TO_PALETTE = {
    # Luxury/Premium
    "luxury": "midnight_luxury",
    "premium": "midnight_luxury",
    "elegant": "midnight_luxury",
    "sophisticated": "monochrome_modern",

    # Sales/Promo
    "sale": "sunset_vibes",
    "discount": "sunset_vibes",
    "promo": "berry_blast",
    "deal": "sunset_vibes",

    # Natural/Organic
    "natural": "forest_fresh",
    "organic": "forest_fresh",
    "eco": "forest_fresh",
    "green": "forest_fresh",

    # Modern/Tech
    "modern": "ocean_breeze",
    "tech": "electric_neon",
    "digital": "electric_neon",
    "innovation": "ocean_breeze",

    # Calm/Wellness
    "calm": "lavender_dreams",
    "peaceful": "ocean_breeze",
    "wellness": "lavender_dreams",
    "spa": "lavender_dreams",

    # Energetic/Bold
    "bold": "electric_neon",
    "energetic": "coral_reef",
    "vibrant": "sunset_vibes",
    "dynamic": "berry_blast",

    # Professional/Corporate
    "professional": "ocean_breeze",
    "corporate": "ocean_breeze",
    "business": "monochrome_modern",

    # Fun/Playful
    "fun": "coral_reef",
    "playful": "berry_blast",
    "creative": "lavender_dreams",

    # Traditional
    "traditional": "earth_tones",
    "rustic": "earth_tones",
    "artisan": "earth_tones",
}


# Color name to hex mapping
COLOR_NAMES = {
    "red": "#FF0000",
    "orange": "#FF8C00",
    "yellow": "#FFD700",
    "green": "#32CD32",
    "blue": "#1E90FF",
    "purple": "#9370DB",
    "pink": "#FF69B4",
    "brown": "#8B4513",
    "black": "#000000",
    "white": "#FFFFFF",
    "gray": "#808080",
    "grey": "#808080",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "navy": "#000080",
    "teal": "#008080",
    "coral": "#FF7F50",
    "lavender": "#E6E6FA",
}


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Convert RGB tuple to hex color"""
    return '#%02x%02x%02x' % rgb


def rgb_to_hsl(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """Convert RGB to HSL"""
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s * 100, l * 100)


def hsl_to_rgb(hsl: Tuple[float, float, float]) -> Tuple[int, int, int]:
    """Convert HSL to RGB"""
    h, s, l = hsl[0] / 360.0, hsl[1] / 100.0, hsl[2] / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return (int(r * 255), int(g * 255), int(b * 255))


def get_luminance(hex_color: str) -> float:
    """Calculate relative luminance for WCAG contrast calculations"""
    rgb = hex_to_rgb(hex_color)

    # Convert to sRGB
    rgb_linear = []
    for val in rgb:
        val = val / 255.0
        if val <= 0.03928:
            rgb_linear.append(val / 12.92)
        else:
            rgb_linear.append(((val + 0.055) / 1.055) ** 2.4)

    # Calculate luminance
    return 0.2126 * rgb_linear[0] + 0.7152 * rgb_linear[1] + 0.0722 * rgb_linear[2]


def get_contrast_ratio(color1: str, color2: str) -> float:
    """Calculate WCAG contrast ratio between two colors"""
    lum1 = get_luminance(color1)
    lum2 = get_luminance(color2)

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)


def adjust_lightness(hex_color: str, amount: float) -> str:
    """Adjust color lightness by amount (-100 to 100)"""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(rgb)

    # Adjust lightness
    l = max(0, min(100, l + amount))

    rgb_new = hsl_to_rgb((h, s, l))
    return rgb_to_hex(rgb_new)


def adjust_saturation(hex_color: str, amount: float) -> str:
    """Adjust color saturation by amount (-100 to 100)"""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(rgb)

    # Adjust saturation
    s = max(0, min(100, s + amount))

    rgb_new = hsl_to_rgb((h, s, l))
    return rgb_to_hex(rgb_new)


def get_complementary_color(hex_color: str) -> str:
    """Get complementary color (opposite on color wheel)"""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(rgb)

    # Add 180 degrees to hue
    h_new = (h + 180) % 360

    rgb_new = hsl_to_rgb((h_new, s, l))
    return rgb_to_hex(rgb_new)


def get_analogous_colors(hex_color: str) -> List[str]:
    """Get analogous colors (adjacent on color wheel)"""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(rgb)

    # +/- 30 degrees
    h1 = (h + 30) % 360
    h2 = (h - 30) % 360

    rgb1 = hsl_to_rgb((h1, s, l))
    rgb2 = hsl_to_rgb((h2, s, l))

    return [rgb_to_hex(rgb1), rgb_to_hex(rgb2)]


def get_triadic_colors(hex_color: str) -> List[str]:
    """Get triadic colors (120 degrees apart)"""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(rgb)

    # +/- 120 degrees
    h1 = (h + 120) % 360
    h2 = (h + 240) % 360

    rgb1 = hsl_to_rgb((h1, s, l))
    rgb2 = hsl_to_rgb((h2, s, l))

    return [rgb_to_hex(rgb1), rgb_to_hex(rgb2)]


def extract_color_keywords(text: str) -> List[str]:
    """Extract color keywords from text description"""
    text_lower = text.lower()
    colors_found = []

    for color_name in COLOR_NAMES.keys():
        if re.search(r'\b' + color_name + r'\b', text_lower):
            colors_found.append(COLOR_NAMES[color_name])

    return colors_found


def extract_dominant_color(description: str) -> Optional[str]:
    """Extract dominant color from image description"""
    colors = extract_color_keywords(description)
    return colors[0] if colors else None


def create_monochromatic_palette(base_color: str) -> ColorPalette:
    """Create monochromatic palette from base color"""
    background = adjust_lightness(base_color, 40)
    primary = base_color
    secondary = adjust_lightness(base_color, 15)
    accent = adjust_saturation(base_color, 20)

    # Determine text colors based on lightness
    rgb = hex_to_rgb(base_color)
    _, _, l = rgb_to_hsl(rgb)

    if l > 50:
        text_dark = adjust_lightness(base_color, -60)
        text_light = "#FFFFFF"
    else:
        text_dark = "#FFFFFF"
        text_light = adjust_lightness(base_color, 60)

    return ColorPalette(
        background=background,
        primary=primary,
        secondary=secondary,
        accent=accent,
        text_dark=text_dark,
        text_light=text_light
    )


def create_complementary_palette(base_color: str) -> ColorPalette:
    """Create complementary palette from base color"""
    complementary = get_complementary_color(base_color)

    return ColorPalette(
        background=adjust_lightness(base_color, 45),
        primary=base_color,
        secondary=adjust_lightness(base_color, 20),
        accent=complementary,
        text_dark="#1A1A1A",
        text_light="#FFFFFF"
    )


def create_analogous_palette(base_color: str) -> ColorPalette:
    """Create analogous palette from base color"""
    analogous = get_analogous_colors(base_color)

    return ColorPalette(
        background=adjust_lightness(base_color, 40),
        primary=base_color,
        secondary=analogous[0],
        accent=analogous[1],
        text_dark="#1A1A1A",
        text_light="#FFFFFF"
    )


def create_triadic_palette(base_color: str) -> ColorPalette:
    """Create triadic palette from base color"""
    triadic = get_triadic_colors(base_color)

    return ColorPalette(
        background=adjust_lightness(base_color, 45),
        primary=base_color,
        secondary=triadic[0],
        accent=triadic[1],
        text_dark="#1A1A1A",
        text_light="#FFFFFF"
    )


def select_palette_by_keywords(prompt: str, template_type: str = "") -> ColorPalette:
    """Select appropriate palette based on keywords in prompt"""
    prompt_lower = prompt.lower()

    # Check for direct keyword matches
    for keyword, palette_name in KEYWORD_TO_PALETTE.items():
        if keyword in prompt_lower:
            return PREDEFINED_PALETTES[palette_name]

    # Template-based defaults
    template_defaults = {
        "product_hero": "ocean_breeze",
        "multi_product_grid": "monochrome_modern",
        "text_heavy_promo": "sunset_vibes",
        "lifestyle_story": "lavender_dreams",
        "minimalist_luxury": "midnight_luxury",
        "event_announcement": "ocean_breeze",
        "split_feature": "monochrome_modern",
        "magazine_layout": "monochrome_modern",
    }

    if template_type in template_defaults:
        return PREDEFINED_PALETTES[template_defaults[template_type]]

    # Default fallback
    return PREDEFINED_PALETTES["ocean_breeze"]


def select_palette_from_image_description(description: str, mood: str = "neutral") -> ColorPalette:
    """Select or generate palette based on image description"""
    # Try to extract dominant color
    dominant_color = extract_dominant_color(description)

    if dominant_color:
        # Generate palette based on mood
        if mood == "vibrant":
            return create_triadic_palette(dominant_color)
        elif mood == "calm":
            return create_monochromatic_palette(dominant_color)
        elif mood == "bold":
            return create_complementary_palette(dominant_color)
        else:
            return create_analogous_palette(dominant_color)

    # Fallback to keyword-based selection
    return select_palette_by_keywords(description)


def ensure_sufficient_contrast(text_color: str, bg_color: str, min_ratio: float = 4.5) -> str:
    """Adjust text color to ensure sufficient contrast with background"""
    current_ratio = get_contrast_ratio(text_color, bg_color)

    if current_ratio >= min_ratio:
        return text_color

    # Try adjusting lightness
    for adjustment in [20, -20, 40, -40, 60, -60]:
        adjusted = adjust_lightness(text_color, adjustment)
        if get_contrast_ratio(adjusted, bg_color) >= min_ratio:
            return adjusted

    # If still insufficient, use black or white
    if get_luminance(bg_color) > 0.5:
        return "#000000"
    else:
        return "#FFFFFF"


def main():
    """Example usage and testing"""
    # Test palette selection
    prompt = "luxury watch sale"
    palette = select_palette_by_keywords(prompt)
    print(f"Selected palette for '{prompt}':")
    print(f"  Background: {palette.background}")
    print(f"  Primary: {palette.primary}")
    print(f"  Accent: {palette.accent}")
    print()

    # Test color extraction
    description = "blue sky and green grass"
    colors = extract_color_keywords(description)
    print(f"Colors in '{description}': {colors}")
    print()

    # Test contrast ratio
    ratio = get_contrast_ratio("#FFFFFF", "#000000")
    print(f"Contrast ratio (white on black): {ratio:.2f}")


if __name__ == "__main__":
    main()
