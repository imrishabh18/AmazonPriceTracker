import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/Lotto-Mens-Vertigo-Running-Shoes/dp/B072X2BGM5?pf_rd_p=694b9d36-2eb6-4ee4-8d67-51e8321505be&pd_rd_wg=eq6Ju&pf_rd_r=29TQXNKHN0YWE69A93ZM&ref_=pd_gw_unk&pd_rd_w=tkc0C&pd_rd_r=67fe2820-7191-4138-9422-6cd8e7e346a7&th=1&psc=1'

headers={"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def checkPrice():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id='productTitle').get_text()
    price=soup.find(id='priceblock_ourprice').get_text()
    converted_price=float(price.replace('\u20b9',' '))

    if(converted_price<700):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('LOGIN_EMAIL','PASSWORD')

    subject='WRITE_THE_SUBJECT'
    body='WRITE_THE_BODY'

    msg=f'Subject:{subject}\n\n{body}'

    server.sendmail(
        'FROM_EMAIL',
        'TO_EMAIL',
        msg
    )
    #print('HEY I HAVE DONE IT')
    server.quit()

checkPrice()