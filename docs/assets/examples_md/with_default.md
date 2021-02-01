# User Preference
Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
|favorite_os|No|enum (of string)|No|No| No||
|favorite_colors|No|array of enum (of string)|No|No| No||
|desired_number_of_shoes|No|integer|No|No| No||

## <a name="favorite_os"></a> 1. Property `User Preference > favorite_os`

    Type: `enum (of string)`
             Default: `"Linux"`

                Must be one of:
                    * "Windows"
                    * "Mac"
                    * "Linux"

## <a name="favorite_colors"></a> 2. Property `User Preference > favorite_colors`

    Type: `array of enum (of string)`
             Default: `["white", "blue"]`

#### Each item of this array must be
Type: `enum (of string)`

                Must be one of:
                    * "green"
                    * "blue"
                    * "orange"
                    * "red"
                    * "white"
                    * "black"

## <a name="desired_number_of_shoes"></a> 3. Property `User Preference > desired_number_of_shoes`

    Type: `integer`
             Default: `2`

        Value must be greater or equal to `0` and lesser or equal to `2`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-01 at 09:18:48 +0100