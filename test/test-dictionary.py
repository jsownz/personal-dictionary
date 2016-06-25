import Mangler


def test_number_swap():
    assert (Mangler.number_swap('0') == ['O'])
    assert (Mangler.number_swap('1') == ['l'])
    assert (Mangler.number_swap('2') == ['Z'])
    assert (Mangler.number_swap('3') == ['E'])
    assert (Mangler.number_swap('4') == ['A'])
    assert (Mangler.number_swap('5') == ['S'])
    assert (Mangler.number_swap('6') == ['b', 'G'])
    assert (Mangler.number_swap('7') == ['T', 'L'])
    assert (Mangler.number_swap('8') == ['B'])
    assert (Mangler.number_swap('9') == ['g', 'q'])
    assert(Mangler.number_swap('0123456789') == [
        'O123456789', '0l23456789', '01Z3456789', '012E456789', '0123A56789',
        '01234S6789', '012345b789', '012345G789', '0123456T89', '0123456L89',
        '01234567B9', '012345678g', '012345678q'])


def test_letter_swap():
    assert (Mangler.letter_swap('a') == ['@', '4'])
    assert (Mangler.letter_swap('b') == ['8'])
    assert (Mangler.letter_swap('c') == ['('])
    assert (Mangler.letter_swap('d') == [])
    assert (Mangler.letter_swap('e') == ['3'])
    assert (Mangler.letter_swap('f') == [])
    assert (Mangler.letter_swap('g') == ['6', '9'])
    assert (Mangler.letter_swap('h') == ['#'])
    assert (Mangler.letter_swap('i') == ['!'])
    assert (Mangler.letter_swap('j') == [])
    assert (Mangler.letter_swap('k') == [])
    assert (Mangler.letter_swap('l') == ['1'])
    assert (Mangler.letter_swap('m') == [])
    assert (Mangler.letter_swap('n') == [])
    assert (Mangler.letter_swap('o') == ['0'])
    assert (Mangler.letter_swap('p') == [])
    assert (Mangler.letter_swap('q') == [])
    assert (Mangler.letter_swap('r') == [])
    assert (Mangler.letter_swap('s') == ['5', '$'])
    assert (Mangler.letter_swap('t') == ['+', '7'])
    assert (Mangler.letter_swap('u') == [])
    assert (Mangler.letter_swap('v') == [])
    assert (Mangler.letter_swap('w') == [])
    assert (Mangler.letter_swap('x') == [])
    assert (Mangler.letter_swap('y') == [])
    assert (Mangler.letter_swap('z') == ['2'])
    assert (Mangler.letter_swap('abcdefg') == [
        '@bcdefg', '4bcdefg', 'a8cdefg', 'ab(defg', 'abcd3fg', 'abcdef6',
        'abcdef9'])
    assert (Mangler.letter_swap('hijklmnop') == [
        '#ijklmnop', 'h!jklmnop', 'hijk1mnop', 'hijklmn0p'])
    assert (Mangler.letter_swap('qrstuvwxyz') == [
        'qr5tuvwxyz', 'qr$tuvwxyz', 'qrs+uvwxyz', 'qrs7uvwxyz', 'qrstuvwxy2'])


def test_alternate_case():
    assert (Mangler.alternate_case('abcdefg', True) == 'AbCdEfG')
    assert (Mangler.alternate_case('ABCDEFG', True) == 'AbCdEfG')
    assert (Mangler.alternate_case('abcdefg', False) == 'aBcDeFg')
    assert (Mangler.alternate_case('ABCDEFG', False) == 'aBcDeFg')


def test_permute_phone():
    assert (Mangler.permute_phone('01234569') == [
        '01234569', '34569', '012', '69', '96543210', '210', 'O1234569',
        '0l234569', '01Z34569', '012E4569', '0123A569', '01234S69', '012345b9',
        '012345G9', '0123456g', '0123456q'])


def test_permute_casing():
    assert (Mangler.permute_casing('a') == ['a', 'A'])
    assert (Mangler.permute_casing('abcdefg') == ['abcdefg', 'Abcdefg'])


def test_permute_year():
    assert (Mangler.permute_year('1984') == [
        '84', '1984', '4891', 'l984', '1g84', '1q84', '19B4', '198A'])
    assert (Mangler.permute_year('2016') == [
        '16', '2016', '6102', 'Z016', '2O16', '20l6', '201b', '201G'])
    assert (Mangler.permute_year('3573') == [
        '73', '3573', '3753', 'E573', '3S73', '35T3', '35L3', '357E'])


def test_reverse_string():
    assert (Mangler.reverse_string('oftg') == 'gtfo')
    assert (Mangler.reverse_string('abcdefghijklmnop') == 'ponmlkjihgfedcba')
    assert (Mangler.reverse_string('12345678') == '87654321')


def test_permute_zip_code():
    assert (Mangler.permute_zip_code('12345') == [
        '54321', 'l2345', '1Z345', '12E45', '123A5', '1234S', '12345'])


def test_permute_music():
    assert (Mangler.permute_music('Cure') == [
        'cure', 'Cure', 'eruC', 'CuRe', 'cUrE', '(ure', 'cur3'])
    assert (Mangler.permute_music('Foo Fighters') == [
        'foo fighters', 'Foo fighters', 'srethgiF ooF', 'FoO fIgHtErS',
        'fOo FiGhTeRs', 'f0o fighters', 'fo0 fighters', 'foo f!ghters',
        'foo fi6hters', 'foo fi9hters', 'foo fig#ters', 'foo figh+ers',
        'foo figh7ers', 'foo fight3rs', 'foo fighter5', 'foo fighter$'])
    assert (Mangler.permute_music('N.W.A') == [
        'n.w.a', 'N.w.a', 'A.W.N', 'N.W.A', 'n.w.a', 'n.w.@', 'n.w.4'])


def test_perm_st_num():
    assert (Mangler.perm_st_num('12') == ['12', '21', 'l2', '1Z'])
    assert (Mangler.perm_st_num('1234') == [
        '1234', '4321', 'l234', '1Z34', '12E4', '123A'])
    assert (Mangler.perm_st_num('55667') == [
        '55667', '76655', 'S5667', '5S667', '55b67', '55G67', '556b7', '556G7',
        '5566T', '5566L'])
    assert (Mangler.perm_st_num('10A') == ['10A', 'A01', 'l0A', '1OA'])


def test_mangle():
    assert (Mangler.mangle(["spike", "tiger"]) == [
        '5pike', '$pike', 'sp!ke', 'spik3', 'spike', 'Spike', 'SpIkE', 'sPiKe',
        '+iger', '7iger', 't!ger', 'ti6er', 'ti9er', 'tig3r', 'tiger', 'Tiger',
        'TiGeR', 'tIgEr'])
    assert (Mangler.mangle(["poker", "lakers"]) == [
        'p0ker', 'pok3r', 'poker', 'Poker', 'PoKeR', 'pOkEr', '1akers',
        'l@kers', 'l4kers', 'lak3rs', 'laker5', 'laker$', 'lakers', 'Lakers',
        'LaKeRs', 'lAkErS'])
