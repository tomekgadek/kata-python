"""
    Szyf Cezara - kodowanie i dekodowanie (paradygmat funkcyjny)

    Jeżeli klucz key = 3, to:

    KODOWANIE:

    xayu -> adbx
    abc -> def
    python -> sbwkrq

    DEKODOWANIE:

    adbx -> xayu
    def -> abc
    sbwkrq -> python
"""

CODE_KEY = 3

def code_caesar(code_key, message):
    prepare_key = lambda key: key if key > 0 else ord('z') - ord('a') + key + 1
    shift_sign = lambda sign, key: chr(ord('a') + key - (ord('z') - ord(sign)) - 1) if ord('z') - ord(sign) < key else chr(ord(sign) + key)
    change_sign = lambda sign: shift_sign(sign, prepare_key(code_key))
    result_code_caesar = map(change_sign, message)

    return "".join(list(result_code_caesar))

def decode_caesar(code_key, message):
    return code_caesar(-code_key, message)

assert code_caesar(CODE_KEY, ['x', 'a', 'y', 'u']) == "adbx"
assert code_caesar(CODE_KEY, ['a', 'b', 'c']) == "def"
assert code_caesar(CODE_KEY, ['p', 'y', 't', 'h', 'o', 'n']) == "sbwkrq"

assert decode_caesar(CODE_KEY, ['a', 'd', 'b', 'x']) == "xayu"
assert decode_caesar(CODE_KEY, ['d', 'e', 'f']) == "abc"
assert decode_caesar(CODE_KEY, ['s', 'b', 'w', 'k', 'r', 'q']) == "python"
