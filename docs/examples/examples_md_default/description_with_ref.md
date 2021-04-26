# Schema Docs

- [1. [Required] Property `root > outer`](#outer)
  - [1.1. [Required] Property `root > outer > inner`](#outer_inner)
- [2. [Optional] Property `root > outer2`](#outer2)

| Type                      | `object`                                                |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
|                           |                                                         |

| Property             | Pattern | Type   | Deprecated | Definition                    | Title/Description      |
| -------------------- | ------- | ------ | ---------- | ----------------------------- | ---------------------- |
| + [outer](#outer )   | No      | object | No         | In #/definitions/inner schema | We should see this     |
| - [outer2](#outer2 ) | No      | object | No         | Same as [outer](#outer )      | We should see this too |
|                      |         |        |            |                               |                        |

## <a name="outer"></a>1. [Required] Property `root > outer`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/inner schema                                                |
|                           |                                                                           |

**Description:** We should see this

| Property                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [inner](#outer_inner ) | No      | string | No         | -          | inner description |
|                          |         |        |            |            |                   |

### <a name="outer_inner"></a>1.1. [Required] Property `root > outer > inner`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** inner description

## <a name="outer2"></a>2. [Optional] Property `root > outer2`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [outer](#outer)                                                           |
|                           |                                                                           |

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date