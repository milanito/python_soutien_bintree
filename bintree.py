# bintree.py

class BinTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        # Helpful for debugging
        return f"BinTree({self.key!r}, {self.left!r}, {self.right!r})"


def leaf(key):
    return BinTree(key, None, None)


def from_tuple(t):
    """
    Convert a nested tuple representation into BinTree.
    Expected format:
      None  -> empty tree
      (key, left, right) where left/right follow same format
    """
    if t is None:
        return None
    key, left, right = t
    return BinTree(key, from_tuple(left), from_tuple(right))
