import re
import functools

import spacy
from spacy.tokens import Doc, Span, Token

from commonregex import regexes

NLP = spacy.load('en')


def token_in_range(token, start, end):
    """
    Does a token's start and end character idxs overlap with 
    a provided start and end character idx?

    [--[++++]------]
    """
    token_start = token.idx
    token_end = token.idx + len(token.text)
    return (
        (token_start < end <= token_end) or 
        (start < token_end <= end)
    )



def get_regex(doc, regex):
    """
    Given a regex, find all valid matches within the spacy document and 
    return list of spans that match the extracted text
    """
    matches = re.finditer(regex, doc.text)

    if not len(doc):
        return []

    span_start = None
    span_end = None

    spans = []
    for match in matches:
        for token in doc:
            if token_in_range(token, match.start(), match.end()):
                if not span_start:
                    # create new span
                    span_start = token.i
                else:
                    # extend existing span
                    span_end = token.i + 1
            else:
                if span_start and span_end:
                    spans.append(doc[span_start:span_end])
                span_start = None
                span_end = None

        if span_start and span_end:
            spans.append(doc[span_start:span_end])
    
    return spans


def get_token_end_idx(token):
    """
    Get index of token's final character in doc
    """
    return token.idx + len(token.text)


def get_start_char_idx(span):   
    """
    Get index of span's first character in doc
    """
    return span[0].idx


def get_end_char_idx(span):
    """
    Get index of span's final character in doc
    """
    return span[-1].idx + len(span[-1].text)


def add_commonregex_extensions():
    for regex_name, regex in regexes.items():
        Doc.set_extension(regex_name, getter=functools.partial(get_regex, regex=regex))

    # Aliases and niceties
    Span.set_extension('idx', getter=get_start_char_idx)
    Span.set_extension('end_idx', getter=get_end_char_idx)
    Token.set_extension('end_idx', getter=get_token_end_idx)


if __name__ == "__main__":
    text = (
        "John, please get that article on www.linkedin.com to me by 5:00PM "
        "on Jan 9th 2012. 4:00 would be ideal, actually. If you have any "
        "questions, You can reach me at (519)-236-2723x341 or get in touch with "
        "my associate at harold.smith@gmail.com"
    )
    add_commonregex_extensions()
    doc = NLP(text)
    import ipdb; ipdb.set_trace()
