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
            try:
                file_size = int(chunks[-1])
            except (IndexError, ValueError):
                pass
            try:
                code_status = chunks[-2]
                size += file_size

                if code_status in {'200', '301', '400', '401', '403', '404',
                                   '405', '500'}:
                    if status.get(code_status, -1) == -1:
                        status[code_status] = 1
                    else:
                        status[code_status] += 1
            except IndexError:
                pass
            if cnt % 10 == 0:
                print_msg(size, status)
    except KeyboardInterrupt:
        print_msg(size, status)
