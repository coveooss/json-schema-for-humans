# HTML in descriptions

- [1. Property `HTML in descriptions > raw_html`](#raw_html)
- [2. Property `HTML in descriptions > html_in_markdown`](#html_in_markdown)
- [3. Property `HTML in descriptions > json_in_markdown`](#json_in_markdown)

**Title:** HTML in descriptions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description                                      |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ------------------------------------------------------ |
| - [raw_html](#raw_html )                 | No      | string | No         | -          | Some raw HTML [(read more)](#raw_html)                 |
| - [html_in_markdown](#html_in_markdown ) | No      | string | No         | -          | Some HTML in Markdown [(read more)](#html_in_markdown) |
| - [json_in_markdown](#json_in_markdown ) | No      | string | No         | -          | Some JSON in Markdown [(read more)](#json_in_markdown) |

## <a name="raw_html"></a>1. Property `HTML in descriptions > raw_html`

**Title:** Some raw HTML

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** <br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>

## <a name="html_in_markdown"></a>2. Property `HTML in descriptions > html_in_markdown`

**Title:** Some HTML in Markdown

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Here is some HTML:
```html
<br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>
```

## <a name="json_in_markdown"></a>3. Property `HTML in descriptions > json_in_markdown`

**Title:** Some JSON in Markdown

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Here is some JSON:
```json
{
  "property": "value"
}
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
