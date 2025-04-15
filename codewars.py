# Solution: Return if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Solution: Turn a number into a string
def number_to_string(num):
    return str(num)
  
# Solution: Count the number of vowels in a sentence
def get_count(sentence):
    count = 0
    for char in sentence:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
        else:
            continue
    return count