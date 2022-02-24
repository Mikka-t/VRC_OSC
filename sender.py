
import argparse
import random
import time
import sys

from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

#引数のargは全部str入力
	
def send_float(address,arg):
	IP = '127.0.0.1'
	PORT = 9000

	client = udp_client.UDPClient(IP, PORT)

	print('sent: '+str(arg)+'	to: '+str(address))
	msg = OscMessageBuilder(address=address)
	msg.add_arg(float(arg))
	m = msg.build()
	client.send(m)

def send_int(address,arg):
	IP = '127.0.0.1'
	PORT = 9000

	client = udp_client.UDPClient(IP, PORT)

	print('sent: '+str(arg)+'	to: '+str(address))
	msg = OscMessageBuilder(address=address)
	msg.add_arg(int(arg))
	m = msg.build()
	client.send(m)

def send_str(address,arg):
	IP = '127.0.0.1'
	PORT = 9000

	client = udp_client.UDPClient(IP, PORT)

	print('sent: '+str(arg)+'	to: '+str(address))
	msg = OscMessageBuilder(address=address)
	msg.add_arg(str(arg))
	m = msg.build()
	client.send(m)

if __name__ == "__main__":
	address = sys.argv[1]
	arg = sys.argv[2]
	send_str(address,arg)