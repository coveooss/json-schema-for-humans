# Schema Docs

- [1. ![badge](https://img.shields.io/badge/Required-blue) Property `root > outer`](#outer)
  - [1.1. ![badge](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`](#outer_inner)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`](#outer2)

| Type                      | `object`                                                                                         |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Additional properties** | [![badge](https://img.shields.io/badge/Not+allowed-red)](# "Additional Properties not allowed.") |
|                           |                                                                                                  |

| Property             | Pattern | Type   | Deprecated | Definition                    | Title/Description      |
| -------------------- | ------- | ------ | ---------- | ----------------------------- | ---------------------- |
| + [outer](#outer )   | No      | object | No         | In #/definitions/inner schema | We should see this     |
| - [outer2](#outer2 ) | No      | object | No         | Same as [outer](#outer )      | We should see this too |
|                      |         |        |            |                               |                        |

## <a name="outer"></a>1. ![badge](https://img.shields.io/badge/Required-blue) Property `root > outer`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/inner schema                                                                                          |
|                           |                                                                                                                     |

**Description:** We should see this

| Property                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [inner](#outer_inner ) | No      | string | No         | -          | inner description |
|                          |         |        |            |            |                   |

### <a name="outer_inner"></a>1.1. ![badge](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** inner description

## <a name="outer2"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [outer](#outer)                                                                                                     |
|                           |                                                                                                                     |

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date