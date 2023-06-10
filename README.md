# Graph Parser and Visualizator

Welcome to the Graph Parser and Visualizator! This application, developed with Django's component-driven approach, offers a comprehensive set of features to parse and visualize graphs effortlessly. Our app comprises several independent components, each serving a unique purpose: the Core, XML parser, JSON parser, D3 Simple Visualizator, and D3 Complex Visualizator. By harnessing the app's robust parsing and visualization capabilities, you can effortlessly transform intricate data into insightful visual representations.

## Components

### Core
At the heart of the Graph Parser and Visualizator App lies the Core component, integrating all other components to ensure a cohesive user experience. With an array of robust functionalities, the Core component empowers users to efficiently search, filter, and manipulate data within the app.

One notable feature of the Core component is its tree-view, resembling a familiar file system structure. This intuitive navigation system enables users to effortlessly explore their data, facilitating a seamless understanding of its organization. Complementing this, the Core component offers both a bird's-eye view and a main canvas, providing multiple perspectives on the data. These visual aids facilitate the identification of patterns and trends, enabling users to extract valuable insights.

In summary, the Core component is an indispensable element of the app, playing a vital role in managing and visualizing complex data. With its comprehensive toolset, users can harness the power of the Graph Parser and Visualizator to effortlessly handle intricate data with ease and precision.

### XML Parser

The XML Parser component within the Graph Parser and Visualizator is a tool designed to parse and visualize XML data effectively. Powered by advanced parsing capabilities, this component effortlessly handles diverse XML data sets and represents them in a graph format.

A standout feature of the XML Parser is its exceptional support for cyclic graphs. This feature proves invaluable when working with intricate data structures that may contain circular references.

Use the XML Parser's capabilities to navigate, analyze, and gain valuable insights from your XML data with ease. This component serves as an essential asset within the Graph Parser and Visualizator, enabling you to visualize and make sense of complex XML datasets.

### JSON Parser

The JSON Parser component of the Graph Parser and Visualizator is another powerful tool designed to parse and visualize JSON data effortlessly. It handles JSON data of any complexity and presents it in a graph format.

Similar to the XML Parser, the JSON Parser also supports cyclic graphs, allowing you to handle complex data structures that may include circular references. This feature provides flexibility and convenience when working with intricate datasets.

### Simple Visualizator

The D3 Simple Visualizator plugin offers a straightforward approach to visualize your data. Powered by the d3.js library, it represents nodes as circles with unique ID numbers, while the connections between nodes are depicted as lines.

This plugin's standout feature is its implementation of a force layout algorithm. By simulating physical forces between nodes, it creates an engaging and user-friendly visualization that effortlessly highlights clusters, trends, and patterns within the data.

With its simplicity and intuitive design, the D3 Simple Visualizer plugin is a perfect choice for users seeking a quick and hassle-free data visualization solution. It provides a high-level overview of the data without overwhelming you with excessive details.

### Complex Visualizator

The D3 Complex Visualizator plugin is a powerful data visualization tool integrated into the Graph Parser and Visualizator. Leveraging the d3.js library, it presents each graph node as a rectangular shape, featuring a title that includes the node's name and ID, along with content displaying the node's attributes as key-value pairs.

To illustrate connections between nodes, the Complex Visualizator plugin employs lines that link the rectangles. Similar to the D3 Simple Visualizer plugin, it incorporates a force layout algorithm, ensuring an intuitive and visually captivating representation of the data.

While both plugins offer visualization capabilities, the Complex Visualizator plugin is particularly suitable for users who desire comprehensive insights into each node within the graph. This functionality proves invaluable when working with intricate datasets containing numerous attributes, enabling the identification of specific patterns and relationships within the data.

Moreover, this plugin serves as a versatile tool for search and filtering tasks. Its rectangular node representation and clear display of key-value pairs make it effortless to search for specific nodes based on their attributes, facilitating efficient data exploration.

## Installation
1. Create your virtual environment
```
virtualenv <environment_name>
```
2. Activate virtual environment
```
environment_name/Scripts/Activate
```
3. Install Django
```
pip install django
```
### Install the App and Run the Server

Windows:
```
run.cmd
```
Linux:
```
run.sh
```
### Open
You can find the app at http://127.0.0.1:8000/

## Authors
- [Miloš Čuturić](https://github.com/cuturic01)
- [Luka Đorđević](https://github.com/lukaDjordjevic01)
- [Marko Janošević](https://github.com/janosevicsm)

## Academic Context
Graph Parser and Visualizator was developed for the purposes of the course [Software Patterns and Components](http://www.ftn.uns.ac.rs/n446798796/softverski-obrasci-i-komponente).
### Course Assistants
- [Vladimir Inđić](https://gitlab.com/vlada_indjic)
- [Ivan Mršulja](https://gitlab.com/ivanmrsulja)
### Course Professor
- [Igor Dejanović](https://gitlab.com/igordejanovic)
