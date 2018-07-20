import sys

def mod(x):
    y = x * x
    return y

if __name__ == '__main__':
    x = float(sys.argv[1])
    sys.stdout.write(str(mod(x)))