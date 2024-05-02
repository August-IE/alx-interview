#!/usr/bin/env python3
'''A script for parsing HTTP request logs and metrics.
'''

import sys
import signal

# Define status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}
line_count = 0


def print_stats():
    print("File size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    print()


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) != 7:
        continue
    try:
        ip_address, date, request, status_code, file_size = parts[:5]
        status_code = int(status_code)
        file_size = int(file_size)
        if status_code in STATUS_CODES:
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
    except ValueError:
        continue
