
import os

def show_banner():
    os.system('clear')
    print("\033[1;32m")
    print("======================================")
    print("             RDG TOOL                ")
    print("======================================")
    print("Author : Malik Habib")
    print("WhatsApp : +923434571018")
    print("\033[0m")

def main_menu():
    print("\n[1] Poll Voting")
    print("[2] Post Reactions")
    print("[3] Comment Voting")
    print("[4] Page Like/Follow")
    print("[5] Group Join")
    print("[6] Reply to Comments")
    print("[7] React to Comments")
    print("[8] Auto Page Create")
    print("[9] Auto FB Account Create")
    print("[0] Exit")

def get_cookie_path():
    path = input("Enter cookies file path (e.g. /sdcard/cookies.txt): ")
    if not os.path.exists(path):
        print("File not found!")
        exit()
    return path

def run_tool():
    show_banner()
    approved = False  # placeholder for actual approval check logic
    if not approved:
        print("Your key is not approved.")
        print("Key: RDG-XXXXX")
        input("Press ENTER to request approval on WhatsApp...")
        os.system("xdg-open 'https://wa.me/923434571018'")
        exit()

    show_banner()
    main_menu()
    choice = input("\nSelect an option: ")
    cookie_file = get_cookie_path()
    print(f"Selected option {choice} with cookies from: {cookie_file}")
    # ... Implement tool logic here ...

if __name__ == "__main__":
    run_tool()
