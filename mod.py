import sys

def bin(x):
    y = x * x
    return y

if __name__ == '__main__':
    x = float(sys.argv[1])
    sys.stdout.write(str(bin(x)))
    