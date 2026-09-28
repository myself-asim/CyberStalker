import subprocess, sys, os

def runNMAP(target):
    ports = "-p 1-1024"
    print("NMAP SCAN INITIALIZED => ", end="")
    scan = subprocess.run(f"nmap -sSCV {target} {ports} > RECON.txt", shell=True, capture_output=True)
    if (scan.returncode != 0):
        print(f"THERE IS SOME ISSUE WHIILE RUNNING NMAP AUTOMATED SCAN")
        print(f"EXCEPTION IS : subprocess.CalledProcessError()")
        sys.exit()
    else:
        print("NMAP SCAN HAS BEEN COMPLETED")

def runGOBUSTER(target):
    print("GOBUSTER SCAN INITIALIZED => ", end="")
    scan = subprocess.run(f"gobuster dir -u {target} -w /usr/share/wordlists/dirb/common.txt > GOBUSTER.txt", shell=True, capture_output=True)
    if (scan.returncode != 0):
        print(f"THERE IS SOME ISSUE WHIILE RUNNING GOBUSTER AUTOMATED SCAN")
        print(f"EXCEPTION IS : subprocess.CalledProcessError()")
        sys.exit()
    else:
        print("GOBUSTER SCAN HAS BEEN COMPLETED")

def arguments():
    try:
        if len(sys.argv) > 1:
            cwd = os.getcwd()
            URL = sys.argv[2]
            TARGET = sys.argv[1]
            print("============================================================================")
            print(f"TARGET : {TARGET}")
            print(f"URL : {URL}")
            print("============================================================================")

            runNMAP(TARGET)
            runGOBUSTER(URL)
    except:
        print(f"INSUFFIIECENT ARGUMENT RECIEVED")
        print(f"RUN IT LIKE THIS : python3 Recon.py Target URL")

def header():
    print("============================================================================")
    print("Best Reconnaissance Tool By Muhammad Asim - RNDx3")
    print("============================================================================")

header()
arguments()
print("============================================================================")