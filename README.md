# Overview
This project is a simple, bare-bones chat application built using Python and TCP sockets. My purpose for creating this software is to demonstrate the most simple way that two or more computers can communicate over a network using sockets. This project has just two files- a server file and a client file. The server program accepts multiple connections and the client program allows users to send and receive messages in real time. 

I designed this softwarte to gain experience with network communication and handling multiple clients at a time. I do not have a lot of experience in this area, so it was helpful to see how relatively simple this was to get working. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This project uses a client/server architecture. The server listens for TCP connections on PORT 5000 and creates a separate "thread" for each connected client. This allows multiple clients to communicate simultaneously without issue. 

This project communicates using TCP, which helps us to have ordered messages in the "chat box."

Messages are sent as USF-8 encoded text. Clients can send either text chat messages that are visible to other clients, or command messages that are as follows: /nick "NAME"- change nickname... /who- lists all connected users... /time- requests server time... /quit- disconnect from server. The server is able to interpret the message and perform the desired outcome. 

# Development Environment

This project was developed using Python, the built-in socket module for network communication, and the "threading" module to support multiple clients at once. No external libraries were required for this project. 

Development and testing were done using Visual Studio Code. Multiple terminals were used at the same time to simulate multiple clients connecting to the server. 


# Useful Websites

* [Python Docs- Socket]https://docs.python.org/3/library/socket.html
* [Geeksforgeeks- Socket Programming in Python]https://www.geeksforgeeks.org/python/socket-programming-python/

# Future Work

One big thing I need to do a better job of is pushing to Github regularly! This is not specific to this project, but is a relevant aspect of this project. Because I am working on this project alone, I often do the work without pushing to Github, but when I'm working with a group it is essential to keep your repositories up to date. This is something I will work on more in the future. 
* Item 2 One thing I could easily implement in the future is timestamps for all messages sent. This helps users know when a message has been sent, similar to how email is set up. 
* Item 3 The last thing I would like to do with this project is create a visually appealing graphical user interface for the chat client. This will make the software much more usable, and the design can fit any use-case needed (internal company communications, communication between friends, messaging between teammates in a game, etc.).