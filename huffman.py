
# Hardcoded characters and frequencies
chars = ['A', 'B', 'C', 'D', 'E']
freq = [5, 9, 12, 13, 16]

# Create nodes
nodes = [[freq[i], chars[i], None, None] for i in range(len(chars))]

# Build Huffman Tree
while len(nodes) > 1:

    # Sort according to frequency
    nodes.sort(key=lambda x: x[0])

    # Pick two minimum frequency nodes
    left = nodes.pop(0)
    right = nodes.pop(0)

    # Combine them
    new_node = [left[0] + right[0], None, left, right]
    nodes.append(new_node)

# Generate Huffman Codes
def print_codes(node, code=""):

    if node[1] is not None:
        print(node[1], ":", code)
        return

    print_codes(node[2], code + "0")
    print_codes(node[3], code + "1")


print("Huffman Codes:")
print_codes(nodes[0])