-- 코드를 입력하세요
SELECT  ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE ANIMAL_INS.INTAKE_CONDITION LIKE 'Sick%'
ORDER BY ANIMAL_ID ASC