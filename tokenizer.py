import tokenize

def method_for_it(token):
    return token.strip().replace(" ", "_").replace("\"","" ) + "(self)"

def translate(readline):
    previous_name = ""
    for type, name,_,_,_ in tokenize.generate_tokens(readline):
        if type ==tokenize.NAME and name =='describe':
            yield tokenize.NAME, 'class'
        elif type ==tokenize.NAME and name =='it':
            yield tokenize.NAME, 'def'
        elif type == 3 and previous_name == 'it': 
            yield 3, method_for_it(name)
        else:
            yield type,name
        previous_name = name
            
            
import codecs, cStringIO, encodings
from encodings import utf_8

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kwargs):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = tokenize.untokenize(translate(self.stream.readline))
        self.stream = cStringIO.StringIO(data)

def search_function(s):
    if s!='pyspec': return None
    utf8=encodings.search_function('utf8') # Assume utf8 encoding
    return codecs.CodecInfo(
        name='pyspec',
        encode = utf8.encode,
        decode = utf8.decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=StreamReader,
        streamwriter=utf8.streamwriter)

codecs.register(search_function)


