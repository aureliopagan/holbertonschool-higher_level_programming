#!/usr/bin/env python3
"""Shape classes for geometry calculations."""

from math import pi

class Shape:
    """Base shape class with required methods."""
    def area(self):
        """Calculate shape area - must be implemented by subclasses."""
        raise NotImplementedError

    def perimeter(self):
        """Calculate shape perimeter - must be implemented by subclasses."""
        raise NotImplementedError


class Circle(Shape):
    """Circle shape defined by its radius."""
    def __init__(self, radius: float):
        """Initialize with given radius."""
        self.radius = radius

    def area(self) -> float:
        """Return circle area using pi*r²."""
        return pi * abs(self.radius) ** 2

    def perimeter(self) -> float:
        """Return circle circumference using 2*pi*r."""
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""
    def __init__(self, width: float, height: float):
        """Initialize with given width and height."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return rectangle area (width * height)."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return rectangle perimeter 2*(width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape_obj):
    """Print area and perimeter of any shape object."""
    print(f"Area: {shape_obj.area()}")
    print(f"Perimeter: {shape_obj.perimeter()}")
