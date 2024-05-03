from enum import Enum
from io import FileIO, TextIOWrapper
from typing import TextIO, Union

TYPE_ARRAY = "array"
TYPE_BOOLEAN = "boolean"
TYPE_CONST = "const"
TYPE_ENUM = "enum"
TYPE_INTEGER = "integer"
TYPE_NULL = "null"
TYPE_NUMBER = "number"
TYPE_OBJECT = "object"
TYPE_STRING = "string"

DESCRIPTION = "description"
DEFAULT = "default"
EXAMPLES = "examples"
ITEMS = "items"
TYPE = "type"
REF = "$ref"
FORMAT = "format"

MULTIPLE_OF = "multipleOf"
MAXIMUM = "maximum"
EXCLUSIVE_MAXIMUM = "exclusiveMaximum"
MINIMUM = "minimum"
EXCLUSIVE_MINIMUM = "exclusiveMinimum"

LINE_WIDTH = 80


FileLikeType = Union[TextIO, TextIOWrapper, FileIO]


class DocumentationTemplate(Enum):
    FLAT = "flat"
    JS = "js"
    JS_OFFLINE = "js_offline"
    MD = "md"
    MD_NESTED = "md_nested"

    @property
    def result_extension(self) -> str:
        if self in [self.FLAT, self.JS, self.JS_OFFLINE]:
            return "html"
        if self in [self.MD, self.MD_NESTED]:
            return "md"
        return "html"


DEFAULT_TEMPLATE_FILE_NAME = "base.html"

DEFAULT_CSS_FILE_NAME = "schema_doc.css"
DEFAULT_JS_FILE_NAME = "schema_doc.min.js"
OFFLINE_CSS_FILE_NAMES = [
    "css/bootstrap-4.3.1.min.css",
    "css/facf9fa52c.css",
    "css/font-awesome-4.7.0.min.css",
    "css/overpass300,400,600,800.css",
    "css/schema_doc.css",
]
OFFLINE_FONT_FILE_NAMES = [
    "font/fontawesome-webfont.eot",
    "font/fontawesome-webfont.svg",
    "font/fontawesome-webfont.ttf",
    "font/fontawesome-webfont.woff",
    "font/fontawesome-webfont.woff2",
    "font/qFdH35WCmI96Ajtm81GhU9vyww.woff2",
    "font/qFdH35WCmI96Ajtm81GlU9s.woff2",
    "font/qFdH35WCmI96Ajtm81GoU9vyww.woff2",
    "font/qFdH35WCmI96Ajtm81GqU9vyww.woff2",
    "font/qFdH35WCmI96Ajtm81GrU9vyww.woff2",
]
OFFLINE_JS_FILE_NAMES = [
    "js/bootstrap-4.3.1.min.js",
    "js/facf9fa52c.js",
    "js/jquery-3.4.1.min.js",
    "js/schema_doc.min.js",
]
