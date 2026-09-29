import os
import time
from datetime import datetime

# terminal color variables
W = "\033[0m"
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[36m"

# database array
students = [
    {"roll": "26BCE1001", "name": "Vansh Sharma"},
    {"roll": "26BCE1002", "name": "Utkarsh Singh"},
    {"roll": "26BCE1003", "name": "Ishaant Jha"},
    {"roll": "26BCE1004", "name": "Harsh"},
    {"roll": "26BCE1005", "name": "Naitik Mishra"},
    {"roll": "26BCE1006", "name": "Prateek Arya"},
    {"roll": "26BCE1007", "name": "Jay"}
]

while True:
    # clear terminal block
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # banner layout
    print(f"{B}==================================================================")
    print(" __      _______ _______   ____  _hopal                      ")
    print(" \\ \\    / /_   _|__   __| |  _ \\| |                          ")
    print("  \\ \\  / /  | |    | |    | |_) | |__   ___  _ __   __ _  |  ")
    print("   \\ \\/ /   | |    | |    |  _ <| '_ \\ / _ \\| '_ \\ / _` | |  ")
    print("    \\  /   _| |_   | |    | |_) | | | | (_) | |_) | (_| | |  ")
    print("     \\/   |_____|  |_|    |____/|_| |_|\\___/| .__/ \\__,_| o  ")
    print("                                            | |              ")
    print("                                            |_|              ")
    print("==================================================================" + W)
    print(f"{Y} >>> FACULTY PORTAL - LIVE CLASS ATTENDANCE ENGINE v1.2 <<<{W}\n")
    
    print("1. Attendance Shuru Karo")
    print("2. Bahar Niklo (Exit)")
    
    choice = input("\nKya karna hai? > ").strip()
    
    if choice == "2" or choice == "exit":
        print(f"\n{B}Portal band ho raha hai... Bye!{W}")
        break
        
    elif choice == "1":
        # resetting lists dynamic updates
        p = []
        ab = []
        lt = []
        history = []
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{B}==================================================================" + W)
        print(f"[*] Session Chalu Hai: {datetime.now().strftime('%d %B %Y, %I:%M %p')}")
        print(f"[*] Total bacche class me: {len(students)}\n")
        print(f"{Y}[Shortcuts] p=Present | a=Absent | l=Late | b=Back{W}\n")
        
        input("Attendance shuru karne ke liye Enter dabao...")
        
        i = 0
        while i < len(students):
            s = students[i]
            
            # fast clear setup inside tracking
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{B}==================================================================" + W)
            print(f"📊 Progress: [{i+1} / {len(students)}]\n")
            print(f"  📌 Roll No: {B}{s['roll']}{W}")
            print(f"  👤 Name: {G}{s['name']}{W}\n")
            
            val = input("Status dalo (p/a/l/b): ").strip().lower()
            
            if val == 'p':
                p.append(s)
                history.append('p')
                print(f"{G}Present mark ho gaya!{W}")
                i += 1
            elif val == 'a':
                ab.append(s)
                history.append('a')
                print(f"{R}Absent mark ho gaya!{W}")
                i += 1
            elif val == 'l':
                lt.append(s)
                history.append('l')
                print(f"{B}Late entry dali hai.{W}")
                i += 1
            elif val == 'b':
                if i == 0:
                    print(f"{R}[!] Bhai ye toh pehla hi student hai, peeche kahan jaoge!{W}")
                    time.sleep(1)
                else:
                    # rollback modifications
                    last = history.pop()
                    if last == 'p': p.pop()
                    elif last == 'a': ab.pop()
                    elif last == 'l': lt.pop()
                    i -= 1
                    print(f"{Y}>> Pichle student par wapas ja rahe hain...{W}")
            else:
                print(f"{R}[!] Galat key dabayi! Sirf p, a, l, ya b chalega.{W}")
                time.sleep(1)
                
            time.sleep(0.1)
            
        # stats calculation calculations
        tot = len(students)
        perc = ((len(p) + len(lt)) / tot) * 100
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{B}==================================================================" + W)
        print(f"📊 {Y}ATTENDANCE SUMMARY (Aaj ka hisab){W} 📊\n")
        print(f"  • Total Strength : {tot}")
        print(f"  • Total Present  : {G}{len(p)}{W}")
        print(f"  • Total Absent   : {R}{len(ab)}{W}")
        print(f"  • Late Aaye Bache: {B}{len(lt)}{W}")
        print(f"  • Attendance %   : {Y}{perc:.2f}%{W}\n")
        print("-" * 50)
        
        # log file dump block
        ts = datetime.now().strftime("%Y-%m-%d_%H-%M")
        fname = f"Attendance_Log_{ts}.txt"
        
        try:
            f = open(fname, "w")
            f.write("==================================================\n")
            f.write(f"OFFICIAL CLASS ATTENDANCE REPORT - {ts}\n")
            f.write("==================================================\n\n")
            f.write(f"Summary Stats:\nPresent: {len(p)}\nAbsent: {len(ab)}\nLate: {len(lt)}\nPercentage: {perc:.2f}%\n\n")
            
            f.write("--- PRESENT STUDENTS ---\n")
            for item in p: f.write(f"[{item['roll']}] {item['name']}\n")
            
            f.write("\n--- ABSENT STUDENTS ---\n")
            for item in ab: f.write(f"[{item['roll']}] {item['name']}\n")
            
            f.write("\n--- LATE ENTRIES ---\n")
            for item in lt: f.write(f"[{item['roll']}] {item['name']}\n")
            f.close()
            
            print(f"{G}[+] Report save ho gayi bhai! File: {fname}{W}")
        except Exception as err:
            print(f"{R}[!] File write me lafda ho gaya: {err}{W}")
            
        print("-" * 50)
        input("\nMain menu me wapas jaane ke liye Enter dabao...")
        
    else:
        print(f"{R}Galat option! Wapas try karo.{W}")
        time.sleep(0.5)
