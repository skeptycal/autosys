# This is the toml example file from <xxx> translated into python

# require("../src/toml.php")
import toml

from typing import Dict

arr: Dict = {
    'a': 1,
    'b': (1, 2, 3),
    'c': {'a': 'apple', 'b': (4, 5, 6)},
    'd': True,
}

# $arr = array(
#     'a'= > 1,
#     'b'= > array (1, 2, 3),
#     'c'= > array ('a' = > 'apple', 'b' = > array(4, 5, 6)),
#     'd'= > true
# )

encoder = toml.dumps
# $encoder = new Toml_Encoder()
print(encoder(arr))
# echo $encoder -> encode($arr)
