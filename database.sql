CREATE DATABASE camara;
USE camara;

CREATE TABLE headers(
    header_id INTEGER PRIMARY KEY,
    header_name VARCHAR(256)
);

CREATE TABLE roles(
    role_id INTEGER PRIMARY KEY,
    role VARCHAR(256)
);

CREATE TABLE salary_data(
    salary_data_id INTEGER PRIMARY KEY,
    base NUMERIC,
    career NUMERIC,
    gratification NUMERIC,
    benefits NUMERIC,
    allowance NUMERIC,
    advace_money NUMERIC,
    vacation NUMERIC,
    thirteen_first_salary NUMERIC,
    rebate NUMERIC,
    discounts NUMERIC,
    gross_salary NUMERIC,
    net_salary NUMERIC
);

CREATE TABLE public_servant(
    public_servant_id INTEGER PRIMARY KEY,
    role_id INTEGER REFERENCES roles (roles_id),
    salary_data_id INTEGER REFERENCES salary_data (salary_data_id),
    name VARCHAR(256)
);