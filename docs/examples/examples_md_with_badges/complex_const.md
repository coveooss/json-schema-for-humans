# Schema Docs

- [1. Property `root > oneOf > 1st constant`](#oneOf_i0)
- [2. Property `root > oneOf > 2nd constant`](#oneOf_i1)

| Type                      | `combining`                                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

| One of(Option)            |
| ------------------------- |
| [1st constant](#oneOf_i0) |
| [2nd constant](#oneOf_i1) |
|                           |

## <a name="oneOf_i0"></a>1. Property `root > oneOf > 1st constant`

**Title:** 1st constant

| Type                      | `const`                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

Specific value: `[
    1,
    2
]`

## <a name="oneOf_i1"></a>2. Property `root > oneOf > 2nd constant`

**Title:** 2nd constant

| Type                      | `const`                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

Specific value: `{
    "a_key": "a_value",
    "another_key": "another_value"
}`

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |
|                      |                    |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date