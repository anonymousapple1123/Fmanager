# Fmanager
A File management tool made in python.

Sync various types of files (non recursively).

How to perform syncing :
1. [cleanup] Remove duplicate files (preferably in both directories target and destination)
2. [Sync] Start 2-way syncing (now both folders- target and destination - have same files)


Additional pros:
1. Do the delta operation on folder.
2. Remove a common substring from all the avialable files.

Cons:
1. No ssh support, use a flash drive to perform sync
2. Device to device sync is unreliable
3. Minimum of 1 flash drive is required to act as hub for every device (physical swapping required)



Why I made this ? 
Lets say I frequently download videos, files, images on my phone, pc, and other devices(tablet) once a while
I wish I had something that does all the syncing for me FOR THAT PARTICULAR FOLDER, bulk rename them, everything done privately on my system, 
no cloud needed, no common network required, need physical connection, Its something I need to do once in 1 or 2 months.
I don't know whether there exist any tool for it. So I made my own.
Currently this tool does all I need, good enough. So further updates are based on other user's requirements.

