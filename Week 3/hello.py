def hello(name):
    if len(name) > 5:
        res = "nonsense"
    else: 
        res = "hello " + name
    print(res)
    return res