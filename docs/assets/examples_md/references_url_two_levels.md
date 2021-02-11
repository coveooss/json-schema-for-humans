# Schema Docs

- [1. Property `root > described`](#described)
  - [1.1. Property `root > described > name`](#described_name)
  - [1.2. Property `root > described > alignment`](#described_alignment)

Type: `object`

**Description:** Testing $ref of a remote $ref

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [described](#described)|No|object|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="described"></a>1. Property `root > described`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

Defined in: https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/description_from_ref.json

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [name](#described_name)|No|string|No| No|a filled string|
| [alignment](#described_alignment)|No|string|No| No|a filled string|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

### <a name="described_name"></a>1.1. Property `root > described > name`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** a filled string

Defined in: #/definitions/filled_string

| Restrictions |   |
| ------------ | - |
| **Min length** | 1 |

### <a name="described_alignment"></a>1.2. Property `root > described > alignment`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** a filled string

Same definition as [name](#described_name)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:07 +0100