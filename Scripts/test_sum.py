import pytest

class Test_sum:
    
    @pytest.mark.parametrize("a, b,expect", [(1,2,3),(4,5,6)])
    def test_sum(self, a, b, expect):
        assert a + b == expect
