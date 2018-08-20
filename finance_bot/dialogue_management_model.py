from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

from wxpy import *

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'domain.yml',
					model_path = './models/dialogue',
					training_data_file = './data/stories.md'):
					
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])
	
	agent.train(
				training_data_file,
				epochs = 300,
				batch_size = 50,
				validation_split = 0.2)
				
	agent.persist(model_path)
	return agent
	
def run_weather_bot(serve_forever=True):
	interpreter = RasaNLUInterpreter('./models/current/nlu_model')
	agent = Agent.load('./models/dialogue', interpreter = interpreter)

	if serve_forever:
		agent.handle_channel(ConsoleInputChannel())
		
	return agent
'''
	bot = Bot(console_qr=True, cache_path=True)
	my_friend = bot.friends()
	
	@bot.register(msg_types = FRIENDS)
	def auto_accept_friends(msg):
		new_friend = msg.card.accept()
		new_friend.send("I've accept your friend request. Now we can talk anything!")

	@bot.register(bot.self, except_self=False)
	def reply_self(msg):
		intent = interpreter.parse(msg.text)["intent"]["name"]

		ans = agent.handle_message(msg.text)
		print(ans)

		return 'received: {} ({})'.format(msg.text, msg.type)

	@bot.register(my_friend)
	def reply_my_friend(msg):
		intent = interpreter.parse(msg.text)["intent"]["name"]

		ans = agent.handle_message(msg.text)
		print(ans)

		return ans[0]['text']
	
	embed()
'''
if __name__ == '__main__':
#	train_dialogue()
	run_weather_bot()
