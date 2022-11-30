# Test

- [1. Property `Test > aProperty`](#aProperty)
- [2. Property `Test > aDictPropertyARequired`](#aDictPropertyARequired)
  - [2.1. Property `Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a)
  - [2.2. Property `Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b)

**Title:** Test

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                             | Pattern | Type             | Deprecated | Definition                     | Title/Description                           |
| ---------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ------------------------------------------- |
| - [aProperty](#aProperty )                           | No      | enum (of string) | No         | In #/definitions/aProperty     | This is the description from the definition |
| - [aDictPropertyARequired](#aDictPropertyARequired ) | No      | object           | No         | In #/definitions/aDictProperty | -                                           |

## <a name="aProperty"></a>1. Property `Test > aProperty`

|                |                           |
| -------------- | ------------------------- |
| **Type**       | `enum (of string)`        |
| **Required**   | No                        |
| **Default**    | `"Default from property"` |
| **Defined in** | #/definitions/aProperty   |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. Property `Test > aDictPropertyARequired`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{"a": "a", "b": "b"}`                                                    |
| **Defined in**            | #/definitions/aDictProperty                                               |

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [a](#aDictPropertyARequired_a ) | No      | string | No         | -          | -                 |
| + [b](#aDictPropertyARequired_b ) | No      | string | No         | -          | -                 |

### <a name="aDictPropertyARequired_a"></a>2.1. Property `Test > aDictPropertyARequired > a`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

### <a name="aDictPropertyARequired_b"></a>2.2. Property `Test > aDictPropertyARequired > b`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
