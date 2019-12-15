import os
import sys
import re

if len(sys.argv) < 2:
    print('Use a file for input')
    quit()

variable = {}
chr = 0
source = ''

with open(sys.argv[1]) as file:
    source = file.read()


def squeeze():
    global chr

    while chr < len(source) and source[chr] in [' ', '\t', '\n']:
        chr += 1


def handle_assignment():
    global chr

    var_name = re.findall(r'^([a-zA-Z0-9]+)\s+?=', source[chr:])[0]

    chr += len(var_name)
    squeeze()
    chr += 1
    squeeze()

    var_content = ''

    if source[chr] == '0':
        print('error')
        while source[chr] != '\n':
            chr += 1
        chr += 1
    elif source[chr] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        while source[chr] != '\n':
            var_content += source[chr]
            chr += 1
        variable[var_name] = int(var_content)

    squeeze()
    print('%s = %s' % (var_name, variable[var_name]))


while chr < len(source):
    if re.match(r'^([a-zA-Z0-9]+)\s+?=', source[chr:]):
        handle_assignment()
        continue

    chr += 1
