import base64
from base64 import decodestring
import sys
from sys import argv


option = sys.argv[1]



if option == '-e':
    print("인코딩 합니다 문자열을 입력해 주세요: ")
    string = input()
    string_s = string.encode('utf-8')
    #Encode as Base64
    string_e = base64.b64encode(string_s)
    string_e = string_e.decode('utf-8')
    print(string_e)
try:
    if option == '-d':
        print("디코딩 합니다 문자열을 입력해 주세요: ")
        a = input()
        a = a.encode('utf-8')
        #Decode from Base64
       # print(base64.b64decode(a))
        print(str(base64.b64decode(a), encoding='utf-8'))
except UnicodeDecodeError:
    print("\n문자열이 깨졌습니다!")
    print("할당받을 수 있는 문자열이 초과되었습니다 제대로 입력했는지 확인하신 후 다시 실행해 주세요")


if option == '-sd':
    ## Encode-or-Decode.py -sd [target file]
    f = open(argv[2], 'rb')
    b = f.read()
    f.close()
    part = b.split(b'\x0d\x0a' * 2)
    for i, j in enumerate(part):
            print(i, j[:4])
            f = open(str(i) + '.bin', 'wb')
            f.write(j)
            f.close()

if option == '-ds':
    ## Encode-or-Decode.py -ds [target file]
    f = open(argv[2], 'rb')
    b = f.read()
    f.close()
    d = decodestring(b)
    f = open('decoded_'+argv[2], 'wb')
    f.write(d)
    f.close()
