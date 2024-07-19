def is_palindrome(n):
    """
    Checks if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    """
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest

# Save the result to the file
with open("102-result", "w") as f:
    f.write(str(largest_palindrome_product()))
