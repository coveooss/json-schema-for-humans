Contributions are more than welcome! Don't hesitate to open an incomplete PR to ask for help!

# Python versions

The library currently supports Python versions 3.6+

# Testing

## With Tox
Just run tox

`tox`

## With pytest directly
`python -m pytest tests`

(Or `python3 -m pytest tests` if you still have Python 2 laying around)

# Adding a new template

Just copy one of the existing template, change the name and start modifying.
If you are looking for examples, you can run `generate_examples.py` from the `docs` folder, after changing this line tp add your template name:
```python
config = GenerationConfiguration(deprecated_from_description=True, expand_buttons=True, template_name="my_new_template")
```

The examples will be in `docs/assets/examples`

# Optional stuff
The maintainer will take care of the following for you if you don't want to bother with it :)

## Formatting with black
Running with tox will ensure the code has been formatted with [black](https://github.com/psf/black)

It is recommended to run black [from your IDE](https://github.com/psf/black/blob/master/docs/editor_integration.md) or as a pre-commit hook

## Modifying Javascript
`schema_doc.js` is not minified automatically, you are responsible for doing it yourself

## Generating doc
The documentation is generated using jekyll and hosted on GitHub Pages

- Change your current working directory to `docs`
- Run ``python generate_examples.py``. This will get all examples from `tests/cases`, render the resulting HTML and
 include it in the appropriate folders in the jekyll site.
- If you have added an example, add the file name (without `.json`), the display name and description in `_data/examples.yaml`