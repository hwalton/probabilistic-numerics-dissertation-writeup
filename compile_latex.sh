#!/bin/bash
xelatex dissertation.tex
makeindex dissertation.nlo -s nomencl.ist -o dissertation.nls
biber dissertation
xelatex dissertation.tex
xelatex dissertation.tex

# Clean up auxiliary files
rm dissertation.aux
rm dissertation.bbl
rm dissertation.bcf
rm dissertation.blg
rm dissertation.ilg
rm dissertation.log
rm dissertation.nlo
rm dissertation.nls
rm dissertation.out
rm dissertation.toc
# Add any other generated files you want to delete
