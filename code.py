# Shell program to select one of the code files
#MODE="default"
MODE="steamworkshop-example"

with open("code-"+MODE+".py") as f:
    exec(f.read())
