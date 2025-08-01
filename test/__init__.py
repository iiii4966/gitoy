"""
Test package initialization.
Sets up import paths for accessing src modules during testing.
"""
import sys
from pathlib import Path

# Add src directory to Python path for imports
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path)) 