# JSON Schema for Humans configuration file

- [1. [Optional] Property JSON Schema for Humans configuration file > minify](#minify-6e696679)
- [2. [Optional] Property JSON Schema for Humans configuration file > description_is_markdown](#description_is_markdown-646f776e)
- [3. [Optional] Property JSON Schema for Humans configuration file > expand_buttons](#expand_buttons-746f6e73)
- [4. [Optional] Property JSON Schema for Humans configuration file > show_breadcrumbs](#show_breadcrumbs-756d6273)
- [5. [Optional] Property JSON Schema for Humans configuration file > collapse_long_descriptions](#collapse_long_descriptions-696f6e73)
- [6. [Optional] Property JSON Schema for Humans configuration file > collapse_long_examples](#collapse_long_examples-706c6573)
- [7. [Optional] Property JSON Schema for Humans configuration file > link_to_reused_ref](#link_to_reused_ref-5f726566)
- [8. [Optional] Property JSON Schema for Humans configuration file > recursive_detection_depth](#recursive_detection_depth-65707468)
- [9. [Optional]~~ Property JSON Schema for Humans configuration file > deprecated_from_description~~](#deprecated_from_description-74696f6e)
- [10. [Optional] Property JSON Schema for Humans configuration file > default_from_description](#default_from_description-74696f6e)
- [11. [Optional] Property JSON Schema for Humans configuration file > copy_css](#copy_css-5f637373)
- [12. [Optional] Property JSON Schema for Humans configuration file > copy_js](#copy_js-795f6a73)
- [13. [Optional]~~ Property JSON Schema for Humans configuration file > templates_directory~~](#templates_directory-746f7279)
- [14. [Optional] Property JSON Schema for Humans configuration file > template_name](#template_name-6e616d65)
- [15. [Optional] Property JSON Schema for Humans configuration file > custom_template_path](#custom_template_path-70617468)
- [16. [Optional] Property JSON Schema for Humans configuration file > show_toc](#show_toc-5f746f63)
- [17. [Optional] Property JSON Schema for Humans configuration file > examples_as_yaml](#examples_as_yaml-79616d6c)
- [18. [Optional] Property JSON Schema for Humans configuration file > markdown_options](#markdown_options-696f6e73)
- [19. [Optional] Property JSON Schema for Humans configuration file > template_md_options](#template_md_options-696f6e73)
  - [19.1. [Optional] Property JSON Schema for Humans configuration file > template_md_options > badge_as_image](#template_md_options_badge_as_image-6d616765)
  - [19.2. [Optional] Property JSON Schema for Humans configuration file > template_md_options > show_heading_numbers](#template_md_options_show_heading_numbers-62657273)
  - [19.3. [Optional] Property JSON Schema for Humans configuration file > template_md_options > show_array_restrictions](#template_md_options_show_array_restrictions-696f6e73)
- [20. [Optional] Property JSON Schema for Humans configuration file > with_footer](#with_footer-6f746572)
- [21. [Optional] Property JSON Schema for Humans configuration file > footer_show_time](#footer_show_time-74696d65)

**Title:** JSON Schema for Humans configuration file

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Choose how to generate JSON Schema for Humans documentation file.

Configuration parameters can be provided in several ways:

- On the CLI using `--config parameter_name=value` (example: `--config template_name=flat`)
- On the CLI using a config file `--config-file config.json`
- From code, by providing a GenerationConfiguration object to the called generation method.

<details>
<summary><strong> <a name="minify-6e696679"></a>1. [Optional] Property JSON Schema for Humans configuration file > minify</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Minify the output HTML document.

</blockquote>
</details>

<details>
<summary><strong> <a name="description_is_markdown-646f776e"></a>2. [Optional] Property JSON Schema for Humans configuration file > description_is_markdown</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to consider the description as markdown and render it accordingly.

</blockquote>
</details>

<details>
<summary><strong> <a name="expand_buttons-746f6e73"></a>3. [Optional] Property JSON Schema for Humans configuration file > expand_buttons</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Add an `Expand all` and a `Collapse all` button at the top of the generated documentation.

</blockquote>
</details>

<details>
<summary><strong> <a name="show_breadcrumbs-756d6273"></a>4. [Optional] Property JSON Schema for Humans configuration file > show_breadcrumbs</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** For each property, show the relative place of that property in the schema.

</blockquote>
</details>

<details>
<summary><strong> <a name="collapse_long_descriptions-696f6e73"></a>5. [Optional] Property JSON Schema for Humans configuration file > collapse_long_descriptions</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** If a description is considered big, show only the beginning and add a `Read more` button.

</blockquote>
</details>

<details>
<summary><strong> <a name="collapse_long_examples-706c6573"></a>6. [Optional] Property JSON Schema for Humans configuration file > collapse_long_examples</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** If an example is considered big, collapse it, it can be displayed with a `Show` option.

</blockquote>
</details>

<details>
<summary><strong> <a name="link_to_reused_ref-5f726566"></a>7. [Optional] Property JSON Schema for Humans configuration file > link_to_reused_ref</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** If several `$ref` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.

*Note*: If this option is off and the schema contains recursive definitions, the generation will crash!

</blockquote>
</details>

<details>
<summary><strong> <a name="recursive_detection_depth-65707468"></a>8. [Optional] Property JSON Schema for Humans configuration file > recursive_detection_depth</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `25`      |

**Description:** *Advanced option*
If `link_to_reused_ref` is false and a `$ref` in the schema refers to a parent of itself, we would get a `RecursionError` trying to render the documentation. To avoid this, each reference is checked for circular references.

This option determines the number of times to recursively follow definitions looking for a circular reference.

In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased.

</blockquote>
</details>

<details>
<summary><strong> <a name="deprecated_from_description-74696f6e"></a>9. [Optional]~~ Property JSON Schema for Humans configuration file > deprecated_from_description~~</strong>  

</summary>
<blockquote>

|                |              |
| -------------- | ------------ |
| **Type**       | `boolean`    |
| **Required**   | No           |
| **Deprecated** | [Deprecated] |
| **Default**    | `false`      |

**Description:** Mark a property as deprecated (with a big red badge) if the description contains the string `[Deprecated`.

</blockquote>
</details>

<details>
<summary><strong> <a name="default_from_description-74696f6e"></a>10. [Optional] Property JSON Schema for Humans configuration file > default_from_description</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Extract the default value of a property from the description like this: ``[Default `the_default_value`]``.

The default value from the "default" attribute will be used in priority.

</blockquote>
</details>

<details>
<summary><strong> <a name="copy_css-5f637373"></a>11. [Optional] Property JSON Schema for Humans configuration file > copy_css</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Copy `schema_doc.css` to the same directory as `RESULT_FILE` after generation.

</blockquote>
</details>

<details>
<summary><strong> <a name="copy_js-795f6a73"></a>12. [Optional] Property JSON Schema for Humans configuration file > copy_js</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Copy `schema_doc.min.js` to the same directory as `RESULT_FILE` after generation.

This file contains the logic for the anchor links.

</blockquote>
</details>

<details>
<summary><strong> <a name="templates_directory-746f7279"></a>13. [Optional]~~ Property JSON Schema for Humans configuration file > templates_directory~~</strong>  

</summary>
<blockquote>

|                |              |
| -------------- | ------------ |
| **Type**       | `string`     |
| **Required**   | No           |
| **Deprecated** | [Deprecated] |

**Description:** [Deprecated]

</blockquote>
</details>

<details>
<summary><strong> <a name="template_name-6e616d65"></a>14. [Optional] Property JSON Schema for Humans configuration file > template_name</strong>  

</summary>
<blockquote>

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"js"`             |

**Description:** The name of the built-in template to use to render the documentation.

`js` is the default and uses javascript for anchor links, collapsible sections and tabs. `flat` uses no javascript, but has no interactivity.

Must be one of:
* "flat"
* "js"
* "md"
* "md_nested"

</blockquote>
</details>

<details>
<summary><strong> <a name="custom_template_path-70617468"></a>15. [Optional] Property JSON Schema for Humans configuration file > custom_template_path</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `null`   |

**Description:** Path to a custom Jinja2 template file.

There can be multiple files to split the template, but this path should be the entry point.

If no output file is specified, the extension of the template file will be used to determine the output documentation extension. i.e. if the template is in ./custom_template/content.html, the resulting documentation will have the html extension.

</blockquote>
</details>

<details>
<summary><strong> <a name="show_toc-5f746f63"></a>16. [Optional] Property JSON Schema for Humans configuration file > show_toc</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to render table of contents.

</blockquote>
</details>

<details>
<summary><strong> <a name="examples_as_yaml-79616d6c"></a>17. [Optional] Property JSON Schema for Humans configuration file > examples_as_yaml</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to display examples as YAML instead of JSON

</blockquote>
</details>

<details>
<summary><strong> <a name="markdown_options-696f6e73"></a>18. [Optional] Property JSON Schema for Humans configuration file > markdown_options</strong>  

</summary>
<blockquote>

|                           |                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                |
| **Required**              | No                                                                                                                      |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.")                                               |
| **Default**               | `{"fenced-code-blocks": {"break-on-newline": true, "cssclass": "highlight jumbotron", "tables": null}, "tables": null}` |

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

</blockquote>
</details>

<details>
<summary><strong> <a name="template_md_options-696f6e73"></a>19. [Optional] Property JSON Schema for Humans configuration file > template_md_options</strong>  

</summary>
<blockquote>

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** specific options to md template

<details>
<summary><strong> <a name="template_md_options_badge_as_image-6d616765"></a>19.1. [Optional] Property JSON Schema for Humans configuration file > template_md_options > badge_as_image</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).

 if false, use text instead

</blockquote>
</details>

<details>
<summary><strong> <a name="template_md_options_show_heading_numbers-62657273"></a>19.2. [Optional] Property JSON Schema for Humans configuration file > template_md_options > show_heading_numbers</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** if true generate heading numbers to correspond to table of contents.

 if false, do not generate heading numbers

</blockquote>
</details>

<details>
<summary><strong> <a name="template_md_options_show_array_restrictions-696f6e73"></a>19.3. [Optional] Property JSON Schema for Humans configuration file > template_md_options > show_array_restrictions</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** if true generate array restrictions section.

 if false, do not generate

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="with_footer-6f746572"></a>20. [Optional] Property JSON Schema for Humans configuration file > with_footer</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to show the footer linking to the library repo and with the generation datetime

</blockquote>
</details>

<details>
<summary><strong> <a name="footer_show_time-74696d65"></a>21. [Optional] Property JSON Schema for Humans configuration file > footer_show_time</strong>  

</summary>
<blockquote>

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether the footer should display the generation time

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)