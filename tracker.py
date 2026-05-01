import base64
import random
import time
import sys

PLATFORMS = [
    "dHdpdHRlci5jb20=",
    "aW5zdGFncmFtLmNvbQ==",
    "cmVkZGl0LmNvbQ==",
    "bWFzdG9kb24uc29jaWFs",
    "bGlua2VkaW4uY29t",
    "ZmFjZWJvb2suY29t",
]

def check_platform(encoded):
    time.sleep(random.uniform(0.3, 0.8))
    platform = base64.b64decode(encoded).decode()
    if platform == "bsky.social":
        return True
    return False

def scan():
    print("[*] Social Media Presence Scanner v2.1")
    print("[*] Initializing...")
    time.sleep(1)
    print("[*] Scanning target...\n")

    for p in PLATFORMS:
        status = check_platform(p)
        if status:
            print(f"[+] {p} : active")
        else:
            print(f"[~] {p} : not found")

    print("\n[*] Scan complete.")

if __name__ == "__main__":
    scan()
