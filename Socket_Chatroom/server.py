# -*- coding: utf-8 -*-
# @Author: IBN_Blank
# @Date:   2018-07-21 12:09:29
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-24 11:03:30

##### Import Libs #####
import socket
import threading

##### Define Variables #####
message = ""
host = socket.gethostname()
# host = ""
port = 18888
con = threading.Condition()     # Lock Condition

##### Define Functions #####
# Function of Notify
def NotifyAll(text):
    global message
    if con.acquire():           # Get Lock
        message = text
        con.notifyAll()
        con.release()
# Function of Sending
def server_send(conn, nick):
    while True:
        if con.acquire():
            con.wait()
            if message:
                try:
                    conn.send(bytes(message, encoding="utf8"))
                    con.release()
                except:
                    con.release()
                    return
# Function of Getting
def server_get(conn, nick):
    while True:
        try:
            temp = str(conn.recv(1024), encoding="utf-8")
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print(message)
        except:
            NotifyAll("{} Error".format(nick))
            print(message)
            return

##### Main #####
if __name__ == '__main__':
    # Socket Message
    # host = input("Please input your hostname or ip address:")
    # Socket Initial
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Creat Socket
    print("Socket Created")
    sock.bind((host,port))                                          # Bind Socket
    print("Socket Binded {}:{}".format(host, port))
    sock.listen(5)                                                  # Listen Socket
    print("Socket New Listening")

    while True:
        conn, addr = sock.accept()                                  # Accept Connection
        print("Connected with {} : {}".format(addr[0], addr[1]))    # addr = (ip,port)
        nick = str(conn.recv(1024), encoding="utf-8")

        NotifyAll("Welcome, {} !".format(nick))
        print(message)
        conn.send(bytes(message, encoding="utf8"))

        threading.Thread(target=server_send, args=(conn,nick)).start()
        threading.Thread(target=server_get, args=(conn,nick)).start()