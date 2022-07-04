# Python Intro I Assignments
Submit a PR for each assignment.

# Ex. 1 Hello World
Create a Python function named `hello_world` that accepts a string 
that represents the number of times the following message is 
printed on the console: `Hello World from Python!`.  This function
must convert the string to an integer and must use a for loop to 
print the message to the console.

Usage: 
```python
hello_world("3")
```

Output:
```
Hello World from Python!
Hello World from Python!
Hello World from Python!
```

# Ex. 2 Array to String
Create a Python function named `array_to_string` that accepts an array of `ints` and returns a string. 
The function must use a for loop and must cast the `ints` to `strings`.

Usage:
```python
array = [1, 2, 3]
result = array_to_string(array)
print(result)
```

Output:
```
1 2 3
```

# Ex. 3 Add Numbers
Create a Python function named `add_numbers` that accepts an array of numeric types and returns the sum of 
them as a float value. The function must use a for loop and must cast the numbers to `floats`.

Usage:
```python
array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)
```

Output:
```
3.1
```

# Ex. 4 Count Words
Create a Python function named `count_words` that counts the number of words that has been entered by the user.
The function must be able to handle any number of spaces between words.

Usage:
```python
sentence = input("Enter sentence: ")
num_words = count_words(sentence)
print(num_words)
```

Example Output #1:
```
Enter sentence: This is a test
Number of Words: 4
```

Example Output #2:
```
Enter sentence: This  is   a    test
Number of Words: 4
```

Example Output #3:
```
Enter sentence: Hello   there
Number of Words: 2
```

# Ex. 5 Replace Period
Create a Python function named `replace_period` that accepts two inputs:
- A string that represents a sentence
- The punctuation character that will replace the period in the sentence

Usage
```python
sentence = "Test.  This is a test.  Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)

```
Ouput:
```
Test!  This is a test!  Testing!
```


# Ex. 6

# Ex. 7 Calculate Total
Create a Python function named `calc_total` that accepts an array of ints and a string that represents the sales tax.
Formatting currency in Python is accomplished in the following manner:

```python
number = 1.00
dollar_number = "${:,.2f}".format(number)
```

[String slicing](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3) might help you convert "10%" to a `float` value.

Usage:
```python
array = [2.00, 4.00, 4.00]
tax = "10%"
result = calc_total(array, tax)
print(result)
```

Ouput:
```
$11.00
```

# Ex. 8

# Ex. 9

# Ex. 10

# Ex. 11

# Ex. 12

# Ex. 13

# Ex. 14

# Ex. 15
