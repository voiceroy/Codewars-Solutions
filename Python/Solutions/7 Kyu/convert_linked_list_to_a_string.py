def stringify(node: Node) -> str:
    if node is None:
        return "None"
    string = str(node.data)
    return string + " -> " + str(stringify(node.next))
