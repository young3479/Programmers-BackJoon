-- 코드를 입력하세요
# 보호소 동물 정보: ANIMAL_INS
# 개 이름에 'el'이 들어가는 개의 아이디와 이름 조회(대소구분 안함)
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
AND NAME LIKE '%el%'
ORDER BY NAME;