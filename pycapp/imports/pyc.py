# This file runs code used by many parts of PyC. Without it, PyC would break.

def hang(errorCode):
  appRunning = False
  print(f"""ERROR!
PyC ran into an issue that it couldn't recover from. Please check the documentation for more information.
Error code: {errorCode}""")
