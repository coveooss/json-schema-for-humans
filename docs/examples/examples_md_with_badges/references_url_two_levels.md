# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described`](#described)
  - [1.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described > name`](#described_name)
  - [1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described > alignment`](#described_alignment)

|                           |                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                        |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)]("Additional Properties of any type are allowed.") |

**Description:** Testing $ref of a remote $ref

| Property                   | Pattern | Type   | Deprecated | Definition                                                                                                              | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [described](#described ) | No      | object | No         | In https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/description_from_ref.json | -                 |

## <a name="described"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described`

|                           |                                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                             |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)]("Additional Properties not allowed.")               |
| **Defined in**            | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/description_from_ref.json |

| Property                             | Pattern | Type   | Deprecated | Definition                       | Title/Description |
| ------------------------------------ | ------- | ------ | ---------- | -------------------------------- | ----------------- |
| - [name](#described_name )           | No      | string | No         | In #/definitions/filled_string   | a filled string   |
| - [alignment](#described_alignment ) | No      | string | No         | Same as [name](#described_name ) | a filled string   |

### <a name="described_name"></a>1.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described > name`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="described_alignment"></a>1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > described > alignment`

|                        |                         |
| ---------------------- | ----------------------- |
| **Type**               | `string`                |
| **Same definition as** | [name](#described_name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
