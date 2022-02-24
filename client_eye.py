import json
import time
import sender
# -*- coding: utf-8 -*-

def main():
    while True:
        with open('communicate_VCrecog.json') as f:
            value = json.load(f)
        num = value["num"]
        if num >= 0.99:
            sender.send_float("/avatar/parameters/sleep",str(0.3))
        else:
            sender.send_float("/avatar/parameters/sleep",str(0))
        time.sleep(1)



if __name__ == "__main__":
    main()