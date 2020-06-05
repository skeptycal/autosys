# from typing import Any, Dict, List, Optional, Sequence, Set, Tuple


class PrettyDict(dict):
    @property
    def _my_class(self):
        return myclass(self)

    def table_list(self, table_rows: List[str], border_char: str = "-") -> str:
        """ Returns a table version of a list.

            - table_rows  = list of rows
            - border_char = string used for border

            e.g.
                print(table_list(my_rows, border_char = "˚`†´"))
            """
        result: List[str] = []
        longest_string: int = len(max(table_rows, key=len))
        border: str = border_char * (longest_string // len(border_char))
        result.append(border)
        result.append(f"{my_class(self)} data for '{self.name}':")
        result.append(border)
        result.extend(table_rows)
        result.append(border)
        return NL.join(result)

    def table_dict(
        self, table_rows: Dict[Any, Any], border_char: str = "-"
    ) -> str:
        """ Returns a table version of a dictionary.

            - table_rows  = dictionary of rows
            - border_char = string used for border

            e.g.
                print(table_dict(my_dict, border_char = "˚`†´", divider = True))
            """
        return self.table_list(
            [f"{k:<15.15}: {v:<35.35}" for k, v in table_rows.items()],
            border_char=border_char,
        )

    def to_dict(self, include_dunders: bool = False) -> Dict[str, str]:
        """ Returns a formatted dictionary view . """
        if include_dunders:
            return {k: v for k, v in self.items()}
        return {k: v for k, v in self.items() if not k.startswith("_")}

    def thats_all(self, border_char="-") -> str:
        return {k: v for k, v in vars(self).items()}

    def pretty_dict(self, border_char="-") -> str:
        """ Returns a pretty version of dictionary.

            - border_char = string used for border

            e.g.
                print(self.pretty(border_char = "˚`†´"))
        """
        return self.table_list(
            [f"{k:<20.20}: {v}" for k, v in self.to_dict().items()],
            border_char=border_char,
        )

    def to_json(self, sort_keys=True, indent=2):
        return json.dumps(
            version.to_dict(), indent=indent, sort_keys=sort_keys
        )
