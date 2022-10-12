# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > anything`](#anything)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                   | Pattern | Type                            | Deprecated | Definition | Title/Description                                         |
| -------------------------- | ------- | ------------------------------- | ---------- | ---------- | --------------------------------------------------------- |
| - [firstName](#firstName ) | No      | string                          | No         | -          | The person's first name.                                  |
| - [lastName](#lastName )   | No      | string or null                  | No         | -          | The person's last name.                                   |
| - [age](#age )             | No      | integer or number               | No         | -          | Age in years which must be equal to or greater than zero. |
| - [anything](#anything )   | No      | integer, string, number or null | No         | -          | Ay other info you like                                    |

## <a name="firstName"></a>1. Property `Person > firstName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

**Description:** The person's last name.

## <a name="age"></a>3. Property `Person > age`

|              |                     |
| ------------ | ------------------- |
| **Type**     | `integer or number` |
| **Required** | No                  |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="anything"></a>4. Property `Person > anything`

|              |                                   |
| ------------ | --------------------------------- |
| **Type**     | `integer, string, number or null` |
| **Required** | No                                |

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
