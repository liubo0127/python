#!coding: utf-8

import os
import argparse


def find_file(path, keywords):
    flag = ''
    length = len(keywords)
    for i, j, k in os.walk(path):
        if len(k) > 0:
            for f in k:
                for x in range(length):
                    if keywords[x] not in f:
                        flag = False
                        break
                if flag:
                    print os.path.join(i, f)
                flag = True


def parse_args():
    parser = argparse.ArgumentParser(description='Find file in a path')
    parser.add_argument('--path', dest='path', help='The path to find, default: /', default='/')
    parser.add_argument('--keywords', dest='keywords', nargs='*', help='The keyword to find, default: null', default='')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    find_file(args.path, args.keywords)
