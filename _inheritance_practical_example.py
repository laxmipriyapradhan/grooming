import csv

class Covid:
    def __init__(self, country, cases, per_million):
        self.country = country
        self.cases = cases
        self.per_million = per_million


filename = '_covid_data.csv'
types = [str, str, int, float]
records = []


def read_csv(filename, types):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skipping headers
        for row in rows:
            converted = [func(val) for func, val in zip(types, row)]
            country, _date, cases, per_million = converted
            records.append(Covid(country, cases, per_million))
    return records


data = read_csv(filename, types)


def print_table(objects, colnames, formatter):
    formatter.headings(colnames)

    for obj in objects:
        row = [str(getattr(obj, col)) for col in colnames]
        formatter.rows(row)


class TableFormatter:  # Acts as a design specification
    def headings(self, headers):
        raise NotImplementedError

    def rows(self, row):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    def __init__(self, width=10):
        self.width = width

    def headings(self, headers):
        for header in headers:
            print(f'{header:>{self.width}}', end='')
        print()

    def rows(self, row):
        for item in row:
            print(f'{item:>{self.width}}', end='')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def rows(self, row):
        print(','.join(row))


class HTMLFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def rows(self, row):
        print('<tr>', end='')
        for item in row:
            print(f'<td>{item}</td>', end='')
        print('<tr>')


class Quoted:
    def rows(self, row):
        r = [f'"{item}"' for item in row]
        super().rows(r)


class QuotedFormatter(Quoted, TextTableFormatter):
    pass


text = TextTableFormatter(20)
_csv = CSVTableFormatter()
a = QuotedFormatter()
html = HTMLFormatter()
print_table(data, ['Country', 'Cases', 'Per_million'], text)