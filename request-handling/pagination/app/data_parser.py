from csv import DictReader
from itertools import islice


def get_data_from_csv(data_file, page, list_size=10):
    with open(data_file, encoding='cp1251') as csv_file:
        csv_reader = DictReader(csv_file)
        start = (page - 1) * list_size
        stop = (page - 1) * list_size + list_size
        data = []
        for row in islice(csv_reader, start, stop):
            data.append(row)
        try:
            is_next_page = bool(csv_reader.__next__())
        except StopIteration:
            is_next_page = False
        return data, is_next_page