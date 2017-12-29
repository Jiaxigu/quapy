#-*- encoding: UTF-8 -*-
import unittest
import json
import gc
from quapy import *

class QuapyTestCases(unittest.TestCase):

    def setUp(self):
        """
        set up geojson and tagger samples.
        """
        self.geojson = \
        """
        { "name": "Scenario with zoom level 15"
        , "properties":
          { "mapZoomLevel": 18
          , "defaultStaticColor": "#005533FF"
          , "defaultLineColor": "#005599FF"
          , "defaultBlockColor": "#999933FF"
          , "defaultActiveColor": "#BB5555FF"
          , "useMapLayer": true
          , "forcedArea": [ ]
          }
        , "geometry":
        {
          "type": "FeatureCollection",
          "generator": "overpass-ide",
          "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
          "timestamp": "2017-08-07T10:01:02Z",
          "features": [
            {
              "type": "Feature",
              "properties": {
                "@id": "way/439956436",
                "building": "yes",
                "building:levels": "5",
                "historic": "memorial",
                "name": "Quianmen Gate South",
                "name:zh": "正阳门箭楼"
              },
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      116.3913051,
                      39.8981208
                    ],
                    [
                      116.3913029,
                      39.8978065
                    ],
                    [
                      116.3920215,
                      39.8978175
                    ],
                    [
                      116.392014,
                      39.8981328
                    ],
                    [
                      116.3917608,
                      39.8981312
                    ],
                    [
                      116.3917545,
                      39.8981791
                    ],
                    [
                      116.3915829,
                      39.898177
                    ],
                    [
                      116.3915816,
                      39.8981241
                    ],
                    [
                      116.3913051,
                      39.8981208
                    ]
                  ]
                ]
              },
              "id": "way/439956436"
            },
            {
              "type": "Feature",
              "properties": {
                "@id": "way/468844172",
                "building": "yes"
              },
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                    [
                      116.3877429,
                      39.8957253
                    ],
                    [
                      116.3877456,
                      39.8956615
                    ],
                    [
                      116.3878877,
                      39.89568
                    ],
                    [
                      116.3878636,
                      39.89575
                    ],
                    [
                      116.3877429,
                      39.8957253
                    ]
                  ]
                ]
              },
              "id": "way/468844172"
            }
          ]
        }
        }
        """
        profit_tagger = {'Quianmen Gate South':'Gate', 'Tiananmen Square':'Square'}
        usage_tagger = {'Quianmen Gate South':'Public', 'Tiananmen Square':'Tourism'}
        self.tagger_dict= {'profit': profit_tagger, 'usage':usage_tagger}
        self.f = json.loads(self.geojson)
        self.s = Scenario(self.f)
    
    def tearDown(self):
        del(self.f)
        gc.collect()
        
    def test_scenario_type(self):
        self.assertIsInstance(self.s, quapy.Scenario)
        
    def test_building_number(self):
        self.assertEqual(len(self.s.buildings), 2)
    
    def test_building_type(self):
        self.assertIsInstance(self.s.buildings[0], quapy.Building)
        
    def test_tagger(self):
        self.s.tag('name', self.tagger_dict)
        self.assertEqual(set(self.s.tags), {'usage', 'profit'})
        
    def test_tagger_effectivity(self):
        self.s.tag('name', self.tagger_dict)
        self.assertEqual(self.s.buildings[0].tags['profit'], 'Gate')
        self.assertEqual(self.s.buildings[0].tags['usage'], 'Public')
        
def suite_loader():
    test_cases = (QuapyTestCases,)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite_loader')
    