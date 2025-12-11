from imports import *
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
  elif prompt == "help":
    exec(help.replCmd())
  else:
    exec(prompt)
    
