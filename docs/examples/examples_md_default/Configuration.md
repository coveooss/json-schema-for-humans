# JSON Schema for Humans configuration file

- [1. Property `JSON Schema for Humans configuration file > description_is_markdown`](#description_is_markdown)
- [2. Property `JSON Schema for Humans configuration file > description_safe_mode`](#description_safe_mode)
- [3. Property `JSON Schema for Humans configuration file > expand_buttons`](#expand_buttons)
- [4. Property `JSON Schema for Humans configuration file > show_breadcrumbs`](#show_breadcrumbs)
- [5. Property `JSON Schema for Humans configuration file > collapse_long_descriptions`](#collapse_long_descriptions)
- [6. Property `JSON Schema for Humans configuration file > collapse_long_examples`](#collapse_long_examples)
- [7. Property `JSON Schema for Humans configuration file > link_to_reused_ref`](#link_to_reused_ref)
- [8. Property `JSON Schema for Humans configuration file > recursive_detection_depth`](#recursive_detection_depth)
- [9. Property `JSON Schema for Humans configuration file > deprecated_from_description`](#deprecated_from_description)
- [10. Property `JSON Schema for Humans configuration file > default_from_description`](#default_from_description)
- [11. Property `JSON Schema for Humans configuration file > copy_css`](#copy_css)
- [12. Property `JSON Schema for Humans configuration file > copy_js`](#copy_js)
- [13. Property `JSON Schema for Humans configuration file > template_name`](#template_name)
- [14. Property `JSON Schema for Humans configuration file > custom_template_path`](#custom_template_path)
- [15. Property `JSON Schema for Humans configuration file > show_toc`](#show_toc)
- [16. Property `JSON Schema for Humans configuration file > examples_as_yaml`](#examples_as_yaml)
- [17. Property `JSON Schema for Humans configuration file > old_anchor_links`](#old_anchor_links)
- [18. Property `JSON Schema for Humans configuration file > markdown_options`](#markdown_options)
- [19. Property `JSON Schema for Humans configuration file > template_md_options`](#template_md_options)
  - [19.1. Property `JSON Schema for Humans configuration file > template_md_options > badge_as_image`](#template_md_options_badge_as_image)
  - [19.2. Property `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers`](#template_md_options_show_heading_numbers)
  - [19.3. Property `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions`](#template_md_options_show_array_restrictions)
  - [19.4. Property `JSON Schema for Humans configuration file > template_md_options > properties_table_columns`](#template_md_options_properties_table_columns)
    - [19.4.1. JSON Schema for Humans configuration file > template_md_options > properties_table_columns > properties_table_columns items](#template_md_options_properties_table_columns_items)
- [20. Property `JSON Schema for Humans configuration file > with_footer`](#with_footer)
- [21. Property `JSON Schema for Humans configuration file > footer_show_time`](#footer_show_time)
- [22. ~~Property `JSON Schema for Humans configuration file > allow_html_description`~~](#allow_html_description)
- [23. ~~Property `JSON Schema for Humans configuration file > minify`~~](#minify)
- [24. ~~Property `JSON Schema for Humans configuration file > templates_directory`~~](#templates_directory)

**Title:** JSON Schema for Humans configuration file

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

**Description:** Choose how to generate JSON Schema for Humans documentation file.

Configuration parameters can be provided in several ways:

- On the CLI using `--config parameter_name=value` (example: `--config template_name=flat`)
- On the CLI using a config file `--config-file config.json`
- From code, by providing a GenerationConfiguration object to the called generation method.

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">description<em>is</em>markdown</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>(HTML outputs only)&lt;br /&gt;Whether to consider the description as Markdown and render it accordingly.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">description<em>safe</em>mode</a></li>
</ul></td>
    <td>No</td>
    <td>enum (of null or string)</td>
    <td>No</td>
    <td>-</td>
    <td>(HTML outputs only)&lt;br /&gt;(Only used with `description<em>is</em>markdown`)&lt;br /&gt;How are HTML tags in descriptions handled. Correspond to the `safe<em>mode` option of the markdown2 library.&lt;br /&gt;&lt;br /&gt;- "escape": Escape all HTML tags in descriptions&lt;br /&gt;- "replace": Replace HTML tags with `[HTML</em>REMOVED]`&lt;br /&gt;- null: Allow HTML in descriptions</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">expand_buttons</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Add an `Expand all` and a `Collapse all` button at the top of the generated documentation.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">show_breadcrumbs</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>For each property, show the relative place of that property in the schema.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">collapse<em>long</em>descriptions</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>If a description is considered big, show only the beginning and add a `Read more` button.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">collapse<em>long</em>examples</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>If an example is considered big, collapse it, it can be displayed with a `Show` option.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">link<em>to</em>reused_ref</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>If several `$ref` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.&lt;br /&gt;&lt;br /&gt;<em>Note</em>: If this option is off and the schema contains recursive definitions, the generation will crash!</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">recursive<em>detection</em>depth</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td><em>Advanced option</em>&lt;br /&gt;If `link<em>to</em>reused_ref` is false and a `$ref` in the schema refers to a parent of itself, we would get a `RecursionError` trying to render the documentation. To avoid this, each reference is checked for circular references.&lt;br /&gt;&lt;br /&gt;This option determines the number of times to recursively follow definitions looking for a circular reference.&lt;br /&gt;&lt;br /&gt;In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">deprecated<em>from</em>description</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Mark a property as deprecated (with a big red badge) if the description contains the string `[​Deprecated`.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">default<em>from</em>description</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Extract the default value of a property from the description like this: ``[Default `the<em>default</em>value`]``.&lt;br /&gt;&lt;br /&gt;The default value from the "default" attribute will be used in priority.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">copy_css</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Copy `schema<em>doc.css` to the same directory as `RESULT</em>FILE` after generation.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">copy_js</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Copy `schema<em>doc.min.js` to the same directory as `RESULT</em>FILE` after generation.&lt;br /&gt;&lt;br /&gt;This file contains the logic for the anchor links.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">template_name</a></li>
</ul></td>
    <td>No</td>
    <td>enum (of string)</td>
    <td>No</td>
    <td>-</td>
    <td>The name of the built-in template to use to render the documentation.&lt;br /&gt;&lt;br /&gt;`js` is the default and uses javascript for anchor links, collapsible sections and tabs.&lt;br /&gt;&lt;br /&gt;`js<em>offline` is identical to `js` except that all CSS, fonts and JavaScript are bundled for offline use.&lt;br /&gt;&lt;br /&gt;`flat` uses no javascript, but has no interactivity.&lt;br /&gt;&lt;br /&gt;`md` is the markdown template.&lt;br /&gt;&lt;br /&gt;`md</em>nested` is the markdown template with collapsible nested sections.&lt;br /&gt;&lt;br /&gt;`techdocs` is optimized for TechDocs/MkDocs Material with collapsible admonitions.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">custom<em>template</em>path</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Path to a custom Jinja2 template file.&lt;br /&gt;&lt;br /&gt;There can be multiple files to split the template, but this path should be the entry point.&lt;br /&gt;&lt;br /&gt;If no output file is specified, the extension of the template file will be used to determine the output documentation extension. i.e. if the template is in ./custom_template/content.html, the resulting documentation will have the html extension.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">show_toc</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Whether to render table of contents.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">examples<em>as</em>yaml</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Whether to display examples as YAML instead of JSON</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">old<em>anchor</em>links</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Generate HTML ids for anchor links without special characters (keep only letters, digits, `_`, and `-`).&lt;br /&gt;&lt;br /&gt;This is the old behaviour and is only needed for browsers that do not support HTML 5.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">markdown_options</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>(Only used with `description<em>is</em>markdown`)&lt;br /&gt;<a href="https://github.com/trentm/python-markdown2/wiki/Extras">Markdown 2 options</a> for the descriptions.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">template<em>md</em>options</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>specific options to md template</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">with_footer</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Whether to show the footer linking to the library repo and with the generation datetime</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">footer<em>show</em>time</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Whether the footer should display the generation time</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">allow<em>html</em>description</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>Deprecated</td>
    <td>-</td>
    <td>[Deprecated]</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">minify</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>Deprecated</td>
    <td>-</td>
    <td>[Deprecated]</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">templates_directory</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>Deprecated</td>
    <td>-</td>
    <td>[Deprecated]</td>
  </tr>
</table>

## <a name="description_is_markdown"></a>1. Property `JSON Schema for Humans configuration file > description_is_markdown`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** (HTML outputs only)
Whether to consider the description as Markdown and render it accordingly.

## <a name="description_safe_mode"></a>2. Property `JSON Schema for Humans configuration file > description_safe_mode`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of null or string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>"escape"</code></td>
  </tr>
</table>

**Description:** (HTML outputs only)
(Only used with `description_is_markdown`)
How are HTML tags in descriptions handled. Correspond to the `safe_mode` option of the markdown2 library.

- "escape": Escape all HTML tags in descriptions
- "replace": Replace HTML tags with `[HTML_REMOVED]`
- null: Allow HTML in descriptions

Must be one of:
* null
* "escape"
* "replace"

## <a name="expand_buttons"></a>3. Property `JSON Schema for Humans configuration file > expand_buttons`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** Add an `Expand all` and a `Collapse all` button at the top of the generated documentation.

## <a name="show_breadcrumbs"></a>4. Property `JSON Schema for Humans configuration file > show_breadcrumbs`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** For each property, show the relative place of that property in the schema.

## <a name="collapse_long_descriptions"></a>5. Property `JSON Schema for Humans configuration file > collapse_long_descriptions`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** If a description is considered big, show only the beginning and add a `Read more` button.

## <a name="collapse_long_examples"></a>6. Property `JSON Schema for Humans configuration file > collapse_long_examples`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** If an example is considered big, collapse it, it can be displayed with a `Show` option.

## <a name="link_to_reused_ref"></a>7. Property `JSON Schema for Humans configuration file > link_to_reused_ref`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** If several `$ref` points to the same definition, only render the documentation for this definition the first time. All other occurrences are replaced by an anchor link to the first occurrence. The first occurrence is the one that is the least nested from the top of the schema and appears first in that nesting level.

*Note*: If this option is off and the schema contains recursive definitions, the generation will crash!

## <a name="recursive_detection_depth"></a>8. Property `JSON Schema for Humans configuration file > recursive_detection_depth`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>integer</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>25</code></td>
  </tr>
</table>

**Description:** *Advanced option*
If `link_to_reused_ref` is false and a `$ref` in the schema refers to a parent of itself, we would get a `RecursionError` trying to render the documentation. To avoid this, each reference is checked for circular references.

This option determines the number of times to recursively follow definitions looking for a circular reference.

In other words, if a schema has a deeply nested element that refers to itself, this option may need to be increased.

## <a name="deprecated_from_description"></a>9. Property `JSON Schema for Humans configuration file > deprecated_from_description`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** Mark a property as deprecated (with a big red badge) if the description contains the string `[​Deprecated`.

## <a name="default_from_description"></a>10. Property `JSON Schema for Humans configuration file > default_from_description`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** Extract the default value of a property from the description like this: ``[Default `the_default_value`]``.

The default value from the "default" attribute will be used in priority.

## <a name="copy_css"></a>11. Property `JSON Schema for Humans configuration file > copy_css`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** Copy `schema_doc.css` to the same directory as `RESULT_FILE` after generation.

## <a name="copy_js"></a>12. Property `JSON Schema for Humans configuration file > copy_js`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** Copy `schema_doc.min.js` to the same directory as `RESULT_FILE` after generation.

This file contains the logic for the anchor links.

## <a name="template_name"></a>13. Property `JSON Schema for Humans configuration file > template_name`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>"js"</code></td>
  </tr>
</table>

**Description:** The name of the built-in template to use to render the documentation.

`js` is the default and uses javascript for anchor links, collapsible sections and tabs.

`js_offline` is identical to `js` except that all CSS, fonts and JavaScript are bundled for offline use.

`flat` uses no javascript, but has no interactivity.

`md` is the markdown template.

`md_nested` is the markdown template with collapsible nested sections.

`techdocs` is optimized for TechDocs/MkDocs Material with collapsible admonitions.

Must be one of:
* "flat"
* "js"
* "js_offline"
* "md"
* "md_nested"
* "md_sober"
* "techdocs"

## <a name="custom_template_path"></a>14. Property `JSON Schema for Humans configuration file > custom_template_path`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>null</code></td>
  </tr>
</table>

**Description:** Path to a custom Jinja2 template file.

There can be multiple files to split the template, but this path should be the entry point.

If no output file is specified, the extension of the template file will be used to determine the output documentation extension. i.e. if the template is in ./custom_template/content.html, the resulting documentation will have the html extension.

## <a name="show_toc"></a>15. Property `JSON Schema for Humans configuration file > show_toc`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** Whether to render table of contents.

## <a name="examples_as_yaml"></a>16. Property `JSON Schema for Humans configuration file > examples_as_yaml`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** Whether to display examples as YAML instead of JSON

## <a name="old_anchor_links"></a>17. Property `JSON Schema for Humans configuration file > old_anchor_links`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** Generate HTML ids for anchor links without special characters (keep only letters, digits, `_`, and `-`).

This is the old behaviour and is only needed for browsers that do not support HTML 5.

## <a name="markdown_options"></a>18. Property `JSON Schema for Humans configuration file > markdown_options`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>{"fenced-code-blocks": {"cssclass": "highlight jumbotron"}, "tables": null, "breaks": {"on_newline": true, "on_backslash": true}}</code></td>
  </tr>
</table>

**Description:** (Only used with `description_is_markdown`)
[Markdown 2 options](https://github.com/trentm/python-markdown2/wiki/Extras) for the descriptions.

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

## <a name="template_md_options"></a>19. Property `JSON Schema for Humans configuration file > template_md_options`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

**Description:** specific options to md template

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">badge<em>as</em>image</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).&lt;br /&gt;&lt;br /&gt; if false, use text instead</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">show<em>heading</em>numbers</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>if true generate heading numbers to correspond to table of contents.&lt;br /&gt;&lt;br /&gt; if false, do not generate heading numbers</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">show<em>array</em>restrictions</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>if true generate array restrictions section.&lt;br /&gt;&lt;br /&gt; if false, do not generate</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">properties<em>table</em>columns</a></li>
</ul></td>
    <td>No</td>
    <td>array of enum (of string)</td>
    <td>No</td>
    <td>-</td>
    <td>array of column names to display in the properties table.&lt;br /&gt;&lt;br /&gt; if empty, the default is ['Property','Pattern','Type','Deprecated','Definition','Title/Description']</td>
  </tr>
</table>

### <a name="template_md_options_badge_as_image"></a>19.1. Property `JSON Schema for Humans configuration file > template_md_options > badge_as_image`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** if true generate badges(eg: optional, required) using embedded image (https://img.shields.io).

 if false, use text instead

### <a name="template_md_options_show_heading_numbers"></a>19.2. Property `JSON Schema for Humans configuration file > template_md_options > show_heading_numbers`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** if true generate heading numbers to correspond to table of contents.

 if false, do not generate heading numbers

### <a name="template_md_options_show_array_restrictions"></a>19.3. Property `JSON Schema for Humans configuration file > template_md_options > show_array_restrictions`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** if true generate array restrictions section.

 if false, do not generate

### <a name="template_md_options_properties_table_columns"></a>19.4. Property `JSON Schema for Humans configuration file > template_md_options > properties_table_columns`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array of enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** array of column names to display in the properties table.

 if empty, the default is ['Property','Pattern','Type','Deprecated','Definition','Title/Description']

<table>
  <tr>
    <th></th>
    <th>Array restrictions</th>
  </tr>
  <tr>
    <td><strong>Min items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Max items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Items unicity</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Additional items</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Tuple validation</strong></td>
    <td>See below</td>
  </tr>
</table>

<table>
  <tr>
    <th>Each item of this array must be</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="#template_md_options_properties_table_columns_items">properties<em>table</em>columns items</a></td>
    <td>-</td>
  </tr>
</table>

#### <a name="template_md_options_properties_table_columns_items"></a>19.4.1. JSON Schema for Humans configuration file > template_md_options > properties_table_columns > properties_table_columns items

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

Must be one of:
* "Property"
* "Pattern"
* "Type"
* "Deprecated"
* "Definition"
* "Title/Description"

## <a name="with_footer"></a>20. Property `JSON Schema for Humans configuration file > with_footer`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** Whether to show the footer linking to the library repo and with the generation datetime

## <a name="footer_show_time"></a>21. Property `JSON Schema for Humans configuration file > footer_show_time`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** Whether the footer should display the generation time

## <a name="allow_html_description"></a>22. ~~Property `JSON Schema for Humans configuration file > allow_html_description`~~

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Deprecated</strong></td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>false</code></td>
  </tr>
</table>

**Description:** [Deprecated]

## <a name="minify"></a>23. ~~Property `JSON Schema for Humans configuration file > minify`~~

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Deprecated</strong></td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>true</code></td>
  </tr>
</table>

**Description:** [Deprecated]

## <a name="templates_directory"></a>24. ~~Property `JSON Schema for Humans configuration file > templates_directory`~~

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Deprecated</strong></td>
  </tr>
</table>

**Description:** [Deprecated]

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
