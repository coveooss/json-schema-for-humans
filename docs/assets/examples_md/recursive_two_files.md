

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|A human being|

##  <a name="person"></a>1.  Property `Person > person`

Type: `object`

**Description:** A human being

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [children](#person_children)|No|array|No|No| No|The children they had|
| [siblings](#person_siblings)|No|object|No|No| No|Person definition from second file. Not the same!|

###  <a name="person_children"></a>1.1.  Property `Person > person > children`

Type: `array`

**Description:** The children they had

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

####  1.1. Each item of this array must be

Type: `object`

**Description:** Person definition from second file. Not the same!
    Same definition as [siblings](#person_siblings)

###  <a name="person_siblings"></a>1.2.  Property `Person > person > siblings`

Type: `object`

**Description:** Person definition from second file. Not the same!

Type: `object`

**Description:** Person definition from second file. Not the same!

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 21:26:31 +0100