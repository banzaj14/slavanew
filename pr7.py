#!/usr/bin/env python
loop = 3
while loop == 3:
    response = raw_input("Enter your name or 'quit' to end ")
    if response == 'quit':
        print 'quiting'
        loop = 0
    else:
        print 'You typed %s' % response
