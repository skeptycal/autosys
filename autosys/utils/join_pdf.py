#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Michael Treanor
# Contact: skeptycal@gmail.com
# Copyright: 2020 Michael Treanor
# License: MIT
""" join - Join pages from a collection of PDF files into a single PDF file.

    Usage:
        join FILES [--output <file>] [--shuffle] [--verbose]

    Parameters:
        --shuffle
            Take a page from each PDF input file in turn before
            taking another from each file. If this option is not
            specified then all of the pages from a PDF file are
            appended to the output PDF file before the next input
            PDF file is processed.

        --verbose
            Write information about the progress of this tool to stderr.

    # modified version of code from macOS Automator (macOS 10.15.4)
    /System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py

    """

__docformat__ = 'reStructuredText'

std_inp = "AREPL requires standard_input to be hardcoded, like so: standard_input = 'hello world'; print(input())"

for d in dir():
    print(d)
    print('-' * 60)
    try:
        print(eval(d))
    except:
        print(eval(d + '()'))
    print('-'*60)

# print(__doc__)

"""
import sys
import os
import getopt
import tempfile
import shutil
from CoreFoundation import *
from Quartz.CoreGraphics import *

verbose = False


def createPDFDocumentWithPath(path):
    global verbose
    if verbose:
        print("Creating PDF document from file {}".format(path))
    return CGPDFDocumentCreateWithURL(CFURLCreateFromFileSystemRepresentation(kCFAllocatorDefault, path, len(path), False))


def writePageFromDoc(writeContext, doc, pageNum):
    global verbose
    page = CGPDFDocumentGetPage(doc, pageNum)
    if page:
        mediaBox = CGPDFPageGetBoxRect(page, kCGPDFMediaBox)
    if CGRectIsEmpty(mediaBox):
        mediaBox = None

    CGContextBeginPage(writeContext, mediaBox)
    CGContextDrawPDFPage(writeContext, page)
    CGContextEndPage(writeContext)
    if verbose:
        print("Copied page %d from %s" % (pageNum, doc))


def shufflePages(writeContext, docs, maxPages):

    for pageNum in xrange(1, maxPages + 1):
        for doc in docs:
            writePageFromDoc(writeContext, doc, pageNum)


def append(writeContext, docs, maxPages):

    for doc in docs:
        for pageNum in xrange(1, maxPages + 1):
            writePageFromDoc(writeContext, doc, pageNum)


def main(argv):

    global verbose

    # The PDF context we will draw into to create a new PDF
    writeContext = None

    # If True then generate more verbose information
    source = None
    shuffle = False

    # Parse the command line options
    try:
        options, args = getopt.getopt(argv, "o:sv", ["output=", "shuffle", "verbose"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for option, arg in options:
        if option in ("-o", "--output"):
            if verbose:
                print("Setting %s as the destination." % (arg))
            writeContext = CGPDFContextCreateWithURL(CFURLCreateFromFileSystemRepresentation(
                    kCFAllocatorDefault, arg, len(arg), False), None, None)

        elif option in ("-s", "--shuffle"):
            if verbose:
                print("Shuffle pages to the output file.")
            shuffle = True

        elif option in ("-v", "--verbose"):
            print("Verbose mode enabled.")
            verbose = True

        else:
            print("Unknown argument: %s" % (option))

    if writeContext:
        # create PDFDocuments for all of the files.
        docs = map(createPDFDocumentWithPath, args)

    # find the maximum number of pages.
    maxPages = 0
    for doc in docs:
        if CGPDFDocumentGetNumberOfPages(doc) > maxPages:
            maxPages = CGPDFDocumentGetNumberOfPages(doc)

    if shuffle:
        shufflePages(writeContext, docs, maxPages)
    else:
        append(writeContext, docs, maxPages)

    CGPDFContextClose(writeContext)
    del writeContext
    #CGContextRelease(writeContext)


def usage():
    print("Usage: join FILES [--output <file>] [--shuffle] [--verbose]")


if __name__ == "__main__":
    main(sys.argv[1:])
"""
