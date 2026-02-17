# Schema Docs

- [1. Property `root > fruits`](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)
- [2. Property `root > vegetables`](#vegetables)
  - [2.1. root > vegetables > veggie](#vegetables_items)
    - [2.1.1. Property `root > vegetables > vegetables items > veggieName`](#vegetables_items_veggieName)
    - [2.1.2. Property `root > vegetables > vegetables items > veggieLike`](#vegetables_items_veggieLike)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A schema with an array

| Property                     | Pattern | Type            | Deprecated | Definition | Title/Description |
| ---------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [fruits](#fruits )         | No      | array of string | No         | -          | -                 |
| - [vegetables](#vegetables ) | No      | array           | No         | -          | -                 |

## <a name="fruits"></a>1. Property `root > fruits`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [fruits items](#fruits_items)   | -           |

### <a name="fruits_items"></a>1.1. root > fruits > fruits items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="vegetables"></a>2. Property `root > vegetables`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [veggie](#vegetables_items)     | -           |

### <a name="vegetables_items"></a>2.1. root > vegetables > veggie

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/definitions/veggie |

| Property                                      | Pattern | Type    | Deprecated | Definition | Title/Description          |
| --------------------------------------------- | ------- | ------- | ---------- | ---------- | -------------------------- |
| + [veggieName](#vegetables_items_veggieName ) | No      | string  | No         | -          | The name of the vegetable. |
| + [veggieLike](#vegetables_items_veggieLike ) | No      | boolean | No         | -          | Do I like this vegetable?  |

#### <a name="vegetables_items_veggieName"></a>2.1.1. Property `root > vegetables > vegetables items > veggieName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** The name of the vegetable.

#### <a name="vegetables_items_veggieLike"></a>2.1.2. Property `root > vegetables > vegetables items > veggieLike`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
