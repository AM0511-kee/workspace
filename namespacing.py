"""name spacing means unique name for every object in python"""
"""there are three types of name spacind they are build in name spacing,local namespacing,global name spacing"""
var=10
def name_spacing():
    global var
    var=var+1
    print(var)
    
name_spacing()

var="string"
def name_spacing():
    var=11
    print("inner scope variable=",var)
print("outter scope variable=",var)
name_spacing()

def outer_scope():
    var="kevin"
    def inner_scope():
        var="Aravind"
        print(var)
    inner_scope()
    print("outer_var:",var)
outer_scope()