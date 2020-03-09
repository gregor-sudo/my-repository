def main():
    # number = int(input("Enter a credit card number as a long integer: "))
    number = 4388576018402626 # Invalid
    # number = 4388576018410707  # Valid
    print("Testing card number:", number)
    if isValid(number):
        print(number, "is valid")
    else:
        print(number, "is invalid")


# Return true if the card number is valid
def isValid(number):
    return getSize(number) >= 13 and getSize(number) <= 16 and \
           (prefixMatched(number, 4) or prefixMatched(number, 5) or \
            prefixMatched(number, 6) or prefixMatched(number, 37)) and \
           (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0


# Step 2: Get the result.
def sumOfDoubleEvenPlace(number):
    result = 0

    number = number // 10  # Starting from the second digit from left
    while number != 0:
        result += getDigit((number % 10) * 2)
        number = number // 100  # Move to the next even place
    # print("Step 2:", result)
    return result


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    return number % 10 + (number // 10)


# Step 3: Return sum of odd place digits in number.
def sumOfOddPlace(number):
    result = 0

    while number != 0:
        result += number % 10
        number = number // 100  # Move two positions to the left
    # print("Step 3:", result)
    return result


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    # print("Here: ", number, ", ", getSize(d))
    return getPrefix(number, getSize(d)) == d


# Return the number of digits in d
def getSize(d):
    numberOfDigits = 0

    while d != 0:
        numberOfDigits += 1
        d = d // 10

    return numberOfDigits


# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    # print("GP I: ", number, ", ", k)
    result = number

    for i in range(getSize(number) - k):
        result //= 10
    # print("GP II Here: ", result)
    return result


main()
