# python_git_versioning
Handles pushing directly to the main branch with arguments to handle versioning. 

Install python requirements through pip, just put this command in the terminal once you installed pip and python
*pip install -r requirements.txt*

* -M
## MAJOR is incremented when:
    Significant changes occur to the product, or a new product direction.
    Breaking changes were taken. There's a high bar to accepting breaking changes.
    An old version is no longer supported.
    A newer MAJOR version of an existing dependency is adopted.
* -m
## MINOR is incremented when:
    Public API surface area is added.
    A new behavior is added.
    A newer MINOR version of an existing dependency is adopted.
    A new dependency is introduced.
    PATCH is incremented when:
* -b
## Bug fixes are made.
    Support for a newer platform is added.
    A newer PATCH version of an existing dependency is adopted.
    Any other change doesn't fit one of the previous cases.