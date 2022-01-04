import gspread
from PIL import Image, ImageDraw, ImageFont
import smtplib
import imghdr
from email.message import EmailMessage
gc = gspread.service_account(filename='path/to/the/downloaded/file.json')
sh = gc.open_by_url("spreadsheet_url")
worksheet = sh.worksheet("worksheet_title")
invoiceuid_list = worksheet.col_values(1)
names_list = worksheet.col_values(2)
emails_list = worksheet.col_values(3)
address_list = worksheet.col_values(4)
itemdescription_list = worksheet.col_values(5)
amount_list = worksheet.col_values(6)
date = '28th December, 2021'

invoiceuid_list.remove(invoiceuid_list[0])
names_list.remove(names_list[0])
emails_list.remove(emails_list[0])
address_list.remove(address_list[0])
itemdescription_list.remove(itemdescription_list[0])
amount_list.remove(amount_list[0])

img = Image.open('Path/To/Invoice/Template.jpg')

n = len(names_list)
for i in range(0, n):
    invoiceuid = invoiceuid_list[i]
    name = names_list[i]
    mailid = emails_list[i]
    address = address_list[i]
    itemdescription = itemdescription_list[i]
    amount = amount_list[i]

    title_font1 = ImageFont.truetype(r'C:\Users\mayan\AppData\Local\Microsoft\Windows\Fonts\futura.ttf', 24)
    title_font2 = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 16)
    title_font3 = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 21)
    title_font4 = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 21)
    title_font5 = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 23)
    title_font6 = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 19)

    d1 = ImageDraw.Draw(img)
    # (x,y) coordinates determine the position of text.
    d1.text((0, 0), invoiceuid, fill="Black", font=title_font4)
    d1.text((100, 100), name, fill="Black", font=title_font1)
    d1.text((200, 200), mailid, fill="Black", font=title_font2)
    d1.text((300, 300), address, fill="Black", font=title_font2, align='left')
    d1.text((400, 400), date, fill="Black", font=title_font4)
    d1.text((500, 500), itemdescription, fill="Black", font=title_font4)
    d1.text((600, 600), amount, fill="Black", font=title_font4)
    # img.show()

    str2 = names_list[i]
    str3 = '.pdf'
    # str3 = '.jpg'
    # str3 = '.png'
    str = str2 + str3
    img.save(str)

    msg = EmailMessage()
    msg['Subject'] = 'Subject_of_Mail'
    msg['From'] = 'Your_EmailId'
    msg['To'] = mailid
    content = "Main_content_of_Mail"
    msg.set_content(content)
    files = [str]

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            # To determine filetype if file is an image
            # file_type = imghdr.what(f.name)
            file_name = f.name

        msg.add_attachment(file_data, maintype='application', subtype='octet-string', filename=file_name)
        # For images,
        # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
         smtp.login('Your_EmailId', 'Your_Password')
         smtp.send_message(msg)
    print(names_list[i], "Invoice sent")