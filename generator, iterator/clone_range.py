class CloneRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
        self.start = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        print("Clone range: ")
        return self

    def __next__(self):
        if self.start < self.stop:
            if self.step < 0:
                raise StopIteration
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start
        else:
            if self.step > 0:
                raise StopIteration
            self.start += self.step
            if self.start <= self.stop:
                raise StopIteration
            return self.start


for i in CloneRange(1, 4, 1):
    print(i)