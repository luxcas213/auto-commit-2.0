import subprocess
import datetime
import os

def commit():
    repo_url = "https://github.com/luxcas213/auto-commit-2.0.git"
    repo_dir = "C:\\Users\\Lgarb\\Downloads\\Repos\\auto-commit-2.0"
    
    if not os.path.isdir(repo_dir):
        subprocess.run(["git", "clone", repo_url, repo_dir])

    os.chdir(repo_dir)

    subprocess.run(["git", "remote", "set-url", "origin", repo_url])

    subprocess.run(["git", "config", "--global", "user.name", "Tu Nombre"])
    subprocess.run(["git", "config", "--global", "user.email", "tuemail@example.com"])
    
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "."])
    
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subprocess.run(["git", "commit", "--allow-empty", "-m", "commit :)", "--date", today])

    subprocess.run(["git", "push"])

commit()
