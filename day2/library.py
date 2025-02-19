def upper(func):
    def wrapper():
        return func().upper()
    return wrapper()
def addd(func):
    def wrapper():
        return func()+'!!!!'
    return wrapper()
@upper
@addd
def func():
    return "sachin awasthi..."
print(func())