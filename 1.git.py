"""
This document will contain all the steps to create a git repository 
and some interesting commands
"""

1. Create the repository in github

2. Copy the repository link, SSH or HTTPS

3. go to the directory where you want to put your github repository, and in the terminal execute this command:

	'$ git clone [link_of_repository] .' #the point means in the current directory.

Now you have a version of that repository in your local machine, and you can start modifying it.

4. after youve created files, modified files.. in your local machine, now you execute these commands:

	4.1 'git status': to check which changes have been commited and which havent.
	
	4.2 'git add [uncommited_files]': this command puts the files that have been modified in the staging area to be commited
	
5. 'git commit -m "message"': after adding all the files to the staging area, we commit the changes we ve made, which means
		   	     taking a screenshot of thee current version and saving it.
    

to be able to pull safely.. youll have to choose which lines you want to keep.

6. 'git push': this command uploads the new/modified files into github.

7.1 'git pull': this commans allows you to download the latest version of the project to your local machine
			   and merge any modifications made by other contributor With your own code.

7.2 "merge conflict":
	If some files were modified on the server that you didnt know of then you tried to pull the latest version 
	of the projec, there could be some issues
	like modifying the same line that another contributer modified youll get an merge conflict.
	the file will look like this:

<<<<<<<<< HEAD
{ 'for example' b = 0 #this is your version 
====================
{ b = 2 #this is the version of the other contributor
>>>>> 656d54df6d46a464c6

7.2

8. 'git log': prints all the versions of your project including their Hash code, date and author
			  and the message related to that versions commit.

9. 'reset --hard [Hash_of_version]': resets your local repository into the commit version in the input.

