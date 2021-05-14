# __main__.py

from configparser import ConfigParser
from importlib import resources  # Python 3.7+
import sys

def main():
    # https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
    """Interact with themap APIs to create awesome maps"""
    # Read configurations from config file
    cfg = ConfigParser()
    # cfg.read_string(resources.read_text("layer", "config.txt"))
    cfg.read_string(resources.read_text(__package__, "config.txt"))
    url = cfg.get("api", "endpoint")

    # If an article ID is given, show the article
    if len(sys.argv) > 1:
        if sys.argv[1] == 'map':
            print("This sub package contains all the map api related functions.")
        if sys.argv[1] == 'layer':
            print("This sub package contains all the layer api related functions.")
        if sys.argv[1] == 'common':
            print("This sub package contains various common functions useful accross sub packages.")
        if sys.argv[1] == 'extras':
            print("This sub package contains helpful functions which are not part of core functionality but still good to have them!")
        
    # If no ID is given, show a list of all articles
    else:
        print("This package contains 4 sub packages to accomplish different functions :")
        print("     1. map")
        print("     2. layer")
        print("     3. common")
        print("     4. extras")
        print(" To know more about individual sub package, you can run package with respective sub package. e.g. python -m themap common")

if __name__ == "__main__":
    main()