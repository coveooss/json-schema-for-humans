# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > anything`](#anything)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|The person's first name.|
| [lastName](#lastName)|No|string or null|No|No| No|The person's last name.|
| [age](#age)|No|integer or number|No|No| No|Age in years which must be equal to or greater than zero.|
| [anything](#anything)|No|integer, string, number or null|No|No| No|Ay other info you like|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="firstName"></a>1. Property `Person > firstName`

Type: `string`

**Description:** The person's first name.

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

## <a name="lastName"></a>2. Property `Person > lastName`

Type: `string or null`

**Description:** The person's last name.

## <a name="age"></a>3. Property `Person > age`

Type: `integer or number`

**Description:** Age in years which must be equal to or greater than zero.

## <a name="anything"></a>4. Property `Person > anything`

Type: `integer, string, number or null`

**Description:** Ay other info you like

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 21:29:40 +0100