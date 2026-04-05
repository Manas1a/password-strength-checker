from password_checker import check_password_strength
from password_checker import calculate_entropy
from password_checker import estimate_crack_time
print("Password Strength Checker\nType 'exit' to quit")
while True:
    password = input("\nEnter your password:")
    if(password.lower() == "exit"): 
        print("Exiting program...")
        break

    score,strength,feedback = check_password_strength(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    print("\nScore:",score,"/5")
    print("Password Strength:",strength)
    if len(feedback)>0:
        print("\nSuggestions:")
        for x in feedback:
            print("-",x)
    print("Entropy: ",entropy)
    print("Estimated crack time: ",crack_time,"years");