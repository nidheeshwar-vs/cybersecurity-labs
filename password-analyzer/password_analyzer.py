import re
import hashlib
import secrets
import string


def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8-12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


print("=== CYBERSECURITY PASSWORD ANALYZER ===")

password = input("Enter a password to analyze: ")

score, strength, feedback = analyze_password(password)

print(f"\nStrength: {strength}")
print(f"Score: {score}/6")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

print("\nSHA-256 demonstration hash:")
print(hash_password(password))

print("\nGenerated secure password:")
print(generate_password())
