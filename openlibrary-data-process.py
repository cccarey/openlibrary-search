#!/usr/bin/env python3

import csv
import sys

input = sys.argv[1]
err_output = "%s_errors" % input

csv.field_size_limit(sys.maxsize)

csv_writers = {}

def open_csv(record_type):
    return csv.writer(open("%s_%s" % (input, record_type), 'w', newline=''), delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)

def write_row(record_type, row):
    if record_type not in csv_writers:
        csv_writers[record_type] = open_csv(record_type)
    csv_writers[record_type].writerow([row[0], row[1], row[2], row[3], row[4]])

with open(err_output, 'w') as err_ouput_file:
    with open(input, 'r') as csvinputfile:
        csvreader = csv.reader(csvinputfile, delimiter='\t')
        for row in csvreader:
            if len(row) > 4:
                record_type = row[0].split("/")[2]
                write_row(record_type, row)
            else:
                err_output_file.write(row)
                err_output_file.flush()

        print('Finished reading')

print('Finished writing')