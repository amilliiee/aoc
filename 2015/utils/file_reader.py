from pathlib import Path
import sys

def read_input(day, test=False, strip=True, remove_comments=True):
    # Read input file for given day
    day_str = f"day{day:02d}"
    filename = "test.txt" if test else "input.txt"
    filepath = Path(__file__).parent.parent / day_str / filename
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
            if remove_comments and test:
                # Remove comment lines for test files
                lines = []
                for line in content.splitlines():
                    clean_line = line.strip()
                    if clean_line and not clean_line.startswith('#'):
                        lines.append(clean_line)
                content = '\n'.join(lines)
            
            return content.strip() if strip else content
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        sys.exit(1)

def read_lines(day, test=False, strip=True, remove_comments=True):
    # Read input as list of lines
    content = read_input(day, test, strip, remove_comments)
    return content.splitlines() if content else []

def read_blocks(day, test=False):
    # Read input separated by blank lines
    content = read_input(day, test, strip=False)
    return content.strip().split('\n\n') if content else []