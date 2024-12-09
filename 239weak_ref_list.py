import weakref 

class MyList(list):
    pass


a_list = MyList(range(10))
print(a_list, type(a_list))

print(weakref.ref(a_list))
print(weakref.ref(a_list))
a_list = [1,2]
print(weakref.ref(a_list)) # TYPEERROR




