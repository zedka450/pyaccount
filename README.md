Pyaccount (or Pyacnt)

Pyaccount is a Python extension that allows you to manage profiles: easily create, connect, delete, and greet users.

------------------------------------------------------------ ------

How to use Pyaccount?

1️⃣ Download Pyaccount:

Click on the Code button to the left of the About section of the GitHub repo.
In the drop-down menu, click on Download ZIP at the bottom.
Unzip the downloaded file.

2️⃣ Place your files:

Place your Python script next to the pyaccount.py file.

3️⃣ Import Pyaccount into your code:

`import pyaccount`
At the top of the code.

Main commands:
-Create an account

`pyaccount.enter(NAME, PASSWORD)`

Replace NAME with the account name and PASSWORD with the password.

-Delete an account

`pyaccount.exit(NAME)`
⚠️ The account must be logged in to be deleted.

-Log in to an account

`pyaccount.connect(NAME, PASSWORD)`

Replace NAME and PASSWORD with the account name and password.

-Display a welcome message

`pyaccount.welcome(NAME)`
⚠️ The account must be logged in for the message to be displayed.

---------------------------------------------------------------------------

💡 Tip: Passwords are secured using SHA-256 hashing, so even if someone accesses your JSON file, they won't be able to see the passwords in plain text.
⚠️ The account must be logged in for the message to be displayed.

💡 Tip: Passwords are secured using SHA-256 hashing, so even if someone accesses your JSON file, they will not be able to see the passwords in plain text.
