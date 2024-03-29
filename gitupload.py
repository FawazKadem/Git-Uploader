
'''
Program to create repo on Github and then upload local project to it.
Motivation: I make lots of small projects that don't greatly benefit from source control.
            I want to upload these projects to GitHub, but not have to go through the tedious process

User flow:
    1. Navigate to project folder that you want to upload as a repo.
    2. Run program with the desired repo name as an argument

Author: Fawaz M. Kadem. https://github.com/FawazMohammad https://fawazm.me/
'''
from github import Github
import git
import sys
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Get repo name from command line. If no argument, prompt user for name
reponame = ''
if len(sys.argv) <= 1:
    reponame = input("Enter desired repo name: ")
else:
    reponame=sys.argv[1]


f = open((os.path.join(__location__, './token.config')), "r")
token = f.readline().rstrip()
f.close()


# create github instance
g = Github(token)

usr = g.get_user()

# delete remote repo if it exists
repoNameAvailable = True

for usrRepo in usr.get_repos():
    if usrRepo.name == reponame:
        repoNameAvailable = False

while not repoNameAvailable:
    ans = input("A repo with this name already exists. D-Delete R-Choose a different name S-Stop upload & exit ")
    if ans == "D":
        usr.get_repo(reponame).delete()
        repoNameAvailable = True
    elif ans == "R":
        reponame = input("Enter desired repo name: ")
    else:
        print("quitting")
        quit()

# Create remote repo
newRepo = usr.create_repo(reponame)

# Configure local repo

commit_message = "Upload"
if len(sys.argv) > 2:
    commit_message = sys.argv[2]
localRepo = git.Repo.init(".")
localRepo.index.add(['*'])
localRepo.index.commit(message=commit_message)


exists = True

try:
    localRepo.remote('origin').exists()
except ValueError:
    exists = False

if not exists:
    origin = localRepo.create_remote('origin', newRepo.html_url)

localRepo.remote('origin').set_url(newRepo.html_url)
localRepo.git.push("origin", "master")



