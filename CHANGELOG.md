
# 0.48

(Issue #190) Now correctly display elements next to a `$ref` with reused nodes, e.g.:

```json
{
  "$schema": "https://json-schema.org/draft/2019-09/schema",
  "type": "object",
  "title": "Example",
  "properties": {
    "prop1": {
      "$ref": "#/$defs/a",
      "description": "Prop1",
      "examples": ["1"]
    },
    "prop2": {
      "$ref": "#/$defs/a",
      "description": "Prop2",
      "examples": ["2"]
    }
  },
  "$defs": {
    "a": {
      "type": "string",
      "maxLength": 5
    }
  }
}
```

Previously, `prop2` would have been a link to `prop1`, hiding the different example for `prop2`.

This may increase the size of rendered schemas in certain situations.
