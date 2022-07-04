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

# Ex. 6 Slice It
Create a Python function named `slice_it` that accepts an array `strings` and returns the first two letters of every 
word.

[String slicing](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)

Usage:
```python
array = ["this", "is", "another", "test"]
r = slice_it(array)
print(r)
```

Ouput:
```
thisante
```

# Ex. 7 Calculate Total
Create a Python function named `calc_total` that accepts an array of ints and a string that represents the sales tax.
Formatting currency in Python is accomplished in the following manner:

Currency example:
```python
number = 1.00
dollar_number = "${:,.2f}".format(number)
print(number)
```

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

# Ex. 8 Temp Converter
Create two Python functions:
- `c_to_f` : Converts from Celsius to Fahrenheit
- `f_to_c` : Converts from Fahrenheit to Celsius

These functions must use a Python [F-String](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/) to return the following output:

Usage:
```
print(f_to_c(22))
print(c_to_f(-6))
```

```
22 degrees Fahrenheit is -6 degrees Celsius.
-6 degrees Celsius is 21 degress Fahrenheit.
```


# Ex. 9 Vowel Counter
Create a Python function named `vowel_counter` that accepts a sentence and returns the number of vowels (forget
about "y").  Use a Python F-String in this function.

Usage:
```
sentence = "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)
```

Ouput:
```
Number of vowels: 4
```


# Ex. 10

# Ex. 11

# Ex. 12

# Ex. 13

# Ex. 14

# Ex. 15
