
from pathlib import Path
from typing import List
from traceback import format_tb
from dev.debug import dbprint


_debug_: bool = True  # dev mode


class FrozenError(ValueError):
    pass


class Leaf:
    """ #### qData container for Tree Structures.

        Data can be any valid object. Name and filename are optional strings.

        If <frozen> = True, no changes can be made to the data after
        instantiation. If <quiet> = True, FrozenErrors are ignored
        and the program continues.
        """

    def __init__(self, data: object, name: str = '', filename: str = '', quiet: bool = True, frozen: bool = False):
        self._data = data
        self._filename:          str = filename
        self._name:              str = name

        # freeze private values if frozen = True
        self._quiet:             bool = quiet
        self._frozen:            bool = frozen

        # super().__init__()

    def __str__(self):
        return str(self._data)

    def summary(self):
        print(f"data: {self}\n  (name:{self.name:<1.10}, file: {bool(self.filename)}, quiet: {self.quiet}, frozen: {self.frozen})")

    def _frozen_error(self):
        raise FrozenError("Changes are not allowed. The data for this leaf is frozen!")
# !----------------------------- Leaf properties

    @property
    def name(self) -> str:
        return self._name

    @property
    def quiet(self) -> bool:
        return self._quiet

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def data(self):
        return self._data

    @property
    def frozen(self) -> bool:
        return self._frozen

    @name.setter
    def name(self, name: str) -> (None, Exception):
        if self.frozen:
            if not self.quiet:
                raise FrozenError
        else:
            if isinstance(name, str):
                self._name = name
            else:
                return TypeError("The type for <name> must be <str>.")

    @filename.setter
    def filename(self, filename: str) -> (None, Exception):
        if self.frozen:
            if not self.quiet:
                raise FrozenError
        else:
            if Path(filename).exists():
                dbprint(f"filename ({filename}) on leaf {self} exists.")
            else:
                try:
                    Path(filename).touch()
                except IOError as e:
                    dbprint(e)
                    return e
            self._filename = filename
            dbprint(f"filename on leaf {self} set to {self.get_name()}")
            return None

    @data.setter
    def data(self, data):
        # TODO --> perhaps add some data validation ...
        if self.frozen:
            if not self.quiet:
                raise FrozenError
        else:
            self._data = data

    @frozen.setter
    def frozen(self, frozen: bool = False):
        if self.frozen:
            if not self.quiet:
                raise FrozenError
        else:
            self._frozen = frozen

    @quiet.setter
    def quiet(self, quiet: bool = True):
        if self.frozen:
            if not quiet:
                raise FrozenError
        else:
            self._quiet = quiet


l = Leaf('test', name='testname', filename='eof', quiet=True, frozen=False)
if _debug_:
    l.summary()
    l.data = 'stuff'
    print("-- changed 'data' to 'stuff'")
    l.summary()
    l.frozen = True
    print("-- changed 'frozen' to 'True'")
    l.summary()
    l.data = 'this'
    print("-- changed 'data' to 'this' (no effect?)")
    l.summary()

"""
    class Tree:
        def __init__(self, data=None, left=None, right=None):
            self.top = Leaf(data=data, name=name, file=file)
            self.children: List[Leaf] = []

        def __str__(self):
            return str(self.data)

        def append(self, Node):
            pass


    root = Tree()
    root.data = "root"
    root.left = Tree()
    root.left.data = "left"
    root.right = Tree()
    root.right.data = "right"

    print(root.left.data)


    root = Tree()
    root.data = "root"
    root.left = Tree()
    root.left.data = "left"
    root.right = Tree()
    root.right.data = "right"

    root.left.left = Tree()
    root.left.left.data = "left 2"
    root.left.right = Tree()
    root.left.right.data = "left-right"

    print(root.data)
    print(root.left.left.data)

    # Reference: https://pythonspot.com/python-tree/


    # no longer binary ...
    class Tree(object):
        def __init__(self):
            self.left = None
            self.child = []
            self.data = []

        def createChildren(self, amount):
            for i in range(0, amount):
                self.child.append(Tree())

        def setChildrenValues(self, list):
            for i in range(0, len(list)):
                self.data.append(list[i])


    root = Tree()
    root.createChildren(3)
    root.setChildrenValues([5, 6, 7])
    root.child[0].createChildren(2)
    root.child[0].setChildrenValues([1, 2])
    # print some values in the tree
    print(root.data[0])
    print(root.child[0].data[0])
    """
