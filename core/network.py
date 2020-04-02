import asyncio
import socket
import struct
import select

class UDP_worker:
    PORT = 44544

    async def listen(self):
        self.__addr = socket.getaddrinfo()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setblocking(False)
        self.__socket.bind()