from PersonalDictionary import *


def test_number_swap():
    assert (number_swap('0') == ['O'])
    assert (number_swap('1') == ['l'])
    assert (number_swap('2') == ['Z'])
    assert (number_swap('3') == ['E'])
    assert (number_swap('4') == ['A'])
    assert (number_swap('5') == ['S'])
    assert (number_swap('6') == ['b', 'G'])
    assert (number_swap('7') == ['T', 'L'])
    assert (number_swap('8') == ['B'])
    assert (number_swap('9') == ['g', 'q'])
    assert(number_swap('0123456789') == [
        'O123456789', '0l23456789', '01Z3456789', '012E456789', '0123A56789',
        '01234S6789', '012345b789', '012345G789', '0123456T89', '0123456L89',
        '01234567B9', '012345678g', '012345678q'])


def test_letter_swap():
    assert (letter_swap('a') == ['@', '4'])
    assert (letter_swap('b') == ['8'])
    assert (letter_swap('c') == ['('])
    assert (letter_swap('d') == [])
    assert (letter_swap('e') == ['3'])
    assert (letter_swap('f') == [])
    assert (letter_swap('g') == ['6', '9'])
    assert (letter_swap('h') == ['#'])
    assert (letter_swap('i') == ['!'])
    assert (letter_swap('j') == [])
    assert (letter_swap('k') == [])
    assert (letter_swap('l') == ['1'])
    assert (letter_swap('m') == [])
    assert (letter_swap('n') == [])
    assert (letter_swap('o') == ['0'])
    assert (letter_swap('p') == [])
    assert (letter_swap('q') == [])
    assert (letter_swap('r') == [])
    assert (letter_swap('s') == ['5', '$'])
    assert (letter_swap('t') == ['+', '7'])
    assert (letter_swap('u') == [])
    assert (letter_swap('v') == [])
    assert (letter_swap('w') == [])
    assert (letter_swap('x') == [])
    assert (letter_swap('y') == [])
    assert (letter_swap('z') == ['2'])
    assert (letter_swap('abcdefg') == [
        '@bcdefg', '4bcdefg', 'a8cdefg', 'ab(defg', 'abcd3fg', 'abcdef6',
        'abcdef9'])
    assert (letter_swap('hijklmnop') == [
        '#ijklmnop', 'h!jklmnop', 'hijk1mnop', 'hijklmn0p'])
    assert (letter_swap('qrstuvwxyz') == [
        'qr5tuvwxyz', 'qr$tuvwxyz', 'qrs+uvwxyz', 'qrs7uvwxyz', 'qrstuvwxy2'])


def test_alternate_case():
    assert (alternate_case('abcdefg', True) == 'AbCdEfG')
    assert (alternate_case('ABCDEFG', True) == 'AbCdEfG')
    assert (alternate_case('abcdefg', False) == 'aBcDeFg')
    assert (alternate_case('ABCDEFG', False) == 'aBcDeFg')


def test_permute_phone():
    assert (permute_phone('01234569') == [
        '0123456789', '3456789', '012', '6789', '9876543210', '210',
        'O123456789', '0l23456789', '01Z3456789', '012E456789', '0123A56789',
        '01234S6789', '012345b789', '012345G789', '0123456T89', '0123456L89',
        '01234567B9', '012345678g', '012345678q'])


def test_permute_casing():
    assert (permute_casing('a') == ['a', 'A'])
    assert (permute_casing('abcdefg') == ['abcdefg', 'Abcdefg'])


def test_permute_year():
    assert (permute_year('1984') == ['84', '1984', '4891', 'l984', '1g84',
                                     '1q84', '19B4', '198A'])
    assert (permute_year('2016') == ['16', '2016', '6102', 'Z016', '2O16',
                                     '20l6', '201b', '201G'])
    assert (permute_year('3573') == ['73', '3573', '3753', 'E573', '3S73',
                                     '35T3', '35L3', '357E'])


def test_reverse_string():
    assert (reverse_string('oftg') == 'gtfo')
    assert (reverse_string('abcdefghijklmnop') == 'ponmlkjihgfedcba')
    assert (reverse_string('12345678') == '87654321')


def test_permute_zip_code():
    assert (permute_zip_code('12345') == ['54321', 'l2345', '1Z345', '12E45',
                                          '123A5', '1234S', '12345'])


def test_permute_music():
    assert (permute_music('Cure') == ['cure', 'Cure', 'eruC', 'CuRe', 'cUrE',
                                      '(ure', 'cur3'])
    assert (permute_music('Foo Fighters') == [
        'foo fighters', 'Foo fighters', 'srethgiF ooF', 'FoO fIgHtErS',
        'fOo FiGhTeRs', 'f0o fighters', 'fo0 fighters', 'foo f!ghters',
        'foo fi6hters', 'foo fi9hters', 'foo fig#ters', 'foo figh+ers',
        'foo figh7ers', 'foo fight3rs', 'foo fighter5', 'foo fighter$'])
    assert (permute_music('N.W.A') == ['n.w.a', 'N.w.a', 'A.W.N', 'N.W.A',
                                       'n.w.a', 'n.w.@', 'n.w.4'])


def test_perm_st_num():
    assert (perm_st_num('12') == ['12', '21', 'l2', '1Z'])
    assert (perm_st_num('1234') == ['1234', '4321', 'l234', '1Z34', '12E4',
                                    '123A'])
    assert (perm_st_num('55667') == [
        '55667', '76655', 'S5667', '5S667', '55b67', '55G67', '556b7', '556G7',
        '5566T', '5566L'])
    assert (perm_st_num('10A') == ['10A', 'A01', 'l0A', '1OA'])


def test_mangle():
    assert (mangle(["spike", "tiger"]) == [
        '5pike', '$pike', 'sp!ke', 'spik3', 'spike', 'Spike', 'SpIkE', 'sPiKe',
        '+iger', '7iger', 't!ger', 'ti6er', 'ti9er', 'tig3r', 'tiger', 'Tiger',
        'TiGeR', 'tIgEr'])
    assert (mangle(["poker", "lakers"]) == [
        'p0ker', 'pok3r', 'poker', 'Poker', 'PoKeR', 'pOkEr', '1akers',
        'l@kers', 'l4kers', 'lak3rs', 'laker5', 'laker$', 'lakers', 'Lakers',
        'LaKeRs', 'lAkErS'])
