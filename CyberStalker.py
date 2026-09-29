import subprocess, sys, os

def runSCAN(target, url):
    STACK = [target, url]
    ARR_COMMAND = [f"nmap -sSCV {target} > RECON.txt",
                f"gobuster  dir -u {url} -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt > GOBUSTER.txt -t 50",
                f"sublist3r -d {target} > SUBLIST3R.txt"]
    ARR_TOOL = ["NMAP", "GOBUSTER", "SUBLIST3R"]


    for i in range(0, 3):
        print(f"{ARR_TOOL[i]} SCAN INITIALIZED => ", end="")
        scan = subprocess.run(ARR_COMMAND[i], shell=True, capture_output=True)
        if (scan.returncode != 0):
            print(f"THERE IS SOME ISSUE WHIILE RUNNING {ARR_TOOL[i]} AUTOMATED SCAN")
            print(f"EXCEPTION IS : subprocess.CalledProcessError()")
            sys.exit()
        
        print(f"{ARR_TOOL[i]} SCAN HAS BEEN COMPLETED")

    print("============================================================================")

def arguments():
    try:
        if len(sys.argv) == 3:
            cwd = os.getcwd()
            URL = sys.argv[2]
            TARGET = sys.argv[1]
            print("============================================================================")
            print(f"TARGET : {TARGET}")
            print(f"URL : {URL}")
            print("============================================================================")

            runSCAN(TARGET, URL)
    except:
        print(f"INSUFFIIECENT ARGUMENT RECIEVED")
        print(f"RUN IT LIKE THIS : python3 Recon.py Target URL")

def header():
    print("============================================================================")
    print("Cyber Stalker - Best Reconnaissance Tool By Muhammad Asim - RNDx3")
    print("============================================================================")

header()
arguments()