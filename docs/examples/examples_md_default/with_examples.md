# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > moreInfo`](#moreInfo)

**Title:** Person

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
<li><a href="#">firstName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">lastName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">age</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">moreInfo</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>Any more info you want as an object</td>
  </tr>
</table>

## <a name="firstName"></a>1. Property `Person > firstName`

**Title:** Person

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

**Description:** the person's first name

**Examples:**

```json
"Guido"
```

```json
"BDFL"
```

## <a name="lastName"></a>2. Property `Person > lastName`

**Title:** Person

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

**Description:** The person's last name.

**Example:**

```json
"Van Rossum"
```

## <a name="age"></a>3. Property `Person > age`

**Title:** Person

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
</table>

**Description:** Age in years which must be equal to or greater than zero.

**Example:**

```json
64
```

<table>
  <tr>
    <th>Restrictions</th>
    <th> </th>
  </tr>
  <tr>
    <td><strong>Minimum</strong></td>
    <td>&ge; 0</td>
  </tr>
</table>

## <a name="moreInfo"></a>4. Property `Person > moreInfo`

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

**Description:** Any more info you want as an object

**Example:**

```json
{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren't special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you're Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it's a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let's do more of those!"
}
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
