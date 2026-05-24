class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor call")
def create_obj():
    print("Making object")
    obj = employee()
    print("Function end ; This is the end ")
    return obj
print("calling create object function")
obj = create_obj()
print("Programming end...")