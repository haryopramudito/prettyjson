
### JSON formatter for Python

From this [StackOverflow answer](https://stackoverflow.com/a/56497521/104668).

`prettyjson()` is a Python function that allows to pretty-print JSON content with line splits and indentations.

Usage:

`txt = prettyjson(obj, indent=2, maxlinelength=80)`

* `obj` - any object containing lists, dicts, tuples and basic types.
* `indent` - number of characters to indent the next level with.
* `maxlinelength` - maximum number of characters per line.


Example of rendered JSON:

    {
      "grid": {"port": "COM5"},
      "policy": {
        "movingaverage": 5,
        "hysteresis": 5,
        "fan1": {
          "name": "fan1",
          "signal": "cpu",
          "mode": "auto",
          "speed": 100,
          "curve": [[0, 75], [65, 75], [75, 100]]
        },
        "fan2": {
          "name": "fan2",
          "signal": "gpu",
          "mode": "auto",
          "speed": 100,
          "curve": [[0, 75], [65, 75], [75, 100]]
        }
      },
      "signals": {
        "cpu": {
          "fn": "max",
          "sensors": [
            "/intelcpu/0, CPU Core #1", "/intelcpu/0, CPU Core #2",
            "/intelcpu/0, CPU Core #3", "/intelcpu/0, CPU Core #4"
          ]
        },
        "gpu": {"fn": "max", "sensors": ["/nvidiagpu/0"]},
        "sys": {"fn": "max", "sensors": ["/intelcpu/0", "/nvidiagpu/0"]}
      },
      "app": {
        "startwithwindows": true, "startminimized": false, "closetotray": true
      }
    }

Various data setups are conveniently rendered:

    {
      "empty_1d": [],
      "empty_2d": [[], []],
      "empty_dict_1d": {},
      "empty_dict_2d": {"a": {}, "b": {}},
      "halfempty_2d": [[223, "hello"], []],
      "string_value": "this is a string",
      "int_value": 5,
      "float_value": 223450.0,
      "float_array_1d": [
        0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0,
        84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663,
        -123.445677, 522340000000000.0, 84492033, -1229340.2234, 12234.5532, 0.5543,
        2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0, 84492033,
        -1229340.2234, 12234.5532
      ],
      "floats_2d_1": [
        [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0],
        [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0],
        [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0]
      ],
      "floats_2d_2": [
        [
          0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0,
          84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663,
          -123.445677, 522340000000000.0, 84492033, -1229340.2234, 12234.5532, 0.5543,
          2.33576, 0.32333455, 1.2345663, -123.445677, 522340000000000.0, 84492033,
          -1229340.2234, 12234.5532
        ]
      ]
    }


##### Enjoy!
