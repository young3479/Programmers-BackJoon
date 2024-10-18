-- 코드를 입력하세요
#동물보호소에 들어온 동물정보(ANIMAL_INS)
#가장 최근에 들어온 동물은 언제 들어왔는지
SELECT DATETIME AS '시간' FROM ANIMAL_INS
ORDER BY DATETIME DESC LIMIT 1;