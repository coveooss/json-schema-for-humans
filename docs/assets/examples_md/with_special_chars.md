# Personne

- [1. Property `Personne > prénom`](#pr_nom)
- [2. Property `Personne > nomDeFamille`](#nomDeFamille)
- [3. Property `Personne > âge`](#a_ge)
- [4. Property `Personne > 0 de quoi d'autre`](#a0_de_quoi_d_autre)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [prénom](#pr_nom)|No|string|No|No| No|Le prénom de la personne.|
| [nomDeFamille](#nomDeFamille)|No|string|No|No| No|Le nom de famille de la personne.|
| [âge](#a_ge)|No|integer|No|No| No|L'âge en années qui doit être plus grand ou égal à 0.|
| [0 de quoi d'autre](#a0_de_quoi_d_autre)|No|string|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="pr_nom"></a>1. Property `Personne > prénom`

Type: `string`

**Description:** Le prénom de la personne.

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

## <a name="nomDeFamille"></a>2. Property `Personne > nomDeFamille`

Type: `string`

**Description:** Le nom de famille de la personne.

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

## <a name="a_ge"></a>3. Property `Personne > âge`

Type: `integer`

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

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

## <a name="a0_de_quoi_d_autre"></a>4. Property `Personne > 0 de quoi d'autre`

Type: `string`

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
"🖖"
```
```json
"صباح الخير"
```
```json
"你好"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 21:29:39 +0100