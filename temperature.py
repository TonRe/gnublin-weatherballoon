#! /usr/bin/python
import os

class Temperature(object):
	
	def __init__(self):
		self.device = "/dev/lpc313x_adc"
		self.select_gpa()
	
	def select_gpa(self):
		"""
		Waehlt einen AD-Kanal aus.
		"""
		adc_file = os.open(self.device, os.RDWR)
		os.write(adc_file, "0x0001")
		os.close(adc_file)

	def get_adc(self):
		"""
		Liest den Wert des AD-Wandlers aus
		"""
		adc_file = os.open(self.device, os.O_RDONLY)
		result = os.read(adc_file, 256)
		os.close(adc_file)
		return result[:-1]

	def calculateTemperature(self, amountOfValues):
		"""
		Berechnet die Temperatur aus einem Hexadezimalen String
		"""
		try:
			count = 0
			temp = 0
			while count != amountOfValues:
				temp += int(self.get_adc(), 16)
				count++
			
			return (temp / amountOfValues)
		except Exception as e:
			raise TemperatureException("Can't calculate the temperature")
