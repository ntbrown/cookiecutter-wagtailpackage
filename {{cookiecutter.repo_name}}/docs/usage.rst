=====
Usage
=====

To use {{ cookiecutter.project_name }} in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}.apps.{{ cookiecutter.app_config_name }}',
        ...
    )
