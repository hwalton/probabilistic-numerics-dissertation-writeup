#!/bin/bash
xelatex dissertation.tex
biber dissertation
xelatex dissertation.tex
xelatex dissertation.tex

