#! /usr/bin/env python3
#######################################################################################

import pprint
import bookmarks_parser

#######################################################################################


def run():
    bookmarks = bookmarks_parser.parse("bookmarks2.html")
    pprint.pprint(bookmarks)


if __name__ == '__main__':
    run()


##
#

