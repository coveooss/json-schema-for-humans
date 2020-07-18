# JSON Schema for Humans

Quickly generate a beautiful HTML static page documenting a JSON schema

[Documentation (with visual examples)](https://coveooss.github.io/json-schema-for-humans)

## Installation
```
pip install json-schema-for-humans
```

## Usage

### From CLI

```
generate-schema-doc [OPTIONS] SCHEMA_FILE [RESULT_FILE]
```

`SCHEMA_FILE` must be a valid JSON Schema (in JSON or YAML format)

The default value for `RESULT_FILE` is `schema_doc.html`

#### CLI options

##### --expand-buttons
Off by default

Add an `Expand all` and a `Collapse all` button at the top of the generated documentation

##### --link-to-reused-ref/--no-link-to-reused-ref
On by default

If several `$ref` points to the same definition, only render the documentation for this definition the first time.
All other occurrences are replaced by an anchor link to the first occurrence.

If the feature is off (`--no-link-to-reused-ref`) and there is a recursive definition, the generation will crash with a `RecursionError`.

##### --minify/--no-minify
On by default

Minify the output HTML document

##### --deprecated-from-description
Off by default

Mark a property as deprecated (with a big red badge) if the description contains the string `[Deprecated`

##### --default-from-description
Off by default

Extract the default value of a property from the description like this: ``[Default `the_default_value`]``

The default value from the "default" attribute will be used in priority

##### --copy-css/--no-copy-css
On by default

Copy `schema_doc.css` to the same directory as `RESULT_FILE`.

##### --copy-js/--no-copy-js
On by default.

Copy `schema_doc.min.js` to the same directory as `RESULT_FILE`.

This file contains the logic for the anchor links

### From code

There are 3 methods that one could use:

Method Name | Schema input | Output | CSS and JS copied?
--- | --- | --- | ---
generate_from_schema | `schema_file` as str, Path (from pathlib) or a file object | Rendered HTML as a str | No
generate_from_filename | `schema_file_name` as a str or Path | Rendered HTML written to the file at path `result_file_name` | Yes
generate_from_file_object | `schema_file` as an open file object (read mode) | Rendered HTML written to the file at `result_file`, which must be an open file object (in write mode) | Yes

Notes:
- When using file objects, it is assumed that files are opened with encoding "utf-8"
- CSS and JS files are copied to the current working directory with names "schema_doc.css" and "schema_doc.min.js" respectively
- Other parameters of these methods are analogous to the CLI parameters documented above.

#### Pre-load schemas
`generate_from_schema` has a `loaded_schemas` parameter that can be used to pre-load schemas. This must be a dict with the key being the real path of the schema file and the value being the result of loading the schema (with `json.load` or `yaml.safe_load`, for example).

This should not be necessary in normal scenarios.

## What's supported

See the excellent [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/index.html) to understand what are those checks

The following are supported:
- Types
- Regular expressions
- String length
- Numeric types multiples and range
- Constant and enumerated values
- Required properties
- Pattern properties
- Default values
- Array `minItems`, `maxItems`, `uniqueItems`, `items` (schema that must apply to all of the array items), and `contains`
- Combining schema with `oneOf`, `allOf`, `anyOf`, and `not`
- Examples
- Conditional subschemas

These are **not** supported at the moment (PRs welcome!):
- String format
- Property names and size
- Array items at specific index (for example, first item must be a string and second must be an integer)
- Property dependencies
- Media

## References

References from inside a schema and to schemas in other files are supported (for example `{ $ref: "#/definitions/something" }` will be replaced by the 
content of `schema["definitions"]["something"]`).

You _can_ have a `description` next to a `$ref`, it will be displayed in priority to the description from the referenced element.

If you have several attributes using the same definition, the definition will only be rendered once.
All other usages of the same definition will be replaced with an anchor link to the first render of the definition.
This can be turned off using `--no-link-to-reused-ref`. See `With references` in the examples.

## Anchor links
Clicking on a property or tab in the output documentation will set the hash of the current window. Opening this anchor link will expand all needed properties and scroll to this section of the schema. Useful for pointing your users to a specific setting.

For this feature to work, you need to include the Javascript file (`schema_doc.min.js`) that is automatically copied next to the output HTML file (`schema_doc.html` by default).

## Development

### Testing
Just run tox

`tox`

### Modifying Javascript
`schema_doc.js` is not minified automatically, you are responsible for doing it yourself

### Generating doc
The documentation is generated using jekyll and hosted on GitHub Pages

- Change your current working directory to `docs`
- Run ``python generate_examples.py``. This will get all examples from `tests/cases`, render the resulting HTML and
 include it in the appropriate folders in the jekyll site.
- If you have added an example, add the file name (without `.json`), the display name and description in `_data/examples.yaml`