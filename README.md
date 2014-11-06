Generate `lstlisting`
===================

Useful when teachers require that you *"The report should contain all your source code in appendices."*

For each file it creates a heading *(like section/subsection -- is
customizable)* labels it with the filename *(also customizable)*, and lastly
includes it using `lstinputlisting` -- maybe even setting the language parameter
if it regonizes the extension.

Requirements
============

* Python 3.2+
* a TeX enviroment with the `lstlisting` package

Usage
=====

    $ generatelstlisting.py <DIR>

This will create the file `generated-lstlisting.tex` in your current directory.

========================

To change the path of output file, use the `-o` options, like so

    $ generatelstlisting.py -o path/output.tex <DIR>

*- adding options to the end is also accepted*

========================

To learn about the "advanced" options run `SOMEPATH/generatelstlisting.py --help` *(like changing the section level to "subsubsection")*

========================

For more LaTeX source code listing generation, see my [difftotex repo](https://github.com/RasmusWL/difftotex).
