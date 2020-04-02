import asyncio
import threading

from network import UDP_worker

class AsyncUDPWorker(UDP_worker):

    def __init__(self):
        self.started = False
        self.__loop = None

    def run(self):
        # TODO берем луп и стартуем
        self.__loop = asyncio.get_event_loop()

        self.started = True

    def run_thread(self):
        pass

    def stop(self):
        if not self.started:
            raise RuntimeError('Worker is not started')
        self.__loop.stop()

