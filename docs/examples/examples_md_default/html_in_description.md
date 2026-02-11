# HTML in descriptions

- [1. Property `HTML in descriptions > raw_html`](#raw_html)
- [2. Property `HTML in descriptions > html_in_markdown`](#html_in_markdown)
- [3. Property `HTML in descriptions > json_in_markdown`](#json_in_markdown)

**Title:** HTML in descriptions

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
<li><a href="#">raw_html</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Some raw HTML</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">html<em>in</em>markdown</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Some HTML in Markdown</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">json<em>in</em>markdown</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Some JSON in Markdown</td>
  </tr>
</table>

## <a name="raw_html"></a>1. Property `HTML in descriptions > raw_html`

**Title:** Some raw HTML

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
</table>

**Description:** <br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>

## <a name="html_in_markdown"></a>2. Property `HTML in descriptions > html_in_markdown`

**Title:** Some HTML in Markdown

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
</table>

**Description:** Here is some HTML:
```html
<br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>
```

## <a name="json_in_markdown"></a>3. Property `HTML in descriptions > json_in_markdown`

**Title:** Some JSON in Markdown

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
</table>

**Description:** Here is some JSON:
```json
{
  "property": "value"
}
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
