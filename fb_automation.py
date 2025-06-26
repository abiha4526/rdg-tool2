#!/usr/bin/env python3
import os, time

def clear(): os.system('clear')
clear()

print("Select option:")
options = [
    "Poll Voting","Post React","Comment Voting","Page Like/Follow",
    "Group Joining","Reply to Comments","React to Comments",
    "Auto Page Creation","Auto ID Creation"
]
for i, opt in enumerate(options,1):
    print(f"[{i}] {opt}")
choice = input(">> ")

if choice not in map(str, range(1,10)):
    print("Invalid choice."); exit()

# Ask cookies after option select
cookie = input("Enter path to your cookies file (.txt): ").strip()
if not os.path.exists(cookie):
    print("File not found!"); exit()

link = ""
if choice in ['1','3','2','6','7','4','5']:
    link = input("Enter post/group/page link: ").strip()

speed = 1
if choice != '9':
    speed = input("Enter speed (1–60): ").strip()
    if not speed.isdigit() or not (1<=int(speed)<=60):
        print("Invalid speed!"); exit()

both = input("Use IDs, Pages, or Both? (i/p/b): ").strip().lower()

clear()
print(f"Processing '{options[int(choice)-1]}'...")
time.sleep(1)
print(f"Cookies file: {cookie}")
print(f"Link: {link}")
print(f"Speed: {speed}")
print(f"Using: {'IDs' if both=='i' else 'Pages' if both=='p' else 'Both'}")
time.sleep(1)

if choice == '9':
    print("Creating IDs...")
    with open("Malik_creation.txt","a") as m:
        m.write(f"[{time.ctime()}] Created new ID | user:pass\n")
else:
    print("Simulating actions...")
    time.sleep(2)

print("Done!")
