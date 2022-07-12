# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > a`](#a)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > b`](#b)

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property   | Pattern | Type   | Deprecated | Definition              | Title/Description    |
| ---------- | ------- | ------ | ---------- | ----------------------- | -------------------- |
| - [a](#a ) | No      | object | No         | In #/definitions/common | Description of a     |
| - [b](#b ) | No      | object | No         | Same as [a](#a )        | A common description |

## <a name="a"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > a`

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from a"`                                                                                                                |
| **Defined in**            | #/definitions/common                                                                                                              |

**Description:** Description of a

## <a name="b"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > b`

| Type                      | `object`                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Default**               | `"Default from b"`                                                                                                                |
| **Same definition as**    | [a](#a)                                                                                                                           |

**Description:** A common description

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
