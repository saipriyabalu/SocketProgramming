# SocketProgramming

Python script of Simple Web Server & Client project:

Pre-requisite: 

-Windows 10 Operating System
- Install Python 3.5.2 32bit- https://www.python.org/downloads/
- Install PyCharm (Python interpreter IDE) - https://www.jetbrains.com/pycharm/download/#section=windows
- Set the environment path variable for Python.exe

References: 
http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php and
http://crystal.uta.edu/~datta/teaching/cse5344_3/Programming%20Assignment%201_reference_Python.pdf
https://www.tutorialspoint.com/python/
http://www.binarytides.com/python-socket-server-code-example/
http://stackoverflow.com/questions/21335682/python-web-server-indexerror-when-splitting-filename

Steps to execute: 

Open a Python file in PyCharm:
- Unzip 1001373543_SaipriyaThirvakadu.zip and save it in D drive of your system
- Open PyCharm, Click File-> Open and go to the file location where you have saved the file-> Select file and click on OK button

Request from browser:
- First open Multithread_Server.py and go to Run menu and select Run 
- The server waits for a connection from the client, now open any browser and open http://localhost:8080/index.html
- Browser opens the file which you have requested 
- If the requested file is not available, then the browser shows a 404 File not found error

Run the script from the command prompt:
- Open command prompt and go the folder location where the file is stored
- Now type, python Client.py localhost 8080 index.html and hit enter
- This should display the data in the file requested from the server
- If the requested file is not available, then it shows a 404 File not found in the command prompt



