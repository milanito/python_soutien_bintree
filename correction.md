# Binary Trees Corrections (correction.md)

This document provides reference solutions for the exercises in **Binary Trees Exercises**.

## Conventions

* Empty tree: `None`
* Non-empty tree: instance of `BinTree` with fields `key`, `left`, `right`
* BFS must use the provided `Queue` class (`enqueue`, `dequeue`, `isempty`)

---

## Exercise 1: Count nodes

```python
def size(B):
    if B is None:
        return 0
    return 1 + size(B.left) + size(B.right)
```

---

## Exercise 2: Height of a binary tree

Definition used:

* `height(None) == -1`
* leaf height is `0`

```python
def height(B):
    if B is None:
        return -1
    hl = height(B.left)
    hr = height(B.right)
    if hl > hr:
        return hl + 1
    return hr + 1
```

---

## Exercise 3: Level-order traversal (breadth-first)

```python
from queue import Queue

def level_order(B):
    if B is None:
        return []

    q = Queue()
    q.enqueue(B)

    res = []

    while not q.isempty():
        node = q.dequeue()
        res.append(node.key)

        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

    return res
```

---

## Exercise 4: First matching key (breadth-first)

```python
from queue import Queue

def first_match_bfs(B, predicate):
    if B is None:
        return None

    q = Queue()
    q.enqueue(B)

    while not q.isempty():
        node = q.dequeue()

        if predicate(node.key):
            return node.key

        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)

    return None
```

---

## Exercise 5: Maximum width of a tree

Approach: BFS by levels. At each level, we process exactly `level_count` nodes (the current queue length), and count children enqueued for the next level.

This solution uses `len(q)` (your provided `Queue` supports `__len__`).

```python
from queue import Queue

def max_width(B):
    if B is None:
        return 0

    q = Queue()
    q.enqueue(B)

    best = 0

    while not q.isempty():
        level_count = len(q)
        if level_count > best:
            best = level_count

        i = 0
        while i < level_count:
            node = q.dequeue()

            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

            i = i + 1

    return best
```

---

## Exercise 6: Almost complete binary tree

Rule: during BFS, once we encounter a `None` child position, all later nodes must have **no children**.

Implementation idea:

* BFS nodes
* Maintain a boolean `seen_gap`
* For each node, check left then right
* If a missing child is seen, set `seen_gap = True`
* If `seen_gap` is True and we later see any non-empty child, return False

```python
from queue import Queue

def is_almost_complete(B):
    if B is None:
        return True

    q = Queue()
    q.enqueue(B)

    seen_gap = False

    while not q.isempty():
        node = q.dequeue()

        # left child
        if node.left is None:
            seen_gap = True
        else:
            if seen_gap:
                return False
            q.enqueue(node.left)

        # right child
        if node.right is None:
            seen_gap = True
        else:
            if seen_gap:
                return False
            q.enqueue(node.right)

    return True
```

---

## Exercise 7: Lowest Common Ancestor (general binary tree)

Assumptions:

* Keys are unique
* Return `None` if either `a` or `b` is missing

Strategy:

1. First, verify both keys exist.
2. Then compute LCA with recursion:

   * If current node matches `a` or `b`, return that node
   * Recurse left and right
   * If both sides return non-None, current node is LCA

```python
def contains(B, x):
    if B is None:
        return False
    if B.key == x:
        return True
    return contains(B.left, x) or contains(B.right, x)


def _lca_node(B, a, b):
    if B is None:
        return None

    if B.key == a or B.key == b:
        return B

    left = _lca_node(B.left, a, b)
    right = _lca_node(B.right, a, b)

    if left is not None and right is not None:
        return B
    if left is not None:
        return left
    return right


def lca(B, a, b):
    if B is None:
        return None

    if not contains(B, a):
        return None
    if not contains(B, b):
        return None

    node = _lca_node(B, a, b)
    if node is None:
        return None
    return node.key
```

---

## Exercise 8: Diameter of a binary tree (O(n))

We compute in one traversal:

* height of subtree
* best diameter inside subtree

Return value of helper: `(height, diameter)`

Conventions:

* height of empty tree = `-1`
* diameter is measured in **edges**

For a node:

* candidate path through node = `left_height + right_height + 2`

```python
def _height_diameter(B):
    if B is None:
        return (-1, 0)

    hl, dl = _height_diameter(B.left)
    hr, dr = _height_diameter(B.right)

    # height
    if hl > hr:
        h = hl + 1
    else:
        h = hr + 1

    # diameter passing through this node
    through = hl + hr + 2

    # best diameter
    d = dl
    if dr > d:
        d = dr
    if through > d:
        d = through

    return (h, d)


def diameter(B):
    return _height_diameter(B)[1]
```

---

## Exercise 9: Validate a Binary Search Tree

Rule:

* left subtree keys strictly smaller
* right subtree keys strictly greater

We propagate bounds:

* `low < key < high`

`low` or `high` can be `None` (no bound).

```python
def _is_bst(B, low, high):
    if B is None:
        return True

    k = B.key

    if low is not None and k <= low:
        return False
    if high is not None and k >= high:
        return False

    if not _is_bst(B.left, low, k):
        return False
    if not _is_bst(B.right, k, high):
        return False

    return True


def is_bst(B):
    return _is_bst(B, None, None)
```

---

## Bonus: Serialize by levels (with None placeholders)

Goal:

* BFS
* Append `None` for missing children
* Trim trailing `None` values at the end for a cleaner result

```python
from queue import Queue

def serialize(B):
    if B is None:
        return []

    q = Queue()
    q.enqueue(B)

    out = []

    while not q.isempty():
        node = q.dequeue()

        if node is None:
            out.append(None)
        else:
            out.append(node.key)
            q.enqueue(node.left)
            q.enqueue(node.right)

    # remove trailing None values
    while out != [] and out[-1] is None:
        out.pop()

    return out
```
