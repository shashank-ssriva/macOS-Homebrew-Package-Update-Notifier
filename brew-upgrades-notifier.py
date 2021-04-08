#Author : Shashank Srivastava
#Date : 07th of April, 2021

from pync import Notifier
import subprocess

def notify(text):
    Notifier.notify(text)

COMMAND = "brew outdated -v"
OUTDATED_PACKAGES = subprocess.check_output([COMMAND], shell=True).decode("utf-8")

if len(OUTDATED_PACKAGES) > 0:
    print("These Mac packages need to be updated.\n" + OUTDATED_PACKAGES)
    notify("Updates available. Install using brew upgrade.\n" + OUTDATED_PACKAGES)
else:
    print("No updates available.")
    notify("No updates available.")
