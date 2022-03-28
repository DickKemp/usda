import requests
import json
import re

def json_list_stream(fd):

    context = None
    header = None

    if not context:
        except_str = 'Extra data: line \d+ column \d+ .*\(char (\d+).*\)'
        e_pat = re.compile(except_str)

        context = { Context.STREAM_SOFAR : "",
                    Context.EX_PATTERN : e_pat}

    chunk = fd.readline()
    while chunk:
        doc, context = consume_docs(context, chunk)
        if doc:
            yield doc
        chunk = fd.readline()

class Context:
    STREAM_SOFAR = "stream_so_far"
    EX_PATTERN = "e_pat"

def consume_docs(context, chunk):
    doc = None
    so_far = "".join([context[Context.STREAM_SOFAR], chunk])
    end_pos = 0

    try:
        json.loads(so_far)
    except ValueError as e:
        m = context[Context.EX_PATTERN].match(e.args[0])
        if m:
            end_pos = int(m.groups()[0])
            doc = json.loads(so_far[:end_pos])
    if doc:
        context[Context.STREAM_SOFAR]  = so_far[end_pos+1:]
    else:
        context[Context.STREAM_SOFAR]  = so_far
    return doc, context

