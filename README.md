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

### Updating documentation with examples... 