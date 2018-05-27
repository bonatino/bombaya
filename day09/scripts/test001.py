import pytest 

class Test_01:

    @pytest.mark.parametrize("a",[1,3,7])
    def test_01(self,a):
        assert a == 7