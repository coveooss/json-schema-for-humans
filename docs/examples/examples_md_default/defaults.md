# Schema Docs

- [1. Property `root > a`](#a-61)
- [2. Property `root > b`](#b-62)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property      | Pattern | Type   | Deprecated | Definition              | Title/Description    |
| ------------- | ------- | ------ | ---------- | ----------------------- | -------------------- |
| - [a](#a-61 ) | No      | object | No         | In #/definitions/common | Description of a     |
| - [b](#b-62 ) | No      | object | No         | Same as [a](#a-61 )     | A common description |

## <a name="a-61"></a>1. Property `root > a`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from a"`                                                        |
| **Defined in**            | #/definitions/common                                                      |

**Description:** Description of a

## <a name="b-62"></a>2. Property `root > b`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from b"`                                                        |
| **Same definition as**    | [a](#a)                                                                   |

**Description:** A common description

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
