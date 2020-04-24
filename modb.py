foo = 'gsdajh'

print(__name__)# здесь будет main, а в mod_lib выведется modb
if __name__=='__main__':#из-за этого не будет работать в mod_lib но здесь будет работать
    print(foo)
    print('shdakh')