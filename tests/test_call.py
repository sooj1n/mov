from src.mov.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd


def test_save2df():
    df = save2df(load_dt='20241231')
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns

    
def test_list2df():
    df = list2df()
    print(df)
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns

def test_req2list():
    l = req2list()
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key

def test_gnt_url():
    url = gen_url()
    #assert url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=8ece39e938f850f4099b0d6f34095640&targetDt=20120101"
    assert "http" in url
    assert "kobis" in url
    
    url = gen_url('20120101')
    

def test_req():
    code, data = req()
    assert code == 200
    
