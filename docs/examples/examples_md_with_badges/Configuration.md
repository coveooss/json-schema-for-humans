# JSON Schema for Humans configuration file

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > minify`](#minify)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > description_is_markdown`](#description_is_markdown)
- [3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > expand_buttons`](#expand_buttons)
- [4. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > show_breadcrumbs`](#show_breadcrumbs)
- [5. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > collapse_long_descriptions`](#collapse_long_descriptions)
- [6. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > link_to_reused_ref`](#link_to_reused_ref)
- [7. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > recursive_detection_depth`](#recursive_detection_depth)
- [8. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > deprecated_from_description`](#deprecated_from_description)
- [9. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > default_from_description`](#default_from_description)
- [10. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > copy_css`](#copy_css)
- [11. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > copy_js`](#copy_js)
- [12. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > templates_directory`](#templates_directory)
- [13. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_name`](#template_name)
- [14. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > show_toc`](#show_toc)
- [15. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > examples_as_yaml`](#examples_as_yaml)
- [16. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > markdown_options`](#markdown_options)
- [17. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options`](#template_md_options)
  - [17.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > badge_as_image`](#template_md_options_badge_as_image)
  - [17.2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers`](#template_md_options_show_heading_numbers)
  - [17.3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions`](#template_md_options_show_array_restrictions)

**Title:** JSON Schema for Humans configuration file

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Choose how to generate JSON Schema for Humans documentation file.

Configuration parameters can be provided in several ways:

- On the CLI using `--config parameter_name=value` (example: `--config template_name=flat`)
- On the CLI using a config file `--config-file config.json`
- From code, by providing a GenerationConfiguration object to the called generation method.

| Property                                                       | Pattern | Type             | Deprecated | Definition | Title/Description                                                                    |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------------------------------ |
| - [minify](#minify )                                           | No      | boolean          | No         | -          | Minify the output HTML document.                                                     |
| - [description_is_markdown](#description_is_markdown )         | No      | boolean          | No         | -          | Whether to consider the description as markdown and render it accordingly.           |
| - [expand_buttons](#expand_buttons )                           | No      | boolean          | No         | -          | Add an 'Expand all' and a 'Collapse all' button at the top of the generated docu ... |
| - [show_breadcrumbs](#show_breadcrumbs )                       | No      | boolean          | No         | -          | For each property, show the relative place of that property in the schema.           |
| - [collapse_long_descriptions](#collapse_long_descriptions )   | No      | boolean          | No         | -          | If a description is considered big, show only the beginning and add a 'Read more ... |
| - [link_to_reused_ref](#link_to_reused_ref )                   | No      | boolean          | No         | -          | If several '$ref' points to the same definition, only render the documentation f ... |
| - [recursive_detection_depth](#recursive_detection_depth )     | No      | integer          | No         | -          | *Advanced option* ...                                                                |
| - [deprecated_from_description](#deprecated_from_description ) | No      | boolean          | No         | -          | Mark a property as deprecated (with a big red badge) if the description contains ... |
| - [default_from_description](#default_from_description )       | No      | boolean          | No         | -          | Extract the default value of a property from the description like this: ''[Defau ... |
| - [copy_css](#copy_css )                                       | No      | boolean          | No         | -          | Copy 'schema_doc.css' to the same directory as 'RESULT_FILE' after generation.       |
| - [copy_js](#copy_js )                                         | No      | boolean          | No         | -          | Copy 'schema_doc.min.js' to the same directory as 'RESULT_FILE' after generation ... |
| - [templates_directory](#templates_directory )                 | No      | string           | No         | -          | The file system path to the directory containing templates, with a default of th ... |
| - [template_name](#template_name )                             | No      | enum (of string) | No         | -          | The name of the set of templates to use to render the documentation. ...             |
| - [show_toc](#show_toc )                                       | No      | boolean          | No         | -          | Whether to render table of contents.                                                 |
| - [examples_as_yaml](#examples_as_yaml )                       | No      | boolean          | No         | -          | Whether to display examples as YAML instead of JSON                                  |
| - [markdown_options](#markdown_options )                       | No      | object           | No         | -          | [Markdown 2 options](https://github.com/trentm/python-markdown2/wiki/Extras) for ... |
| - [template_md_options](#template_md_options )                 | No      | object           | No         | -          | specific options to md template                                                      |
|                                                                |         |                  |            |            |                                                                                      |

## <a name="minify"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > minify`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** Minify the output HTML document.

## <a name="description_is_markdown"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > description_is_markdown`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** Whether to consider the description as markdown and render it accordingly.

## <a name="expand_buttons"></a>3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > expand_buttons`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                                                             |
|                           |                                                                                                                     |

**Description:** Add an `Expand all` and a `Collapse all` button at the top of the generated documentation.

## <a name="show_breadcrumbs"></a>4. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > show_breadcrumbs`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** For each property, show the relative place of that property in the schema.

## <a name="collapse_long_descriptions"></a>5. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > collapse_long_descriptions`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** If a description is considered big, show only the beginning and add a `Read more` button.

## <a name="link_to_reused_ref"></a>6. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > link_to_reused_ref`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** If several `$ref` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.

*Note*: If this option is off and the schema contains recursive definitions, the generation will crash!

## <a name="recursive_detection_depth"></a>7. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > recursive_detection_depth`

| Type                      | `integer`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `25`                                                                                                                |
|                           |                                                                                                                     |

**Description:** *Advanced option*
If `link_to_reused_ref` is false and a `$ref` in the schema refers to a parent of itself, we would get a `RecursionError` trying to render the documentation. To avoid this, each reference is checked for circular references.

This option determines the number of times to recursively follow definitions looking for a circular reference.

In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased.

## <a name="deprecated_from_description"></a>8. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > deprecated_from_description`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                                                             |
|                           |                                                                                                                     |

**Description:** Mark a property as deprecated (with a big red badge) if the description contains the string `[Deprecated`.

## <a name="default_from_description"></a>9. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > default_from_description`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                                                             |
|                           |                                                                                                                     |

**Description:** Extract the default value of a property from the description like this: ``[Default `the_default_value`]``.

The default value from the "default" attribute will be used in priority.

## <a name="copy_css"></a>10. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > copy_css`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** Copy `schema_doc.css` to the same directory as `RESULT_FILE` after generation.

## <a name="copy_js"></a>11. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > copy_js`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** Copy `schema_doc.min.js` to the same directory as `RESULT_FILE` after generation.

This file contains the logic for the anchor links.

## <a name="templates_directory"></a>12. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > templates_directory`

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** The file system path to the directory containing templates, with a default of the `templates` directory within the library source code.

## <a name="template_name"></a>13. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_name`

| Type                      | `enum (of string)`                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `"js"`                                                                                                              |
|                           |                                                                                                                     |

**Description:** The name of the set of templates to use to render the documentation.

`js` is the default and uses javascript for anchor links, collapsible sections and tabs. `flat` uses no javascript, but has no interactivity.

Must be one of:
* "flat"
* "js"
* "md"

## <a name="show_toc"></a>14. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > show_toc`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** Whether to render table of contents.

## <a name="examples_as_yaml"></a>15. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > examples_as_yaml`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                                                             |
|                           |                                                                                                                     |

**Description:** Whether to display examples as YAML instead of JSON

## <a name="markdown_options"></a>16. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > markdown_options`

| Type                      | `object`                                                                                                                |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.")     |
| **Default**               | `{"fenced-code-blocks": {"break-on-newline": true, "cssclass": "highlight jumbotron", "tables": null}, "tables": null}` |
|                           |                                                                                                                         |

**Description:** [Markdown 2 options](https://github.com/trentm/python-markdown2/wiki/Extras) for the descriptions. `description_is_markdown` must be true for this to have any effect.

**WARNING**
Adding an extra, even if the value is false, will activate it. For example `{"break-on-newline": false}` will activate the `break-on-newline` extra.

**Example:** 

```json
{
    "fenced-code-blocks": {
        "cssclass": "highlight jumbotron"
    },
    "tables": null,
    "break-on-newline": true,
    "cuddled-lists": true
}
```

## <a name="template_md_options"></a>17. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** specific options to md template

| Property                                                                   | Pattern | Type    | Deprecated | Definition | Title/Description                                                                    |
| -------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------------------------------------------------------------ |
| - [badge_as_image](#template_md_options_badge_as_image )                   | No      | boolean | No         | -          | if true generate badges(eg: optional, required) using embedded image (https://im ... |
| - [show_heading_numbers](#template_md_options_show_heading_numbers )       | No      | boolean | No         | -          | if true generate heading numbers to correspond to table of contents. ...             |
| - [show_array_restrictions](#template_md_options_show_array_restrictions ) | No      | boolean | No         | -          | if true generate array restrictions section. ...                                     |
|                                                                            |         |         |            |            |                                                                                      |

### <a name="template_md_options_badge_as_image"></a>17.1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > badge_as_image`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `false`                                                                                                             |
|                           |                                                                                                                     |

**Description:** if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).

 if false, use text instead

### <a name="template_md_options_show_heading_numbers"></a>17.2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** if true generate heading numbers to correspond to table of contents.

 if false, do not generate heading numbers

### <a name="template_md_options_show_array_restrictions"></a>17.3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions`

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `true`                                                                                                              |
|                           |                                                                                                                     |

**Description:** if true generate array restrictions section.

 if false, do not generate

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date