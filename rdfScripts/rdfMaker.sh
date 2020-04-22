#!/bin/sh
#Script to convert a file to another file
#Made by Runar Reve
#Fixed by Robert Radley

#argv[1] in file
#argv[2] outfile


zcat ${1} | awk '{print "<http://string-db.org/" $1 ">\t<http://interaction>\t<http://string-db.org/" $2 "> ."}' | awk '{if (NR !=1) {print}}' > ${2}


