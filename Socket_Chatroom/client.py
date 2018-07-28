# -*- coding: utf-8 -*-
# @Author: IBN_Blank
# @Date:   2018-07-21 12:11:04
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-24 11:11:56

##### Import Libs #####
import socket
import threading

##### Define Variables #####
nick = ""
ip = ""
send_message = ""
port = 18888

##### Define Functions #####
# Function of Sending
def client_send(sock):
    global send_message
    while True:
        send_message = input()
        send_message = "{}:{}".format(nick, send_message)
        sock.send(bytes(send_message, encoding="utf8"))
# Function of Getting
def client_get(sock):
    get_message = ""
    while True:
        try:
            get_message = str(sock.recv(1024), encoding="utf-8")
            if not get_message:
                break
            if send_message != get_message: # Check the Source of the Message
                print(get_message)
        except:
            break

##### Main #####
if __name__ == '__main__':
    # Socket Message
    nick = input('Please input your nickname:')
    ip = input('Please input your IP address:')
    # Socket Initial
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Creat Socket
    sock.connect((ip,port))                                         # Connect
    sock.send(bytes(nick, encoding="utf8"))                         # Send Nickname
    # Tread Initial
    th_get = threading.Thread(target=client_get, args=(sock,))      # Tread of Getting
    th_get.start()                                                  # Start the Getting Tread
    th_send = threading.Thread(target=client_send, args=(sock,))    # Tread of Sending
    th_send.start()                                                 # Start the Sending Tread