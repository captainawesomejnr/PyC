def hang(errorCode):
  appRunning = False
  print(f"""ERROR!
PyC ran into an issue that it couldn't recover from. Please check the documentation for more information.
Error code: {errorCode}""")
version = "v0.0-b1"
appRunning = True
print(f"""PyC REPL (Read, Evaluate, Print, Loop)
Version {version}
""")
while appRunning:
  prompt = input("> ")
  prompt = prompt.lower()
  if prompt == "quit":
    appRunning = False
    print("Goodbye")
  elif prompt == "pyc hang":
    hang(userInit)
