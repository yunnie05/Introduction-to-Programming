def division(a,b):
    try:
        res= a/b
    except ZeroDivisionError:
        return "Error: Division by 0!"
    except TypeError:
        return "Error: Unsupported type(s) for division!"
    else:
        return f"{a}/{b} = {res}"
        
