
def  my_test_func():
    print("Beginning")
    baz = "hello"
    print("Inside  program")

my_test_func()


def circle(center_x: float, center_y: float, radius=10.0, *extra_radii, **attributes):
    
    foo = []

    for rad in (radius,) + extra_radii:
        foo.append((rad, attributes))

    return foo

value=circle(4.5,5,7,12,20,(1,2))

print (value)
