import random, string, time, os
from datetime import datetime

# Configuration
ACCOUNTS_FILE = "accounts.txt"
NUM_ACCOUNTS = 12

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

def create_account():
    username = generate_username()
    password = generate_password()
    email = f"{username}@tempmail.org"
    
    account_info = f"{username}:{password}:{email}"
    
    try:
        with open(ACCOUNTS_FILE, 'a') as f:
            f.write(account_info + '\n')
        print(f"✓ Created: {username}")
        return {
            'username': username,
            'password': password,
            'email': email
        }
    except Exception as e:
        print(f"✗ Error creating account: {e}")
        return None

def main():
    print("=" * 50)
    print("Instagram Account Creator - Local Save Version")
    print("=" * 50)
    print(f"Creating {NUM_ACCOUNTS} accounts...")
    print(f"Saving to: {os.path.abspath(ACCOUNTS_FILE)}")
    print("-" * 50)
    
    created_accounts = []
    
    for i in range(NUM_ACCOUNTS):
        account = create_account()
        if account:
            created_accounts.append(account)
        time.sleep(0.5)  # Small delay to avoid issues
    
    print("-" * 50)
    print(f"Successfully created {len(created_accounts)} accounts")
    print(f"Saved to: {os.path.abspath(ACCOUNTS_FILE)}")
    
    # Display created accounts
    print("\nCreated Accounts:")
    for i, acc in enumerate(created_accounts, 1):
        print(f"{i}. {acc['username']}:{acc['password']}")

if __name__ == "__main__":
    main()