def display(name, *subject):
    print(name,"likes to read")
    for sub in subject:
        print(sub)

display('Ajay','Physics','Chemistry')
display('Ajay','Physics','Chemistry','Maths')
display('Ajay')