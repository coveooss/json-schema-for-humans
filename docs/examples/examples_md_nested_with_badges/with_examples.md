# Person

- [1. [Optional] PropertyPerson > firstName](#firstName)
- [2. [Optional] PropertyPerson > lastName](#lastName)
- [3. [Optional] PropertyPerson > age](#age)
- [4. [Optional] PropertyPerson > moreInfo](#moreInfo)

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

**Description:** the person's first name

**Examples:**

```json
"Guido"
```

```json
"BDFL"
```

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

**Example:**

```json
"Van Rossum"
```

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

**Example:**

```json
64
```

</blockquote>
</details>

<details>
<summary>
<strong> <a name="moreInfo"></a>4. [Optional] PropertyPerson > moreInfo</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `object` |

**Description:** Any more info you want as an object

**Example:**

```json
{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren't special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you're Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it's a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let's do more of those!"
}
```

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)