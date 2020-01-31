"""
Program Description: PF Internet to File
Author Name: Ajinkya Wani
Creation Date: 13th May 2019
Revised Date: 14th May 2019
"""

from urllib.request import urlopen
import smtplib
import imaplib
import email
from tkinter import *
from tkinter import filedialog
import os
import xml.etree.ElementTree as ET


def send_email(to, subject):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("pkhodke74@gmail.com", "Easy@123")
        sender = "pkhodke74@gmail.com"
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (sender, ", ".join(to), subject, string_content)
        server.sendmail(sender, to, message)
        server.close()
        print('Email successfully sent\n')
        read_email_from_gmail()
    except:
        print("Failed to send mail\n")


def read_email_from_gmail():
    # Change below values if you wish to read emails from other user's inbox.
    try:
        from_email = "pkhodke74@gmail.com"
        pwd = "Easy@123"
        server = "imap.gmail.com"
        port = 993
        mail = imaplib.IMAP4_SSL(server, port)
        mail.login(from_email,pwd)
        mail.select('inbox')
        type, data = mail.search(None, '(FROM pkhodke74@gmail.com)')
        mail_ids = data[0].split()[-1]
        id = str(mail_ids, 'utf-8')
        typ, data = mail.fetch(id, '(RFC822)' )
        msg = email.message_from_bytes(data[0][1])
        email_subject = str(msg['subject'])
        email_from = str(msg['from'])
        print('From : ' + email_from)
        print('Subject : ' + email_subject)
        print('Body : ' + msg.as_string() + '\n')
    except:
        print("Email not read successfully")


try:
    page = "https://www.w3schools.com/xml/cd_catalog.xml"

    req = urlopen(page)
    string_content = str(req.read(), encoding='utf8')

    file_handler = open("output.xml", "w")
    file_handler.write(string_content)
    file_handler.close()
    print("Data successfully written to file 'output.xml' \n")
    while True:
        send_email_choice = input(
            "Do u wish to get downloaded data from website on your email id? \n Please enter Y/N: ")
        if send_email_choice == "Y":
            to = input("Enter receiver's email id: ")
            subject = input("Enter subject of the email: ")
            send_email(to, subject)
            break
        elif send_email_choice == "N":
            print("Okay, you are good to go and process downloaded file in editor")
            break
        else:
            print("Please enter valid choice")
except:
    print("Source website could not be found")
    exit()



# GUI development

