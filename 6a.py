def computepay(h,r):
    if h<=40:
        print("Pay", h*r)
    elif h>40:
        b=h-40
        c=r*1.5
        d=h-b
        print("Pay", d*r+b*c)
    return

h = input("Enter Hours:")
h = float(h)
r = input("Enter rate:")
r = float(r)

computepay(h,r)
