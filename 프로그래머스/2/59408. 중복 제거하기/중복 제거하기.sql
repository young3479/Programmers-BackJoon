-- 코드를 입력하세요
# 동물 보호소 동물: ANIMAL_INS
SELECT COUNT(DISTINCT NAME) AS count FROM ANIMAL_INS
WHERE NAME IS NOT NULL
