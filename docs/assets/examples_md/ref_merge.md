# Test

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Test > aProperty`](#aProperty)
- [2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Test > aDictPropertyARequired`](#aDictPropertyARequired)
  - [2.1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a)
  - [2.2. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [aProperty](#aProperty)|No|enum (of string)|No|This is the description from the definition|
|-  [aDictPropertyARequired](#aDictPropertyARequired)|No|object|No|-|
|  |  |  |  |  |

## <a name="aProperty"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Test > aProperty`

| Type | `enum (of string)` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `"Default from property"` |
| **Defined in** | #/definitions/aProperty |
|  |  |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Test > aDictPropertyARequired`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `{"a": "a", "b": "b"}` |
| **Defined in** | #/definitions/aDictProperty |
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|+  [a](#aDictPropertyARequired_a)|No|string|No|-|
|+  [b](#aDictPropertyARequired_b)|No|string|No|-|
|  |  |  |  |  |

### <a name="aDictPropertyARequired_a"></a>2.1. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > a`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

### <a name="aDictPropertyARequired_b"></a>2.2. ![made-with-Markdown](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > b`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:34:12 +0100