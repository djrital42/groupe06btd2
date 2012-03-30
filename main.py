"""Test Git"""
from operators import add, mul
from logic import and_, or_


def main():
    """fonction main"""

    print "My application starts..."
    a = 2
    b = 3
    x = True
    y = False
    print add(a, b)
    print mul(x, y)
    print and_(x, y)
    print or_(a, b)

if __name__ == "__main__":
    main()
