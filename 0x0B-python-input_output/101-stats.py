#!/usr/bin/python3
"""
    Script file
"""
import sys


def print_msg(size, status):
    print("File size: {}".format(size))
    for count in sorted(status):
        print("{}: {}".format(count, status[count]))


if __name__ == '__main__':
    cnt = 0
    size = 0
    status = {}

    try:
        for line in sys.stdin:
            if cnt == 10:
                print_msg(size, status)
                cnt = 1
            else:
                cnt += 1

            chunks = line.split()
            try:
                size = int(chunks[-1])
            except Exception:
                pass

            code_status = chunks[-2]
            if code_status in {'200', '301', '400', '401', '403', '404', '405',
                               '500'}:
                if status.get(code_status, -1) < 0:
                    status[code_status] = 1
                else:
                    status[code_status] += 1
        print_msg(size, status)
    except KeyboardInterrupt:
        print_msg(size, status)
