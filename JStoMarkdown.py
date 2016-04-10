#!/usr/bin/python

# Title:        Convert .js scripts to markdown and html
# Author:       Jose Alquicira Hernandez <alquicirajose at gmail.com>
# Status:       Active
# Type: Process
# Created:      09-Mar-2016
# Post-History: 16-Mar-2016
# Python version: 2.6.6

# Parameters:
# 1st = .js file
# 2nd = .output file format
# 3rd (Optional)= css file


# Import "sys" library for managing command parameters
import sys

# Import "re" library for using regular expressions
import re

import io

# Import pandoc wrapper

###############################
## Install pypandoc via:      #  
## "sudo pip install pypandoc"#
###############################

import pypandoc


data = sys.argv[1] # js file
output_format = sys.argv[2] # output format
css = sys.argv[3] # output format

# Flag variables
comment = 0
code = 0

# Open output markdown file
filename = sys.argv[1].replace(".js", "")

md = []
# Open file via a connection
file = open(data, 'r')
for l in file:
        l = l.strip('\n')
        comment_begins  =  re.match(".*[/]+[*]+.*", l)
        comment_ends  =  re.match(".*[*]+[/]+.*", l)
        
        # If a comment ends, indicate that a comment has finished
        if(comment_ends != None):
            comment = 0

         # If we are within a comment, print all lines
        if(comment == 1):
             md.append(l)

        # If a comment begins, indicate that there is a comment
        if(comment_begins != None):
            comment = 1

        # If a comment ends, indicate that a comment has finished
        if(comment_ends != None):
            comment = 0

        # If a comment has not started and has not ended it means that there is a chunk of code. 
        # Print markdown code label and indicate that code has started
        if(comment == 0 and code == 0):
            if(l != '' and l != "*/"):
                md.append("\n```js")
                code = 1

        # If a comment has not started and has not ended it and there is code we want to print all lines
        if(comment == 0 and code):
            if(l != '' and l != "*/"):
                md.append(l)

        # If a comment has started it means that the chunk of code has finished. End chunk of code and indicate
        # that there is no code anymore.
        if(comment_begins != None and code):
            md.append("```")
            code = 0
      
file.close()

if(comment == 0):
    md.append("```")

# Join list of lines
md = '\n'.join(md)

# Write raw markdown file
md_file = open(filename + ".md", "w")
print >> md_file, ''.join(md)
md_file.close()

# Convert markdown to output format

output_file = pypandoc.convert(md, output_format, format = "md", extra_args=['-c ' + css])


# Write html output
output = io.open(filename + "." + output_format, "w", encoding='utf8')
# print >> output, output_file
output.write(output_file)
output.close()