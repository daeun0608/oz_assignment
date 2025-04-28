pi=3.141592

#반지름
def number_input():
    value=input('반지름 : ')
    return float(value)

#둘레
def get_circum(r):
    return 2*pi*r

#넓이
def get_circle(r):
    return pi*r*r