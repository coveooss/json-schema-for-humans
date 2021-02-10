# Schema Docs

- [1. Property `root > fruits`](#fruits)
- [2. Property `root > vegetables`](#vegetables)

Type: `object`

**Description:** A schema with an array

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [fruits](#fruits)|No|array of string|No|No| No|-|
| [vegetables](#vegetables)|No|array|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="fruits"></a>1. Property `root > fruits`

Type: `array of string`

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

## <a name="vegetables"></a>2. Property `root > vegetables`

Type: `array`

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 00:42:31 +0100