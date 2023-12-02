#!/bin/bash
xelatex dissertation.tex
makeindex dissertation.nlo -s nomencl.ist -o dissertation.nls
biber dissertation
xelatex dissertation.tex
xelatex dissertation.tex

