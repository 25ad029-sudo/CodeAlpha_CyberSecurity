print("=== PHISHING AWARENESS TRAINING ===")

score = 0

print("\nQ1. Which is a sign of a phishing email?")
print("1. Official email address")
print("2. Urgent request for personal information")
print("3. Proper grammar")

ans = int(input("Enter your answer (1-3): "))

if ans == 2:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQ2. What should you do before clicking a link?")
print("1. Click immediately")
print("2. Ignore it")
print("3. Check the URL carefully")

ans = int(input("Enter your answer (1-3): "))

if ans == 3:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nQ3. Phishing attackers often try to:")
print("1. Steal sensitive information")
print("2. Improve your computer")
print("3. Update your software")

ans = int(input("Enter your answer (1-3): "))

if ans == 1:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n=== RESULT ===")
print("Your Score:", score, "/ 3")

if score == 3:
    print("Excellent! You are aware of phishing attacks.")
elif score >= 2:
    print("Good! But stay alert.")
else:
    print("You need more phishing awareness training.")

print("\nTips to Avoid Phishing:")
print("- Never share passwords.")
print("- Verify email senders.")
print("- Check website URLs carefully.")
print("- Avoid suspicious links and attachments.")