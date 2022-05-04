#!/usr/bin/env python3
# -*- coding=utf-8 -*-
def my_argparse(host, filename, iface):
    print(host)
    print(filename)
    print(iface)


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = "usage: python arg_parse.py ipaddress -f filename -i interface"

    parser = ArgumentParser(usage=usage)

    parser.add_argument("-f", "--file", dest="filename", help="Write content to FILE", default='1.txt', type=str)
    parser.add_argument("-i", "--interface", dest="iface", help="Specify an interface", default=1, type=int)
    parser.add_argument(nargs='?', dest="host", help="Specify an host", default='10.1.1.1', type=str)
    # parser.add_argument(nargs='*', dest="hosts", help="Specify some hosts", default='10.1.1.1 10.1.1.2', type=str)
    args = parser.parse_args()

    my_argparse(args.host, args.filename, args.iface)

