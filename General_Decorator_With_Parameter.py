def fun_arg(*args_out, **kwargs_out):
    def func(functionName):
        def func_in(*args, **kwargs):
            print("-----记录日志-----")
            if 'heihei' in args_out:
                print('heihei!')
            ret = functionName(*args, **kwargs)
            return ret
        return func_in
    return func

@fun_arg()
def test():
    print("----test----")
    return "haha"

@fun_arg('heihei')
def test2():
    print("----test2---")

@fun_arg('haha')
def test3(a):
    print("-----test3--a=%d--"%a)

ret = test()
print("test return value is %s"%ret)

a = test2()
print("test2 return value is %s"%a)


test3(11)