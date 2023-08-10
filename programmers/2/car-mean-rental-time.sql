-- 코드를 입력하세요
-- 평균 대여 기간이 7일 이상
-- 자동차 ID 평균 대여 기간 - 소수점 두번째 자리 반올림
-- 평균 대여 기간 내림차순, 자동차 ID 내림차순
SELECT 
    CAR_ID, 
    ROUND(AVG(DATEDIFF(END_DATE, START_DATE)+1), 1) as AVERAGE_DURATION
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by 
    CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, CAR_ID desc