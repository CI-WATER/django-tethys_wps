from tethys_datasets.engines import CkanDatasetEngine


ckan_engine = CkanDatasetEngine(api_endpoint="http://ciwweb.chpc.utah.edu/api/3/action",
                                apikey='003654e6-cd89-46a6-9035-28e4037b44d6')
# ckan_engine = CKANDatasetEngine(api_endpoint="http://tethys.byu.edu/api/3/action",
#                                 apikey='8cd924a8-48d3-452a-becf-d5ec19e9801b')


# ckan_engine.list_datasets(limit=5, offset=1, console=True)
# ckan_engine.list_datasets(with_resources=True, limit=1, offset=1, console=True)
# ckan_engine.get_dataset('new_dataset', console=True)
# ckan_engine.get_resource('08929eb9-fc3b-4af3-baeb-417e1135fcdc', console=True)
# ckan_engine.search_resources(query={'model': 'GSSHA', 'name': 'Test_2'}, console=True)
# ckan_engine.search_datasets(console=True, query={'name': 'azure-blob-test'})

# ckan_engine.create_dataset(name='newest-dataset',
#                            notes='This is the newest dataset.',
#                            title='Newest Dataset',
#                            author='Me',
#                            console=True)

# ckan_engine.update_dataset(dataset_id='newest-dataset',
#                            notes='This is a test.',
#                            version='3.0',
#                            author='Someone Else',
#                            console=True)

# ckan_engine.update_resource(resource_id='d4537829-5024-402a-a591-9c077f9eb844',
#                             file='/Users/swainn/testing/timeseries_maps/ParkCityBasic/write/post_gis/ele_png.kmz',
#                             format='kmz',
#                             new_field='new_value',
#                             console=True)

# ckan_engine.delete_dataset(dataset_id='newest-dataset',
#                            console=True)

# ckan_engine.delete_resource(resource_id='0032994e-bc2c-47bc-8d32-17d536e69d33',
#                             console=True)

ckan_engine.create_resource(dataset_id='new_dataset',
                            file='/Users/swainn/testing/test_models/ParkCityBasic.zip',
                            name='Park City Basic',
                            model='GSSHA',
                            format='zip',
                            console=True)

# ckan_engine.create_resource(dataset_id='new_dataset',
#                             file='/Users/swainn/testing/test_models/ParkCityBasic/luse.idx',
#                             format='txt',
#                             mimetype='application/octet-stream',
#                             console=True)


# ckan_engine.create_resource(dataset_id='new_dataset',
#                             url='http://ciwweb.chpc.utah.edu/dataset/6c354b2c-2618-4529-8797-27235f1f5bc3/resource/08929eb9-fc3b-4af3-baeb-417e1135fcdc/download/parkcity.kml',
#                             format='kml',
#                             console=True)