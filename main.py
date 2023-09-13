from serialsearch import *

print(__name__)

def main():
    #set up local variables to store the list, first, size, and target
    a = []
    first = 0
    size = 0
    target = 0

    #prompt the user for the elements and input them into the list
    a = list(map(int,input("Enter seven numbers separated by a space:").split()))

    #prompt the user for the index at which the search will begin
    first = int(input("Enter the index at which the search will begin: "))

    #prompt the user for the number of elements to search
    size = int(input("Enter the size of the list that will be searched: "))

    #prompt the user for the target
    target = int(input("Enter the target value to search for: "))

    print('Target found at index ...', search(a, first, size, target))

if __name__ =="__main__":
    main()

