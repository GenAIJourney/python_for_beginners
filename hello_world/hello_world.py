def print_hello_world():
    if __name__=="__main__":
        print("I am from main within the package")
    else:
        print("hello world from package")

if __name__=="__main__":
    print("I am from main")
    print_hello_world()