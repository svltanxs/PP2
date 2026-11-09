-- ============================================================
-- Practice 8: PostgreSQL Procedures
-- ============================================================

-- Table structure (compatible with Practice 7)
CREATE TABLE IF NOT EXISTS phonebook (
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50),
    phone      VARCHAR(20) NOT NULL UNIQUE
);


-- 2. Procedure: insert user by name and phone; if exists, update phone
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name  VARCHAR,
    p_phone      VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phonebook
        WHERE first_name = p_first_name
          AND (last_name = p_last_name OR (last_name IS NULL AND p_last_name IS NULL))
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_first_name
          AND (last_name = p_last_name OR (last_name IS NULL AND p_last_name IS NULL));
    ELSIF EXISTS (SELECT 1 FROM phonebook WHERE phone = p_phone) THEN
        UPDATE phonebook
        SET first_name = p_first_name, last_name = p_last_name
        WHERE phone = p_phone;
    ELSE
        INSERT INTO phonebook(first_name, last_name, phone)
        VALUES(p_first_name, p_last_name, p_phone);
    END IF;
END;
$$;


-- 3. Procedure: insert many new users from lists; validate phone, return incorrect data
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_first_names   VARCHAR[],
    p_last_names    VARCHAR[],
    p_phones        VARCHAR[],
    INOUT incorrect_data TEXT[] DEFAULT ARRAY[]::TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    n INT;
    v_first_name VARCHAR;
    v_last_name  VARCHAR;
    v_phone      VARCHAR;
BEGIN
    incorrect_data := ARRAY[]::TEXT[];
    n := array_length(p_first_names, 1);
    IF n IS NULL THEN
        RETURN;
    END IF;

    FOR i IN 1..n LOOP
        v_first_name := p_first_names[i];
        v_last_name  := p_last_names[i];
        v_phone      := p_phones[i];

        -- Check phone validation: optional +, then 10 to 15 digits
        IF v_phone ~ '^\+?[0-9]{10,15}$' THEN
            -- Check if contact already exists
            IF EXISTS (
                SELECT 1 FROM phonebook
                WHERE first_name = v_first_name
                  AND (last_name = v_last_name OR (last_name IS NULL AND v_last_name IS NULL))
            ) THEN
                UPDATE phonebook
                SET phone = v_phone
                WHERE first_name = v_first_name
                  AND (last_name = v_last_name OR (last_name IS NULL AND v_last_name IS NULL));
            ELSE
                INSERT INTO phonebook(first_name, last_name, phone)
                VALUES(v_first_name, v_last_name, v_phone)
                ON CONFLICT (phone) DO UPDATE
                SET first_name = EXCLUDED.first_name,
                    last_name = EXCLUDED.last_name;
            END IF;
        ELSE
            -- Collect incorrect data
            incorrect_data := array_append(
                incorrect_data,
                v_first_name || ' ' || COALESCE(v_last_name, '') || ' (' || v_phone || ')'
            );
        END IF;
    END LOOP;
END;
$$;


-- 5. Procedure: delete data from table by username or phone
CREATE OR REPLACE PROCEDURE delete_contact(p_target VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_target
       OR last_name = p_target
       OR phone = p_target;
END;
$$;
