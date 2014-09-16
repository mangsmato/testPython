#python networking
import socket #import socket module
s= socket.socket() #create socket object
host=socket.gethostbyname () #get local machine name
port =1234 #reserver a port for the service
s.bind((host,port))
s.listen(5)
while True :
    c, addr = s.accept()
    print ('got connection from', addr)
    c.send('thanx for connecting')
    c.close()
