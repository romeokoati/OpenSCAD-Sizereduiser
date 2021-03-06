#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""OpenSCAD Minimizer - Reduce the size of your .scad file
<http://github.com/romeokoati/OpenSCAD-Sizereduiser>

Default syntax:

osm < input_file

Description:

Removes unnecessary character data.

Examples:

osm < old.scad > new.scad
    Minimize old.scad and save the result in new.scad.

Bugs:

Please email bug reports including a minimal test file (if applicable) to
koati at knracademie dot com.
"""

__author__ = 'KOATI NEMALEU ROMEO'
__email__ = 'koati@knracademie.com'
__copyright__ = 'Copyright (C) 2022 KOATI NEMALEU ROMEO'
__license__ = 'GPLv3'

from re import compile, sub, DOTALL, MULTILINE
from signal import signal, SIGPIPE, SIG_DFL
import sys

COMMENT_RE = compile(
    r'(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    DOTALL | MULTILINE
)

signal(SIGPIPE, SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""


def _comment_replacer(match):
    start,mid,end = match.group(1,2,3)
    if mid is None:
        # single line comment
        return ''
    elif start is not None or end is not None:
        # multi line comment at start or end of a line
        return ''
    elif '\n' in mid:
        # multi line comment with line break
        return '\n'
    else:
        # multi line comment without line break
        return ' '


def remove_comments(text):
    """
    Remove single- and multi-line comments.

    Thanks to MizardX for the code
    <http://stackoverflow.com/questions/844681/python-regex-question-stripping-multi-line-comments-but-maintaining-a-line-break/844721#844721>.
    """
    return COMMENT_RE.sub(_comment_replacer, text)


def remove_empty_start_end(text):
    """Remove empty lines of text in the input."""
    text = sub(r'\A\n+', r'', text) # Start
    text = sub(r'\n+\Z', r'', text) # End
    return text


def remove_multiple_whitespace(text):
    """."""
    text = sub(r'(\s)\s+', r'\1', text)
    return text


def remove_whitespace(text):
    """Whitespace around operators, commas, braces, parentheses, and line
    endings."""
    text = sub(r'\s*([+*/=,{}();-])\s*', r'\1', text)
    return text


def osm(stream):
    """Run the minimizations."""
    text = stream.read()
    text = remove_comments(text)
    text = remove_empty_start_end(text)
    text = remove_multiple_whitespace(text)
    text = remove_whitespace(text)
    return text


def main(argv = None):
    result = osm(sys.stdin)
    print result

if __name__ == '__main__':
    sys.exit(main())
