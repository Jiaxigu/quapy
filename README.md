# quaPy

Python interface for [qua-kit](https://github.com/achirkin/qua-kit) scenarios. 

The idea is to automatically parse GeoJSON files into efficient data types ready for data and architectural analysis.

## Requirement

- matplotlib
- shapely

## Install (sudo might be required)

    >>> python setup.py install
    
## Testing

	>>> python test.py -v

## Usage

### Init

Read your quakit scenario, normally a GeoJSON file, as follows:

	>>> with open('sample.geojson') as o:
	>>> 	file = json.load(o)

Then init a Scenario object in python:

	>>> s = Scenario(file)

### Scenario attributes

Access longitude / latitude of the center of the scenario (if given in the GeoJSON):

	>>> s.lonlat
	<<< [116.38571085000001, 39.8942916]
	
Access initial zoom level of the scenario:

	>>> s.map_zoom_level
	<<< 17

Access name of the scenario:

	>>> s.name
	<<< 'Yangmeizhu Byway'
	
Access buildings in the scenario:

	>>> for b in s.buidlings:
	>>> 	*do something with b*
	
### Building attributes
	
Access properties in a building:

	>>> b = s.buildings[0]
	>>> b.properties
	<<< {'building': 'yes', 'name': 'Quianmen Gate South', '@id': 'way/439956436', 'historic': 'memorial', 'building:levels': '5', 'name:zh': '正阳门箭楼'}

Access building geometry:

	>>> b.geometry
	
You can do whatever you want to the geometry as it's a shapely object. Refer to [the shapely user manual](http://toblerity.org/shapely/manual.html) for more.

### Tagging

Make a tagger dictionary:

	>>> user_tagger = {'Tiananmen Square':'Tourism', 'Quianmen Gate South': 'Public'}
	>>> type_tagger = {'Tiananmen Square':'Square', 'Quianmen Gate South': 'Gate'}
	>>> tagger_dict = {'type': type_tagger, 'user': user_tagger}

Tag by 'name' property:

	>>> s.tag('name', tagger_dict)

Show all type of tags:

	>>> s.tags
	<<< ['type', 'use']
	
Show building tags:
	
	>>> b.tags
	<<< {'use': 'Public', 'type': 'Gate'}