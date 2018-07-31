from multiprocessing import Process, Value, Lock
import multiprocessing
import logging

lock = Lock()


class Adder(Process):

    def __init__(self, counter, logger):
        super(Adder, self).__init__()
        self.counter = counter
        self.logger = logger

    def run(self):
        for _ in range(50):
            with lock:
                self.counter.value += 1
                self.logger.info('Added 1.')


if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    shared_counter = Value('i', lock=True)
    shared_counter.value = 0
    adders = [Adder(shared_counter, logger) for _ in range(5)]
    [a.start() for a in adders]
    [a.join() for a in adders]
    print(shared_counter.value)
