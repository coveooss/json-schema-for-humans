# Schema Docs

- [1. ~~ Property `root > deprecated1`~~](#deprecated1)
- [2. ~~ Property `root > deprecated2`~~](#deprecated2)
- [3. ~~ Property `root > deprecated3`~~](#deprecated3)
- [4. ~~ Property `root > deprecated4`~~](#deprecated4)
- [5. Property `root > not_deprecated`](#not_deprecated)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Test schema with deprecated in description

| Property                             | Pattern | Type   | Deprecated   | Definition | Title/Description                                   |
| ------------------------------------ | ------- | ------ | ------------ | ---------- | --------------------------------------------------- |
| - [deprecated1](#deprecated1 )       | No      | object | [Deprecated] | -          | [Deprecated]                                        |
| - [deprecated2](#deprecated2 )       | No      | object | [Deprecated] | -          | [Deprecated - Use 'not_deprecated' instead]         |
| - [deprecated3](#deprecated3 )       | No      | object | [Deprecated] | -          | This is [Deprecated]                                |
| - [deprecated4](#deprecated4 )       | No      | object | [Deprecated] | -          | This is [Deprecated - Use 'not_deprecated' instead] |
| - [not_deprecated](#not_deprecated ) | No      | string | No           | -          | -                                                   |

## <a name="deprecated1"></a>1. ~~ Property `root > deprecated1`~~

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** [Deprecated]

## <a name="deprecated2"></a>2. ~~ Property `root > deprecated2`~~

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** [Deprecated - Use `not_deprecated` instead]

## <a name="deprecated3"></a>3. ~~ Property `root > deprecated3`~~

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated]

## <a name="deprecated4"></a>4. ~~ Property `root > deprecated4`~~

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Deprecated**            | [Deprecated]                                                              |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** This is [Deprecated - Use `not_deprecated` instead]

## <a name="not_deprecated"></a>5. Property `root > not_deprecated`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