class TextEditor:
    root = Tk()
    __textarea = Text(root)
    __menubar = Menu(root)
    __filemenu = Menu(__menubar, tearoff=0)
    __editmenu = Menu(__menubar, tearoff=0)
    __helpmenu = Menu(__menubar, tearoff=0)

    def __init__(self, width, height):
        self.__windowwidth = width
        self.__windowheight = height


        # Set the window text
        self.root.title("Untitled - MyEditor")

        # I have referenced the code from internet to make tkinter window at center
        # and make window resizable, and I understand how it works
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__windowwidth / 2)

        top = (screenHeight / 2) - (self.__windowheight / 2)

        self.root.geometry('%dx%d+%d+%d' % (self.__windowwidth,
                                            self.__windowheight,
                                            left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.__textarea.grid(sticky=N + E + S + W)

        self.__filemenu.add_command(label="New",
                                    command=self.new_file)

        self.__filemenu.add_command(label="Open",
                                    command=self.open_file)

        self.__filemenu.add_command(label="Save",
                                    command=self.save_file)

        self.__filemenu.add_separator()
        self.__filemenu.add_command(label="Exit",
                                    command=self.quit_app)

        self.__menubar.add_cascade(label="File",
                                   menu=self.__filemenu)

        self.__menubar.add_cascade(label="Edit",
                                   menu=self.__editmenu)

        self.__editmenu.add_command(label="Sort By Company Tag",
                                    command = self.sort_file)

        self.__editmenu.add_command(label="Cut",
                                        command=self.cut)

        self.__editmenu.add_command(label="Copy",
                                        command=self.copy)

        self.__editmenu.add_command(label="Paste",
                                        command=self.paste)

        self.root.config(menu=self.__menubar)

    def sort_file(self):
        tree = ET.parse("output.xml")
        root = tree.getroot()

        data = []
        for child in root:
            for item in child:
                if item.tag == "COMPANY":
                    data.append((item.tag, item.text))

        data.sort()
        self.__textarea.delete(1.0, END)
        self.__textarea.insert(1.0, data)

    def cut(self):
        self.__textarea.event_generate("<<Cut>>")

    def copy(self):
        self.__textarea.event_generate("<<Copy>>")

    def paste(self):
        self.__textarea.event_generate("<<Paste>>")

    def quit_app(self):
        self.root.destroy()

    def open_file(self):

        self.__file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
        if self.__file == "":

            # no file to open
            self.__file = None
        else:
            self.root.title(os.path.basename(self.__file) + " - MyEditor")
            self.__textarea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__textarea.insert(1.0, file.read())

            file.close()

    def new_file(self):
        self.root.title("Untitled - MyEditor")
        self.__file = None
        self.__textarea.delete(1.0, END)

    def save_file(self):
        self.__file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",
                                                   filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        if self.__file == "":
            self.__file = None
        else:
            file = open(self.__file, "w")
            file.write(self.__textarea.get(1.0, END))
            file.close()
            self.root.title(os.path.basename(self.__file) + " - MyEditor")


my_editor = TextEditor(width=600, height=400)
my_editor.root.mainloop()



""" ************************** Sorted data by company tag ************************************
{COMPANY {A and M}} {COMPANY Atlantic} {COMPANY BMG} {COMPANY CBS} {COMPANY {CBS Records}} {COMPANY Capitol} 
{COMPANY Columbia} {COMPANY Columbia} {COMPANY DECCA} {COMPANY EMI} {COMPANY Elektra} {COMPANY Grammy} {COMPANY Island}
{COMPANY London} {COMPANY Medley} {COMPANY Mega} {COMPANY {Mucik Master}} {COMPANY Pickwick} {COMPANY Polydor} 
{COMPANY Polydor} {COMPANY Polydor} {COMPANY RCA} {COMPANY Siren} {COMPANY {Stax Records}} {COMPANY {Virgin records}}
{COMPANY WEA}
"""

""" ************ File Output (Output.xml) ***********************
<?xml version="1.0" encoding="UTF-8"?>
<CATALOG>
  <CD>
    <TITLE>Empire Burlesque</TITLE>
    <ARTIST>Bob Dylan</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Columbia</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1985</YEAR>
  </CD>
  <CD>
    <TITLE>Hide your heart</TITLE>
    <ARTIST>Bonnie Tyler</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>CBS Records</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1988</YEAR>
  </CD>
  <CD>
    <TITLE>Greatest Hits</TITLE>
    <ARTIST>Dolly Parton</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>RCA</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1982</YEAR>
  </CD>
  <CD>
    <TITLE>Still got the blues</TITLE>
    <ARTIST>Gary Moore</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Virgin records</COMPANY>
    <PRICE>10.20</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Eros</TITLE>
    <ARTIST>Eros Ramazzotti</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>BMG</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1997</YEAR>
  </CD>
  <CD>
    <TITLE>One night only</TITLE>
    <ARTIST>Bee Gees</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1998</YEAR>
  </CD>
  <CD>
    <TITLE>Sylvias Mother</TITLE>
    <ARTIST>Dr.Hook</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>CBS</COMPANY>
    <PRICE>8.10</PRICE>
    <YEAR>1973</YEAR>
  </CD>
  <CD>
    <TITLE>Maggie May</TITLE>
    <ARTIST>Rod Stewart</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Pickwick</COMPANY>
    <PRICE>8.50</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Romanza</TITLE>
    <ARTIST>Andrea Bocelli</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>10.80</PRICE>
    <YEAR>1996</YEAR>
  </CD>
  <CD>
    <TITLE>When a man loves a woman</TITLE>
    <ARTIST>Percy Sledge</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Atlantic</COMPANY>
    <PRICE>8.70</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Black angel</TITLE>
    <ARTIST>Savage Rose</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Mega</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1995</YEAR>
  </CD>
  <CD>
    <TITLE>1999 Grammy Nominees</TITLE>
    <ARTIST>Many</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Grammy</COMPANY>
    <PRICE>10.20</PRICE>
    <YEAR>1999</YEAR>
  </CD>
  <CD>
    <TITLE>For the good times</TITLE>
    <ARTIST>Kenny Rogers</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Mucik Master</COMPANY>
    <PRICE>8.70</PRICE>
    <YEAR>1995</YEAR>
  </CD>
  <CD>
    <TITLE>Big Willie style</TITLE>
    <ARTIST>Will Smith</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Columbia</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1997</YEAR>
  </CD>
  <CD>
    <TITLE>Tupelo Honey</TITLE>
    <ARTIST>Van Morrison</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>8.20</PRICE>
    <YEAR>1971</YEAR>
  </CD>
  <CD>
    <TITLE>Soulsville</TITLE>
    <ARTIST>Jorn Hoel</ARTIST>
    <COUNTRY>Norway</COUNTRY>
    <COMPANY>WEA</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1996</YEAR>
  </CD>
  <CD>
    <TITLE>The very best of</TITLE>
    <ARTIST>Cat Stevens</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Island</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Stop</TITLE>
    <ARTIST>Sam Brown</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>A and M</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1988</YEAR>
  </CD>
  <CD>
    <TITLE>Bridge of Spies</TITLE>
    <ARTIST>T'Pau</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Siren</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Private Dancer</TITLE>
    <ARTIST>Tina Turner</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Capitol</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1983</YEAR>
  </CD>
  <CD>
    <TITLE>Midt om natten</TITLE>
    <ARTIST>Kim Larsen</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Medley</COMPANY>
    <PRICE>7.80</PRICE>
    <YEAR>1983</YEAR>
  </CD>
  <CD>
    <TITLE>Pavarotti Gala Concert</TITLE>
    <ARTIST>Luciano Pavarotti</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>DECCA</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1991</YEAR>
  </CD>
  <CD>
    <TITLE>The dock of the bay</TITLE>
    <ARTIST>Otis Redding</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Stax Records</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1968</YEAR>
  </CD>
  <CD>
    <TITLE>Picture book</TITLE>
    <ARTIST>Simply Red</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Elektra</COMPANY>
    <PRICE>7.20</PRICE>
    <YEAR>1985</YEAR>
  </CD>
  <CD>
    <TITLE>Red</TITLE>
    <ARTIST>The Communards</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>London</COMPANY>
    <PRICE>7.80</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Unchain my heart</TITLE>
    <ARTIST>Joe Cocker</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>EMI</COMPANY>
    <PRICE>8.20</PRICE>
    <YEAR>1987</YEAR>
  </CD>
</CATALOG>

"""

""" ************* Console Output ************************************
******************************** Test 1 - Source website not found/ retrieval failed *********************************

Source website could not be found

Process finished with exit code 0

****************************** Test 2 - Everything goes as expected **************************************************

Data successfully written to file 'output.xml'

Do u wish to get downloaded data from website on your email id?
 Please enter Y/N: Y
Enter receiver's email id: ajinkyawani@gmail.com
Enter subject of the email: XML Data From WebSite
Email successfully sent

From : pkhodke74@gmail.com
Subject : None
Body : Bcc: pkhodke74@gmail.com
Return-Path: <pkhodke74@gmail.com>
Received: from Ajinkyas-MacBook-Pro.local ([2601:19a:c100:21b3:fd:bc44:59f9:32b2])
        by smtp.gmail.com with ESMTPSA id t57sm5478475qtt.7.2019.05.12.07.39.02
        for <pkhodke74@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-CHACHA20-POLY1305 bits=256/256);
        Sun, 12 May 2019 07:39:02 -0700 (PDT)
Message-ID: <5cd83006.1c69fb81.15be4.f9a0@mx.google.com>
Date: Sun, 12 May 2019 07:39:02 -0700 (PDT)
From: pkhodke74@gmail.com

<?xml version="1.0" encoding="UTF-8"?>
<CATALOG>
  <CD>
    <TITLE>Empire Burlesque</TITLE>
    <ARTIST>Bob Dylan</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Columbia</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1985</YEAR>
  </CD>
  <CD>
    <TITLE>Hide your heart</TITLE>
    <ARTIST>Bonnie Tyler</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>CBS Records</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1988</YEAR>
  </CD>
  <CD>
    <TITLE>Greatest Hits</TITLE>
    <ARTIST>Dolly Parton</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>RCA</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1982</YEAR>
  </CD>
  <CD>
    <TITLE>Still got the blues</TITLE>
    <ARTIST>Gary Moore</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Virgin records</COMPANY>
    <PRICE>10.20</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Eros</TITLE>
    <ARTIST>Eros Ramazzotti</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>BMG</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1997</YEAR>
  </CD>
  <CD>
    <TITLE>One night only</TITLE>
    <ARTIST>Bee Gees</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1998</YEAR>
  </CD>
  <CD>
    <TITLE>Sylvias Mother</TITLE>
    <ARTIST>Dr.Hook</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>CBS</COMPANY>
    <PRICE>8.10</PRICE>
    <YEAR>1973</YEAR>
  </CD>
  <CD>
    <TITLE>Maggie May</TITLE>
    <ARTIST>Rod Stewart</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Pickwick</COMPANY>
    <PRICE>8.50</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Romanza</TITLE>
    <ARTIST>Andrea Bocelli</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>10.80</PRICE>
    <YEAR>1996</YEAR>
  </CD>
  <CD>
    <TITLE>When a man loves a woman</TITLE>
    <ARTIST>Percy Sledge</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Atlantic</COMPANY>
    <PRICE>8.70</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Black angel</TITLE>
    <ARTIST>Savage Rose</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Mega</COMPANY>
    <PRICE>10.90</PRICE>
    <YEAR>1995</YEAR>
  </CD>
  <CD>
    <TITLE>1999 Grammy Nominees</TITLE>
    <ARTIST>Many</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Grammy</COMPANY>
    <PRICE>10.20</PRICE>
    <YEAR>1999</YEAR>
  </CD>
  <CD>
    <TITLE>For the good times</TITLE>
    <ARTIST>Kenny Rogers</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Mucik Master</COMPANY>
    <PRICE>8.70</PRICE>
    <YEAR>1995</YEAR>
  </CD>
  <CD>
    <TITLE>Big Willie style</TITLE>
    <ARTIST>Will Smith</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Columbia</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1997</YEAR>
  </CD>
  <CD>
    <TITLE>Tupelo Honey</TITLE>
    <ARTIST>Van Morrison</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Polydor</COMPANY>
    <PRICE>8.20</PRICE>
    <YEAR>1971</YEAR>
  </CD>
  <CD>
    <TITLE>Soulsville</TITLE>
    <ARTIST>Jorn Hoel</ARTIST>
    <COUNTRY>Norway</COUNTRY>
    <COMPANY>WEA</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1996</YEAR>
  </CD>
  <CD>
    <TITLE>The very best of</TITLE>
    <ARTIST>Cat Stevens</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Island</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1990</YEAR>
  </CD>
  <CD>
    <TITLE>Stop</TITLE>
    <ARTIST>Sam Brown</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>A and M</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1988</YEAR>
  </CD>
  <CD>
    <TITLE>Bridge of Spies</TITLE>
    <ARTIST>T'Pau</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Siren</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Private Dancer</TITLE>
    <ARTIST>Tina Turner</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>Capitol</COMPANY>
    <PRICE>8.90</PRICE>
    <YEAR>1983</YEAR>
  </CD>
  <CD>
    <TITLE>Midt om natten</TITLE>
    <ARTIST>Kim Larsen</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Medley</COMPANY>
    <PRICE>7.80</PRICE>
    <YEAR>1983</YEAR>
  </CD>
  <CD>
    <TITLE>Pavarotti Gala Concert</TITLE>
    <ARTIST>Luciano Pavarotti</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>DECCA</COMPANY>
    <PRICE>9.90</PRICE>
    <YEAR>1991</YEAR>
  </CD>
  <CD>
    <TITLE>The dock of the bay</TITLE>
    <ARTIST>Otis Redding</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>Stax Records</COMPANY>
    <PRICE>7.90</PRICE>
    <YEAR>1968</YEAR>
  </CD>
  <CD>
    <TITLE>Picture book</TITLE>
    <ARTIST>Simply Red</ARTIST>
    <COUNTRY>EU</COUNTRY>
    <COMPANY>Elektra</COMPANY>
    <PRICE>7.20</PRICE>
    <YEAR>1985</YEAR>
  </CD>
  <CD>
    <TITLE>Red</TITLE>
    <ARTIST>The Communards</ARTIST>
    <COUNTRY>UK</COUNTRY>
    <COMPANY>London</COMPANY>
    <PRICE>7.80</PRICE>
    <YEAR>1987</YEAR>
  </CD>
  <CD>
    <TITLE>Unchain my heart</TITLE>
    <ARTIST>Joe Cocker</ARTIST>
    <COUNTRY>USA</COUNTRY>
    <COMPANY>EMI</COMPANY>
    <PRICE>8.20</PRICE>
    <YEAR>1987</YEAR>
  </CD>
</CATALOG>

***************************** Test 3 -  Wrong user inputs ************************************************************

Data successfully written to file 'output.xml'

Do u wish to get downloaded data from website on your email id?
 Please enter Y/N: f
Please enter valid choice
Do u wish to get downloaded data from website on your email id?
 Please enter Y/N: N
Okay, you are good to go and process downloaded file in editor


***************************** Test 4 - Email could not be sent *********************************************************

Data successfully written to file 'output.xml'

Do u wish to get downloaded data from website on your email id?
 Please enter Y/N: Y
Enter receiver's email id: ajinkyawani
Enter subject of the email: sfc
Failed to send mail


Process finished with exit code 0
"""