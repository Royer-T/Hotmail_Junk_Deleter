import imaplib
import os
import tkinter as tk
from dotenv import load_dotenv
from tkinter import messagebox

'''
This script connects to the Hotmail IMAP server using SSL and logs in with
your email address and password. It then selects the "Junk" folder and searches
for all messages in that folder. If there are any messages, it marks each one
for deletion and then actually deletes them by calling the expunge method.
Finally, it closes the connection to the IMAP server.

Note that this script assumes that you have enabled IMAP access for your
Hotmail account. If you haven't done so, you'll need to enable it first in
your account settings. Additionally, this script only deletes messages in the
"Junk" folder; if you want to delete messages in other folders, you'll need to
modify the select method call accordingly.
'''

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