"""
This document will contain some interesting git commands, part 2 of the git course
"""

1. Branching:
	Creating new branches out of a stable version of our project so we 
	can add (For example) a new feature, then merging them.

	1.1 to create a branch(we ll call it feature):
		'git branch feature'

	1.2 to view the branches that exist:
		'git branch'

	1.3 to point the head toward a branch(in this case feature):
		'git checkout feature'

	Then we can edit the files however we want.

	1.4 then do a commit:
		'git commit -am "added a new feature"'

	if we execute 'git checkout master', the files in our directory will 
	go back to the original version.
	
	1.5 Now to merge the new modifications into master, 
	we checkout into it and we execute the merge:
		'git checkout master'
		'git merge feature'


	1.6 Upstream branch is the remote in github that contains the files
	so here feature doesnt have an Upstream branch because it was created in
	our local directory, so we execute:
		'git push --set-upstream origin feature'

	1.7 Remote(): is the version saved in the internet or website (like github or gitlab)
	usualy its name starts with origin (like origin/master or origin/feature)

	1.8 Fork(): is an entirely separate version of a repository that gets copied of the
	original, then you can do whatever you want with it.
		After doing what you wanted to do to the project you forked, then you will have
	to submit a Pull_Request(), which is essentialy a merge request.
		Then the owner of the original repository will review your changes and decide if 
	they want to accept them or not.