import sys
import os

extensions = [
    'sphinx.ext.autodoc',  # Support automatic documentation
    'sphinx.ext.coverage', # Automatically check if functions are documented
    'sphinx.ext.mathjax',  # Allow support for algebra
    'sphinx.ext.viewcode', # Include the source code in documentation
    'numpydoc'             # Support NumPy style docstrings
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Hunt'
copyright = u'2019, JL. Castro Gonzalez, K. Goldmann, T. Oruc, O. Thompson-Sargoni'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'PackagingTreatsuredoc'
latex_elements = {
}

latex_documents = [
  ('index', 'Hunt.tex', u'Hunt Documentation',
   u'JL. Castro Gonzalez, K. Goldmann, T. Oruc, O. Thompson-Sargoni', 'manual'),
]

man_pages = [
    ('index', 'Hunt', u'Hunt Documentation',
     [u'JL. Castro Gonzalez, K. Goldmann, T. Oruc, O. Thompson-Sargoni'], 1)
]

texinfo_documents = [
  ('index', 'Hunt', u'Hunt Documentation',
   u'JL. Castro Gonzalez, K. Goldmann, T. Oruc, O. Thompson-Sargoni', 'Hunt', 'We are hunting the wumpus!',
   'Miscellaneous'),
]
