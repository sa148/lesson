# オプショナル引数 #
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text')
    args = parser.parse_args()
    print(args.text)