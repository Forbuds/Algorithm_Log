-- 코드를 입력하세요
SELECT DISTINCT(C.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR AS C
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON H.CAR_ID = C.CAR_ID
WHERE C.CAR_TYPE IN ('세단') AND MONTH(H.start_date) = 10
ORDER BY C.CAR_ID DESC



# SELECT DISTINCT(car_id) FROM car_rental_company_car AS c
# INNER JOIN car_rental_company_rental_history AS h USING(car_id)
# WHERE car_type IN('세단') AND DATE_FORMAT(start_date, '%Y-%m') = '2022-10'
# ORDER BY 1 DESC;