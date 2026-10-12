# LEDGER Documentation

This repo contains the complete documentation for the LEDGER project. The site is built with Material for MkDocs.

To start developing on the documentation please use the following steps:

1. Fork this repository and clone it
2. run `uv sync` to create a development environment 
3. start a development server with `mkdocs serve --livereload` 
4. make changes to the documentation
5. commit changes and open a merge request. 

## Notes
- This site is built with Material for MkDocs, which relies on MkDocs 1.x under the hood. Material is [not backwards compatible with Mkdocs 2.0](https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/). The solution will likely be to use [Zensical](https://zensical.org/) as a drop-in replacement for Mkdocs 1.x. 