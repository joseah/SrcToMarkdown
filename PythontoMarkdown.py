#!/usr/bin/python

#' ---
#' title:        python2markdown
#' author:       Jose Alquicira Hernandez
#' ---


#' | Parameters |                  Description                  |
#' |:----------:|:---------------------------------------------:|
#' | -s         | script file (with comments in markdown style) |
#' | -o         |              output format (html)             |
#' | -c         |                    css file                   |


#' # Usage example
#'
#' ```shell
#' python PythontoMarkdown.py -s example.pl -o html -c kult.css 
#' ```
#'


#' Import `sys` library for managing command parameters
import sys

#' Import `re` library for using regular expressions
import re

#' Import `io to deal with text enconding
import io

# Import pandoc wrapper

###############################
## Install pypandoc via:      #  
## "sudo pip install pypandoc"#
###############################

import pypandoc

#' Import `argparse` to handle command-line arguments
import argparse

parser = argparse.ArgumentParser(description='Gets parameters.')
parser.add_argument("-s", required=True)
parser.add_argument("-o", required=True)
parser.add_argument("-c", required=False)
args = parser.parse_args()


#' Flag variables
comment = 0
code = 0
prev = 0

#' Open output markdown file
filename = args.s.replace(".py", "")

md = []
#' Open file via a connection
file = open(args.s, 'r')

#' Convert script to markdown format 

for l in file:
    l = l.strip('\n')
    md_comm =  re.match(".*^[#]{1}[']{1}.*", l)
    comment_begins  =  l.find("'''#")
    comment_ends  =  l.find("'''")

    # If a comment ends, indicate that a comment has finished
    if(comment_ends != -1 and prev == 1):
        comment = 0
        continue

    # If a comment begins, indicate that there is a comment
    if(comment_begins != -1):
        comment = 1
        

    # If we are within a comment, print all lines
    if(comment == 1):
        if l.find("'''#") == -1:
            md.append(l)
 
    #' If a comment has started it means that the chunk of code has finished. End chunk of code and indicate
    #' that there is no code anymore.
    if(md_comm != None and code and comment == 0):
        md.append("```")
        code = 0

    #' If we are within a markdown comment, format line and append
    if(md_comm and comment == 0):
        l_format = re.sub("#'\s*", '', l)
        md.append(l_format)

    #' If a comment has not started it means that there is a chunk of code. 
    #' Print markdown code label and indicate that code has started

    if(md_comm == None and code == 0 and comment == 0):
        if(l != ''):
            md.append("\n```python")
            code = 1    

    #' If a comment has not started, there is code we want to append
    if(md_comm == None and code and comment == 0):
        if(l != ''):
            md.append(l)

    prev = comment
    
file.close()

if(code):
    md.append("```")

#' Join list of lines
md = '\n'.join(md)

#' Write raw markdown file
md_file = open(filename + ".md", "w")
md_file.write(''.join(md))
md_file.close()

#' # Convert markdown to output format

if args.c:
    output_file = pypandoc.convert(md, args.o, format = "md", extra_args=['-c' + args.c, '--toc', '-N'])
else:
    output_file = pypandoc.convert(md, args.o, format = "md")


#' # Write html output
output = io.open(filename + "." + args.o, "w", encoding='utf8')
output.write(output_file)
output.close()