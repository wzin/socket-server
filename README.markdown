#Usage of application:

## `./server.py <xbee modem device>`

## Application will listen on any interface on port 31415

#Required modules:
Application will ask for installation of required python modules.

If standard python on MacOSX Lion does not have "easy_install" command, XCode with macports must be installed.

#Sample communication 

##Server-side

$./server.py /dev/ttys000
`
Attaching to /dev/ttys000

B('10.0.0.1', 35385) connected!

Received from client: Hai

Unknown command

Received from client: WOT

Unknown command

Received from client: WTF

Unknown command

Received from client: HELLO WORLD

Unknown command

Received from client: lightOnRequest: true

Sending command to xbee..

Received from client:   

A

Unknown command

Received from client: exit

('10.0.0.1', 35385) disconnected!
`

##Client side
`
$telnet 10.0.0.100 31415

Trying 10.0.0.100...

Connected to 10.0.0.100.

Escape character is '^]'.

Hi - this is cesar request handler v.0.1('10.0.0.1', 35385)

Listening for commands 

Hai

Server answer: unknown command

WOT

Server answer: unknown command

WTF

Server answer: unknown command

HELLO WORLD

Server answer: unknown command

lightOnRequest: true

A

+OK

Server answer: unknown command

exit

bye ('10.0.0.1', 35385)

Connection closed by foreign host.
`

