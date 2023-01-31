# コマンドライン引数help使い方 #
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers',
                         help='調べたい数値を入れてください',
                         type=int,
                         nargs=3)
    args = parser.parse_args()
    print(args.numbers)