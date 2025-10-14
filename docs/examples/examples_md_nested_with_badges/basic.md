# Person

- [1. [Optional] PropertyPerson > firstName](#firstName)
- [2. [Optional] PropertyPerson > lastName](#lastName)
- [3. [Optional] PropertyPerson > age](#age)
- [4. [Optional] PropertyPerson > driverLicenseId](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `object` |

<details>
<summary>
<strong> <a name="firstName"></a>1. [Optional] PropertyPerson > firstName</strong>  

</summary>
<blockquote>

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. [Optional] PropertyPerson > lastName</strong>  

</summary>
<blockquote>

**Title:** Person

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="age"></a>3. [Optional] PropertyPerson > age</strong>  

</summary>
<blockquote>

**Title:** Person

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="driverLicenseId"></a>4. [Optional] PropertyPerson > driverLicenseId</strong>  

</summary>
<blockquote>

|          |             |
| -------- | ----------- |
| **Type** | `combining` |

<blockquote>

| All of(Requirement)                            |
| ---------------------------------------------- |
| [no driver licence](#driverLicenseId_allOf_i0) |
| [driver licence id](#driverLicenseId_allOf_i1) |

<blockquote>

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

|          |        |
| -------- | ------ |
| **Type** | `null` |

</blockquote>
<blockquote>

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)