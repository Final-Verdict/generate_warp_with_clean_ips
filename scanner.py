import subprocess
def ip_scanner():
    # Run the batch file
    subprocess.Popen("win_scanner.bat", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    # Send "1" as input to the batch file
    p = subprocess.Popen("win_scanner.bat", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate(input=b"1\n")

    # Print the output if needed
    print(stdout.decode())
    return