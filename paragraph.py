import sys

def calculate_paragraph(addr_int):
    offset = addr_int % 16

    if offset != 0:
        return (addr_int // 16 + 1) * 16
    else:
        return addr_int

def format_hex(value):
    template = '0x{:0>5x}'
    return template.format(value)

if __name__ == '__main__':
    # Check that an address argument was provided
    if len(sys.argv) < 2:
        print('Usage: python paragraph.py <address>')
        sys.exit(1)

    # Calculate the next paragraph boundary
    t = sys.argv[1]
    addr = int(t, 10)
    if t.startswith('0x'):
        addr = int(t, 16)

    paragraph_addr = calculate_paragraph(t)
    formatted_hex = format_hex(paragraph_addr)

    print(formatted_hex)

    if "-r" in sys.argv:
        print('Stored as', formatted_hex[:6])


