import pytest
import sys
sys.path.append('../..')
from pythoncode.calculatoy import Calculatoy
import yaml


def get_datas(name,type='int'):
    with open('./datas/calc.yml')as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas,ids)

# 测试类
class TestCalc:
    #datas:list = get_datas()
    add_int_data = get_datas('add','int')
    add_float_data = get_datas('add','folat')
    div_erro_data = get_datas('div','erro')
    div_int_data = get_datas('div','int')

    def setup_class(self):
        print('开始计算')
        self.calc = Calculatoy()
    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,result',add_int_data[0],ids=add_int_data[1])
    def test_add(self,a,b,result):
        print(f"a={a}, b ={b} ,result={result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,result',add_float_data[0],ids=add_float_data[1])
    def test_add_float(self,a,b,result):
        assert result == round(self.calc.add(a, b),2)

    # todo:相除功能
    @pytest.mark.parametrize('a,b,result', div_int_data[0], ids=div_int_data[1])
    def test_div_int(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.div(a,b)

    @pytest.mark.parametrize('a,b,result', div_erro_data[0], ids=div_erro_data[1])
    def test_div_erro(self,a ,b ,result):
        with pytest.raises(ZeroDivisionError):
            result = a/b
        print(f'a={a}, b={b},result={result}')

