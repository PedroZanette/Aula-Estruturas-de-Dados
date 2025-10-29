from datetime import datetime


class TimeElapsed:

    def __init__(self):
        self.start_time = datetime.now()
        self.elapsed_time = None

    def finish(self):
        self.elapsed_time = (datetime.now() - self.start_time)


def get_sorted_list(amount):
    return [i for i in range(amount)]



