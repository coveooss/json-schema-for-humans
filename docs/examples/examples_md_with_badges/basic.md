# Person

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`](#firstName)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`](#lastName)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > age`](#age)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > driverLicenseId`](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)
- [5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > middleName`](#middleName)

**Title:** Person

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                    |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| Property                               | Pattern | Type        | Deprecated | Definition | Title/Description                |
| -------------------------------------- | ------- | ----------- | ---------- | ---------- | -------------------------------- |
| - [firstName](#firstName )             | No      | string      | No         | -          | Person [(read more)](#firstName) |
| - [lastName](#lastName )               | No      | string      | No         | -          | Person [(read more)](#lastName)  |
| - [age](#age )                         | No      | integer     | No         | -          | Person [(read more)](#age)       |
| - [driverLicenseId](#driverLicenseId ) | No      | Combination | No         | -          | -                                |
| - [middleName](#middleName )           | No      | string      | No         | -          | Middle Name                      |

## <a name="firstName"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > firstName`

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

## <a name="lastName"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > lastName`

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's last name.

## <a name="age"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > age`

**Title:** Person

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="driverLicenseId"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > driverLicenseId`

|                           |                                                                             |
| ------------------------- | --------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                 |
| **Additional properties** | ![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green) |

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|          |        |
| -------- | ------ |
| **Type** | `null` |

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="middleName"></a>5. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > middleName`

**Title:** Middle Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
