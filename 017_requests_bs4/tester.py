import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

r = requests.get('https://www.google.com/search?q=rub+to+eur&sxsrf=AOaemvJBuZl5nvEgOt3jKYRHPqZ1dvKQug%3A1634318858036&source=hp&ei=CbppYdKvO5GSxc8PqqaqwAg&iflsig=ALs-wAMAAAAAYWnIGosPZxwkupFJ1vJYZT1Zx9YA2oAW&ved=0ahUKEwiS2OqX-MzzAhURSfEDHSqTCogQ4dUDCAc&uact=5&oq=rub+to+eur&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABDLATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoECAAQQzoLCC4QgAQQxwEQ0QM6CwguEIAEEMcBEKMCOgsILhCABBDHARCvAToFCC4QgARQuA9Y_h9griNoAXAAeACAAZ0DiAH_DZIBCTAuOC4wLjEuMZgBAKABAbABCg&sclient=gws-wiz', headers=headers)
soup = BS(r.content, 'html.parser')
price = float(soup.find('span', class_='DFlfde SwHCTb')['data-value'])

user_input = input('Please enter amount in EUR: ')
print(float(user_input) / price)
