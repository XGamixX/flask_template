import os
import sys
import py_compile

def check_syntax(directory):
    errors = False
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    py_compile.compile(filepath, doraise=True)
                    print(f"✓ Syntax OK: {filepath}")
                except py_compile.PyCompileError as e:
                    print(f"✗ Syntax ERROR in {filepath}:\n{e}", file=sys.stderr)
                    errors = True
    return errors

if __name__ == "__main__":
    if check_syntax("."):
        sys.exit(1)  # Fail the script if any syntax errors are found
    sys.exit(0)  # Success if no errors