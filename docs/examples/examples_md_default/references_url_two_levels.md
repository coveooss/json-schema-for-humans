# Schema Docs

- [1. Property `root > described`](#described-69626564)
  - [1.1. Property `root > described > name`](#described_name-6e616d65)
  - [1.2. Property `root > described > alignment`](#described_alignment-6d656e74)

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Testing $ref of a remote $ref

| Property                            | Pattern | Type   | Deprecated | Definition                                                                                                              | Title/Description |
| ----------------------------------- | ------- | ------ | ---------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------- |
| - [described](#described-69626564 ) | No      | object | No         | In https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/description_from_ref.json | -                 |

## <a name="described-69626564"></a>1. Property `root > described`

|                           |                                                                                                                      |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                             |
| **Required**              | No                                                                                                                   |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.")                                                              |
| **Defined in**            | https://raw.githubusercontent.com/coveooss/json-schema-for-humans/main/docs/examples/cases/description_from_ref.json |

| Property                                      | Pattern | Type   | Deprecated | Definition                                | Title/Description |
| --------------------------------------------- | ------- | ------ | ---------- | ----------------------------------------- | ----------------- |
| - [name](#described_name-6e616d65 )           | No      | string | No         | In #/definitions/filled_string            | a filled string   |
| - [alignment](#described_alignment-6d656e74 ) | No      | string | No         | Same as [name](#described_name-6e616d65 ) | a filled string   |

### <a name="described_name-6e616d65"></a>1.1. Property `root > described > name`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Required**   | No                          |
| **Defined in** | #/definitions/filled_string |

**Description:** a filled string

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

### <a name="described_alignment-6d656e74"></a>1.2. Property `root > described > alignment`

|                        |                         |
| ---------------------- | ----------------------- |
| **Type**               | `string`                |
| **Required**           | No                      |
| **Same definition as** | [name](#described_name) |

**Description:** a filled string

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
