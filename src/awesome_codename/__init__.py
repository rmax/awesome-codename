import random


from .data import load

__author__ = 'Rolando (Max) Espinoza'
__email__ = 'rolando at rmax.io'
__version__ = '1.0.0'


ADJECTIVES = load('adjectives')
NOUNS = load('nouns')


def generate_codename():
    """Generate a random codename."""
    return ' '.join([random.choice(ADJECTIVES), random.choice(NOUNS)])
