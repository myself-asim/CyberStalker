import subprocess, sys, os, threading

def makeThread(command, tool):
    print(f"{tool} SCAN INITIALIZED")
    scan = subprocess.run(command, shell=True, capture_output=True)
    if (scan.returncode != 0):
        print(f"THERE IS SOME ISSUE WHIILE RUNNING {tool} AUTOMATED SCAN")
        print(f"EXCEPTION IS : subprocess.CalledProcessError()")
        sys.exit()
    
    print(f"{tool} SCAN HAS BEEN COMPLETED")

def runSCAN(target, url):
    ARR_COMMAND = [f"nmap -sV {target} > RECON.txt",
                f"gobuster  dir -u {url} -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt > GOBUSTER.txt -t 50",
                f"sublist3r -d {target} > SUBLIST3R.txt"]
    ARR_TOOL = ["NMAP", "GOBUSTER", "SUBLIST3R"]

    for i in range(0, 3):
        thread = threading.Thread(target=makeThread, args=(ARR_COMMAND[i], ARR_TOOL[i]))
        thread.start()

    thread.join()

def arguments():
    try:
        if len(sys.argv) == 3:
            cwd = os.getcwd()
            URL = sys.argv[2]
            TARGET = sys.argv[1]
            print(f"TARGET : {TARGET}")
            print(f"URL : {URL}")
            print("============================================================================")

            runSCAN(TARGET, URL)
    except:
        print(f"INSUFFIIECENT ARGUMENT RECIEVED")
        print(f"RUN IT LIKE THIS : python3 Recon.py Target URL")

def header():
    print("============================================================================")
    print("One Eye - Best Reconnaissance Tool By Muhammad Asim - RNDx3")
    print("============================================================================")

header()
arguments()