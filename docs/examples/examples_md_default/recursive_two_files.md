# Person

- [1. Property`Person > person`](#person)
  - [1.1. Property`Person > person > children`](#person_children)
    - [1.1.1. Person > person > children > person](#person_children_items)
  - [1.2. Property`Person > person > siblings`](#person_siblings)

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

| Property             | Pattern | Type   | Deprecated | Definition              | Title/Description |
| -------------------- | ------- | ------ | ---------- | ----------------------- | ----------------- |
| - [person](#person ) | No      | object | No         | In #/definitions/person | A human being     |

## <a name="person"></a>1. Property`Person > person`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `object`             |
| **Required**   | No                   |
| **Defined in** | #/definitions/person |

**Description:** A human being

| Property                        | Pattern | Type   | Deprecated | Definition                                               | Title/Description                                 |
| ------------------------------- | ------- | ------ | ---------- | -------------------------------------------------------- | ------------------------------------------------- |
| - [children](#person_children ) | No      | array  | No         | -                                                        | The children they had                             |
| - [siblings](#person_siblings ) | No      | object | No         | Same as [person_children_items](#person_children_items ) | Person definition from second file. Not the same! |

### <a name="person_children"></a>1.1. Property`Person > person > children`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The children they had

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be  | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| [person](#person_children_items) | Person definition from second file. Not the same! |

#### <a name="person_children_items"></a>1.1.1. Person > person > children > person

|                |                                               |
| -------------- | --------------------------------------------- |
| **Type**       | `object`                                      |
| **Required**   | No                                            |
| **Defined in** | recursive_two_files2.json#/definitions/person |

**Description:** Person definition from second file. Not the same!

### <a name="person_siblings"></a>1.2. Property`Person > person > siblings`

|                        |                                                 |
| ---------------------- | ----------------------------------------------- |
| **Type**               | `object`                                        |
| **Required**           | No                                              |
| **Same definition as** | [person_children_items](#person_children_items) |

**Description:** Person definition from second file. Not the same!

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
