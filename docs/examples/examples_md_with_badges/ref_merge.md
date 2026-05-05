# Test

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property`Test > aProperty`](#aProperty)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property`Test > aDictPropertyARequired`](#aDictPropertyARequired)
  - [2.1. ![Required](https://img.shields.io/badge/Required-blue) Property`Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a)
  - [2.2. ![Required](https://img.shields.io/badge/Required-blue) Property`Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b)

**Title:** Test

|          |          |
| -------- | -------- |
| **Type** | `object` |

| Property                                             | Pattern | Type             | Deprecated | Definition                     | Title/Description     |
| ---------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------ | --------------------- |
| - [aProperty](#aProperty )                           | No      | enum (of string) | No         | In #/definitions/aProperty     | Title from definition |
| - [aDictPropertyARequired](#aDictPropertyARequired ) | No      | object           | No         | In #/definitions/aDictProperty | -                     |

## <a name="aProperty"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property`Test > aProperty`

**Title:** Title from definition

|                |                           |
| -------------- | ------------------------- |
| **Type**       | `enum (of string)`        |
| **Default**    | `"Default from property"` |
| **Defined in** | #/definitions/aProperty   |

**Description:** This is the description from the definition

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property`Test > aDictPropertyARequired`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `object`                    |
| **Default**    | `{"a": "a", "b": "b"}`      |
| **Defined in** | #/definitions/aDictProperty |

| Property                          | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [a](#aDictPropertyARequired_a ) | No      | string | No         | -          | -                 |
| + [b](#aDictPropertyARequired_b ) | No      | string | No         | -          | -                 |

### <a name="aDictPropertyARequired_a"></a>2.1. ![Required](https://img.shields.io/badge/Required-blue) Property`Test > aDictPropertyARequired > a`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="aDictPropertyARequired_b"></a>2.2. ![Required](https://img.shields.io/badge/Required-blue) Property`Test > aDictPropertyARequired > b`

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
