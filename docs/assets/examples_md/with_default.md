

# User Preference

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [favorite_os](#favorite_os)|No|enum (of string)|No|No| No||| [favorite_colors](#favorite_colors)|No|array of enum (of string)|No|No| No||| [desired_number_of_shoes](#desired_number_of_shoes)|No|integer|No|No| No||

##  <a name="favorite_os"></a>1.  Property `User Preference > favorite_os`

            Must be one of:
                * "Windows"
                * "Mac"
                * "Linux"

##  <a name="favorite_colors"></a>2.  Property `User Preference > favorite_colors`

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

Type: `enum (of string)`

            Must be one of:
                * "green"
                * "blue"
                * "orange"
                * "red"
                * "white"
                * "black"

##  <a name="desired_number_of_shoes"></a>3.  Property `User Preference > desired_number_of_shoes`

        Value must be greater or equal to `0` and lesser or equal to `2`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 00:44:54 +0100