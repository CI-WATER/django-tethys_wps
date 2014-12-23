from urllib2 import HTTPError

from tethys_apps.base.app_base import TethysAppBase

from owslib.wps import WebProcessingService
from .models import WebProcessingService as WpsModel


def abstract_is_link(process):
    """
    Determine if the process abstract is a link.

    Args:
      process (owslib.wps.Process): WPS Process object.

    Returns:
      (bool): True if abstract is a link, False otherwise.
    """
    try:
        abstract = process.abstract
    except AttributeError:
        return False

    if abstract[:4] == 'http':
        return True

    else:
        return False


def list_wps_service_engines():
    """
    Get all wps engines offered.

    Returns:
      (tuple): A tuple of WPS engine dictionaries.
    """
    # Init vars
    wps_services_list = []

    # If the wps engine cannot be found in the app_class, check settings for site-wide wps engines
    site_wps_services = WpsModel.objects.all()

    for site_wps_service in site_wps_services:

        # Create OWSLib WebProcessingService engine object
        wps = WebProcessingService(site_wps_service.endpoint,
                                   username=site_wps_service.username,
                                   password=site_wps_service.password,
                                   verbose=False,
                                   skip_caps=True)

        # Initialize the object with get capabilities call
        try:
            wps.getcapabilities()
        except HTTPError as e:
            if e.code == 404:
                e.msg = 'The WPS service could not be found at given endpoint "{0}" for site WPS service ' \
                        'named "{1}". Check the configuration of the WPS service in your ' \
                        'settings.py.'.format(site_wps_service.endpoint, site_wps_service.name)
                raise e
            else:
                raise e
        except:
            raise

        wps_services_list.append(wps)

    return wps_services_list


def get_wps_service_engine(name, app_class=None):
    """
    Get a wps engine with the given name.

    Args:
      name (string): Name of the wps engine to retrieve.
      app_class (class): The app class to include in the search for wps engines.

    Returns:
      (owslib.wps.WebProcessingService): A owslib.wps.WebProcessingService object.
    """
    # If the app_class is given, check it first for a wps engine
    app_wps_services = None

    if app_class and issubclass(app_class, TethysAppBase):
        # Instantiate app class and retrieve wps services list
        app = app_class()
        #app_wps_services = app.wps_services()

    if app_wps_services:
        # Search for match
        for app_wps_service in app_wps_services:

            # If match is found, initiate engine object
            if app_wps_service.name == name:
                return None

    # If the wps engine cannot be found in the app_class, check settings for site-wide wps engines
    site_wps_services = WpsModel.objects.all()

    if site_wps_services:
        # Search for match
        for site_wps_service in site_wps_services:

            # If match is found initiate engine object
            if site_wps_service.name == name:
                # Create OWSLib WebProcessingService engine object
                wps = WebProcessingService(site_wps_service.endpoint,
                                           username=site_wps_service.username,
                                           password=site_wps_service.password,
                                           verbose=False,
                                           skip_caps=True)

                # Initialize the object with get capabilities call
                try:
                    wps.getcapabilities()
                except HTTPError as e:
                    if e.code == 404:
                        e.msg = 'The WPS service could not be found at given endpoint "{0}" for site WPS service ' \
                                'named "{1}". Check the configuration of the WPS service in your ' \
                                'settings.py.'.format(site_wps_service.endpoint, site_wps_service.name)
                        raise e
                    else:
                        raise e
                except:
                    raise

                return wps

    raise NameError('Could not find wps service with name "{0}". Please check that a wps service with that name '
                    'exists in the admin console or in your app.py.'.format(name))







