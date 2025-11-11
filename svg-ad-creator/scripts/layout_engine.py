#!/usr/bin/env python3
"""
Layout Engine - Grid calculation and layout management for SVG ads

This module provides utilities for calculating optimal layouts, grid configurations,
spacing, and element positioning based on design principles.
"""

from typing import Tuple, List, Optional
from dataclasses import dataclass


@dataclass
class GridConfig:
    """Grid configuration for multi-element layouts"""
    rows: int
    cols: int
    cell_width: int
    cell_height: int
    gutter: int


@dataclass
class BoundingBox:
    """Bounding box for positioned elements"""
    x: int
    y: int
    width: int
    height: int


class LayoutEngine:
    """Layout engine for calculating positions and dimensions"""

    def __init__(self, canvas_width: int, canvas_height: int, padding: int):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.padding = padding
        self.content_width = canvas_width - (2 * padding)
        self.content_height = canvas_height - (2 * padding)

        # 8-point grid system
        self.grid_unit = 8

    def snap_to_grid(self, value: int) -> int:
        """Snap value to 8-point grid"""
        return round(value / self.grid_unit) * self.grid_unit

    def calculate_grid(self, num_elements: int) -> GridConfig:
        """
        Calculate optimal grid configuration for N elements

        Logic:
        - 1 element: 1x1
        - 2 elements: 2x1 or 1x2 (based on canvas orientation)
        - 3 elements: 3x1 or 2+1 asymmetric
        - 4 elements: 2x2
        - 5-6 elements: 3x2 or 2x3
        - 7-9 elements: 3x3
        """
        is_horizontal = self.canvas_width > self.canvas_height

        if num_elements == 1:
            rows, cols = 1, 1
        elif num_elements == 2:
            rows, cols = (1, 2) if is_horizontal else (2, 1)
        elif num_elements == 3:
            rows, cols = (1, 3) if is_horizontal else (3, 1)
        elif num_elements == 4:
            rows, cols = 2, 2
        elif num_elements <= 6:
            rows, cols = (2, 3) if is_horizontal else (3, 2)
        elif num_elements <= 9:
            rows, cols = 3, 3
        elif num_elements <= 12:
            rows, cols = (3, 4) if is_horizontal else (4, 3)
        else:
            # For many elements, use square-ish grid
            cols = int(num_elements ** 0.5) + 1
            rows = (num_elements + cols - 1) // cols

        gutter = self.snap_to_grid(int(self.canvas_width * 0.02))

        # Calculate cell dimensions
        cell_width = (self.content_width - (cols - 1) * gutter) // cols
        cell_height = (self.content_height - (rows - 1) * gutter) // rows

        return GridConfig(
            rows=rows,
            cols=cols,
            cell_width=cell_width,
            cell_height=cell_height,
            gutter=gutter
        )

    def calculate_centered_box(
        self,
        width: int,
        height: int,
        vertical_offset: int = 0
    ) -> BoundingBox:
        """Calculate centered bounding box with optional vertical offset"""
        x = (self.canvas_width - width) // 2
        y = (self.canvas_height - height) // 2 + vertical_offset

        return BoundingBox(x=x, y=y, width=width, height=height)

    def calculate_aspect_fit(
        self,
        container_width: int,
        container_height: int,
        content_aspect: float
    ) -> Tuple[int, int]:
        """
        Calculate dimensions to fit content aspect ratio in container

        Args:
            container_width: Container width
            container_height: Container height
            content_aspect: Content aspect ratio (width/height)

        Returns:
            (width, height) that fits in container maintaining aspect ratio
        """
        container_aspect = container_width / container_height

        if content_aspect > container_aspect:
            # Content is wider - fit to width
            width = container_width
            height = int(width / content_aspect)
        else:
            # Content is taller - fit to height
            height = container_height
            width = int(height * content_aspect)

        return (width, height)

    def calculate_rule_of_thirds_points(self) -> List[Tuple[int, int]]:
        """Calculate rule of thirds intersection points"""
        third_x = self.canvas_width / 3
        third_y = self.canvas_height / 3

        points = [
            (int(third_x), int(third_y)),           # Top-left
            (int(2 * third_x), int(third_y)),       # Top-right
            (int(third_x), int(2 * third_y)),       # Bottom-left
            (int(2 * third_x), int(2 * third_y)),   # Bottom-right
        ]

        return points

    def calculate_text_max_width(
        self,
        alignment: str = "center",
        margin_percent: float = 10
    ) -> int:
        """
        Calculate maximum text width based on alignment and margins

        Args:
            alignment: 'left', 'center', or 'right'
            margin_percent: Margin percentage (0-100)

        Returns:
            Maximum text width in pixels
        """
        margin = int(self.content_width * (margin_percent / 100))

        if alignment == "center":
            return self.content_width - (2 * margin)
        else:
            return self.content_width - margin

    def calculate_button_size(
        self,
        text_length: int,
        size: str = "medium"
    ) -> Tuple[int, int]:
        """
        Calculate button dimensions based on text length and size

        Args:
            text_length: Number of characters in button text
            size: 'small', 'medium', or 'large'

        Returns:
            (width, height) in pixels
        """
        # Size presets
        presets = {
            "small": {"height": 44, "padding_h": 24, "font_size": 16},
            "medium": {"height": 56, "padding_h": 32, "font_size": 18},
            "large": {"height": 64, "padding_h": 40, "font_size": 20},
        }

        preset = presets.get(size, presets["medium"])

        # Approximate text width: chars * font_size * 0.6
        text_width = int(text_length * preset["font_size"] * 0.6)
        width = text_width + (2 * preset["padding_h"])

        # Snap to grid
        width = self.snap_to_grid(width)
        height = preset["height"]

        # Ensure minimum and maximum widths
        min_width = 120
        max_width = int(self.content_width * 0.8)

        width = max(min_width, min(width, max_width))

        return (width, height)

    def calculate_vertical_rhythm(
        self,
        base_size: int,
        num_lines: int,
        line_height: float = 1.5
    ) -> int:
        """
        Calculate vertical spacing based on typography rhythm

        Args:
            base_size: Base font size
            num_lines: Number of lines
            line_height: Line height multiplier

        Returns:
            Total height in pixels
        """
        return self.snap_to_grid(int(base_size * line_height * num_lines))

    def calculate_image_dimensions(
        self,
        percentage: float,
        aspect_ratio: Optional[float] = None
    ) -> Tuple[int, int]:
        """
        Calculate image dimensions as percentage of canvas

        Args:
            percentage: Percentage of canvas (0-100)
            aspect_ratio: Optional aspect ratio (width/height)

        Returns:
            (width, height) in pixels
        """
        if aspect_ratio:
            # Calculate based on aspect ratio
            height = int(self.canvas_height * (percentage / 100))
            width = int(height * aspect_ratio)

            # Ensure it fits in canvas
            if width > self.content_width:
                width = self.content_width
                height = int(width / aspect_ratio)
        else:
            # Square by default
            size = int(min(self.canvas_width, self.canvas_height) * (percentage / 100))
            width = height = size

        return (width, height)

    def distribute_vertically(
        self,
        elements: List[int],
        total_height: Optional[int] = None,
        alignment: str = "space-between"
    ) -> List[int]:
        """
        Calculate vertical positions for elements

        Args:
            elements: List of element heights
            total_height: Total height to distribute in (default: content_height)
            alignment: 'space-between', 'space-around', or 'center'

        Returns:
            List of Y positions for each element
        """
        if total_height is None:
            total_height = self.content_height

        total_element_height = sum(elements)
        remaining_space = total_height - total_element_height

        positions = []
        current_y = self.padding

        if alignment == "space-between":
            if len(elements) > 1:
                gap = remaining_space / (len(elements) - 1)
            else:
                gap = 0

            for height in elements:
                positions.append(int(current_y))
                current_y += height + gap

        elif alignment == "space-around":
            gap = remaining_space / (len(elements) + 1)
            current_y += gap

            for height in elements:
                positions.append(int(current_y))
                current_y += height + gap

        elif alignment == "center":
            current_y += remaining_space / 2

            for height in elements:
                positions.append(int(current_y))
                current_y += height

        return positions

    def calculate_split_layout(self) -> Tuple[BoundingBox, BoundingBox]:
        """
        Calculate 50/50 split layout (for Split Feature template)

        Returns:
            (left_box, right_box) bounding boxes
        """
        split_x = self.canvas_width // 2

        left_box = BoundingBox(
            x=0,
            y=0,
            width=split_x,
            height=self.canvas_height
        )

        right_box = BoundingBox(
            x=split_x,
            y=0,
            width=split_x,
            height=self.canvas_height
        )

        return (left_box, right_box)

    def calculate_magazine_layout(
        self,
        num_images: int
    ) -> List[BoundingBox]:
        """
        Calculate magazine-style layout with varied image sizes

        Args:
            num_images: Number of images to position

        Returns:
            List of bounding boxes for images
        """
        boxes = []

        # Magazine layout patterns for different image counts
        if num_images == 1:
            # Large hero image
            boxes.append(BoundingBox(
                x=self.padding,
                y=self.padding + 100,
                width=self.content_width,
                height=int(self.content_height * 0.6)
            ))

        elif num_images == 2:
            # One large, one small
            boxes.append(BoundingBox(
                x=self.padding,
                y=self.padding + 80,
                width=int(self.content_width * 0.6),
                height=int(self.content_height * 0.5)
            ))
            boxes.append(BoundingBox(
                x=self.padding + int(self.content_width * 0.65),
                y=self.padding + 80,
                width=int(self.content_width * 0.35),
                height=int(self.content_height * 0.3)
            ))

        elif num_images == 3:
            # L-shaped layout
            boxes.append(BoundingBox(
                x=self.padding,
                y=self.padding + 80,
                width=int(self.content_width * 0.5),
                height=int(self.content_height * 0.5)
            ))
            boxes.append(BoundingBox(
                x=self.padding + int(self.content_width * 0.55),
                y=self.padding + 80,
                width=int(self.content_width * 0.45),
                height=int(self.content_height * 0.25)
            ))
            boxes.append(BoundingBox(
                x=self.padding + int(self.content_width * 0.55),
                y=self.padding + 80 + int(self.content_height * 0.28),
                width=int(self.content_width * 0.45),
                height=int(self.content_height * 0.22)
            ))

        elif num_images >= 4:
            # Mixed grid
            grid_config = self.calculate_grid(num_images)
            for i in range(min(num_images, 4)):
                row, col = divmod(i, 2)
                boxes.append(BoundingBox(
                    x=self.padding + col * (grid_config.cell_width + grid_config.gutter),
                    y=self.padding + 80 + row * (grid_config.cell_height + grid_config.gutter),
                    width=grid_config.cell_width,
                    height=grid_config.cell_height
                ))

        return boxes

    def calculate_golden_ratio_position(
        self,
        element_width: int,
        element_height: int,
        orientation: str = "right"
    ) -> BoundingBox:
        """
        Position element using golden ratio (1.618)

        Args:
            element_width: Element width
            element_height: Element height
            orientation: 'left', 'right', 'top', 'bottom'

        Returns:
            Bounding box positioned at golden ratio point
        """
        golden_ratio = 1.618

        if orientation == "right":
            x = int(self.canvas_width / golden_ratio) - (element_width // 2)
            y = (self.canvas_height - element_height) // 2
        elif orientation == "left":
            x = int(self.canvas_width - (self.canvas_width / golden_ratio)) - (element_width // 2)
            y = (self.canvas_height - element_height) // 2
        elif orientation == "top":
            x = (self.canvas_width - element_width) // 2
            y = int(self.canvas_height / golden_ratio) - (element_height // 2)
        elif orientation == "bottom":
            x = (self.canvas_width - element_width) // 2
            y = int(self.canvas_height - (self.canvas_height / golden_ratio)) - (element_height // 2)
        else:
            # Default center
            x = (self.canvas_width - element_width) // 2
            y = (self.canvas_height - element_height) // 2

        return BoundingBox(x=x, y=y, width=element_width, height=element_height)


def main():
    """Example usage and testing"""
    # Create layout engine for 1080x1080 canvas
    engine = LayoutEngine(1080, 1080, 64)

    # Test grid calculation
    print("Grid configurations:")
    for n in [1, 2, 3, 4, 6, 9]:
        grid = engine.calculate_grid(n)
        print(f"  {n} elements: {grid.rows}x{grid.cols} grid")

    print()

    # Test rule of thirds
    points = engine.calculate_rule_of_thirds_points()
    print("Rule of thirds points:")
    for i, point in enumerate(points):
        print(f"  Point {i+1}: {point}")

    print()

    # Test button sizing
    button = engine.calculate_button_size(12, "medium")
    print(f"Button size for 'Shop Now': {button}")


if __name__ == "__main__":
    main()
