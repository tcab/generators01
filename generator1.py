__author__ = 'Andy'

def gen1():
    yield(1)
    yield(2)

def gen2():
    for i in range(1, 10):
        yield(i)

def gen3(n):
    for i in range(n):
        yield(i+1)

def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    g = gen1()
    print g.next()
    print g.next()

    print '-'*50

    g = gen2()
    print g.next()
    print g.next()
    print g.next()
    for i in g:
        print 'looping', i

    print '-'*50

    g = gen3(5)
    for i in g:
        print 'loop to five:', i

    print 'done'

if __name__ == '__main__':
    main()

