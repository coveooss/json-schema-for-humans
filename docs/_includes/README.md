[![PyPI version](https://badge.fury.io/py/json-schema-for-humans.svg)](https://badge.fury.io/py/json-schema-for-humans)

# JSON Schema for Humans

Quickly generate a beautiful HTML static page documenting a JSON schema

[Documentation (with visual examples)](https://coveooss.github.io/json-schema-for-humans)

## Features

- Support for JSON Schema Draft-07
- Since the result is static, it is easier to host and faster to load
- Different templates to choose from [(See here)](https://coveooss.github.io/json-schema-for-humans/assets/config_schema.html#template_name)
- Anchor links, allow to send a user to a specific section of the documentation
- Support for references (even circular!)

## Installation
```
pip install json-schema-for-humans
```

## Usage

[Options for generation of the doc are documented using this very library](https://coveooss.github.io/json-schema-for-humans/assets/config_schema.html)

They can be supplied in various ways:
- Using a JSON or YAML configuration file with the CLI option `--config-file`
- Using the CLI option `--config`
- Using a `ConfigurationOption` from code

More details are available in the appropriate sections below.

### From CLI

```
generate-schema-doc [OPTIONS] SCHEMA_FILE [RESULT_FILE]
```

`SCHEMA_FILE` must be a valid JSON Schema (in JSON or YAML format)

The default value for `RESULT_FILE` is `schema_doc.html`

#### CLI options

#### --config
Supply generation config parameters. The parameters are documented in the JSON schema `config_schema.json` at the root of the repo or see [the generated doc](https://coveooss.github.io/json-schema-for-humans/assets/config_schema.html).

Each parameter is in the format `--config parameter_name=parameter_value`. Example: `--config expand_buttons=true`. The parameter value must be valid JSON.

For flags, you can also omit the value for `true` or prefix the parameter name with `no_` for `false`. Example: `--config expand_buttons` or `--config no_expand_buttons`.

#### --config-file
Path to a JSON or YAML configuration file respecting the schema `config_schema.json`.

Example: `--config-file jsfh-conf.yaml` where `jsfh-conf.yaml` is in the current directory and contains the following:

```yaml
description_is_markdown: false
expand_buttons: true
copy_js: false
```

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

#### The GenerationConfiguration object
To reduce the number of parameters to pass from function to function in the code, there is a `GenerationConfiguration` object that should be used for providing options.

Example:

```python
from json_schema_for_humans.generate import GenerationConfiguration, generate_from_filename


config = GenerationConfiguration(copy_css=False, expand_buttons=True)

generate_from_filename("my_schema.json", "schema_doc.html", config=config)

# Your doc is now in a file named "schema_doc.html". Next to it, "schema_doc.min.js" was copied, but not "schema_doc.css"
# Your doc will contain a "Expand all" and a "Collapse all" button at the top

```

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

References are supported:

- To another part of the schema, e.g. `{ $ref: "#/definitions/something" }`
- To a local file, `{"$ref": "references.json"}`, `{"$ref": "references.json#/definitions/something"}`
- To a URL, `{"$ref": "http://example.com/schema.json"}`, `{"$ref": "http://example.com/schema.json#/definitions/something"}`


You _can_ have a `description` next to a `$ref`, it will be displayed in priority to the description from the referenced element.

If you have several attributes using the same definition, the definition will only be rendered once.
All other usages of the same definition will be replaced with an anchor link to the first render of the definition.
This can be turned off using `--config no_link_to_reused_ref`. See `With references` in the examples.

## Templates

Templates control the style of the generated documentation.

### js

This is the default template. It uses Bootstrap along with minimal Javascript to allow for the following:

- Properties are in expandable dynamic sections. You can include a button to expand or collapse all. [(See here)](https://coveooss.github.io/json-schema-for-humans/assets/config_schema.html#expand_buttons)
- Conditional subschemas (`anyOf`, `oneOf`, `allOf`) are in tabbed sections
- Anchor links will scroll to, expand, and animate the target section 
- Long descriptions are collapsed by default

When using this template, you need to include the Javascript file (`schema_doc.min.js`) that is automatically copied next to the output HTML file (`schema_doc.html` by default).

### flat

*Note*: This template is a work in progress

It is sometimes not possible or desirable to include custom Javascript in documentation. This template addresses this issue by removing interactive elements in favor of simpler HTML.

At the moment, this means the whole documentation is generated without any collapsible sections, which may make it hard to understand the schema structure. Contributions are welcomed to improve it!

# Contributing
[See CONTRIBUTING.md](https://github.com/coveooss/json-schema-for-humans/blob/master/CONTRIBUTING.md)