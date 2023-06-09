# Password-Generator
Question: 
Write a Python program that generates a random password with a length specified by the user. The password should include at least one uppercase letter, one lowercase letter, one digit, and one special character. The program should then print the generated password

Explanation:

1. The program first imports the random and string modules, which are used to generate random characters and work with strings, respectively.
2. The generate_password() function takes a single argument, length, which is the desired length of the password.
3. The function first defines four character sets: lowercase, uppercase, digits, and special_chars, which contain the allowed characters for the password.
4. The function then creates a list of characters for the password, ensuring that each of the required character types (lowercase, uppercase, digits, and special characters) is represented at least once.
5. After the required character types have been added to the password list, the function randomly chooses additional characters from all allowed character types until the desired password length is reached.
6. The list of password characters is then shuffled using the random.shuffle() function, and the password is returned as a string using the join() method.
7. The program prompts the user for the desired password length using the input() function and converts the input to an integer using the int() function.
8. The program then calls the generate_password() function with the desired length and stores the result in the password variable.
9. Finally, the program prints the generated password using the print() function.
