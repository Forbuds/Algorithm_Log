-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS AS I
WHERE INTAKE_CONDITION NOT LIKE 'Aged'
ORDER BY ANIMAL_ID ASC