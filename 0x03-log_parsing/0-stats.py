#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing metrics.
'''
import re


def extract_input(input_line):
        '''Extracts sections of a line of an HTTP request log.
            '''
                format_parts = (
                                r'\s*(?P<ip>\S+)\s*',
                                        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                                                r'\s*"(?P<request>[^"]*)"\s*',
                                                        r'\s*(?P<status_code>\S+)',
                                                                r'\s*(?P<file_size>\d+)'
                                                                    )
                    info = {'status_code': 0, 'file_size': 0}
                        log_format = '{}\\-{}{}{}{}\\s*'.format(*format_parts)
                            match = re.fullmatch(log_format, input_line)
                                if match is not None:
                                            info['status_code'] = match.group('status_code')
                                                    info['file_size'] = int(match.group('file_size'))
                                                        return info


                                                    def print_statistics(total_file_size, status_codes_stats):
                                                            '''Prints the accumulated statistics of the HTTP request log.
                                                                '''
                                                                    print('File size: {:d}'.format(total_file_size), flush=True)
                                                                        for status_code, num in sorted(status_codes_stats.items()):
                                                                                    if num > 0:
                                                                                                    print('{:s}: {:d}'.format(status_code, num), flush=True)


                                                                                                    def update_metrics(line, total_file_size, status_codes_stats):
                                                                                                            '''Updates the metrics from a given HTTP request log.

                                                                                                                Args:
                                                                                                                        line (str): The line of input from which to retrieve the metrics.

                                                                                                                            Returns:
                                                                                                                                    int: The new total file size.
                                                                                                                                        '''
                                                                                                                                            line_info = extract_input(line)
                                                                                                                                                status_code = line_info['status_code']
                                                                                                                                                    status_codes_stats[status_code] += 1
                                                                                                                                                        return total_file_size + line_info['file_size']


                                                                                                                                                    def run():
                                                                                                                                                            '''Starts the log parser.
                                                                                                                                                                '''
                                                                                                                                                                    line_num = 0
                                                                                                                                                                        total_file_size = 0
                                                                                                                                                                            status_codes_stats = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
                                                                                                                                                                                try:
                                                                                                                                                                                            while True:
                                                                                                                                                                                                            line = input()
                                                                                                                                                                                                                        total_file_size = update_metrics(line, total_file_size, status_codes_stats)
                                                                                                                                                                                                                                    line_num += 1
                                                                                                                                                                                                                                                if line_num % 10 == 0:
                                                                                                                                                                                                                                                                    print_statistics(total_file_size, status_codes_stats)
                                                                                                                                                                                                                                                                        except (KeyboardInterrupt, EOFError):
                                                                                                                                                                                                                                                                                    print_statistics(total_file_size, status_codes_stats)


                                                                                                                                                                                                                                                                                    if __name__ == '__main__':
                                                                                                                                                                                                                                                                                            run()
