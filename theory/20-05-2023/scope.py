def function_1():
    inner_scope = 101
    print(inner_scope)


# function_1()
print(inner_scope)



















def function_2():
    global a
    for i in range(10):
        a = 102
        print( i)
    print('inner', a)

function_2()

print('outer', a)







def function_3():
    inner_scope = 103

    def function_inner():
        print(inner_scope)

    function_inner()


function_3()







def function_4():
    inner_scope = 104

    # BEGIN
    def function_inner():
        print(inner_scope)
    # END

    return function_inner


my_magic_function = function_4()
my_magic_function()







outer_scope = 105
def function_5():
    print(outer_scope)

function_5()










outer_scope = 106

def function_6():
    outer_scope = 1066
    # outer_scope += 1
    print('inner',outer_scope)

function_6()
print('outer', outer_scope)



def function_7(arg):
    arg *= 10
    print('inner', arg)




outer_scope = 107
function_7(outer_scope)
print('out', outer_scope)







outer_scope = {"a": 100, "b": 200}

def function_8(variable):
    variable['a'] = 300
    print('inside', variable)

function_8(outer_scope)
print('outside', outer_scope)

