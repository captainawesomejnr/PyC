# This file runs code used by many parts of PyC, including fatal error handling and reading/writing flags. Without it, PyC would break.

def hang(errorCode):
  appRunning = False
  print(f"""ERROR!
PyC ran into an issue that it couldn't recover from. Please check the documentation for more information.
Error code: {errorCode}""")

def readFlag(filename):
  import os
  import ast

  FLAG_DIR = "flag"
    path = os.path.join(FLAG_DIR, f"{filename}.pcfg")
    if not os.path.exists(path):
        raise FileNotFoundError(f"{filename}.pcfg does not exist.")
    with open(path, "r") as f:
        content = f.read()
    return ast.literal_eval(content)

def writeFlag(filename, key, value):
    import os
    import ast
    FLAG_DIR = "flag"
    path = os.path.join(FLAG_DIR, f"{filename}.pcfg")

    # Load existing flags
    if os.path.exists(path):
        with open(path, "r") as f:
            flags = ast.literal_eval(f.read())
    else:
        flags = {}

    # Update the specific flag
    flags[key] = value

    # Write back to file
    with open(path, "w") as f:
        f.write(str(flags))
