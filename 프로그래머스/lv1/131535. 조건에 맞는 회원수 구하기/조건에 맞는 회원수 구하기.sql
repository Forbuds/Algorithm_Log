-- 코드를 입력하세요
SELECT COUNT(I.USER_ID) AS USERS
FROM USER_INFO AS I
WHERE DATE_FORMAT(I.JOINED ,'%Y')='2021' AND ( I.AGE BETWEEN 20 AND 29)
