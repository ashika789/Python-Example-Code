# This program is designed to return the area and perimeter of a rectangle.
# Define the main function.
def main():
    rectfind()

def showPerimeter(l, w):
    perimeter = 2 * (l + w)
    print('Rectangle perimeter is', perimeter)

def showArea(l, w):
    area = (l * w)
    print('Rectangle area is', area)

def rectfind():
    l = int(input('Enter the length of the rectangle:'))
    w = int(input('Enter the width of the rectangle:'))

    showPerimeter(l,w)
    showArea(l,w)

main()
      