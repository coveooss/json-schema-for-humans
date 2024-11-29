# HTML in descriptions

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > raw_html`](#raw_html)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > html_in_markdown`](#html_in_markdown)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > json_in_markdown`](#json_in_markdown)

**Title:** HTML in descriptions

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description     |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | --------------------- |
| - [raw_html](#raw_html )                 | No      | string | No         | -          | Some raw HTML         |
| - [html_in_markdown](#html_in_markdown ) | No      | string | No         | -          | Some HTML in Markdown |
| - [json_in_markdown](#json_in_markdown ) | No      | string | No         | -          | Some JSON in Markdown |

## <a name="raw_html"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > raw_html`

**Title:** Some raw HTML

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** <br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>

## <a name="html_in_markdown"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > html_in_markdown`

**Title:** Some HTML in Markdown

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Here is some HTML:
```html
<br/><br/><br/><br/><a href="https://example.com">A link to example.com</a>
```

## <a name="json_in_markdown"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `HTML in descriptions > json_in_markdown`

**Title:** Some JSON in Markdown

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Here is some JSON:
```json
{
  "property": "value"
}
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
