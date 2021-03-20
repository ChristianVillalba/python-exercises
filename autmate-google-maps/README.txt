MAPIT : 
Automate google maps

It is an exercise about 
-Web Scraping 
(is the term for using a program to download and process content from the web).
-Custom Automation 
(how to automate our own repetitive tasks using Python)

mapit.py (python file)
-Gets a street address from the command line arguments or clipboard
-Opens the web browser to the Google Maps page for the address

we can open the command line and write: 
mapit + write the addres 
OR
mapit + enter = mapit + address from the clipboard

mapit.py  can be used independently but in order to automate this file, we create the next file:

mapit.bat (batch file)
A batch file is a script file in DOS, OS/2 and Microsoft Windows.stored in a plain text file with the .bat extension,  
It consists of a series of commands to be executed by the command-line interpreter, 
In this case it makes really easy to run Python scripts.
You  will need to personalise this batch file to make it work:
@argument1 argument2 %*
where 
argument1 = full path to your python.exe file 
argument2 = full path to your mapit.py file
(open your text editor, delete "argument1" & "argument2", introduce the paths)

Now, having an address copied in the clipboard, if twe double click the batch file (mapit.bat),
it will automatically run our mapit.py
