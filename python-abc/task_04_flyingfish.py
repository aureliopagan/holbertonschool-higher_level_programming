#!/usr/bin/env python3
"""Demonstrating multiple inheritance with aquatic and aerial creatures."""

class Fish:
    """Represents basic aquatic characteristics."""
    
    def swim(self):
        """Print basic swimming message."""
        print("The fish is swimming.")

    def habitat(self):
        """Describe aquatic habitat."""
        print("The fish lives in the water.")


class Bird:
    """Represents basic aerial characteristics."""
    
    def fly(self):
        """Print basic flying message."""
        print("The bird is flying.")

    def habitat(self):
        """Describe aerial habitat."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """Hybrid creature combining fish and bird traits."""
    
    def fly(self):
        """Override flying with fish-specific behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swimming with flying fish behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describe dual habitat of flying fish."""
        print("The flying fish lives both in water and the sky!")
