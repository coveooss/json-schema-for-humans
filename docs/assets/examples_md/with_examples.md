# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > moreInfo`](#moreInfo)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No| No|the person's first name|
| [lastName](#lastName)|No|string|No| No|The person's last name.|
| [age](#age)|No|integer|No| No|Age in years which must be equal to or greater than zero.|
| [moreInfo](#moreInfo)|No|object|No| No|Any more info you want as an object|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="firstName"></a>1. Property `Person > firstName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** the person's first name

**Examples:** 

```json
"Guido"
```
```json
"BDFL"
```

## <a name="lastName"></a>2. Property `Person > lastName`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `string`

**Description:** The person's last name.

**Example:** 

```json
"Van Rossum"
```

## <a name="age"></a>3. Property `Person > age`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `integer`

**Description:** Age in years which must be equal to or greater than zero.

| Restrictions |   |
| ------------ | - |
| **Minimum** | &ge; 0 |

**Example:** 

```json
64
```

## <a name="moreInfo"></a>4. Property `Person > moreInfo`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** Any more info you want as an object

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

**Example:** 

```json
{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren't special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you're Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it's a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let's do more of those!"
}
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 01:21:03 +0100