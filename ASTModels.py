from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    node_type = "BASE"


@dataclass
class BaseNode(Node):
    statements: List[Node]


@dataclass
class Value(Node):
    node_type = "VALUE"

    type: str
    value: str


@dataclass
class Variable(Node):
    name: str
    type: str

@dataclass
class Operation(Node):
    node_type = "OPERATION"

@dataclass
class BinOp(Operation):
    left: Node
    right: Node
    operation: chr


@dataclass
class Function(Operation):
    name: str
    body: List[Node]
    return_node: Node = None

