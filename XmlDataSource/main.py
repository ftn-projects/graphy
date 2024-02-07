from XmlDataSource.src.graphy_xml_data_source.xml_data_source_service import XmlDataSourceService
from graphy_api.services.reader.file_source_reader import FileSourceReader

service = XmlDataSourceService()
service.reader = FileSourceReader("C:\\Projekti\\sok\\graphy\\XmlDataSource\\books.xml")
graph = service.load()
print(graph)