import codecs

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.nodes import Const, Macro

class WriteFileExtension(Extension):
    tags = {'writefile'}
    files = {}

    def __init__(self, environment):
        super(WriteFileExtension, self).__init__(environment)    

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = ''
        mdFile = [parser.parse_expression()]
         # if there is a comma, the user provided a timeout.  If not use
        # None as second parameter.
        macroName = Const("writeFileReference")
        if parser.stream.skip_if("comma"):
            macroName = parser.parse_expression()
        context = self.call_method('get_context')

        body = parser.parse_statements(['name:endwritefile'], drop_needle=True)
        
        return nodes.CallBlock(self.call_method('_write_file', mdFile, macroName, context), [], [], body).set_lineno(lineno)

    def _write_file(self, mdFile, macroName, context, caller):
        body = caller()
        if len(mdFile) and body:
            fileOpenMode='w'
            if mdFile in self.files:
                fileOpenMode='a'
            with open(mdFile,mode=fileOpenMode, encoding='utf-8') as fh:
                fh.write(body)
                fh.write("\n")
            self.files[mdFile]=True
        
        # ability to write refenrence to new mdFile
        return nodes.Macro(macroName, [mdFile, context], [], body)