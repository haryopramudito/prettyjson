import types
import json
from prettyjson import prettyjson


def test():
    txt = """{
            "grid": {"port": "COM5"},
            "policy": {
                "movingaverage": 5,
                "hysteresis": 5,
                "fan1": {
                    "name": "fan1", "signal": "cpu", "mode": "auto", "speed": 100,
                    "curve": [[0, 75], [65, 75], [75, 100]]
                },
                "fan2": {
                    "name": "fan2", "signal": "gpu", "mode": "auto", "speed": 100,
                    "curve": [[0, 75], [65, 75], [75, 100]]
                }
            },
            "signals": {
                "cpu": {
                    "fn": "max",
                    "sensors": [
                        "/intelcpu/0, CPU Core #1",
                        "/intelcpu/0, CPU Core #2",
                        "/intelcpu/0, CPU Core #3",
                        "/intelcpu/0, CPU Core #4"
                    ]
                },
                "gpu": {
                    "fn": "max", "sensors": ["/nvidiagpu/0"]
                },
                "sys": {
                    "fn": "max",
                    "sensors": ["/intelcpu/0", "/nvidiagpu/0"]
                }
            },
            "app": {
                "startwithwindows": true, "startminimized": false, "closetotray": true
            }
        }"""
    obj = json.loads(txt)
    txt = prettyjson(obj, indent=2, maxlinelength=70)
    print ("demo = " + txt)
    print()
    print()


    txt = """{
    }"""
    obj = json.loads(txt)
    txt = prettyjson(obj, maxlinelength=80)
    print ("empty = " + txt)
    print()
    print()

    txt = """{
        "empty_1d": [],
        "empty_2d": [[],[]],
        "empty_dict_1d": {},
        "empty_dict_2d": {"a":{},"b":{}},
        "halfempty_2d": [[223, "hello"], []],
        "string_value": "this is a string",
        "int_value": 5,
        "float_value": 223.45e3,
        "float_array_1d": [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532],
        "floats_2d_1": [
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14],
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14],
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14]
        ],
        "floats_2d_2": [
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532],
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532],
            [0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532, 0.5543, 2.33576, 0.32333455, 1.2345663, -123.445677, 5.2234e14, 84492033, -1229340.2234, 12234.5532]
        ],
        "floats_dict_1d": { "val1":  0.5543, "val2": 2.33576, "val3":  0.32333455, "val4": 1.2345663, "val5": -123.445677, "val6": 5.2234e14 },
        "floats_dict_2d": {
            "params1": { "val1": 0.5543, "val2": 2.33576, "val3":  0.32333455, "val4": 1.2345663, "val5": -123.445677, "val6": 5.2234e14 },
            "params2": { "val1": 0.5543, "val2": 2.33576, "val3":  0.32333455, "val4": 1.2345663, "val5": -123.445677, "val6": 5.2234e14 },
            "params3": { "val1": 0.5543, "val2": 2.33576, "val3":  0.32333455, "val4": 1.2345663, "val5": -123.445677, "val6": 5.2234e14 }
        },
        "strings_1d_1": [
            "Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet",
            "Lorem ipsum dolor sit amet"
        ],
        "strings_1d_2": [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
        ],
        "strings_1d_3": [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ],
        "strings_1d_4": [
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        ]
    }"""
    obj = json.loads(txt)
    txt = prettyjson(obj, maxlinelength=80)
    print ("test = " + txt)



if __name__ == "__main__":
    test()
