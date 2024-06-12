import csv

from src.variables import CSV_DATA_PATH


def test_vector_database(vector_db):
    with open(CSV_DATA_PATH, 'r', newline='') as file:
        reader = csv.reader(file)
        line_count = sum(1 for row in reader)

    index_stats = vector_db._index.describe_index_stats()

    assert index_stats['dimension'] == 1536
    assert index_stats['total_vector_count'] == line_count - 1
