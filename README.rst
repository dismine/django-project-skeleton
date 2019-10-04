django-project-skeleton
=======================

**django-project-skeleton** is my skeleton for Django projects. It provides a
directory structure for Django projects during development and deployment.


Meta
----

Author:
    Mischback
    Gavin Burnell
    Roman Telezhynskyi (this fork)

Contributors:
    `agirardeaudale <https://github.com/agirardeuadale>`_,
    `jmrbcu <https://github.com/jmrbcu>`_

Status:
    maintained, in development

Version:
    1.3

Django Version:
    1.9, 1.10, 1.11, 2.0

Python Version:
    3.6 (tested)



Usage
-----

To use this repository just use the ``template`` option of `django-admin and run
<https://docs.djangoproject.com/en/1.11/ref/django-admin/#startproject>`_::

    $ django-admin startproject --template=https://github.com/dismine/django-project-skeleton/archive/development.zip [projectname]

If you wish to automagically fill the ``apache2_vhost.sample`` the command is::

    $ django-admin startproject --template=https://github.com/Mischback/django-project-skeleton/archive/development.zip --name apache2_vhost.sample [projectname]


Documentation
-------------

You can see the documentation for the original version over at **Read the Docs**: `django-project-skeleton
<http://django-project-skeleton.readthedocs.org/en/latest/>`_

This fork updates some things for Django 1.10 and Apache 2.4 and changes a few defaults to things I like better.