# Schema Docs

- [1. Property `root > name`](#name-6e616d65)
- [2. Property `root > alignment`](#alignment-6d656e74)

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                            | Pattern | Type   | Deprecated | Definition                      | Title/Description |
| ----------------------------------- | ------- | ------ | ---------- | ------------------------------- | ----------------- |
| - [name](#name-6e616d65 )           | No      | string | No         | In #/definitions/filled_string  | a filled string   |
| - [alignment](#alignment-6d656e74 ) | No      | string | No         | Same as [name](#name-6e616d65 ) | a filled string   |

## <a name="name-6e616d65"></a>1. Property `root > name`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Required**   | No                          |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="alignment-6d656e74"></a>2. Property `root > alignment`

|                        |               |
| ---------------------- | ------------- |
| **Type**               | `string`      |
| **Required**           | No            |
| **Same definition as** | [name](#name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
