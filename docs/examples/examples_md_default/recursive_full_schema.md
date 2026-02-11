# Bug

- [1. Property `Bug > Code`](#Code)
- [2. Property `Bug > RecursiveArray`](#RecursiveArray)
  - [2.1. Bug > RecursiveArray > Bug](#RecursiveArray_items)
- [3. Property `Bug > DecoratedRecursiveArray`](#DecoratedRecursiveArray)
  - [3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items](#DecoratedRecursiveArray_items)
    - [3.1.1. Property `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName`](#DecoratedRecursiveArray_items_SomeName)
    - [3.1.2. Property `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing`](#DecoratedRecursiveArray_items_TheThing)

**Title:** Bug

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

**Description:** Display the issue.

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
<li><a href="#">Code</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Code property</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">RecursiveArray</a></li>
</ul></td>
    <td>No</td>
    <td>array</td>
    <td>No</td>
    <td>-</td>
    <td>RecursiveArray property</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">DecoratedRecursiveArray</a></li>
</ul></td>
    <td>No</td>
    <td>array of object</td>
    <td>No</td>
    <td>-</td>
    <td>DecoratedRecursiveArray property</td>
  </tr>
</table>

## <a name="Code"></a>1. Property `Bug > Code`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** Code property

## <a name="RecursiveArray"></a>2. Property `Bug > RecursiveArray`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** RecursiveArray property

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
    <td><a href="#RecursiveArray_items">Bug</a></td>
    <td>Display the issue.</td>
  </tr>
</table>

### <a name="RecursiveArray_items"></a>2.1. Bug > RecursiveArray > Bug

**Title:** Bug

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
  <tr>
    <td><strong>Same definition as</strong></td>
    <td><a href="#root">Bug</a></td>
  </tr>
</table>

**Description:** Display the issue.

## <a name="DecoratedRecursiveArray"></a>3. Property `Bug > DecoratedRecursiveArray`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array of object</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** DecoratedRecursiveArray property

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
    <td><a href="#DecoratedRecursiveArray_items">DecoratedRecursiveArray items</a></td>
    <td>-</td>
  </tr>
</table>

### <a name="DecoratedRecursiveArray_items"></a>3.1. Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items

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
<li><a href="#">SomeName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">TheThing</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>Same as <a href="#">Bug</a></td>
    <td>Bug</td>
  </tr>
</table>

#### <a name="DecoratedRecursiveArray_items_SomeName"></a>3.1.1. Property `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > SomeName`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

#### <a name="DecoratedRecursiveArray_items_TheThing"></a>3.1.2. Property `Bug > DecoratedRecursiveArray > DecoratedRecursiveArray items > TheThing`

**Title:** Bug

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
  <tr>
    <td><strong>Same definition as</strong></td>
    <td><a href="#root">Bug</a></td>
  </tr>
</table>

**Description:** Display the issue.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
