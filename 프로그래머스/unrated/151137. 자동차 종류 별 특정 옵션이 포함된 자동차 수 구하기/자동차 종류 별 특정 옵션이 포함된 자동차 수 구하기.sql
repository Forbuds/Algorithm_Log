-- 코드를 입력하세요
SELECT C.CAR_TYPE, COUNT(C.CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR  AS C
WHERE C.OPTIONS LIKE '%통풍시트%' OR C.OPTIONS LIKE '%열선시트%' OR C.OPTIONS LIKE '%가죽시트%'
GROUP BY C.CAR_TYPE 
ORDER BY C.CAR_TYPE ASC