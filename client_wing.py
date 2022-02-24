
import random
import time
import sender    #send_float address arg (both is strings)
import json
# -*- coding: utf-8 -*-

def flap(degree,acc_rate):
	# acc_rateは0.01目安
	# degreeは0-1
	# degreeを1.0にするとVRC側でバグるけどめんどいので直さずに0.999で運用してる
	sendNum=0
	velocity=0
	acc=True
	while sendNum<degree:
		if acc:
			velocity+=acc_rate
			sendNum+=velocity
		else:
			velocity-=acc_rate
			sendNum+=velocity

		if velocity<=0:
			break
		elif sendNum*2<=degree:
			acc=True
		else:
			acc=False
		sendNum=round(sendNum,4)
		if sendNum>=1:
			sendNum = 0.999
		elif sendNum<0:
			sendNum = 0
		sender.send_float("/avatar/parameters/wings",str(sendNum))
		time.sleep(0.005)

	time.sleep(0.1)

	velocity=0
	acc=True
	while sendNum>0:
		if acc:
			velocity-=acc_rate
			sendNum+=velocity
		else:
			velocity+=acc_rate
			sendNum+=velocity

		if velocity>=0:
			break
		elif sendNum*2>=degree:
			acc=True
		else:
			acc=False
		sendNum=round(sendNum,4)
		if sendNum>=1:
			sendNum = 0.999
		elif sendNum<0:
			sendNum = 0
		sender.send_float("/avatar/parameters/wings", str(sendNum))
		time.sleep(0.005)
	sendNum = 0
	sender.send_float("/avatar/parameters/wings", str(sendNum))
	

def wing_emo():
	while True:
		with open('communicate_VCrecog.json') as f:
			value = json.load(f)
		freq = value["num"]
		patapata = value["patapata"]
		awkward = value["awkward"]
		positive = value["positive"]
		print("awkward: ",awkward)
		print("patapata:",patapata)
		print("positive:",positive)
		if awkward:
			data_write = {"num":float(0),"patapata":False,"awkward":False,"positive":positive}
			with open('communicate_VCrecog.json','w') as f:
				json.dump(data_write,f)
			print("now this is awkward")
			time.sleep(10)
		elif patapata:
			data_write = {"num":float(0.8),"patapata":False,"awkward":False,"positive":positive}
			with open('communicate_VCrecog.json','w') as f:
				json.dump(data_write,f)
			print("flap: 0.75, 0.03")
			flap(0.75,0.03)
			time.sleep(0.1)
			print("flap: 1, 0.03")
			flap(0.999,0.03)
			print("patapata'd")
			time.sleep(3+random.random())
		else:
			for i in range(random.randint(1,2)):
				print("flap: ",1-(i*0.2),", 0.01")
				flap(0.999-(i*0.2),0.01+0.01*random.random())
				time.sleep(0.2)
			time.sleep(3+(1-freq)*5*(1+random.random())+2*random.random())


# emotionとは独立に動く
def wing_rand():
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
				sender.send_float("/avatar/parameters/wings",str(sendNum))
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
				sender.send_float("/avatar/parameters/wings", str(sendNum))
				time.sleep(0.005)

			sender.send_float("/avatar/parameters/wings", str(0))
			time.sleep(random.random()*0.2)

		time.sleep(10*random.random()+0.5)


if __name__ == "__main__":
	
	wing_emo()