Contributions are more than welcome! Don't hesitate to open an incomplete PR to ask for help!

# Python versions

The library currently supports Python versions 3.6+

# Testing

## With Tox
Just run tox

`tox`

## With pytest directly
`python -m pytest tests`

(Or `python3 -m pytest tests` if you still have Python 2 (e.g.: Ubuntu))

# Adding a new template

Just copy one of the existing template, change the name and start modifying.
If you are looking for examples, you can run `python3 generate_examples.py flat` or `python3 generate_examples.py js` from the `docs` folder.

The examples will be in `docs/assets/examples_flat` (resp. `docs/assets/examples_js`).

Markdown examples are in `tests/expected_md` and are generated running `python3 generate_expected_md.py` from `tests` folder.

# Optional stuff
The maintainer will take care of the following for you if you don't want to bother with it :)

## Formatting with black
Running with tox will ensure the code has been formatted with [black](https://github.com/psf/black)

It is recommended to run black [from your IDE](https://github.com/psf/black/blob/master/docs/editor_integration.md) or as a pre-commit hook

## Modifying Javascript
`schema_doc.js` is not minified automatically, you are responsible for doing it yourself

## Generating doc
The documentation is generated using Jekyll and hosted on GitHub Pages

### Adding examples

- Change your current working directory to `docs`
- Run ``python generate_examples.py``. This will get all examples from `tests/cases`, render the resulting HTML and
 include it in the appropriate folders in the jekyll site.
- If you have added an example, add the file name (without `.json`), the display name and description in `_data/examples.yaml`

### Generating locally

#### Linux
Execute following script from root dir of the repository
```bash
sudo apt update
sudo apt install ruby-bundler ruby-dev
(cd docs && bundle install)
(cd docs && python3 generate_examples.py flat)
(cd docs && python3 generate_examples.py js)
(cd tests && python3 generate_expected_md.py)
mkdir -p docs/_includes/examples_md_with_badge
cp tests/expected_md/with_badge/* docs/_includes/examples_md_with_badge
mkdir -p docs/_includes/examples_md_without_badge
cp -R tests/expected_md/without_badge/* docs/_includes/examples_md_without_badge
(cd docs && bundle exec jekyll build)
```

####  Windows

See https://docs.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll
