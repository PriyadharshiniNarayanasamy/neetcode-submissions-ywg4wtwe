SELECT student_id, exam_id, score FROM exam_results
WHERE (student_id, score, exam_id) IN (
    SELECT student_id, MAX(score), MIN(exam_id)
    FROM exam_results
    WHERE (student_id, score) IN (SELECT student_id, MAX(score) FROM exam_results GROUP BY student_id)
    GROUP BY student_id
)
ORDER BY student_id ASC;