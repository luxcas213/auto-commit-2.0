import subprocess
import datetime


def commit():

    today = datetime.datetime.now().strftime("%m/%d/%Y")
    subprocess.run(["git", "commit", "--allow-empty", "-m", "commit :)", "--date", today])
    subprocess.run(["git", "push"])



if __name__ == "__main__":
    commit()


