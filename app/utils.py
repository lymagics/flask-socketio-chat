import os


def generate_basedir():
    """Generate base directory path."""
    return os.path.abspath(os.path.dirname(__file__))
