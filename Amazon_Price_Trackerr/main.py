from bs4 import BeautifulSoup
import smtplib
import requests

MY_EMAIL = "name@mail.com"
MY_PASSWORD = "passwordpassword"
url = "amazon.com/link"
headers = {'Accept-Language': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0"}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
price = int(price.strip(","))

if price <= 850:
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price alert.\n\nYour selected item is now {price}$\n {url}.")
