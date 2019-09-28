# JSON Schema for Humans

Quickly generate a beautiful HTML static page documenting a JSON schema

[Documentation](https://coveooss.github.io/json-schema-for-humans)

## Installation
```
pip install json-schema-for-humans
```

## Usage

```
generate-schema-doc [OPTIONS] SCHEMA_FILE [RESULT_FILE]
```

`SCHEMA_FILE` must be a valid JSON Schema

A CSS file will be copied in the same directory as `RESULT_FILE`

The default value for `RESULT_FILE` is `schema_doc.html`

## Options

### --minify/--no-minify
On by default

Minify the output HTML document

### --deprecated-from-description
Off by default

Mark a property as deprecated (with a big red badge) if the description contains the string `[Deprecated`

### --default-from-description
Off by default

Extract the default value of a property from the description like this: ``[Default `the_default_value`]``

The default value from the "default" attribute will be used in priority

## What's supported

See the excellent [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/index.html) to understand what are those checks

The following are supported:
- Types
- String length (`minLength`, `maxLength`) and format
- Regular expressions
- Numeric types multiples and range
- Constant and enumerated values
- Required properties
- Default values
- Array `minItems`, `maxItems`, `uniqueItems`, `items` (schema that must apply to all of the array items), and `contains`
- Combining schema with `oneOf`, `allOf`, `anyOf`, and `not`

These are **not** supported at the moment (PRs welcome!):
- Property names, size, and pattern
- Array items at specific index (for example, first item must be a string and second must be an integer)
- Property dependencies
- Examples
- Media
- Conditional subschemas

References from inside a schema are supported (for example `{ $ref: "#/definitions/something" }` will be replaced by the 
content of `schema["definitions"]["something"]`)

References to schemas in other files are not supported for now.

## Development

### Testing
Just run tox

`tox`

### Generating doc
The documentation is generated using jekyll and hosted on GitHub Pages

- Change your current working directory to `docs`
- Run ``python generate_examples.py``. This will get all examples from `tests/cases`, render the resulting HTML and
 include it in the appropriate folders in the jekyll site.
- If you have added an example, add the file name (without `.json`), the display name and description in `_data/examples.yaml`