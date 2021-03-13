# Circular reference Schema

- [1. [Optional] Property `Circular reference Schema > person`](#person)
  - [1.1. [Optional] Property `Circular reference Schema > person > a1`](#person_a1)

**Title:** Circular reference Schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Property             | Pattern | Type   | Deprecated | Definition         | Title/Description |
| -------------------- | ------- | ------ | ---------- | ------------------ | ----------------- |
| - [person](#person ) | No      | object | No         | In #/definitions/a | -                 |
|                      |         |        |            |                    |                   |

## <a name="person"></a>1. [Optional] Property `Circular reference Schema > person`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/a                                                           |
|                           |                                                                           |

| Property            | Pattern | Type   | Deprecated | Definition         | Title/Description  |
| ------------------- | ------- | ------ | ---------- | ------------------ | ------------------ |
| - [a1](#person_a1 ) | No      | string | No         | In #/definitions/b | Description from b |
|                     |         |        |            |                    |                    |

### <a name="person_a1"></a>1.1. [Optional] Property `Circular reference Schema > person > a1`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from c"`                                                        |
| **Defined in**            | #/definitions/b                                                           |
|                           |                                                                           |

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date