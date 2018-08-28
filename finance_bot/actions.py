from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from iexfinance import Stock
from iexfinance import get_historical_data
from iexfinance import get_available_symbols
import matplotlib.pyplot as plt

from datetime import datetime, date, timedelta

import re 


class ActionCurrentPrice(Action):
	def name(self):
		return "action_current_price"

	def run(self, dispatcher, tracker, domain):

		company_x = tracker.get_slot('company')

		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]


		companyobj = Stock(company)
		price = companyobj.get_price()

		response = """{} shares is {} currently.""".format(company, price)
		dispatcher.utter_message(response)
		return [SlotSet('company', company)]


class ActionOpen(Action):
	def name(self):
		return "action_open"

	def run(self, dispatcher, tracker, domain):
		company_x = tracker.get_slot('company')
		time = tracker.get_slot('time')

		print(company_x)
		print(time)
		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]

		pattern = re.compile(r'\.|-|/')
		end_x = re.split(pattern, time)
		end = datetime(int(end_x[0]), int(end_x[1]), int(end_x[2]))
		# start = end - timedelta(1)
		end_date = end.strftime('%Y-%m-%d')
		f = get_historical_data(company, end, end, output_format="pandas")
		openprice = f.loc[end_date]["open"]
		response = """{}'s opening price is {} on {}""".format(company, openprice, time)
		dispatcher.utter_message(response)
		return [SlotSet('company', company), SlotSet('time', time)]


class ActionClose(Action):
	def name(self):
		return "action_close"

	def run(self, dispatcher, tracker, domain):
		company_x = tracker.get_slot('company')
		time = tracker.get_slot('time')

		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]
				
		pattern = re.compile(r'\.|-|/')
		end_x = re.split(pattern, time)
		end = datetime(int(end_x[0]), int(end_x[1]), int(end_x[2]))
		# start = end - timedelta(1)
		end_date = end.strftime('%Y-%m-%d')
		f = get_historical_data(company, end, end, output_format="pandas")
		closingprice = f.loc[end_date]["close"]
		response = """{}'s closing price is {} on {}""".format(company, closingprice, time)
		dispatcher.utter_message(response)
		return [SlotSet('company', company), SlotSet('time', time)]


class ActionVolume(Action):
	def name(self):
		return "action_volume"

	def run(self, dispatcher, tracker, domain):
		company_x = tracker.get_slot('company')
		time = tracker.get_slot('time')

		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]
				
		pattern = re.compile(r'\.|-|/')
		end_x = re.split(pattern, time)
		end = datetime(int(end_x[0]), int(end_x[1]), int(end_x[2]))
		#start = end - timedelta(1)
		end_date = end.strftime('%Y-%m-%d')
		f = get_historical_data(company, end, end, output_format="pandas")
		volume = f.loc[end_date]["volume"]
		response = """{}'s volume is {} on {}""".format(company, volume, time)
		dispatcher.utter_message(response)
		return [SlotSet('company', company), SlotSet('time', time)]



class ActionPeak(Action):
	def name(self):
		return "action_peak"

	def run(self, dispatcher, tracker, domain):
		company_x = tracker.get_slot('company')
		time = tracker.get_slot('time')

		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]
				
		pattern = re.compile(r'\.|-|/')
		end_x = re.split(pattern, time)
		end = datetime(int(end_x[0]), int(end_x[1]), int(end_x[2]))
		# start = end - timedelta(1)
		end_date = end.strftime('%Y-%m-%d')
		f = get_historical_data(company, end, end, output_format="pandas")
		peak = f.loc[end_date]["high"]
		response = """{}'s peak is {} on {}""".format(company, peak, time)
		dispatcher.utter_message(response)
		return [SlotSet('company', company), SlotSet('time', time)]


class ActionHistoricalPlot(Action):
	def name(self):
		return "action_historical_plot"

	def run(self, dispatcher, tracker, domain):
		company_x = tracker.get_slot('company')
		start_time = tracker.get_slot('start_time')
		end_time = tracker.get_slot('end_time')
		pattern = re.compile(r'\.|-|/')
		start_x = re.split(pattern, start_time)
		end_x = re.split(pattern, end_time)
		start = datetime(int(start_x[0]), int(start_x[1]), int(start_x[2]))
		end = datetime(int(end_x[0]), int(end_x[1]), int(end_x[2]))
		symbols = get_available_symbols()
		for i in range(len(symbols)):
			if company_x.lower() in symbols[i]["name"].lower():
				company = symbols[i]["symbol"]

		f = get_historical_data(company, start, end, output_format = 'pandas')
		plt. plot(f["close"])
		plt.title('Time series chart for {}'.format(company))
		fig1 = plt.gcf()
		plt.draw()
		fig1.savefig("1.jpg", dpi=100)
		dispatcher.utter_template("utter_plot", tracker)
		plt.show()
		return [SlotSet('company', company), SlotSet('start_time', start), SlotSet('end_time', end)]
