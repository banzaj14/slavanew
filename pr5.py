#!/usr/bin/env python
Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
DaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
for cntr in range(0,12):
    print '%s has %d days.' % (Months[cntr],DaysInMonth[cntr])
