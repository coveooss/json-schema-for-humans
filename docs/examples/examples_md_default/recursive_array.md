# Person

- [1. Property `Person > person`](#person)
  - [1.1. Person > person > person](#person_items)
    - [1.1.1. Property `Person > person > person items > children`](#person_items_children)
      - [1.1.1.1. Person > person > person items > children > person](#person_items_children_items)

**Title:** Person

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property             | Pattern | Type  | Deprecated | Definition | Title/Description |
| -------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [person](#person ) | No      | array | No         | -          | A list of people  |

## <a name="person"></a>1. Property `Person > person`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of people

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description   |
| ------------------------------- | ------------- |
| [person](#person_items)         | A human being |

### <a name="person_items"></a>1.1. Person > person > person

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/definitions/person |

**Description:** A human being

| Property                              | Pattern | Type  | Deprecated | Definition | Title/Description     |
| ------------------------------------- | ------- | ----- | ---------- | ---------- | --------------------- |
| - [children](#person_items_children ) | No      | array | No         | -          | The children they had |

#### <a name="person_items_children"></a>1.1.1. Property `Person > person > person items > children`

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

| Each item of this array must be        | Description   |
| -------------------------------------- | ------------- |
| [person](#person_items_children_items) | A human being |

##### <a name="person_items_children_items"></a>1.1.1.1. Person > person > person items > children > person

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `object`                      |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [person_items](#person_items) |

**Description:** A human being

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
