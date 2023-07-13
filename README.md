[![PyPI version](https://badge.fury.io/py/json-schema-for-humans.svg)](https://badge.fury.io/py/json-schema-for-humans)

# JSON Schema for Humans

Quickly generate a beautiful static HTML or Markdown page documenting a JSON schema

[Documentation (with visual examples)](https://coveooss.github.io/json-schema-for-humans)

## Features

- Support for JSON Schema Draft-07
- Since the result is static, it is easier to host and faster to load
- HTML and Markdown output support
- Different templates to choose from. More details: [HTML version](https://coveooss.github.io/json-schema-for-humans/examples/examples_js_default/Configuration.html#template_name) - [Markdown version](https://github.com/coveooss/json-schema-for-humans/blob/main/docs/examples/examples_md_default/Configuration.md#template_name)
- Anchor links, allow to send a user to a specific section of the documentation
- Support for references (even circular!)

## Installation
```
pip install json-schema-for-humans
```

## Usage

Options for generation of the doc are documented using the library itself: [HTML version](https://coveooss.github.io/json-schema-for-humans/examples/examples_js_default/Configuration.html) - [Markdown version](https://github.com/coveooss/json-schema-for-humans/blob/main/docs/examples/examples_md_default/Configuration.md)

They can be supplied in various ways:
- Using a JSON or YAML configuration file with the CLI option `--config-file`
- Using the CLI option `--config`
- Using the `ConfigurationOption` object from code

More details are available in the appropriate sections below.

### From CLI

```
generate-schema-doc [OPTIONS] SCHEMA_FILES_OR_DIR [RESULT_FILE_OR_DIR]
```

`SCHEMA_FILES_OR_DIR` can be:
- a path to a single schema file;
- a path to a directory, in this case all files with extensions json, yaml, or yml will be used; 
- a [glob pattern](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob) (starts from the current working directory); or
- a comma-separated list of the above

All schemas provided must be a valid JSON Schema (in JSON or YAML format)

Examples:
- `my_schema.json`
- `my_folder`
- `my_folder/my_schema.yaml,another_schema.json`
- `**/*.yaml.*`

The default value for `RESULT_FILE_OR_DIR` depends on the context:
- the current working directory if more than one schema as been provided as input
- `schema_doc.html` if rendering a single schema as HTML
- `schema_doc.md` if rendering a single schema as Markdown

In a case where more than one schema is provided as input, `RESULT_FILE_OR_DIR` must be a directory. The output documentation will have the same name as the input schema, but with a different extension (`html` or `md`).

#### CLI options

#### --config
Supply generation config parameters. The parameters are documented in the JSON schema `config_schema.json` at the root of the repo or see the generated doc: [HTML version](https://coveooss.github.io/json-schema-for-humans/examples/examples_js_default/Configuration.html) - [Markdown version](https://github.com/coveooss/json-schema-for-humans/blob/main/docs/examples/examples_md_default/Configuration.md).

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

The following methods are available to import from `json_schema_for_humans.generate`

Method Name | Schema input | Output | CSS and JS copied?
--- | --- | --- | ---
generate_from_schema | `schema_file` as str or `pathlib.Path` | Rendered doc as a str | No
generate_from_filename | `schema_file_name` as str or `pathlib.Path` | Rendered doc written to the file at path `result_file_name` | Yes
generate_from_file_object | `schema_file` as an open file object (read mode) | Rendered doc written to the file at `result_file`, which must be an open file object (in write mode) | Yes

Notes:
- When using file objects, it is assumed that files are opened with encoding "utf-8"
- CSS and JS files are copied to the current working directory with names "schema_doc.css" and "schema_doc.min.js" respectively, if necessary
- Other parameters of these methods are analogous to the CLI parameters documented above.

#### The GenerationConfiguration object
To reduce the number of parameters to pass from function to function in the code, there is a `GenerationConfiguration` object that should be used for providing options.

Example:

```python
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

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
- String format
- Numeric types multiples and range
- Constant and enumerated values
- Required properties
- Pattern properties
- Default values
- Array `minItems`, `maxItems`, `uniqueItems`, `items`, `prefixItems`, and `contains`
- Combining schema with `oneOf`, `allOf`, `anyOf`, and `not`
- Examples
- Conditional subschemas

These are **not** supported at the moment (PRs welcome!):
- Property names and size
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

- Properties are in expandable dynamic sections. You can include a button to expand or collapse all. (See doc: [HTML version](https://coveooss.github.io/json-schema-for-humans/examples/examples_js_default/Configuration.html#expand_buttons) - [Markdown version](https://github.com/coveooss/json-schema-for-humans/blob/main/docs/examples/examples_md_default/Configuration.md#expand_buttons))
- Conditional subschemas (`anyOf`, `oneOf`, `allOf`) are in tabbed sections
- Anchor links will scroll to, expand, and animate the target section 
- Long descriptions are collapsed by default

When using this template, you need to include the Javascript file (`schema_doc.min.js`) that is automatically copied next to the output HTML file (`schema_doc.html` by default).

### js_offline

This schema is identical to the js template, but all CSS and JavaScript resources are bundled so that the generated documentation can be used in an offline setting.

### flat

*Note*: This template is a work in progress

It is sometimes not possible or desirable to include custom Javascript in documentation. This template addresses this issue by removing interactive elements in favor of simpler HTML.

At the moment, this means the whole documentation is generated without any collapsible sections, which may make it hard to understand the schema structure. Contributions are welcomed to improve it!

### MD (Markdown)

*Note*: This template is a work in progress

This template allows users to publish the generated documentation without hosting an HTTP server.

On GitHub, this format is rendered directly when browsing code.

A table of content is provided at the beginning of the file for easy navigation.

You can display some important information as badge using an option.
See doc: [HTML version](https://coveooss.github.io/json-schema-for-humans/examples/examples_js_default/Configuration.html#template_md_options_badge_as_image) - [Markdown version](https://github.com/coveooss/json-schema-for-humans/blob/main/docs/examples/examples_md_default/Configuration.md#template_md_options_badge_as_image)

Contributions are welcomed to improve it!


## Contributing
[See CONTRIBUTING.md](CONTRIBUTING.md)