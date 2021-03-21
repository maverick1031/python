import argparse


class Options:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('-c', '--color', metavar='yellow|green', type=str, default='green', help='color of record')

        self.opts = self.parser.parse_args()

    def load(self):
        return self.opts


if __name__ == '__main__':
    o = Options()
    opts = o.load()
    print(opts.color)
