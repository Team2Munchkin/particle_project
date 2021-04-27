import pytest
import src.find_optimal_pairs as find

@pytest.mark.parametrize('list_to_test, expected_result',
    [
        ([[0]],False),
        ([[[0],[1]]],True),
        ([[0],[1],[3]],False),
        ([ [[0],[1]], [[3],[4]] ], True)
    ]
)
def test_check_if_data_contain_only_pairs(list_to_test, expected_result):
    try:
        result = find.check_if_data_contain_only_pairs(list_to_test)
        assert result == expected_result
    except BaseException as exception:
        assert 'data must contains a list with pairs' in str(exception.args)
