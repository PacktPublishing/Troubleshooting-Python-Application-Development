from multiprocessing import Process, Value, Lock


lock = Lock()


class Adder(Process):

    def __init__(self, counter):
        super(Adder, self).__init__()
        self.counter = counter

    def run(self):
        for _ in range(50):
            # self.counter.value += 1
            with lock:
                self.counter.value += 1


if __name__ == '__main__':
    shared_counter = Value('i', lock=True)
    shared_counter.value = 0
    adders = [Adder(shared_counter) for _ in range(5)]
    [a.start() for a in adders]
    [a.join() for a in adders]
    print(shared_counter.value)
