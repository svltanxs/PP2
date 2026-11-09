

CREATE OR REPLACE FUNCTION pattern_check(p_pattern TEXT)
RETURNS TABLE (
    username VARCHAR(255),
    phone VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT p.username, p.phone
    FROM phonebook AS p
    WHERE p.username ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$;

-- ---------------------------------------------
CREATE OR REPLACE FUNCTION get_contacts(
    page_number INT,
    page_size INT
)
RETURNS TABLE (
    id INT,
    username VARCHAR(255),
    phone VARCHAR(255)
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF page_number < 1 OR page_size < 1 THEN
        RAISE EXCEPTION 'page_number and page_size must be greater than zero';
    END IF;

    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook AS p
    ORDER BY p.id
    LIMIT page_size
    OFFSET (page_number - 1) * page_size;
END;
$$;

