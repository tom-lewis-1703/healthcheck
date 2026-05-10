import subprocess

def health_check():

    result = subprocess.run(["ping", "google.com"], capture_output=True, text=True)
    print(result.stdout)

health_check()