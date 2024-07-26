def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "8ece39e938f850f4099b0d6f34095640"

    url= f"{base_url}?key={key}&targetDt={dt}"

    print(url)
