# Python queue file socket

This program is a basic socket-based service that allows to send files between 2 users on an asynchronous way.

## Features
  - Socket completely customizable (port, host, buffer size...) easily.
  - Choice to select which file are going to be sent.
  - Command-line interacting.
  - ~~Full unit testing coverage.~~ Server and client classes coverage
  - *You have a container based deployment strategy.* Code divided on `src` and `test` dirs to improve maintainability.
  - Documentation on design choices and alternatives.
  - Scaling strategy.

## Running
To run the program, we have to open in 2 different terminals:
```bash
python3.5 src/server.py
```
and
```bash
python3.5 src/client.py
```

Once started, server's interface will ask us to input different values like host, port, buffer size... If we don't input anything, default values will be set.

**It's important to follow this order:**
1. First, run `server.py`until ```Waiting for sender...``` message appears.
2. After this, run `client.py` and select the `Sender` mode. Wait until file transfer ends.
3. Finally, run `client.py` selecting the `Receiver` mode and wait until program finish.

>Server init:   
> ![Alt text](img/running/server.png?raw=true "Server init")
>    
> Client init:  
> ![Alt text](img/running/client-sender.png?raw=true "Client init")
> 
> Server shows connection:  
> ![Alt text](img/running/server2.png?raw=true "Server receive")  
>    
> Client receiving:  
> ![Alt text](img/running/client-receiver.png?raw=true "Client receiving")

## Testing

Unit testing coverage isn't full yet. Due to the duration of the test, I haven't been able to cover completely
the program with tests, but in my opinion maybe the best way to cover a socket connection and these kind of methods is by __mocking__ 
the connexion and continue with the test. As the test does not cover all the cases, I have tried to cover most of the 
errors with __try-except__ sentences.

## Deployent

I'm used to working with Docker containers to have an isolated environment and to be able to test the code in an identical
 environment to the production one, but since there were no special requirements in terms of compatibilities, 
 and the time was 4 hours, I haven't seen it necessary.
