import time
import multiprocessing

def hey(name):
	while True:
		print("Hello ", name)
		time.sleep(1)
if __name__ == "__main__":
	p1 = multiprocessing.Process(target=hey, args=("ali",))
	p1.start()
	multiprocessing.Process(target=hey, args=("veli",)).start()
	multiprocessing.Process(target=hey, args=("ayse",)).start()
	multiprocessing.Process(target=hey, args=("orxan",)).start()
