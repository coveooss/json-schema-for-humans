# Circular reference Schema

- [1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Circular reference Schema > person`](#person)
  - [1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Circular reference Schema > person > a1`](#person_a1)

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [person](#person)|No|object|No|-|
|  |  |  |  |  |

## <a name="person"></a>1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Circular reference Schema > person`

| Type | `object` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Defined in** | #/definitions/a |
|  |  |

| Property | Pattern | Type | Deprecated | Description |
| -------- | ------- | ---- | ---------- | ----------- |
|-  [a1](#person_a1)|No|string|No|Description from b|
|  |  |  |  |  |

### <a name="person_a1"></a>1.1. ![made-with-Markdown](https://img.shields.io/badge/Optional-yellow) Property `Circular reference Schema > person > a1`

| Type | `string` |
| ---- | --- |
| **Additional properties** |[![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|
| **Default** | `"Default from c"` |
| **Defined in** | #/definitions/b |
|  |  |

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-12 at 23:34:11 +0100