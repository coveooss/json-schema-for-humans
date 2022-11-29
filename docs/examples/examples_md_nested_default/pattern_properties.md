# Person

- [1. [Optional] Property Person > firstName](#firstName-4e616d65)
- [2. [Optional] Property Person > lastName](#lastName-4e616d65)
- [3. [Optional]Pattern Property Person > paperSize](#pattern1-65726e31)
  - [3.1. [Required] Property Person > paperSize > rating](#pattern1_rating-74696e67)
  - [3.2. [Required] Property Person > paperSize > review](#pattern1_review-76696577)

**Title:** Person

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="firstName-4e616d65"></a>1. [Optional] Property Person > firstName</strong>  

</summary>
<blockquote>

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary><strong> <a name="lastName-4e616d65"></a>2. [Optional] Property Person > lastName</strong>  

</summary>
<blockquote>

**Title:** Person

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary><strong> <a name="pattern1-65726e31"></a>3. [Optional]Pattern Property Person > paperSize</strong>  
> All properties whose name matches the regular expression
```$[a-c][0-9]^``` ([Test](https://regex101.com/?regex=%24%5Ba-c%5D%5B0-9%5D%5E))
must respect the following conditions

</summary>
<blockquote>

**Title:** paperSize

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Review of a paper size.

<details>
<summary><strong> <a name="pattern1_rating-74696e67"></a>3.1. [Required] Property Person > paperSize > rating</strong>  

</summary>
<blockquote>

**Title:** Rating

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | Yes       |

**Description:** Numerical rating for paper size.

</blockquote>
</details>

<details>
<summary><strong> <a name="pattern1_review-76696577"></a>3.2. [Required] Property Person > paperSize > review</strong>  

</summary>
<blockquote>

**Title:** Review

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Narrative review of the paper size.

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)