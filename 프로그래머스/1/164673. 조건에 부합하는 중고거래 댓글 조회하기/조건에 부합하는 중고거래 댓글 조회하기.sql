SELECT BOARD.TITLE, BOARD.BOARD_ID, REPLY.REPLY_ID, REPLY.WRITER_ID, REPLY.CONTENTS, TO_CHAR(REPLY.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
FROM USED_GOODS_BOARD BOARD
INNER JOIN USED_GOODS_REPLY REPLY
ON BOARD.BOARD_ID = REPLY.BOARD_ID
WHERE TO_CHAR(BOARD.CREATED_DATE, 'YYYY-MM') = '2022-10'
ORDER BY CREATED_DATE ASC, TITLE ASC;