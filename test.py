# coding:utf-8
# -*- coding: utf-8 -*-
# @Time    : 1/9/19 4:16 PM
# @Author  : Kevin
# @Site    : 
# @File    : test.py
# @Descri  : 
# @Software: pycharm

import argparse

import happybase


def connection():
    import happybase

    # c = happybase.Connection('node11.testbigdate', autoconnect=False)

    c = happybase.Connection('10.1.220.8', 9090, autoconnect=False)
    c.open()
    print(c.tables())


def connection2():
    import happybase

    connection = happybase.Connection('10.1.220.8')
    table = connection.table('table-name')

    table.put(b'row-key', {b'family:qual1': b'value1',
                           b'family:qual2': b'value2'})

    row = table.row(b'row-key')
    print(row[b'family:qual1'])  # prints 'value1'

    for key, data in table.rows([b'row-key-1', b'row-key-2']):
        print(key, data)  # prints row key and data for each row

    for key, data in table.scan(row_prefix=b'row'):
        print(key, data)  # prints 'value1' and 'value2'

    row = table.delete(b'row-key')


if __name__ == '__main__':
    connection()

    # connection2()
