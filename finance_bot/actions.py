from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from iexfinance import Stock
from iexfinance import get_historical_data
import matplotlib.pyplot as plt

from datetime import datetime

import re 

class ActionPrice(Action):
	def name(self):
		return "action_price"

	def run(self, dispatcher, tracker, domain):

		company = tracker.get_slot('company')
		companyobj = Stock(company)
		price = companyobj.get_price()

		response = """{} shares is {} currently.""".format(company, price)
		dispatcher.utter_message(response)
		return [SlotSet('company', company)]


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
		company = company_x.upper()
		f = get_historical_data(company, start, end, output_format = 'pandas')
		plt. plot(f["close"])
		plt.title('Time series chart for {}'.format(company))
		fig1 = plt.gcf()
		plt.draw()
		fig1.savefig("1.jpg", dpi=100)
		dispatcher.utter_template("utter_plot", tracker)
		plt.show()
		return [SlotSet('company', company), SlotSet('start_time', start), SlotSet('end_time', end)]
