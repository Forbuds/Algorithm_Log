-- 코드를 입력하세요
SELECT DATE_FORMAT(O.SALES_DATE,'%Y-%m-%d') AS SALES_DATE,O.PRODUCT_ID,O.USER_ID,O.SALES_AMOUNT
FROM ONLINE_SALE AS O
WHERE DATE_FORMAT(O.SALES_DATE,'%Y-%m') = '2022-03'

UNION

SELECT DATE_FORMAT(F.SALES_DATE,'%Y-%m-%d')AS SALES_DATE,F.PRODUCT_ID,NULL AS USER_ID,F.SALES_AMOUNT     
FROM OFFLINE_SALE AS F
WHERE DATE_FORMAT(F.SALES_DATE,'%Y-%m') = '2022-03'

ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC