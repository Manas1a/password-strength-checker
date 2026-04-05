import re
import math
weak_passwords = []
with open("common_passwords.txt", "r") as file:
    for line in file:
        weak_passwords.append(line.strip())
def check_password_strength(password):
    score = 0
    feedback =[]
    
    if len(password)>=8:
        score+=1
    else:
        feedback.append("Password should be at least 8 characters long")
    if re.search("[A-Z]",password):
        score+=1
    else:
        feedback.append("Add at least one uppercase letter")
    if re.search("[a-z]",password):
        score+=1
    else:
        feedback.append("Add at least one lowercase letter")
    if re.search("\d",password):
        score+=1
    else:
        feedback.append("Add atleast one digit")
    if re.search("[^A-Za-z0-9]",password):
        score+=1
    else:
        feedback.append("Add at least one special character")
    if password in weak_passwords:
            score = 0
            feedback.append("This is a very common password")
    if score<=2:
        strength = "Weak"
    elif score<=4:
        strength = "Medium"
    elif score==5:
        strength = "Strong"

    return score, strength,feedback
def calculate_entropy(password):
    charset_size = 0
    if re.search("[a-z]",password):
        charset_size+=26
    if re.search("[A-Z]",password):
        charset_size+=26
    if re.search("\d",password):
        charset_size+=10
    if re.search("[^a-zA-Z0-9]",password):
        charset_size+=32
    if charset_size == 0: 
        return 0
    entropy = len(password) * math.log2(charset_size)
    return round(entropy,2)

def estimate_crack_time(entropy):
    guesses_per_second = 1000000000
    combinations = 2**entropy
    seconds = combinations/guesses_per_second
    years = seconds / (60*60*24*365)
    return round(years,2)