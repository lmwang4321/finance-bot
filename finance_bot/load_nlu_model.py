from rasa_nlu.model import Metadata, Interpreter

def load_model():
	interpreter = Interpreter.load('models/current/nlu_model')
	parser = interpreter.parse("can you show me the historical plot of baidu from 2018.5.3 to 2018.6.3?")

	print(parser["intent"]["name"])

if __name__ == "__main__":
	load_model()