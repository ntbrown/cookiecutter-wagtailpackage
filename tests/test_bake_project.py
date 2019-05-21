import os
from contextlib import contextmanager

import sh
import pytest
from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests.

    :param cookies: pytest_cookies.Cookies, cookie to be baked and its temporal
    files will be removed.
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_selecting_license(cookies):
    """Test to check if the LICENSE gets the correct license selected."""
    license_strings = {
        'Apache Software License 2.0': 'Apache',
        'BSD': 'Redistributions of source code must retain the above ' +
        'copyright notice, this',
        'ISCL': 'Permission to use, copy, modify, and/or distribute this ' +
        'software for any purpose with or without fee',
        'MIT': 'MIT ',
    }
    for license, target_string in license_strings.items():
        extra_context = {'open_source_license': license}
        with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
            assert target_string in result.project.join('LICENSE').read()
            assert license in result.project.join('setup.py').read()


def test_readme(cookies):
    """Test to check the README files documentation is properly generated."""
    extra_context = {'app_name': 'helloworld'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        readme_file = result.project.join('README.rst')
        readme_lines = [x.strip() for x in readme_file.readlines(cr=False)]
        assert 'Add it to your `INSTALLED_APPS`:' in readme_lines
        assert '(myenv) $ pip install tox' in readme_lines


def test_pages(cookies):
    """Test to the check if Wagtail Page models are properly generated."""
    extra_context = {'pages': 'ChocolateChip,Zimsterne', 'app_name': 'cookies'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        model_file = result.project.join('cookies', 'models.py')
        model_txt = model_file.read()
        assert 'Page' in model_txt


def test_templates(cookies):
    """Test to check the generation of Django templates in the application."""
    pass


def test_travis(cookies):
    """Test to the check the configuration of the travis.yml file."""
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        travis_file = result.project.join('.travis.yml')
        travis_text = travis_file.read()
        assert 'script: tox -e $TOX_ENV' in travis_text


def test_tox(cookies):
    """Tox file is properly generated from cookiecuttervariables."""
    extra_context = {'app_name': 'cookie_lover'}
    required_text = 'commands = coverage run --source cookie_lover runtests.py'
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
        tox_file = result.project.join('tox.ini')
        tox_text = tox_file.read()
        assert required_text in tox_text


def test_authors(cookies):
    """Ensure the authors are correctly included."""
    extra_context = {'full_name': 'Cookie McCookieface'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        authors_file = result.project.join('AUTHORS.rst')
        authors_text = authors_file.read()
        assert 'Cookie McCookieface' in authors_text


def test_manifest(cookies):
    """Ensure the manifest is properly generated."""
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        manifest_file = result.project.join('MANIFEST.in')
        manifest_text = manifest_file.read()
        assert 'recursive-include cookie_lover *.html *.png *.gif *js ' + \
            '*.css *jpg *jpeg *svg *py' in manifest_text


def test_setup_py(cookies):
    """Test to check setup.py files generation from cookiecutter variables."""
    extra_context = {
        'app_name': 'cookie_lover',
        'full_name': 'Cookie McCookieface'
    }
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        setup_file = result.project.join('setup.py')
        setup_text = setup_file.read()
        assert "version=version" in setup_text
        assert "    author='Cookie McCookieface'," in setup_text


# def test_flake8_compliance(cookies):
#     """Test to ensure flake8 compliance."""
#     extra_context = {'create_example_project': 'Y'}
#     with bake_in_temp_dir(cookies, extra_context=extra_context) as result:
#         for file_obj in result.project.listdir():
#             name = os.path.join(
#                 file_obj.dirname,
#                 file_obj.basename
#             )
#             if not name.endswith('.py'):
#                 continue
#             try:
#                 sh.flake8(name)
#             except sh.ErrorReturnCode as e:
#                 pytest.fail(str(e))


def test_app_config(cookies):
    """Test to the check the app config and INSTALLED_APPS."""
    extra_context = {'app_name': 'cookie_lover'}
    with bake_in_temp_dir(cookies, extra_context=extra_context) as result:

        apps_file = result.project.join('cookie_lover', 'apps.py')
        apps_text = apps_file.read()
        assert 'CookieLoverConfig' in apps_text
        assert "name = 'cookie_lover'" in apps_text
        readme_file = result.project.join('README.rst')
        readme_text = readme_file.read()
        assert "'cookie_lover'," in readme_text


# example project tests from here on
def test_make_migrations(cookies):
    """Generated project should be able to generate migrations."""
    with bake_in_temp_dir(cookies, extra_context={}) as result:
        res = result.project.join('manage.py')
        try:
            sh.python(res, 'makemigrations')
            sh.python(res, 'migrate')
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))


def test_run_tests(cookies):
    """Generated project should run tests."""
    with bake_in_temp_dir(cookies, extra_context={}) as result:
        res = result.project.join('runtests.py')
        try:
            with res.dirpath().as_cwd():
                sh.python(res)
        except sh.ErrorReturnCode as e:
            pytest.fail(str(e))
