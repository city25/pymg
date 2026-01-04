import sys
import os

# When executed directly, ensure the src directory is on sys.path
if __package__ is None:
    here = os.path.dirname(__file__)
    sys.path.append(os.path.abspath(os.path.join(here, "..")))
    sys.path.append(os.path.abspath(os.path.join(here, "..", "..")))

from pymg.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
