#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    file_object = open(filename, 'r')
    file_content = file_object.read()

    year_string = search_year_in_file(file_content)
    if not year_string:
        return 'year not found...'

    result = [year_string]
    top_names_lines = re.findall('<td>(\d+)</td><td>(\w[^<]*)</td><td>(\w[^<]*)</td>', file_content)
    for top_name_line in top_names_lines:
        result.append(top_name_line[1] + ' ' + top_name_line[0])
        result.append(top_name_line[2] + ' ' + top_name_line[0])
    return sorted(result)


def search_year_in_file(file_content):
    year_line_match = re.search('Popularity in.*', file_content)
    if not year_line_match:
        return None

    year_line = year_line_match.group()
    year_str_match = re.search('\d\d\d\d', year_line)
    if not year_str_match:
        return None

    return year_str_match.group()


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for file_name in args:
        names_list = extract_names(file_name)

        if not summary:
            print names_list
        else:
            file_object = open(file_name + '.summary', 'w')
            for line in names_list:
                file_object.write("%s\n" % line)
            file_object.close()

if __name__ == '__main__':
    main()
