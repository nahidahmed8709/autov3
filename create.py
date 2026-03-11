import requests, random, string, time, json, os, sys
from datetime import datetime

# Configuration - LOCAL SAVE VERSION
SAVE_TO_SERVER = False  # Changed to False
LOCAL_SAVE_PATH = "accounts.txt"  # Local file path

def create_account():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    email = f"{username}@tempmail.org"
    
    account_data = {
        'username': username,
        'password': password,
        'email': email,
        'created_at': datetime.now().isoformat()
    }
    
    # Save locally instead of server
    try:
        with open(LOCAL_SAVE_PATH, 'a') as f:
            f.write(f"{username}:{password}:{email}\n")
        print(f"Account saved locally: {username}")
        return account_data
    except Exception as e:
        print(f"Error saving locally: {e}")
        return None

# Main execution
if __name__ == "__main__":
    print(f"Creating accounts and saving to {LOCAL_SAVE_PATH}")
    
    for i in range(12):  # Creates 12 accounts
        account = create_account()
        if account:
            print(f"Created {i+1}/12: {account['username']}:{account['password']}")
        time.sleep(1)  # Reduced delay for faster creation
    
    print(f"\nAll accounts saved to {LOCAL_SAVE_PATH}")
    print("Format: username:password:email")