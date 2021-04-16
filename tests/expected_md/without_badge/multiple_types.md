# Person

- [1. [Optional] Property `Person > firstName`](#firstName)
- [2. [Optional] Property `Person > lastName`](#lastName)
- [3. [Optional] Property `Person > age`](#age)
- [4. [Optional] Property `Person > anything`](#anything)

**Title:** Person

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Property                   | Pattern | Type                            | Deprecated | Definition | Title/Description                                         |
| -------------------------- | ------- | ------------------------------- | ---------- | ---------- | --------------------------------------------------------- |
| - [firstName](#firstName ) | No      | string                          | No         | -          | The person's first name.                                  |
| - [lastName](#lastName )   | No      | string or null                  | No         | -          | The person's last name.                                   |
| - [age](#age )             | No      | integer or number               | No         | -          | Age in years which must be equal to or greater than zero. |
| - [anything](#anything )   | No      | integer, string, number or null | No         | -          | Ay other info you like                                    |
|                            |         |                                 |            |            |                                                           |

## <a name="firstName"></a>1. [Optional] Property `Person > firstName`

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The person's first name.

## <a name="lastName"></a>2. [Optional] Property `Person > lastName`

| Type                      | `string or null`                                                          |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** The person's last name.

## <a name="age"></a>3. [Optional] Property `Person > age`

| Type                      | `integer or number`                                                       |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
|              |        |

## <a name="anything"></a>4. [Optional] Property `Person > anything`

| Type                      | `integer, string, number or null`                                         |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date