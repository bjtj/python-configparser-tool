from configparsertool import getvalues


def main():
    values = getvalues('config.ini', 'default', ('a', 'b', 'c', 'd'))
    assert(values == ['A', 'B', 'C', 'D'])
    a,b,c,d = getvalues('config.ini', 'default', ('a', 'b', 'c', 'd'))
    assert(a == 'A')
    assert(b == 'B')
    assert(c == 'C')
    assert(d == 'D')
    try:
        getvalues('notexists', 'default', ('a',))
    except Exception as e:
        print('expected: "{}"'.format(e))

if __name__ == '__main__':
    main()


