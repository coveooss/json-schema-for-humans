# Schema Docs

- [1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > name`](#name)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > alignment`](#alignment)

| Type                      | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | [![badge](https://img.shields.io/badge/Not+allowed-red)](# "Additional Properties not allowed.") |
|                           |                                                                                                  |

| Property                   | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [name](#name )           | No      | string | No         | In #/definitions/filled_string | a filled string   |
| - [alignment](#alignment ) | No      | string | No         | Same as [name](#name )         | a filled string   |
|                            |         |        |            |                                |                   |

## <a name="name"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > name`

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/filled_string                                                                                         |
|                           |                                                                                                                     |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |
|                |   |

## <a name="alignment"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > alignment`

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [name](#name)                                                                                                       |
|                           |                                                                                                                     |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date