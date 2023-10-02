SELECT S.USER_ID, S.PRODUCT_ID #*, COUNT(S.PRODUCT_ID) AS RE
FROM ONLINE_SALE AS S
GROUP BY S.user_id, S.PRODUCT_ID
HAVING COUNT(S.PRODUCT_ID)>1
ORDER BY S.USER_ID ASC,S.PRODUCT_ID DESC