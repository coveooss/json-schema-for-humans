# Person

- [1. Property `Person > firstName`](#firstName-4e616d65)
- [2. Property `Person > lastName`](#lastName-4e616d65)
- [3. Pattern Property `Person > paperSize`](#pattern1-65726e31)
  - [3.1. Property `Person > paperSize > rating`](#pattern1_rating-74696e67)
  - [3.2. Property `Person > paperSize > review`](#pattern1_review-76696577)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                              | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [firstName](#firstName-4e616d65 )   | No      | string | No         | -          | Person            |
| - [lastName](#lastName-4e616d65 )     | No      | string | No         | -          | Person            |
| - [$[a-c][0-9]^](#pattern1-65726e31 ) | Yes     | object | No         | -          | paperSize         |

## <a name="firstName-4e616d65"></a>1. Property `Person > firstName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

## <a name="lastName-4e616d65"></a>2. Property `Person > lastName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's last name.

## <a name="pattern1-65726e31"></a>3. Pattern Property `Person > paperSize`
> All properties whose name matches the regular expression
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

**Title:** paperSize

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Review of a paper size.

| Property                               | Pattern | Type    | Deprecated | Definition | Title/Description |
| -------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| + [rating](#pattern1_rating-74696e67 ) | No      | integer | No         | -          | Rating            |
| + [review](#pattern1_review-76696577 ) | No      | string  | No         | -          | Review            |

### <a name="pattern1_rating-74696e67"></a>3.1. Property `Person > paperSize > rating`

**Title:** Rating

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Numerical rating for paper size.

### <a name="pattern1_review-76696577"></a>3.2. Property `Person > paperSize > review`

**Title:** Review

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Narrative review of the paper size.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
