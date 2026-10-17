import random

def generate_captcha():
    d=[2,3,4,5,6,7,8,9]
    ds=list(map(str,d))
    a=[c for c in 'ABCDEFGHJKLMNPQRSTUVWXYZ']
    li_d=random.choices(ds,k=2)
    li_a=random.choices(a,k=2)
    li_cap=li_a+li_d
    random.shuffle(li_cap)
    cap=' '.join(li_cap)
    return cap



def generate_password():
    d=list(range(10))
    ds=list(map(str,d))
    a=[chr(i) for i in range(65,91)]
    li_d=random.choices(ds,k=3)
    li_a=random.choices(a,k=3)
    li_pwd=li_a+li_d
    random.shuffle(li_pwd)
    pwd=''.join(li_pwd)
    return pwd

