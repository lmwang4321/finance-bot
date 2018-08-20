from rasa_nlu.model import Metadata, Interpreter

def load_model():
	interpreter = Interpreter.load('models/current/nlu_model')
	print(interpreter.parse("can you show me the stock value of BIDU from 2018.5.2 to 2018.8.10?"))

if __name__ == "__main__":
	load_model()