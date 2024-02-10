from graphy_json_data_source import JsonDataSourceService
from graphy_api.services.reader import FileSourceReader
from graphy_api.services import UtilService


plugin = JsonDataSourceService()
plugin.reader = FileSourceReader('aaa.json')
plugin.util = UtilService()


g = plugin.load()

print(g)
