# Schema Docs

- [1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer`](#outer-75746572)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`](#outer_inner-6e6e6572)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`](#outer2-74657232)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

| Property                      | Pattern | Type   | Deprecated | Definition                        | Title/Description      |
| ----------------------------- | ------- | ------ | ---------- | --------------------------------- | ---------------------- |
| + [outer](#outer-75746572 )   | No      | object | No         | In #/definitions/inner schema     | We should see this     |
| - [outer2](#outer2-74657232 ) | No      | object | No         | Same as [outer](#outer-75746572 ) | We should see this too |

## <a name="outer-75746572"></a>1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/inner schema                                                                               |

**Description:** We should see this

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [inner](#outer_inner-6e6e6572 ) | No      | string | No         | -          | inner description |

### <a name="outer_inner-6e6e6572"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** inner description

## <a name="outer2-74657232"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |
| **Same definition as**    | [outer](#outer)                                                                                          |

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
