# Person

- [1. Property `Person > person`](#person)
  - [1.1. Property `Person > person > children`](#person_children)
  - [1.2. Property `Person > person > siblings`](#person_siblings)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [person](#person)|No|object|No| No|A human being|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="person"></a>1. Property `Person > person`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** A human being

Defined in: #/definitions/person

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [children](#person_children)|No|array|No| No|The children they had|
|-  [siblings](#person_siblings)|No|object|No| No|Person definition from second file. Not the same!|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="person_children"></a>1.1. Property `Person > person > children`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `array`

**Description:** The children they had

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

### <a name="person_siblings"></a>1.2. Property `Person > person > siblings`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** Person definition from second file. Not the same!

Defined in: recursive_two_files2.json#/definitions/person

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:26 +0100