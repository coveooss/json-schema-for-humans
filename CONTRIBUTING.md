# Contributing

Contributions are more than welcome! Don't hesitate to open an incomplete PR to ask for help!

## Python versions

The library currently supports Python versions 3.9+

## Install dependencies

If you don't have it already, install [poetry](https://python-poetry.org/docs/#installation)

Then run
`poetry install`

## Testing

### With Tox

`tox`

### With pytest directly

`poetry run pytest tests`

## Adding a new template

Copy one of the existing template, change the name and start modifying.
If you are looking for examples, you can run `poetry run python docs/generate_examples.py` from the root folder.

The examples will be in:

- `docs/examples/examples_flat_default`
- `docs/examples/examples_js_default`
- `docs/examples/examples_md_default`
- `docs/examples/examples_js_with_bagdes`

## Optional stuff

The maintainer will take care of the following for you if you don't want to bother with it :)

### Formatting with black

Running with tox will ensure the code has been formatted with [black](https://github.com/psf/black)

It is recommended to run black [from your IDE](https://github.com/psf/black/blob/master/docs/editor_integration.md) or as a pre-commit hook

### Modifying Javascript

`schema_doc.js` is not minified automatically, you are responsible for doing it yourself

### Generating doc

The documentation is served by `index.html` deployed on GitHub Pages automatically.
The documentation is using [docsify](https://docsify.js.org/) to render.

#### Adding examples

- Run `poetry run python docs/generate_examples.py`. This will get all examples from `docs/examples/cases`, render the resulting HTML and
  include it in the appropriate folders.
- (optional) If you have added an example, add the file name (without `.json`), the display name and description in `docs/cases_description.yaml`

#### Generating locally

Execute following script from root dir of the repository

```bash
poetry run python docs/generate_examples.py
```

You can check it locally using:

```bash
npm i docsify-cli -g
docsify serve docs
```

Then you can check [generated doc](http://localhost:3000).
