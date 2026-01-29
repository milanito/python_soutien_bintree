# Binary Trees Exercises

## Data Structures

We work with binary trees represented by the following class:

* An empty tree is represented by `None`
* A non-empty tree is a `BinTree` object with:

  * `B.key`   : value stored at the root
  * `B.left`  : left subtree (or `None`)
  * `B.right` : right subtree (or `None`)

For breadth-first traversal, you must use the `Queue` class:

* `Queue()` creates a new empty queue
* `q.enqueue(e)` adds element `e` to the queue
* `q.dequeue()` removes and returns the first element
* `q.isempty()` returns `True` if the queue is empty

---

## Exercise 1: Count nodes

Write a function `size(B)` that returns the number of nodes in the binary tree `B`.

Rules:

* `size(None) = 0`
* Use recursion

---

## Exercise 2: Height of a binary tree

Write a function `height(B)` that returns the height of the binary tree `B`.

Definition:

* An empty tree has height `-1`
* A leaf has height `0`

---

## Exercise 3: Level-order traversal (breadth-first)

Write a function `level_order(B)` that returns a list containing the keys of `B`
in breadth-first order.

Constraints:

* You must use the `Queue` class
* Do not use recursion

Example:

```
      10
     /  \
    5   15
```

Result:

```
[10, 5, 15]
```

---

## Exercise 4: First matching key (breadth-first)

Write a function `first_match_bfs(B, predicate)` that returns the first key
encountered in a breadth-first traversal such that:

```
predicate(key) == True
```

If no such key exists, return `None`.

Constraints:

* Breadth-first traversal only
* Use `Queue`

---

## Exercise 5: Maximum width of a tree

The width of a level is the number of nodes on that level.

Write a function `max_width(B)` that returns the maximum width of the tree.

Constraints:

* Breadth-first traversal
* Do not precompute all levels
* One traversal only

---

## Exercise 6: Almost complete binary tree

A binary tree is called *almost complete* if:

* All levels are completely filled except possibly the last
* Nodes in the last level are as far left as possible

Write a function `is_almost_complete(B)` that returns `True` or `False`.

Hint:

* During a breadth-first traversal, once a missing child is seen,
  all following nodes must be leaves.

Constraints:

* Breadth-first traversal only
* One pass
* No recursion

---

## Exercise 7: Lowest Common Ancestor

Write a function `lca(B, a, b)` that returns the key of the lowest common ancestor
of nodes with keys `a` and `b`.

Rules:

* The tree is not necessarily a binary search tree
* Keys are unique
* If one of the keys does not exist, return `None`

---

## Exercise 8: Diameter of a binary tree

The diameter of a binary tree is the length (number of edges) of the longest path
between two leaves.

Write a function `diameter(B)`.

Constraints:

* Time complexity must be O(n)
* Only one recursive traversal
* You may compute height and diameter together

---

## Exercise 9: Validate a Binary Search Tree

Write a function `is_bst(B)` that checks whether `B` is a valid Binary Search Tree.

Rules:

* All keys in the left subtree are strictly smaller than the root
* All keys in the right subtree are strictly greater than the root

Constraints:

* Do not convert the tree into a list
* Use min and max bounds propagated recursively

---

## Bonus Exercise: Serialize by levels

Write a function `serialize(B)` that returns a list representing the tree
level by level, using `None` for missing children.

Example:

```
        1
       / \
      2   3
           \
            4
```

Result:

```
[1, 2, 3, None, None, None, 4]
```

---

## Notes

* Unless explicitly stated, you may use recursion
* Pay attention to edge cases
* Clear and correct code is more important than short code
