import re


def process_barcode(barcode: str) -> str:
    pattern = r'@#+([A-Z][A-Za-z\d]{4,}[A-Z])@#+'
    matches = re.fullmatch(pattern, barcode)
    product_group = ''
    if matches:
        for ch in matches.group(1):
            if ch.isdigit():
                product_group += ch
        product_group = product_group if product_group else '00'
        return f'Product group: {product_group}'

    return 'Invalid barcode'


n = int(input())

for _ in range(n):
    current_barcode = input()
    print(process_barcode(current_barcode))
