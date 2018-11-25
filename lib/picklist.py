import csv


def csv_to_json_values(csv_file):
    reader = csv.DictReader(csv_file,
                            delimiter=',',
                            fieldnames=['key', 'value'],
                            skipinitialspace=True)

    result = []
    for row in reader:
        if row['key'] and row['value']:
            row['key'] = row['key'].rstrip()
            row['value'] = row['value'].rstrip()
            result.append(row)

    return result


def json_values_to_csv(json_values):
    rows = ['{key},{value}'.format(key=row['key'], value=row['value'])
            for row in json_values]
    return '\n'.join(rows)
