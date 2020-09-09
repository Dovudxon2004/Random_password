import random
import string
a=list(string.ascii_uppercase)
b=list(string.ascii_lowercase)
c=list(range(10))
c=list(map(str, c))
easy_list=["".join((random.choices(b, k=random.randint(2,3)))), "".join((random.choices(c, k=random.randint(1,2))))]
medium_list=["".join((random.choices(c, k=random.randint(3,4)))), "".join((random.choices(b, k=random.randint(2,3)))), "".join((random.choices(c, k=random.randint(1,2))))]
hard_list=["".join((random.choices(a, k=random.randint(2,3)))), "".join((random.choices(b, k=random.randint(1,2)))), "".join((random.choices(c, k=random.randint(1,2)))), "".join((random.choices(c, k=random.randint(3,4))))]
ask= int(input('1-easy, 2-medium, 3-hard'))
if ask==1:
    print("".join(random.choices(easy_list, k= random.randint(2,3))))
elif ask==2:
    print("".join(random.choices(medium_list, k= random.randint(3,4))))
elif ask==3:
    print("".join(random.choices(hard_list, k= random.randint(4,5))))
