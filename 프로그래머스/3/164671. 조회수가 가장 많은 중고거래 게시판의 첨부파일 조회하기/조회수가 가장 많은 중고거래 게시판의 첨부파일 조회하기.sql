-- 코드를 입력하세요
# 중고거래 게시판: USED_GOODS_BOARD, 중고거래 게시판 첨부파일: USED_GOODS_FILE
# 조회수 가장 높은 게시물에 대한 첨부파일 경로 조회
SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH FROM USED_GOODS_FILE F JOIN USED_GOODS_BOARD B
ON F.BOARD_ID = B.BOARD_ID
# 조회수가 가장 높은 Board_id를 선택
# 서브쿼리로 조회수 가장 높은 보드 선택해서 F.Borad id랑 같으면 출력
WHERE B.BOARD_ID = (
    SELECT BOARD_ID FROM USED_GOODS_BOARD ORDER BY VIEWS DESC LIMIT 1
)
ORDER BY F.FILE_ID DESC;