# Schema Docs

- [1. Property `root > fruits`](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** A schema with an array

| Property             | Pattern | Type            | Deprecated | Definition | Title/Description |
| -------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [fruits](#fruits ) | No      | array of string | No         | -          | -                 |

## <a name="fruits"></a>1. Property `root > fruits`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Example:** 

```json
[
    "apple",
    "banana"
]
```

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

**Example:** 

```json
"apple"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
