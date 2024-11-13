WITH
    city AS (
        SELECT
            city,
            country
        FROM
            Children ch
            JOIN ChristmasList cl ON ch.child_id = cl.child_id
        GROUP BY
            city,
            country
        HAVING
            COUNT(*) >= 5
    ),
    childs AS (
        SELECT
            ch.child_id,
            naughty_nice_score,
            city,
            country
        FROM
            Children ch
            JOIN ChristmasList cl ON ch.child_id = cl.child_id
    ),
    top_city AS (
        SELECT
            c.country,
            c.city,
            AVG(naughty_nice_score) AS naughty_nice_score,
            ROW_NUMBER() OVER       (
                PARTITION BY
                    c.country
                ORDER BY
                    AVG(naughty_nice_score) DESC
            ) rn
        FROM
            city c
            JOIN childs ch ON c.city = ch.city
            AND c.country = ch.country
        GROUP BY
            c.country,
            c.city
    )
SELECT
    country,
    city,
    naughty_nice_score
FROM
    top_city
WHERE
    rn <= 3
ORDER BY
    naughty_nice_score DESC;