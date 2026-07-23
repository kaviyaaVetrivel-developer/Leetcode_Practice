## DAY 1:
    PROBLEM: Two Sum
    SOLUTION EXPLANATION:

        - Use the first loop to select one element from the array.
        - Use the second loop to compare it with every element that comes after it.
        - If the sum of the two elements is equal to the target, return their indices.

-------------------------------------------------------------------------------------------

## DAY 2:
    PROBLEM: Reverse String
    SOLUTION EXPLANATION:

        - used Python's built-in `reverse()` function method to reverse the characters in the list.

-------------------------------------------------------------------------------------------

## DAY 3:
    PROBLEM: Fizz Buzz
    SOLUTION EXPLANATION:

        - Create an empty list `arr` to store the results.
        - Use a `for` loop to iterate through all numbers from `1` to `n`.
        - Use an `if` statement to check if the current number is divisible by both `3` and `5`. If true, append `"FizzBuzz"` to the list.
        - Use an `elif` statement to check if the current number is divisible only by `3`. If true, append `"Fizz"` to the list.
        - Use another `elif` statement to check if the current number is divisible only by `5`. If true, append `"Buzz"` to the list.
        - Use an `else` statement to convert the current number to a string and append it to the list.
        - After all numbers have been processed, return the final list containing the required output.

 ------------------------------------------------------------------------------------------

## DAY 3:
    PROBLEM: Palindrome Number
    SOLUTION EXPLANATION:

        - Store the original number in a variable.
        - Use a `while` loop to reverse the number digit by digit.
        - Build the reversed number using the formula `palindrome_num = palindrome_num * 10 + digit`.
        - Use an `if` statement to compare the original number with the reversed number.
        - Return `True` if both are equal; otherwise, return `False`.

-------------------------------------------------------------------------------------------        