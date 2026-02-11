# Person

- [1. [Optional] Property Person > firstName](#firstName)
- [2. [Optional] Property Person > lastName](#lastName)
- [3. [Optional] Property Person > age](#age)
- [4. [Optional] Property Person > moreInfo](#moreInfo)

<p><strong>Title:</strong> Person</p>

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

<details>
<summary>
<strong> <a name="firstName"></a>1. [Optional] Property Person > firstName</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

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

<p><strong>Description:</strong> the person's first name</p>

<p><strong>Examples:</strong></p>

```json
"Guido"
```

```json
"BDFL"
```

</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. [Optional] Property Person > lastName</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

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

<p><strong>Description:</strong> The person's last name.</p>

<p><strong>Example:</strong></p>

```json
"Van Rossum"
```

</details>

<details>
<summary>
<strong> <a name="age"></a>3. [Optional] Property Person > age</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

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

<p><strong>Description:</strong> Age in years which must be equal to or greater than zero.</p>

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

<p><strong>Example:</strong></p>

```json
64
```

</details>

<details>
<summary>
<strong> <a name="moreInfo"></a>4. [Optional] Property Person > moreInfo</strong>  

</summary>

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

<p><strong>Description:</strong> Any more info you want as an object</p>

<p><strong>Example:</strong></p>

```json
{
    "birthplace": "Haarlem, Netherlands",
    "favorite_emoji": "🐍",
    "motto": "Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren't special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you're Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it's a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let's do more of those!"
}
```

</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)