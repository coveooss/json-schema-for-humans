# Circular reference Schema

- [1. Property `Circular reference Schema > person`](#person-72736f6e)
  - [1.1. Property `Circular reference Schema > person > a1`](#person_a1-6e5f6131)

**Title:** Circular reference Schema

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                      | Pattern | Type   | Deprecated | Definition         | Title/Description |
| ----------------------------- | ------- | ------ | ---------- | ------------------ | ----------------- |
| - [person](#person-72736f6e ) | No      | object | No         | In #/definitions/a | -                 |

## <a name="person-72736f6e"></a>1. Property `Circular reference Schema > person`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/a                                                           |

| Property                     | Pattern | Type   | Deprecated | Definition         | Title/Description  |
| ---------------------------- | ------- | ------ | ---------- | ------------------ | ------------------ |
| - [a1](#person_a1-6e5f6131 ) | No      | string | No         | In #/definitions/b | Description from b |

### <a name="person_a1-6e5f6131"></a>1.1. Property `Circular reference Schema > person > a1`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Default**    | `"Default from c"` |
| **Defined in** | #/definitions/b    |

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
