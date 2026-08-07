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

## DAY 5:
    PROBLEM: Reverse Interger
    SOLUTION EXPLANATION:

        - Check if the number is negative and convert it to a positive number for easier processing.
        - Use a `while` loop to reverse the number digit by digit.
        - Build the reversed number using the formula `reverse = reverse * 10 + digit`.
        - Restore the negative sign if the original number was negative.
        - Use an `if` statement to check whether the reversed number is within the 32-bit signed integer range.
        - Return `0` if the reversed number is out of range; otherwise, return the reversed number.

----------------------------------------------------------------------------------------------------

## DAY 6:
    PROBLEM: Happy numbers
    SOLUTION EXPLANATIOn:

        - Create an empty `set` to store the numbers that have already been seen.
        - Use a `while` loop to repeat the process until the number becomes `1`.
        - Use an `if` statement to check if the current number is already in the set. If it is, return `False` because a cycle is detected.
        - Add the current number to the set.
        - Calculate the sum of the squares of each digit and update the value of `n`.
        - Return `True` if the number becomes `1`.

----------------------------------------------------------------------------------------------------

## DAY 7:
    PROBLEM: To lower case
    SOLUTION EXPLANATIOn:

        - Use the built-in `lower()` method to convert all uppercase letters in the string to lowercase.
        - Return the converted string.

----------------------------------------------------------------------------------------------------

## DAY 8:
    PROBLEM: Remove element 
    SOLUTION EXPLANATION:

        - Initialize a variable `k` to keep track of the position for the next valid element.
        - Use a `for` loop to traverse the array.
        - Use an `if` statement to check if the current element is not equal to `val`.
        - If the element is valid, place it at index `k` and increment `k`.
        - Return `k`, which represents the number of elements remaining after removing all occurrences of `val`.

----------------------------------------------------------------------------------------------------

## DAY 9:
    PROBLEM:Defanging an IP Address
    SOLUTION EXPLANATION:

        - Use the built-in `replace()` method to replace every `"."` with `"[.]"`.
        - Return the modified IP address.

----------------------------------------------------------------------------------------------------

## DAY 10:
    PROBLEM:Concatenation-of-array
    SOLUTION EXPLANATION:

        - Use the `+` operator to concatenate the array with itself.
        - Return the new array containing two copies of the original array.

----------------------------------------------------------------------------------------------------

## DAY 11:
    PROBLEM: Squares of a Sorted Array
    SOLUTION EXPLANATION:

        - Use a generator expression to calculate the square of each element in the array.
        - Use the built-in `sorted()` function to sort the squared values in non-decreasing order.
        - Return the sorted array.

----------------------------------------------------------------------------------------------------

## DAY 12:
    PROBLEM: Find the difference
    SOLUTION EXPLANATION:

        - Use the `ord()` function to convert each character in both strings into its ASCII value.
        - Use the `sum()` function to calculate the total ASCII value of each string.
        - Find the difference between the two sums to get the ASCII value of the extra character.
        - Use the `chr()` function to convert the ASCII value back into the corresponding character.
        - Return the extra character.

----------------------------------------------------------------------------------------------------

## DAY 13:
    PROBLEM: Smallest Even Multiple
    SOLUTION EXPLANATION:
        - Use an `if-else` conditional expression to check whether the number is even.
        - If the number is even, return the number itself.
        - Otherwise, return the number multiplied by `2`, which is the smallest even multiple.

----------------------------------------------------------------------------------------------------

## DAY 14:

    PROBLEM: Intersection of Two Arrays
    SOLUTION EXPLANATION:
        - Convert both arrays into sets to remove duplicate elements.
        - Use the `&` operator to find the common elements between the two sets.
        - Convert the resulting set back into a list.
        - Return the list containing the intersection of the two arrays.

----------------------------------------------------------------------------------------------------

## DAY 14:

    PROBLEM: Add Two Integer
    SOLUTION EXPLANATION:
        - Use the `+` operator to add `num1` and `num2`.
        - Return the sum of the two numbers.

----------------------------------------------------------------------------------------------------