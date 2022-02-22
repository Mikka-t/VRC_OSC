
import argparse
import random
import time
import sys

from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

	#parser = argparse.ArgumentParser()
	#parser.add_argument("--ip", default="127.0.0.1",help="The ip of the OSC server")
	#parser.add_argument("--port", type=int, default=9000,help="The port the OSC server is listening on")
	#args = parser.parse_args()
	
def send_float(address,arg):
	IP = '127.0.0.1'
	PORT = 9000

	client = udp_client.UDPClient(IP, PORT)

	#client.send_message("/avatar/parameters/wings", 1.0)
	#print('Address: '+address)
	print('Arg: '+str(arg))
	msg = OscMessageBuilder(address=address)
	msg.add_arg(float(arg))
	m = msg.build()
	client.send(m)


if __name__ == "__main__":
	address = sys.argv[1]
	arg = sys.argv[2]
	send_float(address,arg)