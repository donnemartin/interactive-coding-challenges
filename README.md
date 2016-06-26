<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/cover_challenge.gif">
</p>

interactive-coding-challenges
============

**Continually updated, interactive and test-driven coding challenges**.

Challenges focus on **algorithms** and **data structures** that are typically found in **coding interviews**.

Each challenge has one or more reference solutions that are:
* Fully functional
* Unit tested
* Easy-to-understand

Challenges will soon provide on-demand [incremental hints](https://github.com/donnemartin/interactive-coding-challenges/issues/22) to help you arrive at the optimal solution.

Notebooks also detail:
* Constraints
* Test cases
* Algorithms
* Big-O time and space complexities

## Challenge Solutions

<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/cover_solution.gif">
</p>
<br/>

## Notebook Structure

Each challenge has two notebooks, a **challenge notebook** for you to solve and a **solution notebook** for reference.

### Problem Statement

* States the problem to solve.

### Constraints

* Describes any constraints or assumptions.

### Test Cases

* Describes the general and edge test cases that will be evaluated in the unit test.

### Algorithm

* [Challenge Notebook] Empty, refer to the solution notebook algorithm section if you need a hint.
* [Solution Notebook] One or more algorithm solution discussions, with Big-O time and space complexities.

### Hints

* [Challenge Notebook] Provides on-demand [incremental hints](https://github.com/donnemartin/interactive-coding-challenges/issues/22) to help you arrive at the optimal solution.  Coming soon!

### Code (Challenge: Implement Me!)

* [Challenge Notebook] Skeleton code for you to implement.
* [Solution Notebook] One or more reference solutions.

### Unit Test

* [Challenge Notebook] Unit test for your code.  Expected to fail until you solve the challenge.
* [Solution Notebook] Unit test for the reference solution(s).

## Future Development

Challenges, solutions, and unit tests are presented in the form of **IPython/Jupyter Notebooks**.

* Notebooks currently contain mostly Python solutions (tested on both Python 2.7 and Python 3.4), but can be extended to include [44 supported languages](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages)
* Repo will be **continually updated** with new solutions and challenges
* [Contributions](#contributing) are welcome!

## Index

### Challenges Categories

* [Arrays and Strings](#arrays-and-strings)
* [Linked Lists](#linked-lists)
* [Stacks and Queues](#stacks-and-queues)
* [Graphs and Trees](#graphs-and-trees)
* [Sorting](#sorting)
* [Recursion and Dynamic Programming](#recursion-and-dynamic-programming)
* [Bit Manipulation](#bit-manipulation)
* [Scalability and Memory Limits](#scalability-and-memory-limits)
* [Concurrency](#concurrency)
* [Online Judges](#online-judges)

### Installing and Running Challenges

* [Repo Structure](#repo-structure)
* [Notebook Installation](#notebook-installation)
    * [Nose Installation](#nose-installation)
* [Running Challenges](#running-challenges)

### Misc

* [Contributing](#contributing)
* [Credits](#credits)
* [Contact Info](#contact-info)
* [License](#license)

## Challenges

[Image Credits](#credits)

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/arrays_nltk.png">
</p>
<br/>

### Arrays and Strings

| Challenge | Static Notebook |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Determine if a string contains unique characters | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/unique_chars/unique_chars_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/unique_chars/unique_chars_solution.ipynb) |
| Determine if a string is a permutation of another | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/permutation/permutation_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/permutation/permutation_solution.ipynb) |
| Determine if a string is a rotation of another | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/rotation/rotation_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/rotation/rotation_solution.ipynb) |
| Compress a string | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress/compress_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress/compress_solution.ipynb) |
| Reverse characters in a string | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/reverse_string/reverse_string_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/reverse_string/reverse_string_solution.ipynb) |
| Implement a hash table | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/hash_map/hash_map_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/hash_map/hash_map_solution.ipynb) |
| Find the first non-repeated character in a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Remove specified characters in a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Reverse words in a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Convert a string to an integer | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Convert an integer to a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/linked_lists_wikipedia.png">
</p>
<br/>

### Linked Lists

| Challenge | Static Notebook |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Remove duplicates from a linked list | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/remove_duplicates/remove_duplicates_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/remove_duplicates/remove_duplicates_solution.ipynb) |
| Find the kth to last element of a linked list | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/kth_to_last_elem/kth_to_last_elem_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/kth_to_last_elem/kth_to_last_elem_solution.ipynb) |
| Delete a node in the middle of a linked list | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/delete_mid/delete_mid_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/delete_mid/delete_mid_solution.ipynb) |
| Partition a linked list around a given value | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/partition/partition_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/partition/partition_solution.ipynb) |
| Add two numbers whose digits are stored in a linked list | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/add_reverse/add_reverse_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/add_reverse/add_reverse_solution.ipynb) |
| Find the start of a linked list loop | [Challenge]()│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/find_loop_start/find_loop_start_solution.ipynb) |
| Determine if a linked list is a palindrome | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/palindrome/palindrome_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/palindrome/palindrome_solution.ipynb) |
| Implement a linked list | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/linked_list/linked_list_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/linked_lists/linked_list/linked_list_solution.ipynb) |
| Determine if a list is cyclic or acyclic | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/stack_queue_wikipedia.png">
</p>
<br/>

### Stacks and Queues

| Challenge | Static Notebook |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Implement n stacks using a single array | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/n_stacks/n_stacks_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/n_stacks/n_stacks_solution.ipynb) |
| Implement a stack that keeps track of its minimum element | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack_min/stack_min_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack_min/stack_min_solution.ipynb) |
| Implement a set of stacks class that wraps a list of capacity-bounded stacks | [Challenge]()│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/set_of_stacks/set_of_stacks_solution.ipynb) |
| Implement a queue using two stacks | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_from_stacks/queue_from_stacks_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_from_stacks/queue_from_stacks_solution.ipynb) |
| Sort a stack using another stack as a buffer | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/sort_stack/sort_stack_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/sort_stack/sort_stack_solution.ipynb) |
| Implement a stack | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack/stack_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/stack/stack_solution.ipynb) |
| Implement a queue | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_list/queue_list_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/stacks_queues/queue_list/queue_list_solution.ipynb) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/binary_tree_wikipedia.png">
</p>
<br/>

### Graphs and Trees

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Implement depth-first search (pre-, in-, post-order) on a tree |  [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_dfs/dfs_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_dfs/dfs_solution.ipynb) |
| Implement breadth-first search on a tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_bfs/bfs_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_bfs/bfs_solution.ipynb) |
| Determine the height of a tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_height/height_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_height/height_solution.ipynb) |
| Create a binary search tree with minimal height from a sorted array | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_min/bst_min_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_min/bst_min_solution.ipynb) |
| Create a linked list for each level of a binary tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_level_lists/tree_level_lists_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/tree_level_lists/tree_level_lists_solution.ipynb) |
| Check if a binary tree is balanced | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/check_balance/check_balance_solution.ipynb) |
| Determine if a tree is a valid binary search tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_validate/bst_validate_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_validate/bst_validate_solution.ipynb) |
| Find the in-order successor of a given node in a binary search tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_successor/bst_successor_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst_successor/bst_successor_solution.ipynb) |
| Implement a binary search tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst/bst_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/bst/bst_solution.ipynb) |
| Implement depth-first search on a graph |  [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_dfs/dfs_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_dfs/dfs_solution.ipynb) |
| Implement breadth-first search on a graph | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_bfs/bfs_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_bfs/bfs_solution.ipynb) |
| Determine if there is a path between two nodes in a graph | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph_path_exists/path_exists_solution.ipynb) |
| Implement a graph | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph/graph_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/graphs_trees/graph/graph_solution.ipynb) |
| Print a tree using pre-order traversal without recursion | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Determine the lowest common ancestor of two nodes | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Transform a binary tree into a heap | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Implement a right and left rotation on a tree | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Check if a binary tree is binary search tree | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif">
</p>
<br/>

