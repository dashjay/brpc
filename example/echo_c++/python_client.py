from math import exp
import grpc
import echo_pb2
import echo_pb2_grpc
import random
import time
import string

keySize = 4096
size = keySize * 1024
v_large = ''.join(random.choices(string.ascii_lowercase, k=size))
bv_large = str.encode(v_large)

options = [
    ('grpc.max_receive_message_length', 83804160),
    ('grpc.max_send_message_length', 83804160),
]

channel = grpc.insecure_channel('0.0.0.0:8000', [])
client = echo_pb2_grpc.EchoServiceStub(channel)
req = echo_pb2.EchoRequest(message = bv_large)

def send():
    resp = client.Echo(req, timeout=10)
    print(len(resp.message))


if __name__ == '__main__':
    while True:
        try:
            send()
        except KeyboardInterrupt as e:
            break
