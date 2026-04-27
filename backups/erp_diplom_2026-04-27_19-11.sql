--
-- PostgreSQL database dump
--

\restrict nHhbtmcM6VgTEqnMqDpWTNs1PPyMqVggNq5OOji5OdaTLf8OeU7BLx98mILVvc2

-- Dumped from database version 18.3 (Debian 18.3-1.pgdg13+1)
-- Dumped by pg_dump version 18.3 (Debian 18.3-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: accounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accounts (
    id integer NOT NULL,
    code character varying,
    name character varying,
    type character varying
);


ALTER TABLE public.accounts OWNER TO postgres;

--
-- Name: accounts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.accounts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.accounts_id_seq OWNER TO postgres;

--
-- Name: accounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.accounts_id_seq OWNED BY public.accounts.id;


--
-- Name: entry_lines; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.entry_lines (
    id integer NOT NULL,
    account_id integer,
    debit integer,
    credit integer
);


ALTER TABLE public.entry_lines OWNER TO postgres;

--
-- Name: entry_lines_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.entry_lines_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.entry_lines_id_seq OWNER TO postgres;

--
-- Name: entry_lines_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.entry_lines_id_seq OWNED BY public.entry_lines.id;


--
-- Name: journal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.journal (
    id integer NOT NULL,
    date date NOT NULL,
    operation text NOT NULL,
    status text NOT NULL,
    amount numeric
);


ALTER TABLE public.journal OWNER TO postgres;

--
-- Name: journal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.journal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.journal_id_seq OWNER TO postgres;

--
-- Name: journal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.journal_id_seq OWNED BY public.journal.id;


--
-- Name: accounts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts ALTER COLUMN id SET DEFAULT nextval('public.accounts_id_seq'::regclass);


--
-- Name: entry_lines id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.entry_lines ALTER COLUMN id SET DEFAULT nextval('public.entry_lines_id_seq'::regclass);


--
-- Name: journal id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.journal ALTER COLUMN id SET DEFAULT nextval('public.journal_id_seq'::regclass);


--
-- Data for Name: accounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accounts (id, code, name, type) FROM stdin;
1	30	Cash	актив
2	70	Revenue	дохід
\.


--
-- Data for Name: entry_lines; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.entry_lines (id, account_id, debit, credit) FROM stdin;
1	1	100	0
2	2	0	100
3	1	200	0
4	2	0	200
5	1	300	0
6	2	0	300
\.


--
-- Data for Name: journal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.journal (id, date, operation, status, amount) FROM stdin;
1	2026-04-23	Test operation 1	OK	\N
2	2026-04-23	Test operation 2	FAIL	\N
4	2026-04-23	Видалення запису	ERROR	\N
5	2026-04-23	Створення рахунку	SUCCESS	\N
6	2026-04-23	Оновлення проводки	WARNING	\N
7	2026-04-23	Видалення клієнта	ERROR	\N
8	2026-04-27	Cash→Revenue	SUCCESS	100
9	2026-04-27	Cash→Revenue	SUCCESS	200
10	2026-04-27	Cash→Revenue	SUCCESS	300
3	2026-04-23	Оновлення даних	WARNING	50
\.


--
-- Name: accounts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.accounts_id_seq', 2, true);


--
-- Name: entry_lines_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.entry_lines_id_seq', 6, true);


--
-- Name: journal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.journal_id_seq', 10, true);


--
-- Name: accounts accounts_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_code_key UNIQUE (code);


--
-- Name: accounts accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (id);


--
-- Name: entry_lines entry_lines_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.entry_lines
    ADD CONSTRAINT entry_lines_pkey PRIMARY KEY (id);


--
-- Name: journal journal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.journal
    ADD CONSTRAINT journal_pkey PRIMARY KEY (id);


--
-- Name: ix_accounts_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_accounts_id ON public.accounts USING btree (id);


--
-- Name: ix_entry_lines_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_entry_lines_id ON public.entry_lines USING btree (id);


--
-- Name: entry_lines entry_lines_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.entry_lines
    ADD CONSTRAINT entry_lines_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.accounts(id);


--
-- PostgreSQL database dump complete
--

\unrestrict nHhbtmcM6VgTEqnMqDpWTNs1PPyMqVggNq5OOji5OdaTLf8OeU7BLx98mILVvc2

