from django.conf import settings
from tethys_apps.base.app_base import TethysAppBase
from .valid_engines import VALID_ENGINES


class DatasetService:
    """
    Used to define dataset services for apps.
    """

    def __init__(self, name, type, endpoint, apikey=None, username=None, password=None):
        """
        Constructor
        """
        self.name = name

        # Validate the types
        if type in VALID_ENGINES:
            self.type = type
            self.engine = VALID_ENGINES[type]
        else:
            if len(VALID_ENGINES) > 2:
                comma_separated_types = ', '.join('"{0}"'.format(t) for t in VALID_ENGINES.keys()[:-1])
                last_type = '"{0}"'.format(VALID_ENGINES.keys()[-1])
                valid_types_string = '{0}, and {1}'.format(comma_separated_types, last_type)
            elif len(VALID_ENGINES) == 2:
                valid_types_string = '"{0}" and "{1}"'.format(VALID_ENGINES.keys()[0], VALID_ENGINES.keys()[1])
            else:
                valid_types_string = '"{0}"'.format(VALID_ENGINES.keys()[0])

            raise ValueError('The value "{0}" is not a valid for argument "type" of DatasetService. Valid values for '
                             '"type" argument include {1}.'.format(type, valid_types_string))

        self.endpoint = endpoint
        self.apikey = apikey
        self.username = username
        self.password = password

    def __repr__(self):
        """
        String representation
        """
        return '<DatasetService: type={0}, api_endpoint={1}>'.format(self.type, self.endpoint)


def initialize_engine_object(engine, endpoint, apikey=None, username=None, password=None):
    """
    Initialize a DatasetEngine object from a string that points at the engine class.
    """
    # Derive import parts from engine string
    engine_split = engine.split('.')
    module_string = '.'.join(engine_split[:-1])
    engine_class_string = engine_split[-1]

    # Import
    module = __import__(module_string, fromlist=[engine_class_string])
    EngineClass = getattr(module, engine_class_string)

    # Create Engine Object
    engine_instance = EngineClass(endpoint=endpoint,
                                  apikey=apikey,
                                  username=username,
                                  password=password)
    return engine_instance


def get_dataset_engine(name, app_class=None):
    """
    Get a dataset engine with the given name.

    Args:
      name (string): Name of the dataset engine to retrieve.
      app_class (class): The app class to include in the search for dataset engines.

    Returns:
      (DatasetEngine): A dataset engine object.
    """
    # If the app_class is given, check it first for a dataset engine
    app_dataset_services = None

    if app_class and issubclass(app_class, TethysAppBase):
        # Instantiate app class and retrieve dataset services list
        app = app_class()
        app_dataset_services = app.dataset_services()

    if app_dataset_services:
        # Search for match
        for app_dataset_service in app_dataset_services:

            # If match is found, initiate engine object
            if app_dataset_service.name == name:
                return initialize_engine_object(engine=app_dataset_service.engine,
                                                endpoint=app_dataset_service.endpoint,
                                                apikey=app_dataset_service.apikey,
                                                username=app_dataset_service.username,
                                                password=app_dataset_service.password)

    # If the dataset engine cannot be found in the app_class, check settings for site-wide dataset engines
    site_dataset_services = None

    if hasattr(settings, 'TETHYS_DATASET_SERVICES'):
        site_dataset_services = settings.TETHYS_DATASET_SERVICES

    if site_dataset_services:
        # Search for match
        for site_dataset_service_name, site_dataset_service in site_dataset_services.iteritems():

            # If match is found initiate engine object
            if site_dataset_service_name == name:
                engine = site_dataset_service['ENGINE']
                endpoint = site_dataset_service['ENDPOINT']
                apikey = site_dataset_service['APIKEY'] if 'APIKEY' in site_dataset_service else None
                username = site_dataset_service['USERNAME'] if 'USERNAME' in site_dataset_service else None
                password = site_dataset_service['PASSWORD'] if 'PASSWORD' in site_dataset_service else None

                return initialize_engine_object(engine=engine,
                                                endpoint=endpoint,
                                                apikey=apikey,
                                                username=username,
                                                password=password)

    raise NameError('Could not find dataset service with name "{0}". Please check that dataset service with that name '
                    'exists in settings.py or in your app.py.'.format(name))







