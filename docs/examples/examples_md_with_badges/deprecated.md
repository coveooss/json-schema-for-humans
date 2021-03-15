# Schema Docs

- [1. ![badge](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~](#deprecated1)
- [2. ![badge](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~](#deprecated2)
- [3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`](#not_deprecated)

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** Test schema with deprecated in description

| Property                             | Pattern | Type   | Deprecated                                            | Definition | Title/Description                           |
| ------------------------------------ | ------- | ------ | ----------------------------------------------------- | ---------- | ------------------------------------------- |
| - [deprecated1](#deprecated1 )       | No      | object | ![badge](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated]                                |
| - [deprecated2](#deprecated2 )       | No      | object | ![badge](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated - Use 'not_deprecated' instead] |
| - [not_deprecated](#not_deprecated ) | No      | string | No                                                    | -          | -                                           |
|                                      |         |        |                                                       |            |                                             |

## <a name="deprecated1"></a>1. ![badge](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Deprecated**            | ![badge](https://img.shields.io/badge/Deprecated-red)                                                               |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** [Deprecated]

## <a name="deprecated2"></a>2. ![badge](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Deprecated**            | ![badge](https://img.shields.io/badge/Deprecated-red)                                                               |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

**Description:** [Deprecated - Use `not_deprecated` instead]

## <a name="not_deprecated"></a>3. ![badge](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date