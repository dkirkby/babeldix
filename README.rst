====================================
BabelDix: ten languages in ten weeks
====================================

Install the challenge server from github using::

	git clone https://github.com/dkirkby/babeldix.git

When you are ready to take a challenge, start the server::

	cd babeldix
	python server.py

Finally, run your program from a different command-line to keep its output seperate from the server messages.

----------------
Challenge Format
----------------

All challenges require that you use a TCP socket to connect to the server.  Since the server is running on your computer, you can use the hostname `localhost`.  The port number should be `1234`.

All communication with the server uses ASCII text.  Each message consists of a sequence of printable characters (except newline) followed by a newline character.  Note that you many need to read from your socket several times to assemble a complete message, ending with a newline character.

The text of each message is always valid `json <http://json.org>`_, so you can either use one of the many JSON libraries available or else, since the format is simple enough, parse the message text yourself.

All challenges consist of the following phases:

1. Your program sends the name of challenge you wish to attempt as a string, e.g. `"histogram"`.
2. The server responds with the challenge data (or `"error"` if the name is not recognized).
3. Your program send the challenge solution.
4. The server responds with either `"yes"`, if your solution is correct, or else `"no"`.

If you are having trouble communicating with the server, check the server log messages for useful diagnostics.

The available challenges are described below.

Hello Challenge
---------------

This is the easiest challenge, and just requires that you are able to open a socket and perform basic communication with the server. Send the name `"hello"` to begin this challenge.  The server responds with `"hello"`.  You answer `"goodbye"`.

Histogram Challenge
-------------------

In this challenge, you build a histogram of positive integer values provided by the server. Send the name `"histogram"` to begin this challenge.  The server responds with a message like::

	[[10,3],[26,0,1,21,22,11,21,19,3,12,20,24,26,6,27,9,16,9,5,22,21,7,16,7,5,11,8,4,4,5,8,15,2,0,25,8,1,15,9,17,29,19,25,11,0,28,25,10,23,10,7,7,27,11,12,27,3,12,7,8,8,23,18,4,12,5,1,16,12,16,10,16,13,27,13,6,27,14,15,7,0,26,16,26,3,27,26,7,23,10,24,27,7,28,9,16,26,18,23,13]]

The square brackets `[...]` in this message identify JSON arrays, so this message consists of an array of two arrays.  The first array `[10,3]` describes the histogram you need to build: it has 10 bins, with 3 consecutive integers falling into each bin::

	bin-0: 0,1,2
	bin-1: 3,4,5
	bin-2: 6,7,8
	...
	bin-8: 24,25,26
	bin-9: 27,28,29

Your challenge is to count how many values in the second array `[26,0,1,...,23,13]` fall into each bin and then return these counts.  The correct answer in this case is `[8,10,15,12,9,11,5,9,11,10]`, which means that the are 8 values equal to 0, 1, or 2 (`bin-0`), etc.
