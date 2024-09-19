# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > driverLicenseId`](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

**Title:** Person

|                           |                                                                         |
| ------------------------- | ----------------------------------------------------------------------- |
| **Type**                  | `object`                                                                |
| **Required**              | No                                                                      |
| **Additional properties** | [[Any type: allowed]]("Additional Properties of any type are allowed.") |

| Property                               | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [firstName](#firstName )             | No      | string      | No         | -          | Person            |
| - [lastName](#lastName )               | No      | string      | No         | -          | Person            |
| - [age](#age )                         | No      | integer     | No         | -          | Person            |
| - [driverLicenseId](#driverLicenseId ) | No      | Combination | No         | -          | -                 |

## <a name="firstName"></a>1. Property `Person > firstName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

## <a name="lastName"></a>2. Property `Person > lastName`

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's last name.

## <a name="age"></a>3. Property `Person > age`

**Title:** Person

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="driverLicenseId"></a>4. Property `Person > driverLicenseId`

|                           |                                                                         |
| ------------------------- | ----------------------------------------------------------------------- |
| **Type**                  | `combining`                                                             |
| **Required**              | No                                                                      |
| **Additional properties** | [[Any type: allowed]]("Additional Properties of any type are allowed.") |

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
