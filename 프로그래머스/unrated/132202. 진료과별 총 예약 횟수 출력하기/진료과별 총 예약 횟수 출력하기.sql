SELECT A.MCDP_CD AS '진료과 코드', COUNT(A.APNT_NO) AS '5월예약건수'
FROM APPOINTMENT AS A

WHERE A.APNT_YMD LIKE '2022-05%' #AND A.APNT_CNCL_YN NOT LIKE 'Y'
GROUP BY A.MCDP_CD
ORDER BY COUNT(A.APNT_NO) ASC, A.MCDP_CD ASC
