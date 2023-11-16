import execjs

# Define some JavaScript code
js_code = """
function setReqVals(){
    var req = new GlideRecord('sc_req_item');
    req.get(current.sys_id);
    req.short_description = current.cat_item.getDisplayValue() + " " +   current.variables.requested_for.name;
    req.update();
}
"""

# Use execjs to execute the JavaScript code
ctx = execjs.compile(js_code)

# Get the result of the JavaScript code
result = ctx.eval('result')

# Print the result
print(result)