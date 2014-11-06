from classes import *

latexBegin = r'''
\newcommand{\includecodelang}[2]{\lstinputlisting[escapechar=, language=#2]{#1}}
\newcommand{\includecode}[1]{\lstinputlisting[escapechar=]{#1}}

'''

latexIncludeCode = "\\includecode{%s}"
latexIncludeCodeLang = "\\includecodelang{%s}{%s}"

latexFileHeading = "\\%s{%s\label{%s:%s}}"
latexFileHeadingNoLabel = "\\%s{%s}"

latexReplacements = {
    '\t': '\\ ' * 4,
    '&': '\\&',
    '%': '\\%',
    '$': '\\$',
    '#': '\\#',
    '_': '\\_',
    '{': '\\{',
    '}': '\\}',
    '~': '\\textasciitilde ',
    '^': '\\textasciicircum '
}

def escapeForLatex(text):
    text = text.replace('\\', '\\textbackslash')
    text = text.replace(' ', '\\ ')
    text = text.replace('\\textbackslash', '\\textbackslash ')

    for i, j in latexReplacements.items():
        text = text.replace(i, j)

    text = text.replace('"', '\char`\"{}')
    return text

def output_start(out_file):
    out_file.write(latexBegin)

def output(filename, rel_path, out_file):
    out_file.write("%" * 80)
    out_file.write("\n")
    out_file.write("%% %s\n\n" % rel_path)

    if settings.shouldAddLabel:
        # apparently, no escape in labels
        heading = latexFileHeading % (settings.headingStyle, escapeForLatex(rel_path), settings.labelPrefix, rel_path)
    else:
        heading = latexFileHeadingNoLabel % (settings.headingStyle, escapeForLatex(rel_path) )

    out_file.write(heading)
    out_file.write("\n")


    language = None

    for key in fileExtensionMap:
        if filename.endswith(key):
            language = fileExtensionMap[key]
            break

    if language is None:
        include_line = latexIncludeCode % (filename)
    else:
        include_line = latexIncludeCodeLang % (filename, language)

    out_file.write(include_line)
    out_file.write("\n")

    out_file.write("\n")


fileExtensionMap = {
    '.erl'    : 'erlang'
  , '.hs'     : 'Haskell'
  , '.py'     : 'Python'
  , '.java'   : 'Java'
  , '.sh'     : 'sh'
  , '.bash'   : 'bash'
  , '.sml'    : 'ML'
  , '.sig'    : 'ML'
}

