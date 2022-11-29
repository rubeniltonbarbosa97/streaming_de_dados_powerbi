import requests
import random
import datetime
import time

print("Streaming de Dados - Power bi")

URL = "https://api.powerbi.com/beta/1096f5e7-4729-42f2-a640-2ee479abdd16/datasets/a85ee10a-94cd-40e0-b03b-c5f8dad34841/rows?responseError=UserNotLicensedru%3Dhttps%3A%2F%2Fapp.powerbi.com%2F%3FresponseError%3DUserNotLicensedru%253Dhttps%253A%252F%252Fapp.powerbi.com%252Fgroups%252Fme%252Fapps%253FrefreshAccessToken%253Dtrue%26pbi_source%3Dweb_nolicense_redirect%26redirectedFromSignup%3D1%26noSignUpCheck%3D1%26ScenarioId%3DSignup&redirectedFromSignup=1&redirectedWaitSimple=1&key=cd%2F5UMKL99ykz8WjKyINsvQuEefe52nAqa85PwEUdmou3NecxFqKUwHZKktuhjDakjDtX6n3ywj9Do6EayNPMg%3D%3D"

data = []

for i in range(150):
	data = []
	datahora = datetime.datetime.now()
	datahoraformatada = datahora.strftime("%Y-%m-%d %H:%M:%S")
	temp = random.randint(30,40)
	umidade = random.randint(10,70)
	registro = { "Data": datahoraformatada, "Temperatura": temp, "UmidadeRelativa": umidade}
	data.append(registro)
	requests.post(url = URL, json = data)
	time.sleep(0.2)

print(data)