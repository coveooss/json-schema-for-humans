# User Preference

- [1. Property `User Preference > favorite_os`](#favorite_os)
- [2. Property `User Preference > favorite_colors`](#favorite_colors)
  - [2.1. User Preference > favorite_colors > favorite_colors items](#favorite_colors_items)
- [3. Property `User Preference > desired_number_of_shoes`](#desired_number_of_shoes)

**Title:** User Preference

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">favorite_os</a></li>
</ul></td>
    <td>No</td>
    <td>enum (of string)</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">favorite_colors</a></li>
</ul></td>
    <td>No</td>
    <td>array of enum (of string)</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">desired<em>number</em>of_shoes</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

## <a name="favorite_os"></a>1. Property `User Preference > favorite_os`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>"Linux"</code></td>
  </tr>
</table>

Must be one of:
* "Windows"
* "Mac"
* "Linux"

## <a name="favorite_colors"></a>2. Property `User Preference > favorite_colors`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array of enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>["white", "blue"]</code></td>
  </tr>
</table>

<table>
  <tr>
    <th></th>
    <th>Array restrictions</th>
  </tr>
  <tr>
    <td><strong>Min items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Max items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Items unicity</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Additional items</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Tuple validation</strong></td>
    <td>See below</td>
  </tr>
</table>

<table>
  <tr>
    <th>Each item of this array must be</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="#favorite_colors_items">favorite_colors items</a></td>
    <td>-</td>
  </tr>
</table>

### <a name="favorite_colors_items"></a>2.1. User Preference > favorite_colors > favorite_colors items

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>enum (of string)</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

Must be one of:
* "green"
* "blue"
* "orange"
* "red"
* "white"
* "black"

## <a name="desired_number_of_shoes"></a>3. Property `User Preference > desired_number_of_shoes`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>integer</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Default</strong></td>
    <td><code>2</code></td>
  </tr>
</table>

<table>
  <tr>
    <th>Restrictions</th>
    <th> </th>
  </tr>
  <tr>
    <td><strong>Minimum</strong></td>
    <td>&ge; 0</td>
  </tr>
  <tr>
    <td><strong>Maximum</strong></td>
    <td>&le; 2</td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
