# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

def digital_root(n):
    # ...
    bomb = False
    total = n
    dig = []
    while bomb != True:
        dig = [[int(x) for x in str(total)]]
        total = 0
        for y in dig:
            total += sum(y)
        dig.clear()
        dig = [[int(x) for x in str(total)]]
        if total < 10:
            bomb = True
    return total

if __name__ == "__main__":
    n = 942
    output = digital_root(n)
    print(output)