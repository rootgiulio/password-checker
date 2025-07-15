import re

common_passwords = ['password', '123456', 'qwerty', 'admin', 'letmein', 'abc123']

def check_password_strength(password):
    feedback = []

    if len(password) < 15:
        feedback.append("❌ The password is too short (minimum of 15 characters).")
    if not re.search(r"[A-Z]", password):
        feedback.append("❌ Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("❌ Add at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        feedback.append("❌ Add at least one number.")
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", password):
        feedback.append("❌ Add at least one special character.")
    if password.lower() in common_passwords:
        feedback.append("❌ The password is too common :(.")

    if not feedback:
        return "✅ Your password is strong and meets all security requirements :D !"
    else:
        return "\n".join(feedback)

# User input
pwd = input("Enter a password to check: ")
print(check_password_strength(pwd))
