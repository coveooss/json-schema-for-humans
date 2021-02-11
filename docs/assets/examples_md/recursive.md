# Person

- [1. Property `Person > person`](#person)
  - [1.1. Property `Person > person > children`](#person_children)

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:30 +0100