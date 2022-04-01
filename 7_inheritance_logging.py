import csv

# Logging classes
class ConsoleLogger:
    def log(self, message):
        print(message)

class TextLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message +"\n")
        self.file.flush()

class CSVLogger:
    def __init__(self, file):
        self.file = file

    def log(self, message):

        csv_writer = csv.writer(self.file)
        csv_writer.writerow(message)
        self.file.flush()

# the below class cannot work independently    
class FilteredLogger:
    pattern = None  # class variable
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    pattern = "ERROR"

class FilteredTextLogger(FilteredLogger, TextLogger):
    pattern = "ERROR"
