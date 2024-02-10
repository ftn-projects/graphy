# Graphy

Graphy is a modular application developed using Django and D3.js designed for visualizing directed, undirected, and cyclic graphs. Its flexibility and modular architecture make it a comprehensive tool for a broad range of graph visualization needs. Graphy supports various data sources including JSON, XML, and RDF (Turtle format), catering to developers and researchers looking to analyze and visualize complex graph data.

## Application Architecture

Graphy is built on a plugin-based architecture, enabling high customizability and extensibility. The architecture is designed to support a variety of functionalities through its plugins, which include visualizers, data source readers, and platform management components. The main components are as follows:

### Plugins

#### Visualizers

- **BlockVisualizer**: Displays graphs in the form of blocks, presenting all related information. This plugin is ideal for smaller graphs but not recommended for very large graphs due to the potential complexity and information density.
- **SimpleVisualizer**: Displays graphs with nodes showing minimal information, suitable for a quick overview of larger graphs without overwhelming detail.

#### Data Source Readers

- **JsonDataSource**: Reads JSON formatted graphs, supporting cyclic edges with a special annotation (`@`) to denote cyclic relationships.
- **XmlDataSource**: Reads XML files with support for cyclic edges, using relative paths (references) to denote cycles within the graph structure.
- **RdfDataSource**: Reads RDF files, facilitating the visualization of semantic web data and other complex relationships encoded in RDF format.

#### API and Platform

- The API component includes models (Graph, Edge, Node), abstract services, and utility classes that provide the backbone for Graphy's functionality. These models represent the structure of graphs, their components, and the relationships between them.
- The Platform component is responsible for creating workspaces and managing currently used graphs. It offers features for searching and filtering graphs, allowing users to efficiently work with and visualize a large number of graph datasets.

## Supported Data Sources

Graphy supports the following data sources, enabling the visualization of a wide array of graph data:

- **JSON**: A lightweight format that is easy for humans to read and write, as well as for machines to parse and generate.
- **XML**: A markup language for encoding documents in both human-readable and machine-readable formats.
- **RDF (Turtle)**: A format for expressing data within the Resource Description Framework (RDF), suitable for representing personal data, social networks, digital artifacts metadata, and as part of the Semantic Web standards.

## Getting Started

To begin using Graphy, ensure you have Django installed in your development environment. The following steps will guide you through the setup process to get Graphy up and running:

1. **Clone the Graphy repository**:
   Start by cloning the Graphy repository from GitHub to your local machine. Open a terminal and run the following command:

This command clones the Graphy repository into a directory named `graphy` in your current working directory.

2. **Navigate to the Graphy directory**:
Change into the Graphy directory that was just cloned:

3. **Install Graphy plugins**:
Graphy's functionality is extended through its plugins. To install all necessary plugins, you can use the Python package installer `pip`. Since the plugins are developed as editable installations (meaning any changes to the plugin source code will immediately affect the Graphy installation without needing a reinstall), use the `-e` option with `pip`. For example, to install a plugin named `API`, you would use the following command:

Repeat this step for each plugin you need to install, including `JsonDataSource`, `XmlDataSource`, `RdfDataSource`, and any visualizer plugins like `BlockVisualizer` or `SimpleVisualizer`. Please replace `path/to/API` with the actual path to the plugin directory within the Graphy project.

Note: The above command is a generic example. You will need to replace `path/to/API` with the actual paths to the directories of the plugins you wish to install. These paths will be relative to the root of the Graphy project directory.

You can now access the Graphy application by visiting `http://127.0.0.1:8000/` in your web browser.

By following these steps, you should have a fully functional Graphy setup ready for graph visualization tasks.

## Authors

Graphy is developed and maintained by a team of dedicated contributors:

- Dimitrije Gašić, SV31/2021
- Gojko Vučković, SV49/2021
- Maša Ivanov, SV54/2021
- Milan Arežina, SV55/2021
- Milica Mišić, SV62/2021

Their combined efforts and expertise have contributed to making Graphy a versatile and powerful tool for graph visualization.
