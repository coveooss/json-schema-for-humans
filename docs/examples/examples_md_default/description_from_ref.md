# Schema Docs

- [1. [Optional] Property `root > name`](#name)
- [2. [Optional] Property `root > alignment`](#alignment)

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
|                           |                                                         |

| Property                   | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [name](#name )           | No      | string | No         | In #/definitions/filled_string | a filled string   |
| - [alignment](#alignment ) | No      | string | No         | Same as [name](#name )         | a filled string   |
|                            |         |        |            |                                |                   |

## <a name="name"></a>1. [Optional] Property `root > name`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/filled_string                                               |
|                           |                                                                           |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |
|                |   |

## <a name="alignment"></a>2. [Optional] Property `root > alignment`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [name](#name)                                                             |
|                           |                                                                           |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date