### Sorting

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Implement selection sort | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/selection_sort/selection_sort_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/selection_sort/selection_sort_solution.ipynb) |
| Implement insertion sort | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/insertion_sort/insertion_sort_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/insertion_sort/insertion_sort_solution.ipynb) |
| Implement quick sort | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/quick_sort/quick_sort_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/quick_sort/quick_sort_solution.ipynb) |
| Implement merge sort | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/merge_sort/merge_sort_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/sorting_searching/merge_sort/merge_sort_solution.ipynb) |
| Implement a stable selection sort | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Make an unstable sort stable | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Implement an efficient, in-place version of quicksort | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Given two sorted arrays, merge one into the other in sorted order | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Sort an array of strings so all anagrams are next to each other | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Find an element in a rotated and sorted array of integers | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/fibonacci_wikipedia.png">
</p>
<br/>

### Recursion and Dynamic Programming

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Implement fibonacci recursively, dynamically, and iteratively | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/fibonacci/fibonacci_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/fibonacci/fibonacci_solution.ipynb) |
| Implement the Towers of Hanoi with 3 towers and N disks | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/hanoi/hanoi_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/hanoi/hanoi_solution.ipynb) |
| Find the number of ways to represent n cents given an array of coins | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change_ways/coin_change_ways_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/coin_change_ways/coin_change_ways_solution.ipynb) |
| Print all valid combinations of n-pairs of parentheses | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/n_pairs_parentheses/n_pairs_parentheses_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/recursion_dynamic/n_pairs_parentheses/n_pairs_parentheses_solution.ipynb) |
| Implement factorial recursively, dynamically, and iteratively | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Perform a binary search on a sorted array of integers | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Print all subsets of a set | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Print all permutations of a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Print all combinations of a string | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Implement a paint fill function | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Find all permutations to represent n cents, given 1, 5, 10, 25 cent coins | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/probability_distribution_wikipedia.png">
</p>
<br/>

