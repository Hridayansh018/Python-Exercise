shapes= ("Triangle,Rectangle")
def calculate_area():
    while True:
        shape = input("Enter Shape(Triangle/Rectangle):- ")
        if shape not in shapes:
            print("Enter Valid Shape..!")
        elif shape == "Triangle" or "triangle":
            length = int(input("Enter Length :- "))
            height = int(input("Enter Height :- "))
            area = 1/2*length*height
            print("Area of triangle is:- ",area)
            break
        elif shape == "Rectangle" or "rectangle":
            length = int(input("Enter Length :- "))
            width = int(input("Enter Width :- "))
            area = length*width
            print("Area of rectangle is:- ",area)
            break
        else:
            break

def p_pat(n):
    for i in range (n):
        s = " "
        for j in range (i+1):
            s = s + "*"
        print(s)

calculate_area()