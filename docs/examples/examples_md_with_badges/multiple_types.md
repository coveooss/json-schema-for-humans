# Person

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`](#firstName-4e616d65)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`](#lastName-4e616d65)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > age`](#age-616765)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > anything`](#anything-68696e67)

**Title:** Person

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                            | Pattern | Type                            | Deprecated | Definition | Title/Description                                         |
| ----------------------------------- | ------- | ------------------------------- | ---------- | ---------- | --------------------------------------------------------- |
| - [firstName](#firstName-4e616d65 ) | No      | string                          | No         | -          | The person's first name.                                  |
| - [lastName](#lastName-4e616d65 )   | No      | string or null                  | No         | -          | The person's last name.                                   |
| - [age](#age-616765 )               | No      | integer or number               | No         | -          | Age in years which must be equal to or greater than zero. |
| - [anything](#anything-68696e67 )   | No      | integer, string, number or null | No         | -          | Ay other info you like                                    |

## <a name="firstName-4e616d65"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

## <a name="lastName-4e616d65"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`

|          |                  |
| -------- | ---------------- |
| **Type** | `string or null` |

**Description:** The person's last name.

## <a name="age-616765"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > age`

|          |                     |
| -------- | ------------------- |
| **Type** | `integer or number` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="anything-68696e67"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > anything`

|          |                                   |
| -------- | --------------------------------- |
| **Type** | `integer, string, number or null` |

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
