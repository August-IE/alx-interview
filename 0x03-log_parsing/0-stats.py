#!/usr/bin/python3
"""
HTTP request log parsing and metrics
"""

import sys
import re


def parse_log_line(line: str) -> tuple:
    """
    Parses a single line of HTTP request log.
    Returns a tuple containing status code and file size.
    """
    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
                       r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
                       r'"GET /projects/260 HTTP/1.1" (\S{3}) (\d+)')
    match = regex.match(line)
    if match:
        return match.group(3), int(match.group(4))
    else:
        return None, 0


def update_statistics(log: dict, status_code: str, file_size: int) -> None:
    """
    Updates the statistics based on the provided status code and file size.
    """
    log["file_size"] += file_size
    if status_code in log["code_frequency"]:
        log["code_frequency"][status_code] += 1


def output_statistics(log: dict) -> None:
    """
    Outputs the accumulated statistics of the HTTP request log.
    """
    print("File size:", log["file_size"])
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print(code + ":", log["code_frequency"][code])


if __name__ == "__main__":
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0
            for code in [200, 301, 400, 401, 403, 404, 405, 500]
        }
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            status_code, file_size = parse_log_line(line)
            if status_code is not None:
                update_statistics(log, status_code, file_size)
                line_count += 1
                if line_count % 10 == 0:
                    output_statistics(log)
                else:
                    continue  # skip lines with wrong format
    except KeyboardInterrupt:
        pass
    finally:
        output_statistics(log)
