# Person

- [1. [Optional] Property Person > firstName](#firstName)
- [2. [Optional] Property Person > lastName](#lastName)
- [3. [Optional] Property Person > age](#age)
- [4. [Optional] Property Person > anything](#anything)

**Title:** Person

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

<details>
<summary>
<strong> <a name="firstName"></a>1. [Optional] Property Person > firstName</strong>  

</summary>
<blockquote>

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. [Optional] Property Person > lastName</strong>  

</summary>
<blockquote>

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string or null` |
| **Required** | No               |

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="age"></a>3. [Optional] Property Person > age</strong>  

</summary>
<blockquote>

|              |                     |
| ------------ | ------------------- |
| **Type**     | `integer or number` |
| **Required** | No                  |

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anything"></a>4. [Optional] Property Person > anything</strong>  

</summary>
<blockquote>

|              |                                   |
| ------------ | --------------------------------- |
| **Type**     | `integer, string, number or null` |
| **Required** | No                                |

**Description:** Ay other info you like

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)