# mov

### install
```
# main
$ pip install git+https://github.com/sooj1n/mov.git

# branch
$ pip install git_https://github.com/sooj1n/mov.git@<BRANCH_NAME>
```
### start dev
```
$ git clone <URL>
$ cd <DIR>

$ option
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pytest
```

### setting env
```bash
cat ~/.zshrc | tail -n 3
# MY_ENV
export MOVIE_API_KEY="<KEY>"
```

### 트러블슈팅
- [ ] 영화진흥위원회 가입 및 키 생성
```
{'faultInfo': {'message': '유효하지않은 키값입니다.', 'errorCode': '320010'}}
```
