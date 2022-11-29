# Schema Docs

- [1. Property `root > outer`](#outer-75746572)
  - [1.1. Property `root > outer > inner`](#outer_inner-6e6e6572)
- [2. Property `root > outer2`](#outer2-74657232)

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |

| Property                      | Pattern | Type   | Deprecated | Definition                        | Title/Description      |
| ----------------------------- | ------- | ------ | ---------- | --------------------------------- | ---------------------- |
| + [outer](#outer-75746572 )   | No      | object | No         | In #/definitions/inner schema     | We should see this     |
| - [outer2](#outer2-74657232 ) | No      | object | No         | Same as [outer](#outer-75746572 ) | We should see this too |

## <a name="outer-75746572"></a>1. Property `root > outer`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | Yes                                                     |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/inner schema                              |

**Description:** We should see this

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [inner](#outer_inner-6e6e6572 ) | No      | string | No         | -          | inner description |

### <a name="outer_inner-6e6e6572"></a>1.1. Property `root > outer > inner`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** inner description

## <a name="outer2-74657232"></a>2. Property `root > outer2`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Same definition as**    | [outer](#outer)                                         |

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
