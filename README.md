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
- [codenode_python.node.Node](#codenode_pythonnodenode)
- [codenode_python.Function](#codenode_pythonfunction)
- [codenode_python.Class](#codenode_pythonclass)
- [codenode_python.method.Method](#codenode_pythonmethodmethod)
- [codenode_python.If](#codenode_pythonif)
- [codenode_python.conditional.Elif](#codenode_pythonconditionalelif)
- [codenode_python.conditional.Else](#codenode_pythonconditionalelse)
- [codenode_python.For](#codenode_pythonfor)
- [codenode_python.While](#codenode_pythonwhile)
- [codenode_python.Try](#codenode_pythontry)
- [codenode_python.try_except.Except](#codenode_pythontry_exceptexcept)
- [codenode_python.try_except.Finally](#codenode_pythontry_exceptfinally)
- [codenode_python.With](#codenode_pythonwith)
- [codenode_python.Match](#codenode_pythonmatch)
- [codenode_python.match_statement.Case](#codenode_pythonmatch_statementcase)
- [codenode_python.DocString](#codenode_pythondocstring)
- [codenode_python.Comment](#codenode_pythoncomment)
- [codenode_python.commented](#codenode_pythoncommented)


---
### codenode_python.node.Node<a id="codenode_pythonnodenode"></a>

> ```python
> class Node(codenode_utilities.PartitionedNode): ...
> ```
> 
> Nodes that can contain an arbitrary number of
> inner python statements.
> 
> Due to inheriting from PartitionedNode:
> - Each node has a list of children nodes, along with a
>   add_child and add_children method
> - Each node has an inherited convenience dump/dumps method.
> - Overridable methods yielding nodes for three different innner
>   sections:
>     - header
>     - body (indented by default in `PartitionedNode.__iter__`)
>     - footer
> 
> Documentation for ParitionedNode can be viewed
> [here](https://github.com/0xf0f/codenode/tree/master/codenode_utilities#codenode_utilitiespartitionednode).
> 
> 
> Will output a single 'pass' line as its body section if no other
> nodes are added as its children.
---
### codenode_python.Function<a id="codenode_pythonfunction"></a>

> ```python
> class Function(Node): ...
> ```
> 
> Nodes representing a python function definition.
#### Methods
> ##### `__init__`
> ```python
> class Function(Node):
>     def __init__(self, name: str, *args: str, **kwargs: str): ...
> ````
> 
> 
> #### Parameters
> * > ***name:*** 
>   > Name of function.
> * > ***args:*** 
>   > Positional argument names of function.
> * > ***kwargs:*** 
>   > Keyword argument names and values of function.

> ##### `add_decorator`
> ```python
> class Function(Node):
>     def add_decorator(self, decorator: str): ...
> ````
> 
> Adds a decorator to this function definition.
> 
> 
> #### Parameters
> * > ***decorator:*** 
>   > Decorator to add.

#### Attributes
> ***name:*** str - 
> Name of function.

> ***args:*** 'tuple[str]' - 
> Tuple of positional argument names of function.

> ***kwargs:*** 'dict[str, str]' - 
> Keyword argument names and values of function.

> ***decorators:*** 'list[str]' - 
> List of decorators applied to this function definition, 
>     each one a single string.

> ***return_type:*** Optional[str] - 
> Return type annotation of function.

---
### codenode_python.Class<a id="codenode_pythonclass"></a>

> ```python
> class Class(Node): ...
> ```
> 
> Nodes representing a python class definition.
> 
#### Methods
> ##### `__init__`
> ```python
> class Class(Node):
>     def __init__(self, name, *parents): ...
> ````
> 
> 
> #### Parameters
> * > ***name:*** 
>   > Name of class.
> * > ***parents:*** 
>   > Parent class names/

> ##### `add_decorator`
> ```python
> class Class(Node):
>     def add_decorator(self, decorator: str): ...
> ````
> 
> Adds a decorator to this class definition.
> 
> 
> #### Parameters
> * > ***decorator:*** 
>   > Decorator to add.

> ##### `add_method`
> ```python
> class Class(Node):
>     def add_method(self, name: str, *args: str, **kwargs: str) -> Method: ...
> ````
> 
> Creates a method definition, adds it to this class definition's
> body, then returns it.
> 
> 
> #### Parameters
> * > ***name:*** 
>   > Name of method.
> * > ***args:*** 
>   > Positional argument names of method.
> * > ***kwargs:*** 
>   > Keyword argument names and values of method.
> #### Returns
> * > New method.
> 

#### Attributes
> ***name:*** str - 
> Name of class.

> ***parents:*** 'tuple[str]' - 
> Tuple of parent class names.

> ***decorators:*** 'list[str]' - 
> List of decorators applied to this class definition, each one a 
>     single string.

---
### codenode_python.method.Method<a id="codenode_pythonmethodmethod"></a>

> ```python
> class Method(Function): ...
> ```
> 
> Nodes representing a method definition.
> Don't instantiate these directly, use the parent node's add_method
> method instead.
#### Methods
> ##### `__init__`
> ```python
> class Method(Function):
>     def __init__(self, name, *args: str, **kwargs: str): ...
> ````
> 
> 
> #### Parameters
> * > ***name:*** 
>   > Name of method.
> * > ***args:*** 
>   > Positional argument names of method.
> * > ***kwargs:*** 
>   > Keyword argument names and values of method.

---
### codenode_python.If<a id="codenode_pythonif"></a>

> ```python
> class If(Node): ...
> ```
> 
> Nodes representing a python if statement.
#### Methods
> ##### `__init__`
> ```python
> class If(Node):
>     def __init__(self, condition: str): ...
> ````
> 
> 
> #### Parameters
> * > ***condition:*** 
>   > Condition checked for by the if.

> ##### `add_elif`
> ```python
> class If(Node):
>     def add_elif(self, condition: str) -> 'Elif': ...
> ````
> 
> Create an Elif node, add it to this node's elifs,
> then return it.
> 
> 
> #### Parameters
> * > ***condition:*** 
>   > Condition checked for by elif.
> #### Returns
> * > New Elif node.
> 

> ##### `add_else`
> ```python
> class If(Node):
>     def add_else(self) -> 'Else': ...
> ````
> 
> Create an Else node, set it to this node's else node,
> then return it.
> 
> 
> #### Returns
> * > New Else node
> 

#### Attributes
> ***condition:*** str - 
> Condition checked for by the if.

> ***elif_nodes:*** 'list[Elif]' - 
> List of Elif nodes following the if check.

> ***else_node:*** Optional[Else] - 
> Optional Else node following the if check and its elifs.

---
### codenode_python.conditional.Elif<a id="codenode_pythonconditionalelif"></a>

> ```python
> class Elif(Node): ...
> ```
> 
> Nodes representing a python elif statement.
> Don't instantiate these directly, use If.add_elif instead.
#### Methods
> ##### `__init__`
> ```python
> class Elif(Node):
>     def __init__(self, condition: str): ...
> ````
> 
> 
> 
> #### Parameters
> * > ***condition:*** 
>   > Condition check for by elif.

#### Attributes
> ***condition:*** str - 
> Condition checked for by elif.

---
### codenode_python.conditional.Else<a id="codenode_pythonconditionalelse"></a>

> ```python
> class Else(Node): ...
> ```
> 
> Nodes representing a python else statement.
> Don't instantiate these directly, use the parent node's add_else
> method instead.
---
### codenode_python.For<a id="codenode_pythonfor"></a>

> ```python
> class For(Node): ...
> ```
> 
> Nodes representing a python for loop.
#### Methods
> ##### `__init__`
> ```python
> class For(Node):
>     def __init__(self, expression: str): ...
> ````
> 
> 
> #### Parameters
> * > ***expression:*** 
>   > Expression iterated over by the for loop.

> ##### `add_else`
> ```python
> class For(Node):
>     def add_else(self) -> Else: ...
> ````
> 
> Create an Else node, set it to this node's else node,
> then return it.
> 
> 
> #### Returns
> * > New Else node
> 

#### Attributes
> ***expression:*** str - 
> Expression iterated over by the for loop.

> ***else_node:*** Else - 
> Optional Else node following the for loop.

---
### codenode_python.While<a id="codenode_pythonwhile"></a>

> ```python
> class While(Node): ...
> ```
> 
> Nodes representing a python while loop statement.
#### Methods
> ##### `__init__`
> ```python
> class While(Node):
>     def __init__(self, condition: str): ...
> ````
> 
> 
> #### Parameters
> * > ***condition:*** 
>   > The condition the while loop will check.

> ##### `add_else`
> ```python
> class While(Node):
>     def add_else(self): ...
> ````
> 
> Creates a new else node, sets it as this node's else node,
> then returns it.
> 
> 
> #### Returns
> * > New else node.
> 

#### Attributes
> ***condition:*** 
> The condition the while loop will check.

> ***else_node:*** Optional[Else] - 
> Optional else node following this while statement node.

---
### codenode_python.Try<a id="codenode_pythontry"></a>

> ```python
> class Try(Node): ...
> ```
> 
> Nodes representing a python try statement.
#### Methods
> ##### `add_except`
> ```python
> class Try(Node):
>     def add_except(self, types: 'tuple[str, ...]'=(), name: Optional[str]=None, exception_group=False) -> Except: ...
> ````
> 
> Creates a new except clause node, adds it to this node's list of
> except nodes, then returns it.
> 
> 
> #### Parameters
> * > ***types:*** 
>   > Exception types this clause catches.
> * > ***name:*** 
>   > Named assigned to caught exception.
> * > ***exception_group:*** 
>   > If true, exception clause is treated as
>   >                                an exception group extraction clause
>   >                                instead.
> #### Returns
> * > New except clause node.
> 

> ##### `add_else`
> ```python
> class Try(Node):
>     def add_else(self) -> Else: ...
> ````
> 
> Creates a new else node, sets it as this node's else node,
> then returns it.
> 
> 
> #### Returns
> * > New else node.
> 

> ##### `add_finally`
> ```python
> class Try(Node):
>     def add_finally(self) -> Finally: ...
> ````
> 
> Creates a new finally node, sets it as this node's finally node,
> then returns it.
> 
> 
> #### Returns
> * > New finally node.
> 

#### Attributes
> ***except_nodes:*** 'list[Except]' - 
> List of except nodes following this try statement node.

> ***finally_node:*** Optional[Finally] - 
> Optional finally clause node following this try statement node.

> ***else_node:*** Optional[Else] - 
> Optional else node following this try statement node.

---
### codenode_python.try_except.Except<a id="codenode_pythontry_exceptexcept"></a>

> ```python
> class Except(Node): ...
> ```
> 
> Nodes representing an except block following a python try block.
> Don't instantiate these directly, use the parent method's add_except
> method instead.
#### Methods
> ##### `__init__`
> ```python
> class Except(Node):
>     def __init__(self, types=(), name: Optional[str]=None, exception_group=False): ...
> ````
> 
> 
> #### Parameters
> * > ***types:*** 
>   > Exception types this clause catches.
> * > ***name:*** 
>   > Named assigned to caught exception.
> * > ***exception_group:*** 
>   > If true, exception clause is treated as
>   >                                an exception group extraction clause
>   >                                instead.

#### Attributes
> ***types:*** 'tuple[str, ...]' - 
> Exception types this clause catches.

> ***name:*** Optional[str] - 
> Named assigned to caught exception.

> ***exception_group:*** bool - 
> If true, exception clause is treated as an exception group 
>     extraction clause instead.

---
### codenode_python.try_except.Finally<a id="codenode_pythontry_exceptfinally"></a>

> ```python
> class Finally(Node): ...
> ```
> 
> Node representing a finally clause following a python try statement.
> Don't instantiate these directly, use the parent node's add_finally
> method instead.
---
### codenode_python.With<a id="codenode_pythonwith"></a>

> ```python
> class With(Node): ...
> ```
> 
> Nodes representing a python with statement.
#### Methods
> ##### `__init__`
> ```python
> class With(Node):
>     def __init__(self, *expressions: str): ...
> ````
> 
> 
> #### Parameters
> * > ***expressions:*** 
>   > Expressions used within the context of the
>   >                            with block.

#### Attributes
> ***expressions:*** 'tuple[str]' - 
> Expressions used within the context of the with block.

---
### codenode_python.Match<a id="codenode_pythonmatch"></a>

> ```python
> class Match: ...
> ```
> 
> Nodes representing a python match statement.
#### Methods
> ##### `__init__`
> ```python
> class Match:
>     def __init__(self, subject: str): ...
> ````
> 
> 
> #### Parameters
> * > ***subject:*** 
>   > Subject of match statement.

> ##### `add_case`
> ```python
> class Match:
>     def add_case(self, pattern: str) -> Case: ...
> ````
> 
> Creates a new case node, adds it to this node's case node list,
> then returns it.
> 
> 
> #### Parameters
> * > ***pattern:*** 
>   > Pattern new case will match to.
> #### Returns
> * > New case node.
> 

#### Attributes
> ***subject:*** str - 
> Subject of match statement.

> ***cases:*** 'list[Case]' - 
> List of case block nodes belonging to this match statement.

---
### codenode_python.match_statement.Case<a id="codenode_pythonmatch_statementcase"></a>

> ```python
> class Case(Node): ...
> ```
> 
> Nodes representing a case block in a python match statement.
> Don't instantiate these directly, use the parent node's add_case
> method instead.
#### Methods
> ##### `__init__`
> ```python
> class Case(Node):
>     def __init__(self, pattern: str): ...
> ````
> 
> 
> #### Parameters
> * > ***pattern:*** 
>   > Pattern this case will match to.

#### Attributes
> ***pattern:*** str - 
> Pattern this case will match to.

---
### codenode_python.DocString<a id="codenode_pythondocstring"></a>

> ```python
> class DocString: ...
> ```
> 
> Nodes representing a python docstring.
#### Methods
> ##### `__init__`
> ```python
> class DocString:
>     def __init__(self, content=''): ...
> ````
> 
> 
> #### Parameters
> * > ***content:*** 
>   > Content of docstring.
>   >                        Will be broken down into separate lines.

#### Attributes
> ***content:*** 
> Content of docstring.

---
### codenode_python.Comment<a id="codenode_pythoncomment"></a>

> ```python
> class Comment: ...
> ```
> 
> Nodes representing a python comment.
#### Methods
> ##### `__init__`
> ```python
> class Comment:
>     def __init__(self, content=''): ...
> ````
> 
> 
> #### Parameters
> * > ***content:*** 
>   > Comment content. Will be split into individual
>   >                        lines.

#### Attributes
> ***content:*** 
> Comment content.

---
### codenode_python.commented<a id="codenode_pythoncommented"></a>

> ```python
> def commented(node, dumps=lambda node: codenode.dumps(node)) -> Comment: ...
> ````
> 
> Returns a comment node whose content is based on the string output
> of processing another node.
> 
> 
> #### Parameters
> * > ***node:*** 
>   > Node whose string output will be used as the content
>   >                 of the comment.
> * > ***dumps:*** 
>   > Function used to convert the node to a string.
> #### Returns
> * > New comment node.
> 


