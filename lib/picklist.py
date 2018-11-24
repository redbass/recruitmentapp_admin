import csv


def csv_to_json_values(csv_file):
    reader = csv.DictReader(csv_file,
                            delimiter=',',
                            fieldnames=['key', 'value'],
                            skipinitialspace=True)

    for row in reader:
        if row['key'] and row['value']:
            row['key'] = row['key'].rstrip()
            row['value'] = row['value'].rstrip()
            yield dict(row)
