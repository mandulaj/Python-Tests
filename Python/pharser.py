
def checksyntax(exp):
    ok = True
    if not exp.count("(") == exp.count(")"):
        ok = False
    return ok

print (checksyntax(""))

def phars(exp):
    if checksyntax(exp):
        pass
    else:
        return "Syntax"
