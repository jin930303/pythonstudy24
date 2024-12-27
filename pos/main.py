import pay
import update
import management
import gmanagement
import ep

#재고및 물품 정보를 텍스트 파일에서 읽기

# goods, day_sale 딕셔너리 생성

f = open("재고/goods.txt","r")     # "r" 은 읽기 모드 / "w" 는 쓰기 모드/ "a" 는 추가 모드
goods ={}
day_sale = {"card":0,"cash":0}  #일 매출 정보 저장    카드와 현금 딕셔너리 key value 값으로

while True:
    tmp_dic ={}                 # 딕셔너리
    line = f.readline()         # goods.txt 라인 일기
    line = line.rstrip("\n")    # 라인내의 오른쪽 띄어쓰기 제거하고 다음줄로 바꿈
    if line== "":               # 라인이 비어있으면 중지
        break

    st_list = line.split("/")   # goods.txt 를 "/" 단위로 자른다

    tmp_dic["분류"] = st_list[1]         #1번 라면, 아이스크림, 과자, 담배
    tmp_dic["품목"] = st_list[2]         #2번
    tmp_dic["가격"] = int(st_list[3])    #3번 가격
    tmp_dic["재고"] = int(st_list[4])    #4번 수량       fix

    goods[st_list[0]] = tmp_dic         # 상품의 번호 = tmp_dic
    day_sale[st_list[0]] = 0            # 일매출(상품의 번호) = 0 초기화

# menu 불러오기

while True:
    print("="*30)
    print("1. 결제 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print("="*30,end="\n")
    select_num =input('선택 : ')

    #판매 및 재고, 일 매출 정리
    if select_num =='1':                                        #선택 번호가 1일 경우
        tmp = pay.main(goods)
        update.main(goods,tmp,day_sale)                         #update에 상품 tmp 일매출

    #재고 및 발주 관리
    elif select_num == '2' :
        gmanagement.main(goods)

    #일매출 및 월 매출 확인
    elif select_num == '3' :
        management.main(goods,day_sale)

    #프로그램 종료 전에 메모리에 있는 정보를 텍스트 파일로 저장
    elif select_num == '9' :
        ep.main(goods,day_sale)
        break
    else :
        print("다른 번호를 선택 하세요\n")

print("\nSystem down")



