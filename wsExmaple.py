import websocket
from threading import Thread
import time
import json
import sys


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

data={
    "name":"fromClient",
    "data":
    {
        "case":"start"
    }
}

## controlCMDAbs/controlCMDRel
message={
    "name":"fromClient",
    "data":
    {
        "case":"controlCMDAbs",
        "velocity": {
        "pan": [5,5,5,5],
        "tilt": [5,5,5,5]
        },
        "position": {
            "pan": [-20,20,-20,20],
            "tilt": [-20,20,-20,20]
        }
    }
    
    }
def on_open(ws):
    def run(*args):
        for i in range(2):
            # send the message, then wait
            # so thread doesn't exit and socket
            # isn't closed
            if i ==0 :
                ws.send(json.dumps(data))
            else:
                ws.send(json.dumps(message))
            time.sleep(1)
        for i in range (20):
            time.sleep(1)
        
        time.sleep(1)
        ws.close()
        print("Thread terminating...")

    Thread(target=run).start()


if __name__ == "__main__":
    websocket.enableTrace(True)
    if len(sys.argv) < 2:
        host = "ws://10.42.0.1:2100/ws"
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()