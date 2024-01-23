# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os 
import sys


current_dir = os.path.dirname(__file__)
target_dir = os.path.abspath(os.path.join(current_dir, "../text2graph-api"))
sys.path.insert(0, target_dir)
print('current_dir: ', current_dir)
print('target_dir: ', target_dir)

#sys.path.insert(0, os.path.abspath('../text2graph-api/src'))
#print('target_dir: ', os.path.abspath('../text2graph-api/src'))


#current_dir = os.path.dirname(__file__)
#target_dir = os.path.abspath(os.path.join(current_dir, "../src/models/"))
#sys.path.insert(0, target_dir)
#sys.path.append("C:/Users/Qualtop/Desktop/andric/Projects/text2graph-API/src/")

#print('current_dir: ', current_dir)
#print('target_dir: ', target_dir)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'text2graph-api'
copyright = '2022, PLN-disca-iimas'
author = 'PLN-disca-iimas'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
