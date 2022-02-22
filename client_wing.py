
import random
import time
import client_float as cf    #send_float address arg (both is strings)

	#parser = argparse.ArgumentParser()
	#parser.add_argument("--ip", default="127.0.0.1",help="The ip of the OSC server")
	#parser.add_argument("--port", type=int, default=9000,help="The port the OSC server is listening on")
	#args = parser.parse_args()
	
def main():
	
	
	while(True):
		for i in range(random.randint(1,3)):
			rands=0.5*random.random()+0.5
			sendNum=0
			velocity=0
			acc=1
			while sendNum<rands:
				if acc==1:
					velocity+=0.01
					sendNum+=velocity
				elif acc == 2:
					velocity-=0.01
					sendNum+=velocity

				if velocity<=0:
					break
				elif sendNum*2<=rands:
					acc=1
				else:
					acc=2
				sendNum=round(sendNum,3)
				cf.send_float("/avatar/parameters/wings",str(sendNum))
				time.sleep(0.005)
			
			time.sleep(0.1)

			velocity=0
			acc=2
			while sendNum>0:
				if acc == 2:
					velocity-=0.01
					sendNum+=velocity
				elif acc == 1:
					velocity+=0.01
					sendNum+=velocity

				if velocity>=0:
					break
				elif sendNum*2>=rands:
					acc=2
				else:
					acc=1
				sendNum=round(sendNum,3)
				cf.send_float("/avatar/parameters/wings", str(sendNum))
				time.sleep(0.005)

			cf.send_float("/avatar/parameters/wings", str(0))
			time.sleep(random.random()*0.2)

		time.sleep(10*random.random()+0.5)


if __name__ == "__main__":
	
	main()