#Imports
import requests
from bs4 import BeautifulSoup
import time


class Corona:
	def __init__(self):
		print("Made By : Marwan Darwish")
		time.sleep(1)

    #input from user
		contry = str(input("Enter the contry : "))
    
		#Url , response , source , soup  
		self.url = f"https://www.worldometers.info/coronavirus/country/{contry}/"

		self.response = requests.get(self.url)

		self.source = self.response.content

		self.soup = BeautifulSoup(self.source , "html.parser")

	def findData(self):
		#Find the div 
		self.cases = self.soup.find_all("div" , class_="maincounter-number")

		#Data list
		self.data = []

		#Find the span and get the data from it
		for i in self.cases:
			self.span = i.find("span")
			self.data.append(self.span.string)
		print(f"total cases is : {self.data[0]}")
		print(f"total Deaths is : {self.data[1]}")
		print(f"total Recovered is : {self.data[2]}")
        





if __name__ == "__main__":
	c = Corona()
	c.findData()
