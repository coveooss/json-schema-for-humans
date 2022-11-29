# Test

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Test > aProperty`](#aProperty-65727479)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Test > aDictPropertyARequired`](#aDictPropertyARequired-69726564)
  - [2.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a-65645f61)
  - [2.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b-65645f62)

**Title:** Test

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                                      | Pattern | Type             | Deprecated | Definition                     | Title/Description                           |
| ------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | ------------------------------------------- |
| - [aProperty](#aProperty-65727479 )                           | No      | enum (of string) | No         | In #/definitions/aProperty     | This is the description from the definition |
| - [aDictPropertyARequired](#aDictPropertyARequired-69726564 ) | No      | object           | No         | In #/definitions/aDictProperty | -                                           |

## <a name="aProperty-65727479"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Test > aProperty`

|                |                           |
| -------------- | ------------------------- |
| **Type**       | `enum (of string)`        |
| **Default**    | `"Default from property"` |
| **Defined in** | #/definitions/aProperty   |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired-69726564"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Test > aDictPropertyARequired`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `{"a": "a", "b": "b"}`                                                                                                            |
| **Defined in**            | #/definitions/aDictProperty                                                                                                       |

| Property                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| + [a](#aDictPropertyARequired_a-65645f61 ) | No      | string | No         | -          | -                 |
| + [b](#aDictPropertyARequired_b-65645f62 ) | No      | string | No         | -          | -                 |

### <a name="aDictPropertyARequired_a-65645f61"></a>2.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > a`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="aDictPropertyARequired_b-65645f62"></a>2.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Test > aDictPropertyARequired > b`

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
