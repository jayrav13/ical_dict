#!/usr/bin/env python

###
#   Imports
#
import sys
import os
import urllib2


###
#   class iCalDict
#
#   Convert a .ics file into a Dictionary object.
#
class iCalDict():

    ###
    #   __init__
    #
    #   Create a new iCalDict instance with a string representing a .ics file
    #   (referenced by a string as a file path or URL) and an optional mapping
    #   between .ics file keys and returned keys in the Dictionary.
    #
    def __init__(self, ics_file, mapping = {}):
        self.__ics_file = ics_file
        self.__mapping = mapping
        self.content = self.__file_get_contents(self.__ics_file)
        self.data = None

    ###
    #   convert
    #
    #   Convert the .ics file into a Dictionary.
    #
    def convert(self):

        self.data = self.__sanitize_data()

        self.__validate()

        return self.data
        # return self.content

    ###
    #   __file_get_contents
    #
    #   Retrieve the contents of the .ics file as an array,
    #   separated by line.
    #
    def __file_get_contents(self, content):

        content = None

        if os.path.isfile(self.__ics_file):
            content = open(self.__ics_file, 'r').read()
        else:
            content = urllib2.urlopen(self.__ics_file).read()

        return [line for line in content.split("\r\n")]

    ###
    #   __sanitize_data
    #
    #   Sanitize the class variable such that wrapped lines are
    #   appended to the array elements they belong with.
    #
    def __sanitize_data(self):
        
        output = []

        for line in self.content:

            if len(line) == 0: continue

            if line[0] == ' ':
                output[len(output) - 1] += line
            else:
                output.append(line.rstrip(" ").lstrip(" "))

        return output

    ###
    #   __validate
    #
    #   Validate the .ics file's data and raise exceptions where needed.
    #
    def __validate(self):

        # If the file does not start with "BEGIN:VCALENDAR".
        if self.data[0] is not "BEGIN:VCALENDAR":
            raise Exception(self.__error_messages("invalid_file"))

    ###
    #   __error_messages
    #
    #   Return an error message
    #
    def __error_messages(self, key):

        messages = {
            "invalid_file": "This file is invalid. A .ics file is identified as a file in which the first line is \"BEGIN:VCALENDAR\"."
        }

        if key not in messages: return "An unknown error has occured."

        return messages[key]

###
#   Testing the above.
#
if __name__ == '__main__':
    # converter = iCalDict('http://25livepub.collegenet.com/calendars/NJIT_EVENTS.ics')
    converter = iCalDict('events.ics')
    for x in converter.convert():
        print x
