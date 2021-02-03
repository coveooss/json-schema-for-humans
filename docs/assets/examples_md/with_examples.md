

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [firstName](#firstName)|No|string|No|No| No|the person's first name|
| [lastName](#lastName)|No|string|No|No| No|The person's last name.|
| [age](#age)|No|integer|No|No| No|Age in years which must be equal to or greater than zero.|
| [moreInfo](#moreInfo)|No|object|No|No| No|Any more info you want as an object|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="firstName"></a>1.  Property `Person > firstName`

Type: `string`

**Description:** the person's first name

**Examples:** 

```
    <div class="highlight"><pre><span></span><span class="s2">&quot;Guido&quot;</span>
</pre></div>

```
```
    <div class="highlight"><pre><span></span><span class="s2">&quot;BDFL&quot;</span>
</pre></div>

```

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="lastName"></a>2.  Property `Person > lastName`

Type: `string`

**Description:** The person's last name.

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="s2">&quot;Van Rossum&quot;</span>
</pre></div>

```

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="age"></a>3.  Property `Person > age`

Type: `integer`

**Description:** Age in years which must be equal to or greater than zero.

        Value must be greater or equal to `0`

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="mi">64</span>
</pre></div>

```

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="moreInfo"></a>4.  Property `Person > moreInfo`

Type: `object`

**Description:** Any more info you want as an object

**Example:** 

```
    <div class="highlight"><pre><span></span><span class="p">{</span>
    <span class="s2">&quot;birthplace&quot;</span><span class="o">:</span> <span class="s2">&quot;Haarlem, Netherlands&quot;</span><span class="p">,</span>
    <span class="s2">&quot;favorite_emoji&quot;</span><span class="o">:</span> <span class="s2">&quot;🐍&quot;</span><span class="p">,</span>
    <span class="s2">&quot;motto&quot;</span><span class="o">:</span> <span class="s2">&quot;Beautiful is better than ugly.\\nExplicit is better than implicit.\\nSimple is better than complex.\\nComplex is better than complicated.\\nFlat is better than nested.\\nSparse is better than dense.\\nReadability counts.\\nSpecial cases aren&#39;t special enough to break the rules.\\nAlthough practicality beats purity.\\nErrors should never pass silently.\\nUnless explicitly silenced.\\nIn the face of ambiguity, refuse the temptation to guess.\\nThere should be one-- and preferably only one --obvious way to do it.\\nAlthough that way may not be obvious at first unless you&#39;re Dutch.\\nNow is better than never.\\nAlthough never is often better than *right* now.\\nIf the implementation is hard to explain, it&#39;s a bad idea.\\nIf the implementation is easy to explain, it may be a good idea.\\nNamespaces are one honking great idea -- let&#39;s do more of those!&quot;</span>
<span class="p">}</span>
</pre></div>

```

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:46 +0100