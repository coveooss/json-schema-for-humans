## [1.3.1](https://github.com/coveooss/json-schema-for-humans/compare/v1.3.0...v1.3.1) (2024-11-29)


### Bug Fixes

* Fix markdown "break on newline" configurability ([#236](https://github.com/coveooss/json-schema-for-humans/issues/236)) ([c0c9d09](https://github.com/coveooss/json-schema-for-humans/commit/c0c9d09e00427786dc571d4cd71b7c36c80dc811))

# [1.3.0](https://github.com/coveooss/json-schema-for-humans/compare/v1.2.0...v1.3.0) (2024-11-29)


### Features

* Look up property title by following references ([#280](https://github.com/coveooss/json-schema-for-humans/issues/280)) ([57f68d6](https://github.com/coveooss/json-schema-for-humans/commit/57f68d6be7670882718e0e1931610e32e0963ad3)), closes [#278](https://github.com/coveooss/json-schema-for-humans/issues/278)

# [1.2.0](https://github.com/coveooss/json-schema-for-humans/compare/v1.1.1...v1.2.0) (2024-11-29)


### Features

* Add `description_safe_mode` config option ([#283](https://github.com/coveooss/json-schema-for-humans/issues/283)) ([a17ce95](https://github.com/coveooss/json-schema-for-humans/commit/a17ce95475e3e9b83e340ef35f4bb30427b62a7b))

## [1.1.1](https://github.com/coveooss/json-schema-for-humans/compare/v1.1.0...v1.1.1) (2024-11-29)


### Bug Fixes

* Deprecate `minify` CLI option ([b428474](https://github.com/coveooss/json-schema-for-humans/commit/b428474ba6eeee0c0dd66ce9ae842a4a46c3b3d6))

# [1.1.0](https://github.com/coveooss/json-schema-for-humans/compare/v1.0.4...v1.1.0) (2024-11-29)


### Features

* Add `allow_html_description` config option ([#282](https://github.com/coveooss/json-schema-for-humans/issues/282)) ([6c5f00e](https://github.com/coveooss/json-schema-for-humans/commit/6c5f00e9d74095214a74820800d7389fac1ddcbe))

## [1.0.4](https://github.com/coveooss/json-schema-for-humans/compare/v1.0.3...v1.0.4) (2024-11-27)


### Bug Fixes

* **python:** support python3.13 and drop python3.8 ([#273](https://github.com/coveooss/json-schema-for-humans/issues/273)) ([063410e](https://github.com/coveooss/json-schema-for-humans/commit/063410e6cf13975c0a01280c404287a996a537dd))

## [1.0.3](https://github.com/coveooss/json-schema-for-humans/compare/v1.0.2...v1.0.3) (2024-08-30)


### Bug Fixes

* new properties are ignored whith allOf using $ref ([#249](https://github.com/coveooss/json-schema-for-humans/issues/249)) ([7049af7](https://github.com/coveooss/json-schema-for-humans/commit/7049af7bc51b40d7ea6b9117b89125e03b98fde7))

## [1.0.2](https://github.com/coveooss/json-schema-for-humans/compare/v1.0.1...v1.0.2) (2024-05-16)


### Bug Fixes

* Fix for unstable enum description templating_utils.py ([#243](https://github.com/coveooss/json-schema-for-humans/issues/243)) ([c304af8](https://github.com/coveooss/json-schema-for-humans/commit/c304af8f0a104e18b3b4f42ee280392918c62368))

## [1.0.1](https://github.com/coveooss/json-schema-for-humans/compare/v1.0.0...v1.0.1) (2024-05-06)


### Bug Fixes

* Move types packages to dev-dependencies ([#242](https://github.com/coveooss/json-schema-for-humans/issues/242)) ([8050904](https://github.com/coveooss/json-schema-for-humans/commit/805090460bbbce5dccb5eb9a5d7c960a8cdae73e))

# [1.0.0](https://github.com/coveooss/json-schema-for-humans/compare/v0.47.5...v1.0.0) (2024-05-03)

# 0.48

(Issue #190) Now correctly display elements next to a `$ref` with reused nodes, e.g.:

```json
{
  "$schema": "https://json-schema.org/draft/2019-09/schema",
  "type": "object",
  "title": "Example",
  "properties": {
    "prop1": {
      "$ref": "#/$defs/a",
      "description": "Prop1",
      "examples": ["1"]
    },
    "prop2": {
      "$ref": "#/$defs/a",
      "description": "Prop2",
      "examples": ["2"]
    }
  },
  "$defs": {
    "a": {
      "type": "string",
      "maxLength": 5
    }
  }
}
```

Previously, `prop2` would have been a link to `prop1`, hiding the different example for `prop2`.

This may increase the size of rendered schemas in certain situations.
