import argparse
import csv
import json
import os
from typing import Any, Dict, List

ENCODING = 'UTF-8'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='Convert CSV file to JSON Django fixture')
parser.add_argument('input_file', type=str, help='Input file (csv)')
parser.add_argument('model', type=str, help='Model name')
parser.add_argument('--indent', type=int, default=4, help='Indent (default: 2)')
parser.add_argument('--pk', type=str, default='id', help='Pk filed name (default: id)')
args = parser.parse_args()


def convert(filepath: str, model: str, pk_field_name: str = 'id') -> List[Dict[str, Any]]:
    with open(filepath, encoding=ENCODING) as csv_file:
        results = []
        for line in csv.DictReader(csv_file):
            fields = {}
            for k, v in line.items():
                if k == pk_field_name:
                    continue

                if v.isdigit():
                    value = int(v)
                elif v.lower() == 'true':
                    value = True
                elif v.lower() == 'false':
                    value = False
                else:
                    value = v
                fields[k] = value

            results.append({
                'model': model,
                'pk': int(line.pop(pk_field_name)),
                'fields': fields
            })

        return results


def write_results(filename: str, data: List[Dict[str, Any]], indent: int):
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    print(f'File {filename} converted successfully')


def main():
    data = convert(filepath=args.input_file, model=args.model, pk_field_name=args.pk)
    output_file = os.path.join(BASE_DIR, os.path.splitext(os.path.basename(args.input_file))[0] + '.json')
    write_results(filename=output_file, data=data, indent=args.indent)


if __name__ == '__main__':
    main()
