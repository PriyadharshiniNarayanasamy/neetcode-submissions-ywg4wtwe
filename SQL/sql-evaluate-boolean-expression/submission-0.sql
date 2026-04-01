-- Write your query below
SELECT e.left_operand, e.operator, e.right_operand,
CASE 
    WHEN e.operator = '>' AND v_left.value > v_right.value THEN 'true'
    WHEN e.operator = '<' AND v_left.value < v_right.value THEN 'true'
    WHEN e.operator = '=' AND v_left.value = v_right.value THEN 'true'
    ELSE 'false'
END AS value
FROM expressions e
JOIN variables v_left ON e.left_operand = v_left.name
JOIN variables v_right ON e.right_operand = v_right.name;
