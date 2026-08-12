import sys
import re

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score == 4:
        return f"{GREEN}[+] Password Strength: Very Strong 💪{RESET}"
    elif score == 3:
        return f"{YELLOW}[!] Password Strength: Medium ⚠️{RESET}"
    else:
        return f"{RED}[-] Password Strength: Weak ❌{RESET}"

def main():
    print(f"{CYAN}==================================={RESET}")
    print(f"{CYAN}   Password Checker Tool v1.0 🔐  {RESET}")
    print(f"{CYAN}         By: MARWAN SWEDAN        {RESET}")
    print(f"{CYAN}==================================={RESET}\n")

    while True:
        try:
            pwd = input("Enter password to check (or 'exit' to quit): ")
            if pwd.lower() in ['exit', 'quit']:
                print("Goodbye! 👋")
                break
            if not pwd:
                continue
            
            print(check_password_strength(pwd))
            print("-" * 35)
        except KeyboardInterrupt:
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()