# Schema Docs

- [1. Property`root > name`](#name)
- [2. Property`root > alignment`](#alignment)

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                   | Pattern | Type   | Deprecated | Definition                     | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ------------------------------ | ----------------- |
| - [name](#name )           | No      | string | No         | In #/definitions/filled_string | a filled string   |
| - [alignment](#alignment ) | No      | string | No         | Same as [name](#name )         | a filled string   |

## <a name="name"></a>1. Property`root > name`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Required**   | No                          |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

## <a name="alignment"></a>2. Property`root > alignment`

|                        |               |
| ---------------------- | ------------- |
| **Type**               | `string`      |
| **Required**           | No            |
| **Same definition as** | [name](#name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
