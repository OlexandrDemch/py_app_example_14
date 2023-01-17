try:

    end = int(input('x->'))
    symbol = input('symbol->')
    print((symbol + "\n") * end)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')