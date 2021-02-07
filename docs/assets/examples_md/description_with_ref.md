# Schema Docs

- [1. Property `root > outer`](#outer)
  - [1.1. Property `root > outer > inner`](#outer_inner)
- [2. Property `root > outer2`](#outer2)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [outer](#outer)|No|object|Yes|No| No|We should see this|
| [outer2](#outer2)|No|object|No|No| No|We should see this too|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

## <a name="outer"></a>1. Property `root > outer`

Type: `object`

**Description:** We should see this
Defined in: #/definitions/inner schema

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [inner](#outer_inner)|No|string|Yes|No| No|inner description|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

### <a name="outer_inner"></a>1.1. Property `root > outer > inner`

Type: `string`

**Description:** inner description

<table>
 	<tr>
    <td><b>Min length</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max length</b></td>
    <td>N/A</td>
	</tr>
</table>

## <a name="outer2"></a>2. Property `root > outer2`

Type: `object`

**Description:** We should see this too
Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 12:13:14 +0100