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

{Describe the tools that you used to develop the software}
This project was developed using Python, the built-in socket module for network communication, and the "threading" module to support multiple clients at once. No external libraries were required for this project. 

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3