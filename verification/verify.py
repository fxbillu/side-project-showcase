#!/usr/bin/env python3
"""Offline verification of the published simulated-data examples (Python 3 only)."""
import csv
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = Decimal


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rows(name):
    with (ROOT / 'data' / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def main():
    manifest = json.loads((ROOT / 'evidence-manifest.json').read_text())
    for name, expected in manifest['sha256'].items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected,
                'File hash mismatch: ' + name)
    inventory = rows('r1-inventory.csv')
    quantity = sum((D(r['quantity']) for r in inventory), D(0))
    value = sum((D(r['value']) for r in inventory), D(0))
    require(len(inventory) == 2 and quantity == D('74') and value == D('740'),
            'R1 inventory expected two warehouses,74 units,value740')
    statement = rows('r1-statement.csv')
    balance = D(0)
    for row in statement:
        balance += D(row['amount']) - D(row['settlement'])
        require(balance == D(row['balance']), 'Statement running balance mismatch')
    require(len(statement) == 6 and balance == 0, 'R1 six rows must settle to zero')
    batches = json.loads((ROOT / 'data' / 'settlement-batches.json').read_text())
    order = batches['order']
    expected_total = (D(order['quantity']) * D(order['unitPrice'])).quantize(D('.01'), rounding=ROUND_HALF_UP)
    require(expected_total == D(order['totalAmount']) == D('1.01'), 'Order total mismatch')
    amounts = [D(r['settlementAmount']) for r in batches['batchesByApprovalTime']]
    require(amounts == [D('.34'), D('.33'), D('.34')] and sum(amounts) == expected_total,
            'Preserved batch settlement amounts mismatch')
    require(all(r['status'] == 'REVERSED' for r in batches['batchesByApprovalTime']),
            'Excerpt must retain actual reversed status')
    print(json.dumps({'status': 'PASS', 'arithmeticExamples': 3,
                     'inventory': {'quantity': str(quantity), 'value': str(value)},
                     'statementFinalBalance': str(balance),
                     'preservedBatchAmounts': [str(n) for n in amounts],
                     'limits': 'Checks published snapshots and arithmetic only; does not rerun backend or prove current live balances.'},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
