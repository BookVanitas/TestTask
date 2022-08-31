import pytest
from pageObgect.page_obgect import Automat


class TestAutomat(Automat):

    @pytest.mark.parametrize('point', [0, 1, 99, 100])
    def test_positive_automat_1(self, point):
        result = self.send_automat_value(point)
        assert result == 0.01

    @pytest.mark.parametrize('point', [101, 102, 200])
    def test_positive_automat_3(self, point):
        result = self.send_automat_value(point)
        assert result == 0.03

    @pytest.mark.parametrize('point', [201, 202, 500])
    def test_positive_automat_5(self, point):
        result = self.send_automat_value(point)
        assert result == 0.05

    @pytest.mark.parametrize('point', [501, 502, 700])
    def test_positive_automat_10(self, point):
        result = self.send_automat_value(point)
        assert result == 0.1

    @pytest.mark.parametrize('point', ['700', None, ''])
    def test_neg_automat_exception(self, point):
        with pytest.raises(Exception):
            self.send_automat_value(point)

    @pytest.mark.xfail
    @pytest.mark.parametrize('point', [-1, -100])
    def test_neg_automat_fall(self, point):
        result = self.send_automat_value(point)
        assert result == 0
