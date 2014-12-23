=============================
Tethys Web Processing Service
=============================

Tethys Web Processing Service (WPS) provides an API for WPS services such as 52 North WPS. WPS services can be
used to add geoprocessing functionality to web sites that use this app. The Tethys WPS django app also adds
a development tool that can be used to browse the available processing capabilities. When Tethys WPS is installed,
it also installs, OWSLib. OWSLib is a Python client for OGC web services and it includes an excellent WPS module.

Installation
------------

Tethys Datasets can be installed via pip or downloading the source. To install via pip::

  pip install django-tethys_wps

To install via download::

  git clone https://github.com/CI-WATER/django-tethys_wps.git
  cd django-tethys_wps
  python setup.py install

Django Configuration
--------------------

1. Add "tethys_datasets" to your INSTALLED_APPS setting like so::

  INSTALLED_APPS = (
      ...
      'tethys_wps',
  )

2. Include the URLconf in your project urls.py::

  url(r'^wps/', include('tethys_wps.urls')),

3. Use the admin console of your site to link WPS services to your site.