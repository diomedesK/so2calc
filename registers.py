import sys
from paragraph import calculate_paragraph as pg
from paragraph import format_hex as fh

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python paragraph.py <OS> <CS> <DS> <ES> <SS>')
        sys.exit(1)

    sz = {k: int(v, 16) if v.startswith('0x') else int(v) for k, v in zip(['os', 'cs', 'ds', 'es', 'ss'], sys.argv[1:])}
    sz['psp'] = 0x100

    ram_regs = { "cs": 0, "ds": 0, "es": 0, "ss": 0, "psp": 0}

    ram_regs['psp'] = pg( sz['os'] )
    ram_regs['cs'] = pg( sz['os'] + sz['psp'] )
    ram_regs['ds'] = pg( ram_regs['cs'] + sz['cs'] )
    ram_regs['es'] = pg( ram_regs['ds'] + sz['ds'] )
    ram_regs['ss'] = pg( ram_regs['es'] + sz['es'] )
    
    load_regs = ram_regs.copy()
    load_regs['ds'] = load_regs['psp']
    load_regs['es'] = load_regs['psp']

    print('Load:')
    print( { k: fh(v)[:6] for k, v in load_regs.items()  } )

    print('Allocation')
    print( { k: fh(v)[:6] for k, v in ram_regs.items()  } )
