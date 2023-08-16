### Contents
- [What is this?](#what-is-this)
- [How do I install it?](#how-do-i-install-it)
- [How do I use it?](#how-do-i-use-it)
- [Extensions](#extensions)
- [Reference](#reference)

### What is this?<a id="what-is-this"></a>
This module contains some helper classes and functions for generating
python code using [codenode](https://github.com/0xf0f/codenode).

### How do I install it?<a id="how-do-i-install-it"></a>

#### From PyPI:
`pip install codenode-python`

#### From GitHub:
`pip install git+https://github.com/0xf0f/codenode-python`

### How do I use it?<a id="how-do-i-use-it"></a>
Helpers imported from `codenode_python` can be used to describe python 
code, and, like any other iterable, passed into `codenode.dump/dumps` 
to generate output.

Compound statement nodes, which inherit from `codenode_python.node.Node`,
have `add_child` and `add_children` methods for adding inner nodes.
They also have convenience `dump`/`dumps` methods to generate output 
by calling codenode's default `dump`/`dumps` with the node as an 
argument.

Simple example:
```python
import codenode as cn
import codenode_python as py

block = []

for i in range(5):
    func = py.Function(f'count_to_{i}')
    count_loop = py.For(f'i in range({i})')
    count_loop.add_child(py.Call('print', 'i'))
    func.add_child(count_loop)
    block.append(func)
    block.append(cn.empty_lines(1))

print(cn.dumps(block))
```

Which outputs:
```
def count_to_0():
    for i in range(0):
        print(i)

def count_to_1():
    for i in range(1):
        print(i)

def count_to_2():
    for i in range(2):
        print(i)

def count_to_3():
    for i in range(3):
        print(i)

def count_to_4():
    for i in range(4):
        print(i)

```

### Extensions<a id="extensions"></a>
New compound statement nodes can be implemented by creating 
subclasses of `codenode_python.node.Node`.

### Reference<a id="reference"></a>

#### Contents
${reference_contents}

${reference}
