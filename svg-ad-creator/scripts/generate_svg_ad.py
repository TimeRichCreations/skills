#!/usr/bin/env python3
"""
SVG Ad Generator - Main script for creating SVG advertisements

This script generates complete SVG ad code based on template selection,
design principles, and user specifications.

Usage:
    generate_svg_ad.py --template <template_name> --size <width>x<height> --output <filename>

Features:
    - 8 pre-defined template archetypes
    - Responsive layouts for different canvas sizes
    - Randomized variations for uniqueness
    - Design principle compliance
"""

import sys
import hashlib
import random
from typing import Dict, List, Tuple, Optional
from color_utils import ColorPalette, extract_dominant_color, get_contrast_ratio
from layout_engine import LayoutEngine, GridConfig


class SVGAdGenerator:
    """Main class for generating SVG advertisements"""

    def __init__(self, width: int = 1080, height: int = 1080, seed: Optional[str] = None):
        self.width = width
        self.height = height
        self.padding = max(40, int(min(width, height) * 0.06))
        self.content_width = width - (2 * self.padding)
        self.content_height = height - (2 * self.padding)

        # Initialize random seed for reproducibility
        if seed:
            self.seed = int(hashlib.md5(seed.encode()).hexdigest(), 16) % (2**32)
            random.seed(self.seed)

        self.layout_engine = LayoutEngine(width, height, self.padding)

    def generate_svg_header(self) -> str:
        """Generate SVG opening tag and definitions"""
        return f'''<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Gradients -->
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:rgb(102,126,234);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(118,75,162);stop-opacity:1" />
    </linearGradient>

    <!-- Shadows -->
    <filter id="shadow-sm" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.1"/>
    </filter>
    <filter id="shadow-md" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.15"/>
    </filter>
    <filter id="shadow-lg" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-opacity="0.2"/>
    </filter>
  </defs>
'''

    def generate_svg_footer(self) -> str:
        """Generate SVG closing tag"""
        return '</svg>'

    def create_text_element(
        self,
        text: str,
        x: int,
        y: int,
        font_size: int,
        font_weight: int = 400,
        color: str = "#000000",
        font_family: str = "Inter, sans-serif",
        anchor: str = "start",
        max_width: Optional[int] = None
    ) -> str:
        """Create an SVG text element with proper formatting"""

        # Handle text wrapping if max_width specified
        if max_width:
            lines = self._wrap_text(text, font_size, max_width)
            line_height = font_size * 1.5
            text_elements = []
            for i, line in enumerate(lines):
                line_y = y + (i * line_height)
                text_elements.append(
                    f'  <text x="{x}" y="{line_y}" font-family="{font_family}" '
                    f'font-size="{font_size}" font-weight="{font_weight}" '
                    f'fill="{color}" text-anchor="{anchor}">{self._escape_xml(line)}</text>'
                )
            return '\n'.join(text_elements)
        else:
            return (
                f'  <text x="{x}" y="{y}" font-family="{font_family}" '
                f'font-size="{font_size}" font-weight="{font_weight}" '
                f'fill="{color}" text-anchor="{anchor}">{self._escape_xml(text)}</text>'
            )

    def create_rect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        fill: str = "#FFFFFF",
        stroke: Optional[str] = None,
        stroke_width: int = 0,
        rx: int = 0,
        opacity: float = 1.0,
        shadow: Optional[str] = None
    ) -> str:
        """Create an SVG rectangle element"""
        attrs = [
            f'x="{x}"',
            f'y="{y}"',
            f'width="{width}"',
            f'height="{height}"',
            f'fill="{fill}"'
        ]

        if rx > 0:
            attrs.append(f'rx="{rx}"')
        if stroke:
            attrs.append(f'stroke="{stroke}"')
            attrs.append(f'stroke-width="{stroke_width}"')
        if opacity < 1.0:
            attrs.append(f'opacity="{opacity}"')
        if shadow:
            attrs.append(f'filter="url(#{shadow})"')

        return f'  <rect {" ".join(attrs)} />'

    def create_circle(
        self,
        cx: int,
        cy: int,
        r: int,
        fill: str = "#FFFFFF",
        stroke: Optional[str] = None,
        stroke_width: int = 0,
        opacity: float = 1.0
    ) -> str:
        """Create an SVG circle element"""
        attrs = [
            f'cx="{cx}"',
            f'cy="{cy}"',
            f'r="{r}"',
            f'fill="{fill}"'
        ]

        if stroke:
            attrs.append(f'stroke="{stroke}"')
            attrs.append(f'stroke-width="{stroke_width}"')
        if opacity < 1.0:
            attrs.append(f'opacity="{opacity}"')

        return f'  <circle {" ".join(attrs)} />'

    def create_image_placeholder(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        label: str = "Image",
        bg_color: str = "#E5E5E5",
        rx: int = 0
    ) -> str:
        """Create an image placeholder with label"""
        elements = []

        # Background rectangle
        elements.append(self.create_rect(x, y, width, height, bg_color, rx=rx))

        # Center label
        text_x = x + width // 2
        text_y = y + height // 2
        elements.append(
            self.create_text_element(
                label,
                text_x,
                text_y,
                int(min(width, height) * 0.15),
                600,
                "#999999",
                anchor="middle"
            )
        )

        return '\n'.join(elements)

    def create_cta_button(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        bg_color: str,
        text_color: str,
        font_size: int = 18
    ) -> str:
        """Create a call-to-action button"""
        elements = []

        # Button background with rounded corners
        elements.append(
            self.create_rect(x, y, width, height, bg_color, rx=8, shadow="shadow-md")
        )

        # Button text (centered)
        text_x = x + width // 2
        text_y = y + height // 2 + font_size // 3
        elements.append(
            self.create_text_element(
                text,
                text_x,
                text_y,
                font_size,
                700,
                text_color,
                anchor="middle"
            )
        )

        return '\n'.join(elements)

    def _wrap_text(self, text: str, font_size: int, max_width: int) -> List[str]:
        """Wrap text to fit within max_width (approximate)"""
        # Rough approximation: average char width = font_size * 0.6
        chars_per_line = int(max_width / (font_size * 0.6))
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            word_length = len(word) + 1  # +1 for space
            if current_length + word_length <= chars_per_line:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def _escape_xml(self, text: str) -> str:
        """Escape XML special characters"""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;')
                   .replace("'", '&apos;'))

    # Template Generation Methods

    def generate_product_hero(
        self,
        product_name: str,
        description: str,
        cta_text: str,
        palette: ColorPalette,
        brand_text: str = ""
    ) -> str:
        """Generate Product Hero template"""
        elements = [self.generate_svg_header()]

        # Background
        elements.append(self.create_rect(0, 0, self.width, self.height, palette.background))

        # Brand/Logo at top
        if brand_text:
            elements.append(
                self.create_text_element(
                    brand_text,
                    self.padding,
                    self.padding + 32,
                    24,
                    600,
                    palette.text_dark
                )
            )

        # Product image placeholder (center, 60% of height)
        img_height = int(self.height * 0.6)
        img_width = int(img_height * 0.8)
        img_x = (self.width - img_width) // 2
        img_y = self.padding + (80 if brand_text else 40)

        elements.append(
            self.create_image_placeholder(
                img_x, img_y, img_width, img_height, "Product", palette.secondary, rx=16
            )
        )

        # Product name
        name_y = img_y + img_height + 48
        elements.append(
            self.create_text_element(
                product_name,
                self.width // 2,
                name_y,
                44,
                700,
                palette.primary,
                anchor="middle"
            )
        )

        # Description
        desc_y = name_y + 56
        elements.append(
            self.create_text_element(
                description,
                self.width // 2,
                desc_y,
                18,
                400,
                palette.text_dark,
                anchor="middle",
                max_width=self.content_width - 100
            )
        )

        # CTA Button
        btn_width = 240
        btn_height = 56
        btn_x = (self.width - btn_width) // 2
        btn_y = self.height - self.padding - btn_height - 40

        elements.append(
            self.create_cta_button(
                btn_x, btn_y, btn_width, btn_height,
                cta_text, palette.accent, palette.text_light
            )
        )

        elements.append(self.generate_svg_footer())
        return '\n'.join(elements)

    def generate_text_heavy_promo(
        self,
        main_text: str,
        subtext: str,
        details: str,
        cta_text: str,
        palette: ColorPalette,
        discount: str = ""
    ) -> str:
        """Generate Text-Heavy Promo template"""
        elements = [self.generate_svg_header()]

        # Background
        elements.append(self.create_rect(0, 0, self.width, self.height, palette.background))

        # Large discount badge (if provided)
        if discount:
            badge_size = 280
            badge_x = (self.width - badge_size) // 2
            badge_y = self.padding + 80

            # Circle badge
            elements.append(
                self.create_circle(
                    badge_x + badge_size // 2,
                    badge_y + badge_size // 2,
                    badge_size // 2,
                    palette.accent,
                    shadow="shadow-lg"
                )
            )

            # Discount text
            elements.append(
                self.create_text_element(
                    discount,
                    self.width // 2,
                    badge_y + badge_size // 2 + 30,
                    72,
                    900,
                    palette.text_light,
                    anchor="middle"
                )
            )

            main_text_y = badge_y + badge_size + 64
        else:
            main_text_y = self.padding + 120

        # Main message
        elements.append(
            self.create_text_element(
                main_text,
                self.width // 2,
                main_text_y,
                48,
                800,
                palette.primary,
                anchor="middle",
                max_width=self.content_width
            )
        )

        # Subtext
        elements.append(
            self.create_text_element(
                subtext,
                self.width // 2,
                main_text_y + 80,
                32,
                600,
                palette.primary,
                anchor="middle",
                max_width=self.content_width
            )
        )

        # Details
        elements.append(
            self.create_text_element(
                details,
                self.width // 2,
                main_text_y + 160,
                18,
                400,
                palette.text_dark,
                anchor="middle",
                max_width=self.content_width - 100
            )
        )

        # CTA Button
        btn_width = 280
        btn_height = 64
        btn_x = (self.width - btn_width) // 2
        btn_y = self.height - self.padding - btn_height - 40

        elements.append(
            self.create_cta_button(
                btn_x, btn_y, btn_width, btn_height,
                cta_text, palette.primary, palette.text_light, 20
            )
        )

        elements.append(self.generate_svg_footer())
        return '\n'.join(elements)

    def generate_multi_product_grid(
        self,
        header_text: str,
        num_images: int,
        cta_text: str,
        palette: ColorPalette
    ) -> str:
        """Generate Multi-Product Grid template"""
        elements = [self.generate_svg_header()]

        # Background
        elements.append(self.create_rect(0, 0, self.width, self.height, palette.background))

        # Header
        header_height = int(self.height * 0.15)
        elements.append(
            self.create_text_element(
                header_text,
                self.width // 2,
                self.padding + 48,
                40,
                700,
                palette.primary,
                anchor="middle"
            )
        )

        # Calculate grid layout
        grid_config = self.layout_engine.calculate_grid(num_images)
        grid_top = self.padding + header_height
        grid_height = self.height - grid_top - self.padding - 100  # Leave space for CTA

        gutter = int(self.width * 0.02)

        # Generate grid cells
        for i in range(num_images):
            row, col = divmod(i, grid_config.cols)
            if row >= grid_config.rows:
                break

            cell_width = (self.content_width - (grid_config.cols - 1) * gutter) // grid_config.cols
            cell_height = (grid_height - (grid_config.rows - 1) * gutter) // grid_config.rows

            x = self.padding + col * (cell_width + gutter)
            y = grid_top + row * (cell_height + gutter)

            elements.append(
                self.create_image_placeholder(
                    x, y, cell_width, cell_height,
                    f"Product {i+1}", palette.secondary, rx=12
                )
            )

        # CTA Button
        btn_width = 240
        btn_height = 56
        btn_x = (self.width - btn_width) // 2
        btn_y = self.height - self.padding - btn_height - 24

        elements.append(
            self.create_cta_button(
                btn_x, btn_y, btn_width, btn_height,
                cta_text, palette.accent, palette.text_light
            )
        )

        elements.append(self.generate_svg_footer())
        return '\n'.join(elements)

    def generate_minimalist_luxury(
        self,
        product_name: str,
        tagline: str,
        palette: ColorPalette
    ) -> str:
        """Generate Minimalist Luxury template"""
        elements = [self.generate_svg_header()]

        # Background
        elements.append(self.create_rect(0, 0, self.width, self.height, palette.background))

        # Product image (smaller, centered, lots of negative space)
        img_size = int(min(self.width, self.height) * 0.35)
        img_x = (self.width - img_size) // 2
        img_y = (self.height - img_size) // 2 - 60

        elements.append(
            self.create_image_placeholder(
                img_x, img_y, img_size, img_size,
                "Product", palette.secondary, rx=8
            )
        )

        # Product name (below image)
        elements.append(
            self.create_text_element(
                product_name,
                self.width // 2,
                img_y + img_size + 64,
                32,
                400,
                palette.primary,
                anchor="middle"
            )
        )

        # Tagline (subtle, below name)
        if tagline:
            elements.append(
                self.create_text_element(
                    tagline,
                    self.width // 2,
                    img_y + img_size + 104,
                    16,
                    300,
                    palette.text_dark,
                    anchor="middle"
                )
            )

        elements.append(self.generate_svg_footer())
        return '\n'.join(elements)


def main():
    """Example usage"""
    # Example: Product Hero
    generator = SVGAdGenerator(1080, 1080, seed="example-seed")
    palette = ColorPalette(
        background="#F0F8FF",
        primary="#2E5266",
        secondary="#6E8898",
        accent="#D3AF37",
        text_dark="#1A1A1A",
        text_light="#FFFFFF"
    )

    svg = generator.generate_product_hero(
        "Premium Headphones",
        "Experience crystal-clear audio with our latest wireless technology",
        "Shop Now",
        palette,
        "AudioBrand"
    )

    print(svg)


if __name__ == "__main__":
    main()
