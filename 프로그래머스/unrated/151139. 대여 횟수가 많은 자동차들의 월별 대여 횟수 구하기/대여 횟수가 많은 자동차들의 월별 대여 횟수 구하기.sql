-- 코드를 입력하세요
SELECT MONTH(H.START_DATE) AS MONTH , H.CAR_ID,  COUNT(H.HISTORY_ID) AS RECORDS #,C #, H.START_DATE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
WHERE H.CAR_ID IN 
    (SELECT H.CAR_ID #, COUNT(H.CAR_ID) AS C
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
        WHERE H.START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY H.CAR_ID
        HAVING COUNT(*)>=5) AND  H.START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH, H.CAR_ID
ORDER BY MONTH ASC, H.CAR_ID DESC