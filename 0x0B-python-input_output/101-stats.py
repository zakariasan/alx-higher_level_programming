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
            cnt += 1

            chunks = line.split()
            if (len(chunks) >= 2):
                try:
                    file_size = int(chunks[-1])
                except (IndexError, ValueError):
                    pass
                code_status = chunks[-2]
                size += file_size

                if code_status in {'200', '301', '400', '401', '403', '404',
                                   '405', '500'}:
                    status[code_status] = status.get(code_status, 0) + 1
            if cnt % 10 == 0:
                print_msg(size, status)
    except KeyboardInterrupt:
        print_msg(size, status)
