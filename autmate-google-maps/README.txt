mapit.py
It is an exercise about 
-Web Scraping 
(is the term for using a program to download and process content from the web).
-Custom Automation 
(how to automate our own repetitive tasks using Python)

This folder contains 2 files (besides the README file)

mapit.py (python file)
-Gets a street address from the command line arguments or clipboard
-Opens the web browser to the Google Maps page for the address
It can be used independently but in order to automate this file, we will use:

mapit.bat (batch file)
A batch file is a script file in DOS, OS/2 and Microsoft Windows. 
It consists of a series of commands to be executed by the command-line interpreter, 
stored in a plain text file, in this case it makes really easy to run Python scripts.
You  will need to personalise this batch file to make it work:
@argument1 argument2 %*
where 
argument1 = full path to your python.exe file 
argument2 = full path to your mapit.py file
(open your text editor, delete "argument1" & "argument2", introduce the paths)


Now we can open the command line and write: 
mapit + write the addres 
OR
mapit + enter = mapit + address from the clipboard