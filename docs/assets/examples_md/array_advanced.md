

# Schema Docs

Type: `object`

**Description:** A little food fun

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [fruits](#fruits)|No|array of string|No|No| No|5 to 8 fruits that you like|| [vegetables](#vegetables)|No|array|No|No| No||

##  <a name="fruits"></a>1.  Property `root > fruits`

**Description**:  5 to 8 fruits that you like

<table>
 	<tr>
    <td><b>Min items</b></td>
    <td>5</td>
 	</tr>
	<tr>
    <td><b>Max items</b></td>
    <td>8</td>
	</tr>
	<tr>
    <td><b>Items unicity</b></td>
    <td>True</td>
 	</tr>
</table>

###  1. Each item of this array must be

Type: `string`

##  <a name="vegetables"></a>2.  Property `root > vegetables`

<table>
 	<tr>
    <td><b>Min items</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max items</b></td>
    <td>N/A</td>
	</tr>
	<tr>
    <td><b>Items unicity</b></td>
    <td>False</td>
 	</tr>
</table>

###  2. Each item of this array must be

Type: `object`

###  2. At least one of the items must be

Type: `const`

            Specific value: `"eggplant"`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 00:44:57 +0100