# Longitude and Latitude Values

- [1. Property `Longitude and Latitude Values > latitude`](#latitude)
- [2. Property `Longitude and Latitude Values > longitude`](#longitude)

Type: `object`

**Description:** A geographical coordinate.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [latitude](#latitude)|No|number|Yes|No| No|-|
| [longitude](#longitude)|No|number|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="latitude"></a>1. Property `Longitude and Latitude Values > latitude`

Type: `number`

<table>
 	<tr>
    <td><b>Multiple of</b></td>
    <td>N/A</td>
 	</tr>
    <td><b>Minimum</b></td>
    <td>&ge; -90</td>
 	</tr>
	<tr>
    <td><b>Maximum</b></td>
    <td>&le; 90</td>
 	</tr>
</table>

## <a name="longitude"></a>2. Property `Longitude and Latitude Values > longitude`

Type: `number`

<table>
 	<tr>
    <td><b>Multiple of</b></td>
    <td>N/A</td>
 	</tr>
    <td><b>Minimum</b></td>
    <td>&ge; -180</td>
 	</tr>
	<tr>
    <td><b>Maximum</b></td>
    <td>&le; 180</td>
 	</tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 21:34:05 +0100