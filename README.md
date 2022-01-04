# Automated Invoice Generator
This is a python program which will read data from a spreadsheet and generate an invoice with the same. <br />
Prerequisites: <br />
A] Enabling API access:
   1) Go to https://console.developers.google.com <br />
   2) Search and enable Google Drive API and Sheets API.
B] Allowing access through a service account : https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account
C] Creating an app password: 
   1) Go to https://myaccount.google.com
   2) Search for app passwords
   3) In select app choose other and enter a custom name. 
   4) Click on generate and copy the password displayed into the program.
   In case you haven't enabled 2-factor authentication, you simply need to search for less secure app access in your google account and enable it.  
D] Installing gspread and pillow modules. To do this, type pip install gspread in your command/terminal and press enter. Use pip install pillow for pillow.  
   
