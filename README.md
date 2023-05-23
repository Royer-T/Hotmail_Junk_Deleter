# Hotmail_Junk_Deleter
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
