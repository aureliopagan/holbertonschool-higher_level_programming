#!/usr/bin/env python3
"""Demonstrating mixins with a Dragon class."""

class SwimMixin:
    """Provides swimming capability to any class."""
    
    def swim(self):
        """Print swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability to any class."""
    
    def fly(self):
        """Print flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Mythical creature combining swimming and flying abilities."""
    
    def roar(self):
        """Print dragon's roar."""
        print("The dragon roars!")
