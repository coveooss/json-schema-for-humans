# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > name`](#name-6e616d65)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > alignment`](#alignment-6d656e74)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

| Property                            | Pattern | Type   | Deprecated | Definition                      | Title/Description |
| ----------------------------------- | ------- | ------ | ---------- | ------------------------------- | ----------------- |
| - [name](#name-6e616d65 )           | No      | string | No         | In #/definitions/filled_string  | a filled string   |
| - [alignment](#alignment-6d656e74 ) | No      | string | No         | Same as [name](#name-6e616d65 ) | a filled string   |

## <a name="name-6e616d65"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > name`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="alignment-6d656e74"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > alignment`

|                        |               |
| ---------------------- | ------------- |
| **Type**               | `string`      |
| **Same definition as** | [name](#name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
