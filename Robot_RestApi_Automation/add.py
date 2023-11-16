import js2py

js = """
function add(x,y) {
return x+y;
}

const result = add(2,3)"""

cotext = js2py.EvalJs();
cotext.execute(js)
print(cotext.result)