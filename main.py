import imaplib
import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import messagebox

#  load environment file constants so they are available
load_dotenv()

# these are the email addresses I am looking to manage
email = [
    {os.environ['HOTMAIL_ACCOUNT']: os.environ['HOTMAIL_PASSWORD'],
     os.environ['MSN_ACCOUNT']: os.environ['MSN_PASSWORD']}
]

# loop through the email addresses
for email_dict in email:
    for address, password in email_dict.items():
        # Connect to the Hotmail IMAP server
        imap = imaplib.IMAP4_SSL('imap-mail.outlook.com')
        imap.login(address, password)
        imap.select('Junk')

        # Search for junk mail messages
        status, messages = imap.search(None, 'ALL')

        if messages[0]:
            # Convert the message IDs into a list of message IDs
            message_ids = messages[0].split(b' ')

            # Mark each junk mail message for deletion
            for ids in message_ids:
                imap.store(ids, '+FLAGS', '\\Deleted')

            # Actually delete the marked messages
            imap.expunge()

        # Close the connection to the Hotmail IMAP server
        imap.close()
        imap.logout()

# When your script has finished running:
root = tk.Tk()
root.withdraw()
messagebox.showinfo('Email Maintenance', "'Junk Email' deleted.")
