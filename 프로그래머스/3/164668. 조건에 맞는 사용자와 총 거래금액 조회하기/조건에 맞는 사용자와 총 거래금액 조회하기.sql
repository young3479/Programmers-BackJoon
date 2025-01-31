-- 코드를 입력하세요
# 중고거래 게시판 정보: USED_GOODS_BOARD, 중고거래 게시판 사용자 정보: USED_GOODS_USER
# 완료된 중고 거래와 총 금액이 70만원 이상인 사람의 정보 조회, 금액 기준 오름 차순 정렬
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER U JOIN USED_GOODS_BOARD B
ON U.USER_ID = B.WRITER_ID
WHERE STATUS = 'DONE'
GROUP BY U.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES;