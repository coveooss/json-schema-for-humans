# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > moreInfo`](#moreInfo)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|the person's first name|
| [lastName](#lastName)|No|string|No|No| No|The person's last name.|
| [age](#age)|No|integer|No|No| No|Age in years which must be equal to or greater than zero.|
| [moreInfo](#moreInfo)|No|object|No|No| No|Any more info you want as an object|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="firstName"></a>1. Property `Person > firstName`

Type: `string`

**Description:** the person's first name

<table>
 	<tr>
    <td><b>Min length</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max length</b></td>
    <td>N/A</td>
	</tr>
    <tr>
    <td><b>Must match regular expression</b></td>
    <td>N/A</td>
	</tr>
</table>

**Examples:** 

```json
"Guido"
```
```json
"BDFL"
```

## <a name="lastName"></a>2. Property `Person > lastName`

Type: `string`

**Description:** The person's last name.

<table>
 	<tr>
    <td><b>Min length</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max length</b></td>
    <td>N/A</td>
	</tr>
    <tr>
    <td><b>Must match regular expression</b></td>
    <td>N/A</td>
	</tr>
</table>

**Example:** 

```json
"Van Rossum"
```

## <a name="age"></a>3. Property `Person > age`

Type: `integer`

**Description:** Age in years which must be equal to or greater than zero.

<table>
 	<tr>
    <td><b>Multiple of</b></td>
    <td>N/A</td>
 	</tr>
    <td><b>Minimum</b></td>
    <td>&ge; 0</td>
 	</tr>
	<tr>
    <td><b>Maximum</b></td>
    <td>N/A</td>
 	</tr>
</table>

**Example:** 

```json
64
```

## <a name="moreInfo"></a>4. Property `Person > moreInfo`

Type: `object`

**Description:** Any more info you want as an object

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
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
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 21:29:38 +0100