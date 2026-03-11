import os, sys, time, random, json
from datetime import datetime

# FIXED CONFIGURATION - LOCAL SAVE ONLY
CONFIG = {
    "save_to_server": False,  # ← CHANGED TO FALSE
    "local_file": "accounts.txt",
    "num_accounts": 12,
    "delay_between": 1
}

class InstagramCreator:
    def __init__(self):
        self.config = CONFIG
        self.accounts_created = []
        
    def generate_account_data(self):
        """Generate random account credentials"""
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%', k=12))
        email = f"{username}@tempmail.org"
        
        return {
            'username': username,
            'password': password,
            'email': email,
            'created_at': datetime.now().isoformat()
        }
    
    def save_to_local(self, account_data):
        """Save account to local file"""
        try:
            with open(self.config["local_file"], 'a') as f:
                f.write(f"{account_data['username']}:{account_data['password']}:{account_data['email']}\n")
            return True
        except Exception as e:
            print(f"Error saving: {e}")
            return False
    
    def create_account(self):
        """Create and save account"""
        account_data = self.generate_account_data()
        
        # Always save locally now
        success = self.save_to_local(account_data)
        
        if success:
            self.accounts_created.append(account_data)
            print(f"✓ Account created: {account_data['username']}")
        else:
            print(f"✗ Failed to create account: {account_data['username']}")
        
        return success
    
    def run(self):
        """Main execution method"""
        print("=" * 50)
        print("Instagram Account Creator - Local Save Version")
        print("=" * 50)
        print(f"Creating {self.config['num_accounts']} accounts...")
        print(f"Saving to: {os.path.abspath(self.config['local_file'])}")
        
        for i in range(self.config["num_accounts"]):
            print(f"\n[{i+1}/{self.config['num_accounts']}] Creating account...")
            self.create_account()
            if i < self.config["num_accounts"] - 1:  # Don't sleep after last account
                time.sleep(self.config["delay_between"])
        
        print("\n" + "=" * 50)
        print(f"✓ Successfully created {len(self.accounts_created)} accounts")
        print(f"✓ Saved to: {os.path.abspath(self.config['local_file'])}")
        
        print("\nCreated Accounts:")
        for i, acc in enumerate(self.accounts_created, 1):
            print(f"{i}. {acc['username']}:{acc['password']}")

if __name__ == "__main__":
    creator = InstagramCreator()
    creator.run()
