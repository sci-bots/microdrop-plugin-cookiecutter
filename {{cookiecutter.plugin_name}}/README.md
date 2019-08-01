# {{cookiecutter.project_name}} #

{{cookiecutter.project_short_description}}

-------------------------------------------------------------------------------

Install
-------

The latest [`{{cookiecutter.package_name}}` release][1] is available as a
[Conda][2] package from the [`{{cookiecutter.github_organization or cookiecutter.github_username}}`][2] channel.

To install `{{cookiecutter.package_name}}` in an **activated Conda environment**, run:

    conda install -c {{cookiecutter.github_organization or cookiecutter.github_username}} -c conda-forge {{cookiecutter.package_name}}

-------------------------------------------------------------------------------

Develop
-------

 1. Install dependencies listed in `requirements.host` section of
    [`.conda-recipe/meta.yaml`](/.conda-recipe/meta.yaml).
 2. Run the following command from the repository root:
 ```
 python -m mpm.bin.build -p {{cookiecutter.package_name}} --properties-only -s . -t .
 ```
 3. Select or create directory as root to hold development plugins, e.g.,
 ```
 mkdir %USERPROFILE%\microdrop-dev-plugins
 ```
 4. Create link to repo directory in development root with import-friendly
    **_plugin_** name, e.g.:
 ```sh
 mklink /J %USERPROFILE%\microdrop-dev-plugins\{{cookiecutter.plugin_name}} %REPO_DIR%
 ```
 5. Add development plugins directory to `;`-separated list of paths in
    `MICRODROP_PLUGINS_PATH` environment variable.

-------------------------------------------------------------------------------

License
-------

This project is licensed under the terms of the [{{cookiecutter.license}} license](/LICENSE.md)

-------------------------------------------------------------------------------

Contributors
------------

 - {{cookiecutter.full_name}} ([@{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}}))


[1]: https://github.com/{{cookiecutter.github_organization or cookiecutter.github_username}}/{{cookiecutter.package_name}}
[2]: https://anaconda.org/{{cookiecutter.github_organization or cookiecutter.github_username}}/{{cookiecutter.package_name}}
