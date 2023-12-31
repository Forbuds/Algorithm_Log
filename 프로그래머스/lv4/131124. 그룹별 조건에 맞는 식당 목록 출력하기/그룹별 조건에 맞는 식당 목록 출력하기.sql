SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW AS R
JOIN MEMBER_PROFILE AS P ON R.MEMBER_ID = P.MEMBER_ID
WHERE R.MEMBER_ID = (SELECT R.MEMBER_ID  #, COUNT(R.REVIEW_ID) AS F
                    FROM REST_REVIEW AS R
                    GROUP BY R.MEMBER_ID
                    ORDER BY COUNT(R.REVIEW_ID) DESC
                    LIMIT 1)
ORDER BY R.REVIEW_DATE ASC, R.REVIEW_TEXT ASC

