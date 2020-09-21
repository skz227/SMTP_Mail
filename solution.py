from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver= '127.0.0.1'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket= socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 1025))
    recv = clientSocket.recv(1024).decode()
    

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    

    # Send MAIL FROM command and print server response.
    mail_From= 'Mail From:<skz227@nyu.edu>\r\n'
    clientSocket.send(mail_From.encode())
    recv2 = clientSocket.recv(1024).decode()
    
    

    # Send RCPT TO command and print server response.
    rcpt_To= 'RCPT TO:<zaidisyedkamran78@gmail.com>\r\n'
    clientSocket.send(rcpt_To.encode())
    recv3 = clientSocket.recv(1024).decode()
    
    

    # Send DATA command and print server response.
    data= 'DATA\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    
    

    # Send message data.
    clientSocket.send(msg.encode())
    
    # Message ends with a single period.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    
    

    # Send QUIT command and get server response.
    quitCommand= 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
