# Password Strength Checker

A python tool that analyzes password strength using regex rules, entropy calculation and crack time estimation.

## Project Structure

password-strength-checker/
│
├── main.py
├── password_checker.py
├── common_passwords.txt
└── README.md

## Features

- Length validation
- Uppercase detection
- Lowercase detection
- Digit detection
- Special character detection
- Common password dictionary
- Feedback suggestions

## Password Entropy

This tool estimates password strength using entropy, a concept from information theory.

Entropy measures how unpredictable a password is.

Formula used:

Entropy = password_length × log₂(character_set_size)

Character sets include:
- lowercase letters (26)
- uppercase letters (26)
- digits (10)
- symbols (~32)

Higher entropy means the password is harder to guess.

## Crack Time Estimation

The tool estimates how long it would take an attacker to brute-force the password.

Assumption:
1 billion guesses per second.

Estimated crack time = (2^entropy) / guesses_per_second

This gives an approximate time required for a brute-force attack.

## Example Usage

Password Strength Checker
Type 'exit' to quit

Enter your password: Hello@123

Score: 5 / 5
Password Strength: Strong
Entropy: 59.02
Estimated crack time: 18.3 years

## Future Improvements

- Detect repeated characters (aaa, 111)
- Detect sequential patterns (1234, abcd)
- GUI password strength meter
- Web-based password checker

## Installation

git clone <repo>
cd password-strength-checker
python main.py

