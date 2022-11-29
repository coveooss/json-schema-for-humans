# Person

- [1. Property `Person > firstName`](#firstName-4e616d65)
- [2. Property `Person > lastName`](#lastName-4e616d65)
- [3. Property `Person > age`](#age-616765)
- [4. Property `Person > driverLicenseId`](#driverLicenseId-73654964)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0-665f6930)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1-665f6931)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                        | Pattern | Type        | Deprecated | Definition | Title/Description |
| ----------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [firstName](#firstName-4e616d65 )             | No      | string      | No         | -          | Person            |
| - [lastName](#lastName-4e616d65 )               | No      | string      | No         | -          | Person            |
| - [age](#age-616765 )                           | No      | integer     | No         | -          | Person            |
| - [driverLicenseId](#driverLicenseId-73654964 ) | No      | Combination | No         | -          | -                 |

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

## <a name="age-616765"></a>3. Property `Person > age`

**Title:** Person

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="driverLicenseId-73654964"></a>4. Property `Person > driverLicenseId`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| All of(Requirement)                                     |
| ------------------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0-665f6930) |
| [driver licence id](#driverLicenseId_allOf_i1-665f6931) |

### <a name="driverLicenseId_allOf_i0-665f6930"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="driverLicenseId_allOf_i1-665f6931"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
