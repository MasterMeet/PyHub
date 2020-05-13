# Using Gmail Servers -> Go to Gmail settings and enable IMAP and POP
import smtplib

host = "smtp.gmail.com"     # For Gmail.
port = 587                  # Don't change the port.

username = str(input("Enter Gmail Username : "))                    # Enter your Gmail Username
password = str(input ("Enter Gmail Password: "))                    # Enter your Gmail Password
message = input("Enter the message you want to send : ")            # Enter message to be sent
_to = [username,"username2@gmail.com"]                              # Enter the to gmail address here.
# To mail more than one ID, add a comma to the above _to variable and add the new Gmail ID.
_from = username
try:
    connection = smtplib.SMTP(host,port)
    connection.ehlo()
    connection.starttls()
    connection.login(username,password)         # Go to your Google Account settings and enable Less secure app access.
    print("\nCONNECTION SUCCESSFUL")
    connection.sendmail(_from,_to,message)      # 1st arg = From, 2nd arg = To, 3rd arg = message.
    print("Message has been sent Successfully")
    connection.quit()                           # To close the connection.
    print("Connection has been closed.")
except:
    print("CONNECTION ERROR")