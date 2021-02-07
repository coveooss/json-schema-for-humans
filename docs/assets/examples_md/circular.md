# Circular reference Schema

- [1. Property `Circular reference Schema > person`](#person)
  - [1.1. Property `Circular reference Schema > person > a1`](#person_a1)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="person"></a>1. Property `Circular reference Schema > person`

Type: `object`

Defined in: #/definitions/a

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a1](#person_a1)|No|string|No|No| No|Description from b|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="person_a1"></a>1.1. Property `Circular reference Schema > person > a1`

Type: `string`
Default: `"Default from c"`

**Description:** Description from b

Defined in: #/definitions/b

Defined in: #/definitions/c

Defined in: #/definitions/a/properties/a1

<table>
 	<tr>
    <td><b>Min length</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max length</b></td>
    <td>N/A</td>
	</tr>
    <tr>
    <td><b>Must match regular expression</b></td>
    <td>N/A</td>
	</tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 21:29:39 +0100