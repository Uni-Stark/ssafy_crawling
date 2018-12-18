from elice_utils import EliceUtils

elice_utils = EliceUtils()
import re


def main():
    sentence = "제보는 032-232-3245 또는 010-222-2233 으로 연락주시기 바랍니다."

    compile_text = re.compile(r'010-\d\d\d-\d\d\d\d')
#   번호를 알기 위한 정규식은 이런 방식으로 사용이 된다.

    match_text = compile_text.findall(sentence)
#   compile_text 가 거름망이 되어서 sentence를 걸러내서 내가 원하는 자료들만 내놓는 것이다.
    print(match_text)

    email = ["aa2@naver.com", "kbc@aaaaa", "Alice@Alice.com", "ILove@CodingLove"]

    compile_text = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')

    for i in email:
        print(compile_text.match(i) != None)


if __name__ == "__main__":
    main()
