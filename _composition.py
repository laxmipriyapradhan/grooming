class Engine:
    def __init__(self, ncylinders, bhp):
        self.bhp = bhp
        self.ncylinders = ncylinders

    def start(self):
        print('Engine Started')

    def stop(self):
        print('Engine Stopper')

    def accelerate(self):
        print('Accelerating Engine')


class Car:
    def __init__(self, model, color, year, engine):
        self.model = model
        self.color = color
        self.year = year
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def accelerate(self):
        self.engine.accelerate()


toyota = Car('Innova', 'White', 2020, Engine(4, 147))
hyundai = Car('Creta', 'Black', 2020, Engine(4, 123))

# -------------------------------------------------------------------------------
# problem with sub-classes
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class CSVFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        import csv
        csv_writer = csv.writer(self.file)
        csv_writer.writerow(message)
        self.file.flush()

class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern

    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)
            
# -------------------------------------------------------------------------------
# Customized Logger class
class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.log(message)

class FilteredLogger(Logger):
    def __init__(self, pattern, handler):
        self.pattern = pattern
        super().__init__(handler)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Implementation of each class is hidden from the user.
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class CSVFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        import csv
        csv_writer = csv.writer(self.file)
        csv_writer.writerow(message)
        self.file.flush()