### Mathematics and Probability

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Check if a number is prime | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Generate a list of primes | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Determine if two lines on a Cartesian plane intersect | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Using only add, implement multiply, subtract, and divide for ints | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Find the kth number such that the only prime factors are 3, 5, and 7 | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/bit_manipulation_wikipedia.png">
</p>
<br/>

### Bit Manipulation

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Given a number between 0 and 1, print the binary representation | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Determine the number of bits required to convert integer A to integer B | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Swap odd and even bits in an integer with as few instructions as possible | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Determine the number of 1 bits in the binary representation of a given integer | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

<br/>
<p>
  <img src="https://raw.githubusercontent.com/donnemartin/interactive-coding-challenges/master/images/logo_topcoder.png">
</p>
<br/>

### Online Judges

| Challenge | Static Notebooks |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Utopian tree | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/online_judges/utopian_tree/utopian_tree_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/online_judges/utopian_tree/utopian_tree_solution.ipynb) |
| Maximizing xor | [Challenge](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/online_judges/maximizing_xor/maximizing_xor_challenge.ipynb)│[Solution](http://nbviewer.ipython.org/github/donnemartin/interactive-coding-challenges/blob/master/online_judges/maximizing_xor/maximizing_xor_solution.ipynb) |
| Add a challenge | [Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md)│[Contribute](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) |

## Repo Structure

```
interactive-coding-challenges        # Repo
├─ arrays_strings                    # Category of challenges
│  ├─ rotation                       # Challenge folder
│  │  ├─ rotation_challenge.ipynb    # Challenge notebook
│  │  ├─ rotation_solution.ipynb     # Solution notebook
│  │  ├─ test_rotation.py            # Unit test*
│  ├─ compress
│  │  ├─ compress_challenge.ipynb
│  │  ├─ compress_solution.ipynb
│  │  ├─ test_compress.py
│  ├─ ...
├─ linked_lists
│  ├─ palindrome
│  │  └─ ...
│  ├─ ...
├─ ...
```

<i>\*The notebooks (.pynb) read/write the associated unit test (.py) file.</i>


## Notebook Installation

### IPython Notebook

If you already have Python installed and are familiar with installing packages, you can get IPython Notebook with pip:

```
pip install "ipython[notebook]"
```

If you run into an issue about pyzmq, refer to the following [Stack Overflow post](http://stackoverflow.com/questions/24995438/pyzmq-missing-when-running-ipython-notebook) and run:

```
pip uninstall ipython
pip install "ipython[all]"
```

As an alternative, you can also use the provided ```requirements.txt``` file:

```
pip install -r requirements.txt
```

For detailed instructions, scripts, and tools to more optimally set up your development environment, check out the [dev-setup](https://github.com/donnemartin/dev-setup) repo.

For more details on notebook installation, follow the directions [here](http://ipython.org/install.html).

More information on IPython/Jupyter Notebooks can be found [here](http://ipython.org/notebook.html).

### Nose Tests

Install nose using setuptools/distribute:

```
easy_install nose
```

or

```
pip install nose
```

More information on Nose can be found [here](https://nose.readthedocs.org/en/latest/).

## Running Challenges

### Notebooks

Challenges are provided in the form of **IPython/Jupyter Notebooks** and have been **tested with Python 2.7 and Python 3.4**.

*If you need to install IPython/Jupyter Notebook, see the [Notebook Installation](#notebook-installation) section.*

* This README contains links to [nbviewer](http://nbviewer.ipython.org), which hosts **static notebooks** of the repo's contents
* To interact with or to modify elements within the **dynamic notebooks**, refer to the instructions below

Run the notebook of challenges:

```
$ git clone https://github.com/donnemartin/interactive-coding-challenges.git
$ cd interactive-coding-challenges
$ jupyter notebook
```

This will launch your web browser with the list of challenge categories:
* Navigate to the **Challenge Notebook** you wish to solve
* Run the cells within the challenge notebook (Cell->Run All)
    * This will result in an expected unit test error
* Solve the challenge and verify it passes the unit test
* Check out the accompanying **Solution Notebook** for further discussion

To **debug** your solution with pdb, refer to the following [ticket](https://github.com/donnemartin/interactive-coding-challenges/issues/11).

Note: If your solution is different from those listed in the Solution Notebook, consider submitting a pull request so others can benefit from your work.  Review the [Contributing Guidelines](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) for details.

## Contributing

Contributions are welcome!

Review the [Contributing Guidelines](https://github.com/donnemartin/interactive-coding-challenges/blob/master/CONTRIBUTING.md) for details on how to:
* Submit issues
* Add solutions to existing challenges
* Add new challenges

## Credits

### Resources

* [Cracking the Coding Interview](http://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X) | [GitHub Solutions](https://github.com/gaylemcd/ctci)
* [Elements of Programming Interviews](http://www.amazon.com/Elements-Programming-Interviews-Insiders-Guide/dp/1479274836) | [GitHub Solutions](https://github.com/epibook/epibook.github.io)
* [Programming Interviews Exposed](http://www.amazon.com/gp/product/1118261364/)
* [The Algorithm Design Manual](http://www.amazon.com/Algorithm-Design-Manual-Steve-Skiena/dp/0387948600) | [Solutions](http://www.algorithm.cs.sunysb.edu/algowiki/index.php/The_Algorithms_Design_Manual_(Second_Edition))
* [CareerCup](http://www.careercup.com/)
* [Quora](http://www.quora.com/)
* [HackerRank](https://www.hackerrank.com)
* [LeetCode](https://leetcode.com/)
* [TopCoder](https://www.topcoder.com/)

### Images

* [Arrays and Strings: nltk.org](http://www.nltk.org/images/string-slicing.png)
* [Linked Lists: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg)
* [Stacks: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/2/29/Data_stack.svg)
* [Queues: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/5/52/Data_Queue.svg)
* [Sorting: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)
* [Recursion and Dynamic Programming: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/b/bf/PascalTriangleFibanacci.svg)
* [Graphs and Trees: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/f/f7/Binary_tree.svg)
* [Mathematics and Probability: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/d/d2/Gaussian_distribution_2.jpg)
* [Bit Manipulation: wikipedia.org](https://upload.wikimedia.org/wikipedia/commons/5/5c/Rotate_left_logically.svg)
* [Online Judges: topcoder.com](https://www.topcoder.com/wp-content/uploads/2014/05/topcoder_logo_home_sm.png)

## Contact Info

Feel free to contact me to discuss any issues, questions, or comments.

My contact info can be found on my [GitHub page](https://github.com/donnemartin).

## License

    Copyright 2015 Donne Martin

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
