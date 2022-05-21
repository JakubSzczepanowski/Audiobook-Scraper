

class ConsoleProgressBar:

    def __init__(self, total: int, prefix='', suffix='', length = 100, fill = '█', printEnd = "\r"):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.printEnd = printEnd
        self.printProgressBar(0)

    def printProgressBar(self, writed: int):
        percent = 100 * (writed / float(self.total))
        if percent > 100:
            percent = 100.0
        percent_str = ("{0:.2f}").format(percent)
        
        filledLength = int(self.length * writed // self.total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(f'\r{self.prefix} |{bar}| {percent_str}% {self.suffix}', end = self.printEnd)