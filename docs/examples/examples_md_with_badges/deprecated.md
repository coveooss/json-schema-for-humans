# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~](#deprecated1)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~](#deprecated2)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated3`~~](#deprecated3)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated4`~~](#deprecated4)
- [5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`](#not_deprecated)

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** Test schema with deprecated in description

| Property                             | Pattern | Type   | Deprecated                                                 | Definition | Title/Description                                     |
| ------------------------------------ | ------- | ------ | ---------------------------------------------------------- | ---------- | ----------------------------------------------------- |
| - [deprecated1](#deprecated1 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated]                                          |
| - [deprecated2](#deprecated2 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | [Deprecated - Use \`not_deprecated\` instead]         |
| - [deprecated3](#deprecated3 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | This is [Deprecated]                                  |
| - [deprecated4](#deprecated4 )       | No      | object | ![Deprecated](https://img.shields.io/badge/Deprecated-red) | -          | This is [Deprecated - Use \`not_deprecated\` instead] |
| - [not_deprecated](#not_deprecated ) | No      | string | No                                                         | -          | -                                                     |

## <a name="deprecated1"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated1`~~

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                      |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** [Deprecated]

## <a name="deprecated2"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated2`~~

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                      |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** [Deprecated - Use `not_deprecated` instead]

## <a name="deprecated3"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated3`~~

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                      |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated]

## <a name="deprecated4"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow)~~ Property `root > deprecated4`~~

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Deprecated**            | ![Deprecated](https://img.shields.io/badge/Deprecated-red)                                                                      |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated - Use `not_deprecated` instead]

## <a name="not_deprecated"></a>5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > not_deprecated`

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
