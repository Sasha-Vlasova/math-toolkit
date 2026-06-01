from core.quadratic import solve_quadratic

def test_two_real_roots():
    roots = solve_quadratic(1,-3,2)

    assert roots[0] == 2
    assert roots[1] == 1
    
def test_repeated_root():
    roots = solve_quadratic(1,-3,2)

    assert roots[0] == 1
    assert roots[1] == 1


def test_complex_roots():
    roots = solve_quadratic(1, 2, 5)

    assert roots[0] == (-1 + 2j)
    assert roots[1] == (-1 - 2j)