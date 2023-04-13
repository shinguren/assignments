from re import S
from this import s


def update():
    global s
    s=20
    print(s)

s=10
print(s)
update()
print(s)