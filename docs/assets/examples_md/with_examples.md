# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|firstName|No|string|No|No| No|the person's first name|
|lastName|No|string|No|No| No|The person's last name.|
|age|No|integer|No|No| No|Age in years which must be equal to or greater than zero.|
| [moreInfo](#moreInfo)|No|object|No|No| No|Any more info you want as an object|

  ## <a name="moreInfo"></a>Property `moreInfo`

  **Description**:  Any more info you want as an object

      Person
 >   moreInfo

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-01-31 at 20:34:34 +0100