# Git-Uploader
Python script to automate uploading project to Github

Motivation: I make lots of small projects that don't greatly benefit from source control. I want to upload these projects to GitHub once they're finished, but not have to go through the tedious process everytime.

This program will:
  1. Create a repo on your github account with your desired name
  2. Initialize a local repo in the CWD. (Handles duplicate repo name if necessary)
  3. Push the local files to your github repo
  
How to use:
  1. Create token.config file which includes nothing except your personal github access token
  2. Navigate to the directory of the project you want to upload
  3. Run the program. 
    a. First argument is the name you want for your repository on Github. Program will prompt you if no arguments
    b. Second argument is the commit message. If no second argument, will default to "Upload"
    

