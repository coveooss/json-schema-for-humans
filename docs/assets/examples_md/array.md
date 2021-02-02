

# Schema Docs

Type: `object`

**Description:** A schema with an array

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [fruits](#fruits)|No|array of string|No|No| No|-|
| [vegetables](#vegetables)|No|array|No|No| No|-|

##  <a name="fruits"></a>1.  Property `root > fruits`

Type: `array of string`

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

###  1. Each item of this array must be

Type: `string`

##  <a name="vegetables"></a>2.  Property `root > vegetables`

Type: `array`

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

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [veggieName](#vegetables_items_veggieName)|No|string|Yes|No| No|The name of the vegetable.|
| [veggieLike](#vegetables_items_veggieLike)|No|boolean|Yes|No| No|Do I like this vegetable?|

###  <a name="vegetables_items_veggieName"></a>2.1.  Property `root > vegetables > items > veggieName`

Type: `string`

**Description:** The name of the vegetable.

###  <a name="vegetables_items_veggieLike"></a>2.2.  Property `root > vegetables > items > veggieLike`

Type: `boolean`

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 21:26:34 +0100