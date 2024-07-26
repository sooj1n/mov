from src.mov.api.call import gen_url, req, get_key, req2dataframe

def test_req2dataframe():
    l = req2dataframe()
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

def test_req():
    code, data = req()
    assert code == 200
    
