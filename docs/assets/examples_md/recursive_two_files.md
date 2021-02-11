# Person

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person`](#person)
  - [1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person > children`](#person_children)
  - [1.2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person > siblings`](#person_siblings)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [person](#person)|No|object|No|A human being|

## <a name="person"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/person |

**Description:** A human being

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [children](#person_children)|No|array|No|The children they had|
|-  [siblings](#person_siblings)|No|object|No|Person definition from second file. Not the same!|

### <a name="person_children"></a>1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person > children`

| Type | `array` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|

**Description:** The children they had

|                       | Array restrictions |
| --------------------- | ------------------ |
| **Min items**         | N/A |
| **Max items**         | N/A |
| **Items unicity**     | False |
| **Additional items**  | False |
| **Tuple validation**  | N/A |

### <a name="person_siblings"></a>1.2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Person > person > siblings`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | recursive_two_files2.json#/definitions/person |

**Description:** Person definition from second file. Not the same!

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 22:25:42 +0100