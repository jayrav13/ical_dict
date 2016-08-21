#!/usr/bin/env python

#
#   Imports
#
import sys
import os
import urllib2


###
#   class iCalDict
#
class iCalDict():

    ###
    #   convert(ics_file, mapping = {})
    #
    #   Given a string ics_file, which is either a file path or URL,
    #   convert the ics file to a Dictionary.
    #
    #   Optionally, include a mapping to convert ics keys to customized
    #   Dictionary keys.
    #
    def convert(self, ics_file, mapping = {}):

        content = self.file_get_contents(ics_file)

        content = [x.rstrip("\r\n") for x in content]

        return content

    ###
    #   file_get_contents
    #
    #   Given a string ics_file, which is either a file path or URL,
    #   return the contents of the file.
    #
    def file_get_contents(self, ics_file):

        content = None

        if os.path.isfile(ics_file):
            content = open(ics_file, 'r').readlines()
        else:
            content = urllib2.urlopen(ics_file).readlines()

        return content


###
#   Testing the above.
#
if __name__ == '__main__':
    converter = iCalDict()
    # print converter.convert('http://25livepub.collegenet.com/calendars/NJIT_EVENTS.ics')
    print [x for x in converter.convert('events.ics')]
