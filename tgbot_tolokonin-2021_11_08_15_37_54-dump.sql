--
--
--

-- Dumped from database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: adminuser; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.adminuser (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    token character varying(255) NOT NULL
);


ALTER TABLE public.adminuser OWNER TO tgbot;

--
-- Name: adminuser_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.adminuser_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.adminuser_id_seq OWNER TO tgbot;

--
-- Name: adminuser_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.adminuser_id_seq OWNED BY public.adminuser.id;


--
-- Name: answersstatistic; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.answersstatistic (
    id integer NOT NULL,
    tg_user_id integer NOT NULL,
    datetime timestamp without time zone NOT NULL,
    question character varying(255) NOT NULL,
    answer character varying(255)
);


ALTER TABLE public.answersstatistic OWNER TO tgbot;

--
-- Name: answersstatistic_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.answersstatistic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answersstatistic_id_seq OWNER TO tgbot;

--
-- Name: answersstatistic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.answersstatistic_id_seq OWNED BY public.answersstatistic.id;


--
-- Name: commands; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.commands (
    id integer NOT NULL,
    text character varying(255) NOT NULL,
    to_status_id integer,
    answer text NOT NULL
);


ALTER TABLE public.commands OWNER TO tgbot;

--
-- Name: commands_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.commands_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.commands_id_seq OWNER TO tgbot;

--
-- Name: commands_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.commands_id_seq OWNED BY public.commands.id;


--
-- Name: menu; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.menu (
    id integer NOT NULL,
    descr character varying(255) NOT NULL,
    status_id integer
);


ALTER TABLE public.menu OWNER TO tgbot;

--
-- Name: menu_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.menu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.menu_id_seq OWNER TO tgbot;

--
-- Name: menu_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.menu_id_seq OWNED BY public.menu.id;


--
-- Name: menubutton; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.menubutton (
    id integer NOT NULL,
    menu_id integer,
    text character varying(255) NOT NULL,
    to_status_id integer,
    set_action character varying(255),
    answer text NOT NULL
);


ALTER TABLE public.menubutton OWNER TO tgbot;

--
-- Name: menubutton_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.menubutton_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.menubutton_id_seq OWNER TO tgbot;

--
-- Name: menubutton_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.menubutton_id_seq OWNED BY public.menubutton.id;


--
-- Name: migratehistory; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.migratehistory (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    migrated timestamp without time zone NOT NULL
);


ALTER TABLE public.migratehistory OWNER TO tgbot;

--
-- Name: migratehistory_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.migratehistory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.migratehistory_id_seq OWNER TO tgbot;

--
-- Name: migratehistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.migratehistory_id_seq OWNED BY public.migratehistory.id;


--
-- Name: statuses; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.statuses (
    id integer NOT NULL,
    descr character varying(255) NOT NULL,
    action character varying(255)
);


ALTER TABLE public.statuses OWNER TO tgbot;

--
-- Name: statuses_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.statuses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.statuses_id_seq OWNER TO tgbot;

--
-- Name: statuses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.statuses_id_seq OWNED BY public.statuses.id;


--
-- Name: textanswers; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.textanswers (
    id integer NOT NULL,
    answer text NOT NULL,
    question text NOT NULL
);


ALTER TABLE public.textanswers OWNER TO tgbot;

--
-- Name: textanswers_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.textanswers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.textanswers_id_seq OWNER TO tgbot;

--
-- Name: textanswers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.textanswers_id_seq OWNED BY public.textanswers.id;


--
-- Name: tgclient; Type: TABLE; Schema: public; Owner: tgbot
--

CREATE TABLE public.tgclient (
    id integer NOT NULL,
    tg_id integer NOT NULL,
    status_id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    username character varying(255)
);


ALTER TABLE public.tgclient OWNER TO tgbot;

--
-- Name: tgclient_id_seq; Type: SEQUENCE; Schema: public; Owner: tgbot
--

CREATE SEQUENCE public.tgclient_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tgclient_id_seq OWNER TO tgbot;

--
-- Name: tgclient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tgbot
--

ALTER SEQUENCE public.tgclient_id_seq OWNED BY public.tgclient.id;


--
-- Name: adminuser id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.adminuser ALTER COLUMN id SET DEFAULT nextval('public.adminuser_id_seq'::regclass);


--
-- Name: answersstatistic id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.answersstatistic ALTER COLUMN id SET DEFAULT nextval('public.answersstatistic_id_seq'::regclass);


--
-- Name: commands id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.commands ALTER COLUMN id SET DEFAULT nextval('public.commands_id_seq'::regclass);


--
-- Name: menu id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menu ALTER COLUMN id SET DEFAULT nextval('public.menu_id_seq'::regclass);


--
-- Name: menubutton id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menubutton ALTER COLUMN id SET DEFAULT nextval('public.menubutton_id_seq'::regclass);


--
-- Name: migratehistory id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.migratehistory ALTER COLUMN id SET DEFAULT nextval('public.migratehistory_id_seq'::regclass);


--
-- Name: statuses id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.statuses ALTER COLUMN id SET DEFAULT nextval('public.statuses_id_seq'::regclass);


--
-- Name: textanswers id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.textanswers ALTER COLUMN id SET DEFAULT nextval('public.textanswers_id_seq'::regclass);


--
-- Name: tgclient id; Type: DEFAULT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.tgclient ALTER COLUMN id SET DEFAULT nextval('public.tgclient_id_seq'::regclass);


--
-- Data for Name: adminuser; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.adminuser (id, name, email, password, token) FROM stdin;
1	admin	admin@admin.admin	a1866e3ece5cf912e2ed75454fc2eb146983f6befccc6cf76d9a293de52364a07c4d96d058d04cd53d6fdb8e1682c5d828994e4a0327cf28c86d6b052b8cc891f9216f8a69ba7863903b93d85b5395135928450607ba908023404e33d4dec715	9d4b7190-637c-4dbd-90ef-2331b4006753
\.


--
-- Data for Name: answersstatistic; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.answersstatistic (id, tg_user_id, datetime, question, answer) FROM stdin;
13	278565148	2021-08-06 20:56:01.500537	🧘‍ Медитации	\N
14	278565148	2021-08-06 20:56:13.740676	алопеция	Алопеция в психосоматике: сильные переживания за ребенка, конфликт потери привлекательности, самообесценивание
15	278565148	2021-08-06 20:56:27.112961	алопеция	\N
16	318317550	2021-08-12 12:57:35.434316	COVID-19	\N
17	318317550	2021-08-12 12:57:59.490176	миома матки	\N
18	318317550	2021-08-12 12:58:03.315295	👩‍ Психосоматика	\N
19	318317550	2021-08-12 12:58:10.809852	миома матки	чувство стыда с ощущением загрязненности в интимной жизни, в мыслях
20	318317550	2021-08-13 15:30:05.934696	псориаз	Псориаз в психосоматике: шоковый конфликт расставания, нарушение целостности личности, личных границ с желанием вернуть потеряннный контакт с кем-то или восстановить самомнение, подавленная агрессия к другому, вышедшая наружу
21	318317550	2021-08-13 15:30:09.144745	рак	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ
22	318317550	2021-08-13 15:30:15.762716	миома	меня мало как женщины, страх не выносить ребенка , страх перед родами.
23	318317550	2021-08-13 15:30:36.464571	алопеция	Алопеция в психосоматике: сильные переживания за ребенка, конфликт потери привлекательности, самообесценивание
24	431225750	2021-08-26 23:20:15.121449	Мигрень	\N
25	431225750	2021-08-26 23:20:31.449225	Мегрега	\N
26	431225750	2021-08-26 23:20:42.628877	Эндометриоз	\N
27	709688236	2021-08-29 16:27:22.065808	Добрый день	\N
28	454811911	2021-09-14 10:37:33.581733	Температура	\N
29	721679488	2021-09-19 09:21:45.740693	👩‍ Психосоматика	\N
30	498369382	2021-09-30 23:27:57.191143	Зарабатываю мало денег	\N
31	318317550	2021-10-08 12:12:09.657392	рак	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ
32	318317550	2021-10-08 12:12:21.319249	алопеция	Алопеция в психосоматике: сильные переживания за ребенка, конфликт потери привлекательности, самообесценивание
33	119578893	2021-10-08 14:35:44.847678	Анемия	1. недостаток любви, единства в семье \r\n2. конфликт сильного самообесценивания, связанный с предками\r\n#message\r\nhttps://youtu.be/YnfxAAymFBo?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=662
34	119578893	2021-10-08 14:36:28.989574	Анорексия	1. Активный конфликт с матерью, чувство соперничества                                                                                              2. Разногласия, недопонимания с родными людьми
35	318317550	2021-10-10 13:40:46.528471	Рак	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ
36	318317550	2021-10-10 13:41:05.369571	Алопеция	Алопеция в психосоматике: сильные переживания за ребенка, конфликт потери привлекательности, самообесценивание
37	318317550	2021-10-17 11:16:13.706084	БАС	\N
38	119578893	2021-10-22 10:30:38.89935	остеопороз	конфликт самообесценивания - ощущение себя бесполезным, ненужным, потеря опоры личности\r\n#message\r\nhttps://www.youtube.com/watch?v=qawicHJ-lmI&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=214  
39	119578893	2021-10-22 10:30:48.920796	артрит	конфликт сомообесценивания, невыносимые обстоятельства, люди (терпеть не могу кого-то)\r\n#message\r\nhttps://youtu.be/6dcuNFZgjOo
40	119578893	2021-10-22 10:31:07.309822	остеомиелит	Самообесценивание, воздействующее на глубочайшую часть центра кости, связанное с семьей
41	119578893	2021-10-22 10:31:40.191083	рак кости	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ
\.


--
-- Data for Name: commands; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.commands (id, text, to_status_id, answer) FROM stdin;
1	/start	1	Я рад вас видеть! Воспользуйтесь меню для перехода в нужный раздел
\.


--
-- Data for Name: menu; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.menu (id, descr, status_id) FROM stdin;
1	Главное меню	1
\.


--
-- Data for Name: menubutton; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.menubutton (id, menu_id, text, to_status_id, set_action, answer) FROM stdin;
3	1	📹 YouTube	1	\N	Посетите наш YouTube канал! https://www.youtube.com/user/artemtolokonin
6	1	📝 Запись на консультацию	1	\N	Для записи на консультацию, пожалуйста посетите наш сайт: https://tolokonin.com
1	1	👩 ‍Психосоматика	1	listen	Введите вашу проблему, я подскажу как ее решить
5	1	👩‍🎓 Институт психосоматики	1	\N	Посетите наш институт психосоматики: https://psy-university.com/
4	1	📰 Telegram канал	1	\N	Посетите наш телеграм канал!  https://t.me/Tolokonincom
2	1	🧘 Медитации	1	\N	Скачивайте наше приложение для медитаций: \r\n#message\r\nIphone - https://apps.apple.com/ru/app/tolokonin-com/id1451054670\r\n#message\r\nAndroid - https://play.google.com/store/apps/details?id=com.tolokonin
\.


--
-- Data for Name: migratehistory; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.migratehistory (id, name, migrated) FROM stdin;
1	0001_migration_202108041053	2021-08-06 16:47:17.653879
2	0002_migration_202108051139	2021-08-06 16:47:17.657748
3	0003_migration_202108051243	2021-08-06 16:47:17.659149
4	0004_migration_202108131424	2021-08-13 12:28:55.479458
5	0005_migration_202108131435	2021-08-13 12:28:55.490563
6	0006_migration_202108131436	2021-08-13 12:28:55.499413
7	0007_migration_202108131436	2021-08-13 12:28:55.515111
\.


--
-- Data for Name: statuses; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.statuses (id, descr, action) FROM stdin;
1	new_status	listen
\.


--
-- Data for Name: textanswers; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.textanswers (id, answer, question) FROM stdin;
82	поиск решения неразрешенного конфликта, который не дает покоя даже ночью. \r\n#message\r\nhttps://youtu.be/9YR4wh6zF_I?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=550	Нарушение сна - инсомния
95	1. обиды на мать, ощущение тяжелой женской доли, унаследование тяжести жизни от матери,  груза ответственности \r\n2. ощущение брошенности и одиночества\r\n3. ограничение личной свободы \r\n#message \r\nhttps://youtu.be/nRXDrHUbEQA?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=90    \r\n#message                                         \r\nhttps://www.youtube.com/watch?v=u0wYuCiexOo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=225 \r\n\r\n	Варикозное расширение вен (варикоз)
107	1. страх непреднамеренной беременности, страх не выносить плод, чувство сожаления об отстутствии гармоничных отношений с мужчиной                                                                                                                                                           2. огромное желание забеременеть кем-то из предков без реализации желаемого\r\n#message \r\nhttps://www.youtube.com/watch?v=z8g4PIlpVMQ	Менструальная боль (менструальный дискомфорт, предменструальный синдром)
120	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества, воспоминания об утонувших в роду\r\n	Острая почечная недостаточность, острый некротический нефроз (острая тубулопатия)
133	отсутствие следования предназначению, внутреннему призванию, ощущение бессмысленности жизни	Синдром эмоционального выгорания
145	1. Двойной конфликт, связанный с некрасивой ситуацией плюс конфликт страха нехватки и беспомощности                                                                           2.Невозможность переварить (принять) что-либо - часто с аспетком голода (прибыль, на которую покупается еда)\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Болезнь Крона
157	конфликт самообесценивания - ощущение себя некрасивым   «Моя часть\r\nтела подвергается насмешкам, я не считаю себя красивым».\r\n#message \r\nhttps://www.youtube.com/watch?v=VXmo3WiwiGo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=247	Опухоль жировой ткани (жировик, липома, фиброма)
170	Конфликт искажения реальности - Я отказываюсь видеть реальность такой, какая она есть. \r\n#message\r\nhttps://www.youtube.com/watch?v=OFmzQnZcee0&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=93 	Астигматизм (искривление роговицы)
182	1. Конфликт самообесценивания с локализацией \r\n•        Кости черепа, шейный отдел позвоночника, шея - моральное или интеллектуальное самообесценивание - ощущение несправедливости, угнетения, борьбы.\r\n•        Глазницы (орбиты) - конфликт самообесценивания в отношении своих глаз\r\n•        Верхняя и нижняя челюсти - конфликт самообесценивания с содержанием """"не могу удержать ситуацию""""\r\n•        Плечи - общий конфликт взаимоотношений, неспособности обнять или поддержать кого-то - подставить плечо\r\n•        Локти - конфликт неспособности кого-то обнять, удержать, бросить. Неудовлетворенное честолюбие\r\n•        Руки и пальцы - отсутствие веры в то, что человек что-либо неправильно делает или делает недостаточно активно. \r\n•        Грудной отдел позвоночника - ощущение себя униженным, конфликт неполучения чего-либо - должности, знаний, полномочий \r\n•        Грудина, ребра - локальный конфликт самообесценивания, например, после мастэктомии\r\n•        Поясничный отдел позвоночника - потеря уверенности в себе и своих действиях, заниженная самооценка\r\n•        Копчик - локальный конфликт с сексуальным содержанием - чувство неуверенности в постели\r\n•        Лобковая кость - локальный конфликт с сексуальным содержанием - чувство неуверенности в постели, ощущение фригидности, проблемы с потенцией, отсутствие достаточного сексуального опыта\r\n•        Тазовые кости - локальный конфликт с сексуальным содержанием - чувство неуверенности в постели\r\n•        Седалищная кость - общий конфликт неспособности обладать чем-то \r\n•        Бедренная кость и шейка бедра - невозможность продолжать делать что-либо или управлять чем-то\r\n•        Колени - конфликт отсутствия признания, неудовлетворенного честолюбия. \r\n•        Лодыжки, стопы, пальцы ног - ощущение невозможности удержаться на ногах, на каком-либо месте\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим	Подагра
194	Невозможность бороться, спорить, удерживать ситуацию под контролем, обладать удерживать что-то \r\n#message\r\nhttps://www.youtube.com/watch?v=H_f-zf-QOKM 	Выпадение зубов
23	все надо успеть, но нет уже сил. 	гипотиреоз
83	1. конфликт разделения - потеря отношений с родным человеком / потеря уважения                                                2. конфликт самообесценивания - низкий уровень энергии и самооценки/ наличие крайне нежелательного общения\r\n#message \r\nhttps://youtu.be/D_W86MWEACw?t=459 \r\n	Невралгия тройничного нерва
96	1. семейные конфликты, проблемы с кровными родственниками;                                                                           2. нежелание возвращаться домой - “я торможу возвращение крови к сердцу по венам”;                                                 3. тональность предыдущего конфликта: “дома мама, она меня не любит,  я не хочу домой”;                                                    4.слишком большая ответственность - тяжелый груз - тяжесть и застой крови в ногах;                                                   5. "ядро на цепи” - человек ощущает ограничения личной свободы, “оковы”, тяготится чем-то или кем-то в своей жизни (дети как помеха свободе) ;                                           6. желание богатства, но не свободного и честного (радостного), а в виде накопительства, жадности, скряжничества - застой крови в ногах;                                                             7. самообесценивание женщины - она считает себя жертвой, недостойной, в сравнении с другими в семье;                                                                           8. “грязь” в семье - венозная кровь как использованная, “грязная кровь” вмещает в себя психологическое напряжение от того, что в семье “нечисто”.	Тромбоз
108	1. конфликт угрозы существования - ""все потеряно"" - страх потерять все - имущество, состояние;    2.психологическая неготовность принятия беременности и ребенка\r\n3. отсутствие перспектив, неуверенности в завтрашнем дне\r\n4. глубокие конфликты отвержения/брошенности - чувство изоляции, полного одиночества \r\n#message \r\nhttps://www.instagram.com/p/Bx9COjqlize/?utm_source=ig_web_copy_link \r\n	Токсикозы при беременности 
121	1. территориальный конфликт - неожиданное вторжение в личные границы человека - ""мои границы нарушены, потому что я их четко не обозначил""\r\n2. конфликт борьбы за выживание\r\n#message \r\nhttps://youtu.be/SQag5uK5YJU?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Камни в почках (мочекаменная болезнь), песок в почках
134	1. конфликт, связанный с потерей территории (работа, дом, семья) \r\n2. конфликт, связанный с обозначением личных границ \r\n3. конфликт, связанный с повторяющимися спорами, разногласиями, ссорами с кем-либо\r\n4. конфликт самообесценивания - низкая самооценка, чувство вины. Зависание на негативном впечатлении. \r\n#message \r\nhttps://www.youtube.com/watch?v=0EDBP76sfAY&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=22              \r\n#message \r\nhttps://www.youtube.com/watch?v=LAG5LkZYLAA&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=220 	Депрессия
146	1. конфликт неперевариваемого гнева - тяжелая ситуация, с которой трудно справиться\r\n2. конфликт, связанный с членами семьи и разделом общего имущества или наследства\r\n3. конфликт нарушения личных границ человека\r\n#message \r\nhttps://www.youtube.com/watch?v=zxjZWytix_o&list=PLvvQng9TolQPhSKiN9ty1Fp0XQXiEasDI&index=9 	Метеоризм (вздутие кишечника)
158	конфликт разделения, связанный с непониманием аргументов и мотивов - человек не понимает чужих доводов\r\n#message \r\nhttps://www.youtube.com/watch?v=UYMiRrl4Rig&list=PLvvQng9TolQN16eiuK4Ef8WckwQrL5HYj&index=15  \r\n#message \r\n https://www.youtube.com/watch?v=OFgcKox7Ed8&list=PLvvQng9TolQN16eiuK4Ef8WckwQrL5HYj&index=16 	Перхоть, облысение, частичное выпадение волос
171	Страх за раскрытие семейной тайны, которая не должна быть услышана.\r\n#message\r\nhttps://www.youtube.com/watch?v=D_W86MWEACw&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=52&t=613s 	Тугоухость
183	\r\n1. общий конфликт самообесценивания - чувство сломленности, унижения, самообесценивание из-за сравнения\r\nсебя с другими\r\n2. локальный конфликт самообесценивания - чувство, что что-то не так в отношении моей груди/грудной клетки\r\n#message\r\nhttps://www.youtube.com/watch?v=N1x2zgNKUv0&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=67&t=1134s \r\n	Боковое искривление позвоночника (сколиоз)
195	невозможность высказаться - «Я должен держать рот на замке», сдерживаемый внутри гнев	Скрежет зубама (бруксизм)
84	"страх быть обездвиженным / отсутствие возможности или желания двигаться по жизни                                                                                                                                                                 Локализация\r\n•        Лицевая мускулатура: оказаться в дураках / стать посмешищем \r\n•        Мышцы плечевого пояса и спины: невозможность уклониться от кого-то или чего-то \r\n•        Сгибатели рук и ног: невозможность удержать, обнять, приблизить к себе кого-нибудь или что-нибудь \r\n•        Разгибатели рук и ног: невозможность избавиться, защититься, оттолкнуть что-либо или кого-либо\r\n•        Ноги: не найти выхода из создавшегося положения. Невозможность уйти, избежать чего-нибудь, успеть что-либо\r\n"	Инсульт
97	1. потеря или страх потери любимых людей (ребенок, супруг, родитель, друг) из-за смерти, ухода, переезда, пропажи. \r\n2. возвращение мыслями к болезненному прошлому \r\n3. потеря чувства сексуальности, проблемы с детьми\r\n#message \r\nhttps://youtu.be/alUSAFKzwv4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Киста яичника
109	нежелание рожать, неготовность к материнству, конфликт между родителями.  Страх, что плод не сможет быть точным повторением ребенка, который умер ранее\r\n#message \r\nhttps://youtu.be/iySEV0yQDro?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Выкидыш, преждевременные роды
122	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ\r\n	Рак мочевого пузыря
135	1. душевный и эмоциональный конфликт, случившийся в глубоком детстве: мысли матери об аборте, конфликтные отношения с партнером во время беременности, тяжелые роды                                                                                                     2. психологические травмы, полученные кем-то из предков в роду\r\n#message \r\nhttps://youtu.be/edB--oPhFGU?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG	Панические атаки
147	1. Конфликт нехватки, «недостатка чего-то жизненно важного»: страх за свое существование, страх, что еды может быть слишком мало\r\n2. Скопление внутри гнева и агрессии с невозможностью ее проявления	Рак печени 
159	1. Наличие резкой неприятной ситуации связанной с аспектом семейного (родового) содержания                                                   2. Конфликт, связанный с потерей сверхъестественных способностей                                                                                           3. Конфликт с уверенной конкретной силой - ощущение потери уверенности, защищенности 	Седые волосы
172	1. конфликт падения в прямом смысле - с лестницы, на скользской поверхности                                                          2. потеря внутреннего равновесия - отсутствие поддержки, уход почвы из под ног\r\n3. конфликт самобесценивания - Я волнуюсь о будущем\r\n	Болезнь Меньера
184	1. общий конфликт самообесценивания - ощущение себя выбившимся из сил, не способным выдержать большого напряжения, большое содержание стресса, невозможность выдержать давление обстоятельств или людей, невозможность устоять всем телом\r\n2. локальный конфликт самообесценивания часто с сексуальным содержанием - ""в постели я недостаточно хорош""\r\n#message\r\nhttps://www.youtube.com/watch?v=AzY24Pj57fQ  	Грыжа, протрузия, выпадение (пролапс) межпозвонкового диска поясничного отдела позвоночника
196	1. двигательный конфликт - запрет или невозможность говорить\r\n2. конфликт самообесценивания - ""я не могу говорить хорошо""\r\n3. конфликт смертельного испуга \r\n#message\r\nhttps://www.youtube.com/watch?v=E8AqbzXmm34&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=100 	Заикание
47	обиды на партнера "он меня больно ранит", осознание себя нежеланной \r\n#message\r\nhttps://youtu.be/P6BrVVyYJIo?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=2250\r\n#message\r\nhttps://www.youtube.com/watch?v=jhJxPR43DX8&t=189s 	Эрозия шейки матки
54	самоосуждение себя за интимную жизнь, страх перед сексом.	Вагинальный спазм (вагинизм)
85	1. конфликт потери необходимого контакта , связи с близким и родным человеком\r\n2. крайне нежелательное общение с кем-либо	Нейродермит
98	1. боль от измены, боль от факта рождения ребенка на стороне у партнера \r\n2. конфликт нежелательной беременности после аборта, самоосуждение за аборт\r\n3. психологический запрет на рождение ребенка во имя самореализации\r\n#message \r\nhttps://youtu.be/alUSAFKzwv4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Эндометриоз
110	самоосуждение себя за интимную жизнь, страх перед сексом.	Вагинальный спазм (вагинизм)
123	1. территориальный конфликт - потеря личного пространства (квартира, работа - "меня выживают")         2. у женщин - раздражение по поводу полового партнера\r\n#message \r\nhttps://www.youtube.com/watch?v=Y8t7hCtFo14&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=197	Цистит
136	Подавленное чувство угрозы жизни человека (выкидыш, мысли об аборте) в период беременности матери	Аэрофобия
148	Скопление внутри гнева и агрессии с невозможностью ее проявления	Жировой гепатоз (ожирение печени)
160	конфликт смертельной угрозы, конфликт смертельной опасности, смертельный испуг, страх близкой смерти\r\n#message \r\nhttps://youtu.be/NVjnwTPPOFU?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Рак легких
173	1. Конфликт дурного запаха, желание решить затянувшуюся ситуацию                                                                                             2. Конфликт проблемы или\r\nсложности, которую человек хочет отогнать.  \r\n#message\r\nhttps://www.youtube.com/watch?v=1s0bvyhN7po&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=56&t=7s \r\n3. Негативное ожидание проблем.\r\n4. Неспособность переносить запах других (вторжение в личную территорию человека).\r\n	Насморк (ринит), воспаление пазух (синусит)
185	1. конфликт, связанный с сексуальными отношениями, конфликт деторождения - тяжелые роды, невозможность родить\r\n2. локальный конфликт самообесценивания по отношению к этой части тела - у меня слишком широкие/узкие бедра 	Артроз тазобедренного сустава (коксартроз)
197	1. тревога, заедание стресса, жизнь по принципу ""хорошего человека должно быть много"", желание казаться весомым, значимым, уметь отстоять свое мнение, защитить себя и близких\r\n2. ощущение медлительности\r\n3. конфликт, связанный с попаданием на ложный путь\r\n#message\r\nhttps://www.youtube.com/watch?v=Mf82Iu76WKs&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=42  \r\n#message\r\nhttps://www.youtube.com/watch?v=N1x2zgNKUv0&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=67&t=1134s 	Избыточный вес, ожирение
86	у мужчин -  конфликт потери территории: потеря дома, работы, должности и т.д. \r\nу женщин - конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми.	Боль в груди - стенокардия
99	конфликт тяжелой утраты - фактическая потеря (утрата) очень близкого человека или людей (ребенка, любимого человека или животного), потеря собственного дела, которое воспринималось как дитя. \r\n	Рак яичника
111	сильный конфликт утраты - потеря или страх потери любимых людей (ребенок, супруга, родитель, любимое животное) из-за смерти, ухода, переезда. 	Рак яичника
124	1. компенсация тревоги взаимоотношений в семье, способ заявить о себе                                                                \r\n2. конфликт, связанный с отцом - отца нет или он очень властный и ребенок его боится \r\n3. желание вернуться в утробу матери и быть защищенным\r\n#message \r\nhttps://youtu.be/NkcYbDnAh6M?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Недержание мочи у детей
137	неосознанное желание трансформировать свою жизнь, страх сделать выбор, способного повлиять на будущее\r\nСимптомы:\r\n•        кашель - отсутствие реализации желаемого, болезненное реагирование на неразрешенную ситуацию \r\n•        бронхит - нарушение личных границ человека, постоянное раздражение на окружающий мир\r\n•        пневмония - страх смерти, ощущение глубоких потрясений, угрожающих жизни\r\n•        потеря обоняния - пребывание в дурнопахнущей, неприятной ситуации, оставившей отпечаток на психике.\r\n#message \r\nhttps://www.instagram.com/tv/CQej_aMIXix/?utm_source=ig_web_copy_link   \r\n#message \r\nhttps://www.instagram.com/tv/CQoxqmTokKV/?utm_source=ig_web_copy_link https://www.youtube.com/watch?v=66KlO-Moop8 	COVID-19, коронавирус
149	1. конфликт территориального гнева -  нарушение личных границ человека,                                                                   2. конфликт, связанный с принятием решения "Не знаю, какое решение принять"                                                             3. Страх недостатка чего-либо - еды, денег и т.д	Гепатит, острая печеночная недостаточность, печеночная энцефалопатия
1	Псориаз в психосоматике: шоковый конфликт расставания, нарушение целостности личности, личных границ с желанием вернуть потеряннный контакт с кем-то или восстановить самомнение, подавленная агрессия к другому, вышедшая наружу	псориаз
2	Алопеция в психосоматике: сильные переживания за ребенка, конфликт потери привлекательности, самообесценивание	алопеция
3	меня мало как женщины, страх не выносить ребенка , страх перед родами.	миома матки
4	нежелание иметь детей, переживание измены 	эндометриоз
5	 нежелание полового контакта, способ его избегания	молочница
6	сильное раздражение(он меня изьязвляет) на полового партнера бывшего, существующего сейчас или возможного в будущем	эрозия шейки матки
7	ощущение себя "загнанной лошадью", все надо успеть!	гипертиреоз
8	интеллектуальный конфликт, я не понимаю почему так складывается ситуация или почему так поступают другие люди	мигрень
9	правой - не смогла удержать партнера, переживания по поводу измены; левой переживания о ребенке.	рак груди
10	я непереварию что-то или кого-то , притензии к себе( себя не перевариваю)	гастрит
161	конфликт страха смерти: «Это не дает мне дышать, высасывает из меня воздух», «У меня нет выхода!»\r\n	Саркоидоз легких
174	1. конфликт дурного запаха, желание решить затянувшуюся ситуацию \r\n2. конфликт чутья - желание учуять опасность, почуять перспективу \r\n3. пребывание в дурнопахнущей, неприятной ситуации, оставившей отпечаток на психике.\r\n#message\r\nhttps://www.youtube.com/watch?v=K3mn2h2Hjf4&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=6 	Снижение или потеря обоняния 
186	1. общий конфликт самообесценивания, связанный со спортивными достижениями, с отсутствием признания, неудовлетворенного самолюбия. \r\n2. локальный конфликт самообесценивания с содержанием ""не могу бегать, прыгать, пинать быстро, сильно""                                                                                                                 3. страх за будущее детей, родных, ощущение вины за свои неудачи и неудачи своих детей	Боль в колене, воспаление коленного сустава (артрит), воспаление суставной сумки коленного сустава (бурсит)
87	1. сильный конфликт самообесценивания\r\n2. у мужчин чувство потери территории: потеря дома, работы, должности и т.д. \r\nу женщин конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми	Инфаркт миокарда
100	1. огромное желание забеременеть без возможности сделать это\r\n2.огромное желание самореализации у женщины и осуждение этого со стороны окружающих.\r\n#message \r\nhttps://www.youtube.com/watch?v=B3j-j8PAWwE&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=188	Синдром поликистозных яичников (СПКЯ, поликистоз или склерокистоз яичников)
112	боязнь оказаться не на высоте во время интимных отношений, страх расстаться с кем-либо или чем-либо	Гидроцеле (водянка яичка) 
125	1. Запрет восприятия реальности, происходящих событий - "мне не позволено видеть мир таким какой он есть"                                                          2. часто в фазе программирования или семейном дереве, конфликт, при котором реальность воспринимается очень болезненно, шоковые события в роду.\r\n#message \r\nhttps://www.youtube.com/watch?v=dDW1OJdW3Gc             #message \r\nhttps://www.youtube.com/watch?v=HnXO9TAqShs&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=200 	Шизофрения
138	1. конфликт невысказанности, желание избавиться от кого-то или чего-то, неспособность получить желаемое                                                2.желание получить внимание и любовь от матери\r\n#message \r\nhttps://www.youtube.com/watch?v=zq1vwJ36VQc&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=84 	Тонзиллит 
150	1.Конфликт с семьей.                                                                             2.Конфликт из-за денег                                                                             3.Конфликт в отношении нехватки (чего угодно, чего может не хватать).\r\n4. Страх умереть от серьезного заболевания кишечника	Цирроз печени
162	1. Рак молочных желез - аденокарцинома\r\nДрама в семье. Конфликт материнства - чрезмерные переживания за родных\r\n2. Рак молочных протоков\r\nКонфликт разделения в семье, недостаток общения, неспособность выражать собственную любовь.\r\n3. Рак кожи груди - конфликт потери или запятнанности собственной чистоты внутри семьи                                            4. Нейрофиброматоз груди\r\n*Конфликт контакта - контакт навязывается и воспринимается как неприятный, нежеланный, болезненный.\r\n*Конфликт желания расставания внутри семьи, желание прекратить контакт\r\n*Человек хочет расстаться, но не может. Например, мужчина настаивает, а женщина\r\nбольше не желает этого контакта.\r\n#message\r\nhttps://youtu.be/FRuoH4IyvJg?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG \r\n	Рак груди
175	ломота в теле = конфликт самообесценивания - низкий уровень энергии, снижение самооценки\r\nнасморк = конфликт дурного запаха (желание решить затянувшуюся ситуацию) или ""чутья"" (желание учуять опасность, почуять перспективу )\r\nвоспаление горла = конфликт ""не хочу это принимать""\r\nларингит = конфликт сильного страха/испуга\r\n	Грипп
187	1. конфликт потери территории - потеря дома, работы, должности                                                                                2. конфликт разделения - потеря отношений с родным человеком / потеря уважения	Эпилесия
198	1. конфликт, связанный с партнером\r\n2. обесценивание, связанное с будущим\r\n3. ощущение движения, развития не в ту сторону\r\n4. желание сбежать из-за неспособности что-либо сделать\r\n#message\r\nhttps://www.youtube.com/watch?v=vx1xJX5ADjc&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=45 \r\n#message\r\nhttps://www.youtube.com/watch?v=E8AqbzXmm34&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=100 	БАС
17	стыд , страх близких доверительных отношений. 	акне
88	конфликт самообесценивания, связанный с сердцем - страх, что с сердцем что-то не так, вера в то, что сердце недостаточно сильное.	Сужение митрального клапана
101	1. сексуальный конфликт, связанный с мужчиной: конфликт женственности - ощущение, что ""мной как женщиной пренебрегают, я оскорблена""\r\n2. ощущение запятнанной сексуальной репутации - что скажут люди?\r\n3. Эмоциональный конфликт между бабушкой и внучкой, между мамой и дочерью.\r\n	Воспаление маточных труб 
113	отчаянье мужчины по причине неспособности стать хорошим родителем, неуверенность в себе как в мужчине	Аденома простаты
126	эмоциональная травма, полученная в раннем детстве из-за конфликта родителей - чувство брошенности, расставания, нежелания жить \r\n#message \r\nhttps://youtu.be/LWMbcVOAmkc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Суицидальные наклонности, постоянные мысли о смерти и о "жизни после смерти"
139	невозможность проглотить (принять) что-либо очень нужное / желание предотвратить проглатывание (принятие) чего-либо опасного\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Рак пищевода (карцинома)
151	конфликт борьбы, страх нападения, переход организма в режим "боевой готовности" -  быть готовым к битве, к сражению\r\n#message \r\nhttps://www.youtube.com/watch?v=ls3Pc3S_NmU&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=19 	сахарный диабет 1 тип 
163	чрезмерная материнская забота, желание защитить, взваливание на себя чрезмерной ответственности.\r\n\r\n	Мастопатия
176	конфликт самообесценивания - ощущение себя бесполезным, ненужным, потеря опоры личности\r\n#message\r\nhttps://www.youtube.com/watch?v=qawicHJ-lmI&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=214  	Потеря костной массы (остеопороз)
188	1. общий двигательный конфликт - конфликт страха, блокирующего движение. Конфликт невозможности движения (не имею права, не хочу или не могу двигаться)  Страх быть парализованным, потрерять дар речи. \r\n2. локальный двигательный конфликт - конфликт невозможности избежать кого-то или чего-то\r\nневозможность удержать, использовать, обнять \r\nневозможность оттолкнуть, отодвинуть\r\nневозможность уйти, убежать, разрешить ситуацию 	Синдром беспокойных ног (болезнь Виллиса-Экбома)
89	1. страх, что с сердцем что-то не так, вера в то, что сердце недостаточно сильное                                                   2. ощущение угнетенности, сильное нежелание выполнять обязанности на работе, по дому и т.д.                                                                                   3. тревога за свое будущее, тревога за личную жизнь\r\n#message \r\nhttps://youtu.be/6uztRhy0Elc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=314	Аритмия
102	1. конфликт невозможности забеременеть из-за отсутствия или невозможности полового контакта\r\n2. женский конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, осознание себя нежеланной, проблемы с детьми, \r\n3. сексуальный конфликт разделения - измена, расставание с партнером\r\n	Рак шейки матки 
114	1. сильный конфликт неощущениея себя мужественным, потеря собственной значимости как мужчины, самообесценивание \r\n2. беспокойство за потомство - дети, внуки \r\n3. неудовлетворение семейной жизнью	Рак простаты
127	территориальный конфликт:\r\nу мужчин -  конфликт потери территории: потеря дома, работы, должности и т.д. \r\nу женщин -  конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми\r\n\r\n	Клаустрофобия
140	невозможность проглотить (принять) что-либо очень нужное / желание предотвратить проглатывание (принятие) чего-либо опасного\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Воспаление пищевода (эзофагит)
152	конфликт сопротивления, нежелание делать что-то, защита от кого-то или чего-то, конфликт между человеком и его семьей\r\n#message \r\nhttps://www.youtube.com/watch?v=dceHvp2Cw8Y&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=94	сахарный диабет 2 тип
164	конфликт самообесценивания - потеря ощущения женственности, мысли о недостаточной заботе о ребенке	Рак лимфоузлов (лимфома, болезнь Ходжкина, аденомапатия)
177	1. Конфликт самообесценивания - ощущение страха неудач детей в будущем \r\n2. Борьба, бой, отказ принятия ситуации\r\n3. Ощущение чувства вины за неудачи в жизни детей и близких                                                                                      4. конфликт тотальной непереносимости, непринятие друг друга в роду - ревматоидный артрит\r\n#message\r\nhttps://www.youtube.com/watch?v=qdoIdVbeRdE&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=137 \r\n#message\r\nhttps://www.youtube.com/watch?v=wknH1RMSFkY&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=246  \r\n	Воспаление суставов (артрит)
189	1. общий конфликт самообесценивания с самоощущением ""не могу стоять/устоять"" в какой-либо ситуации, желание уйти из слоившейся ситуации\r\n2. локальный конфликт самообесценивания - ощущение невозможности хорошо бегать, прыгать, пинать, удерживать равновесие\r\nощущение неловкости во время работы \r\n	Растяжение и разрыв мышц
90	1. недостаток любви, единства в семье \r\n2. конфликт сильного самообесценивания, связанный с предками\r\n#message \r\nhttps://youtu.be/YnfxAAymFBo?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Анемия
103	обиды на партнера "он меня больно ранит", осознание себя нежеланной \r\n#message \r\n1. https://youtu.be/P6BrVVyYJIo?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG\r\n#message                                           \r\n2. https://www.youtube.com/watch?v=jhJxPR43DX8&t=189s 	Эрозия шейки матки
115	1. конфликт самообесценивания - снижение самооценки, низкий уровень энергии, переживания по поводу потери детей в роду                                                                               \r\n2. психологический запрет на возможность иметь детей, связанный с конкурентным воспитанием (в моем стаде я не альфа самец)\r\n#message \r\nhttps://youtu.be/iX3-aeZzMU4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG \r\n#message                                    \r\nhttps://www.youtube.com/watch?v=4-ai6nLG01A&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=187    \r\n#message            \r\nhttps://www.youtube.com/watch?v=47qzgFDk55k&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=198	Мужское бесплодие
128	страх осуждения, невозможность занять свое место в жизни\r\n#message \r\nhttps://www.youtube.com/watch?v=Spuh4jkdkM0	Агорафобия
141	неспособность переварить недавнюю сильную конфликтную ситуацию\r\n#message \r\nhttps://www.youtube.com/watch?v=OFgcKox7Ed8&list=PLvvQng9TolQN16eiuK4Ef8WckwQrL5HYj&index=16 	Рак желудка
153	Локализация:                                                                                                      •        тыльная сторона руки - конфликт с письмом (трудности с письмом в школе) \r\n•        на шее - человека брали за горло, неприятность прикосновений \r\n•        на носу - ощущение стыда за своего отца \r\n•        подошвы - конфликт спортивных достижений \r\n•        лобок - чувство стыда за эту часть тела\r\n          	Бородавки, базалиома
165	1. конфликт невозможности смотреть в нужном направлении\r\n2. невозможно избежать ситуации, когда на кого-то или что-то невозможно больше смотреть\r\n3. желание найти глазами ушедшего человека или закончившуюся ситуацию\r\n	Косоглазие
178	Самообесценивание, воздействующее на глубочайшую часть центра кости, связанное с семьей	Воспаление костного мозга (остеомиелит)
190	1. двигательный конфликт - запрет или невозможность движения\r\n2. конфликт самообесценивания - низкий уровень энергии	Атрофия мышц
91	сильный конфликт самообесценивания, часто переданный по роду. У детей лейкемия выражается конфликтом «Я несу в себе недостаток самооценки своих родителей».\r\n#message \r\nhttps://youtu.be/G96o7Sg7Ju8?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG \r\n	Лейкемия
104	1. ощущение одиночества, отсутствия востребованности на работе, в семье, страх за будущее, неосознанное нежелание человека жить                                                                                                                                                                                                2.сильный конфликт с существующим или воображаемым партнером	Рак матки
116	недостаток качества сексуального контакта - "я расстроена, что не могу получить то, что хочу"	Половой герпес
129	1. Активный конфликт с матерью, чувство соперничества                                                                                              2. Разногласия, недопонимания с родными людьми	Анорексия 
142	1. Регулярное повторение неприятной ситуации, которая не соответствует образу жизни человека. Желание выплеснуть то, что не нравится, но без выполнения действий.                                                                                  2. Желание наладить контакт с матерью, услышать от нее хорошие слова\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Изжога
154	1. конфликт обезображенности, конфликт ощущения словесной грязи, насилие против чистоты - неприкосновенности, нарушение личных границ                    2. конфликт чего-то, что было оторвано. Потеря физической целостности (например, ампутация)\r\n#message \r\nhttps://www.youtube.com/watch?v=VXmo3WiwiGo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=247	Рак кожи 
166	конфликт визуального разделения. Кто-то очень нужный был потерян из виду. \r\n#message\r\nhttps://www.youtube.com/watch?v=QSGQohf14G4&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=121 	Помутнение хрусталика - катаракта
179	Сильное самообесценивание, воздействующее на глубочайшую часть центра кости, связанное с семьей	Рак костного мозга
191	1. отказ матери от будущего ребенка, мысли об аборте                                2. конфликт между принятием божественного начала и его отрицанием	Миастения
92	накопление и удержание эмоциональных проблем, неразрешение конфликтов, проблема гиперконтроля\r\n#message \r\nhttps://youtu.be/n75EZtbReDc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG \r\n#message \r\n https://www.youtube.com/watch?v=PohsywNCw-c&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=228 	Высокое кровяное давление - гипертония
105	чувство стыда с ощущением загрязненности в интимной жизни, в мыслях	Генитальные бородавки (кондиломы) шейки матки
117	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества\r\n	Рак почек
130	страх голода, недостатка пищи, недостаток чего-то необходимого, страх быть брошенным	Булимия 
143	1. конфликт территориального гнева - нарушение личных границ человека                                                                     2.конфликт, связанный с принятием решения "Не знаю, какое решение принять"                                                      3. Конфликт нехватки желаемого, неспособности переварить то, что уже есть.\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Язва двенадцатиперстной кишки
155	1. Конфликт расставания с кем-то дорогим или кем-то, кем вы восхищались\r\n2. Желание обелить себя, снять с себя бремя вины, смыть что-то с себя.\r\n3. Желание очистить себя от чего-то, от невыносимой ситуации, от того, что вы сказали или сделали\r\n4. Некрасивая или жесткая ситуация расставания с любимым или кем-то, кем вы восхищались\r\n#message \r\nhttps://www.youtube.com/watch?v=xFeOzMWp7Jw&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=89 \r\n#message \r\n https://www.youtube.com/watch?v=iHKQ6Uvyclo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=101 	Витилиго (болезнь белых пятен), нарушение пигментации
167	1. Сильное беспокойство насчет ближайшего будущего                                                                               2. Желание вникать во все быстрее, быть в центре событий    	Глаукома
180	конфликт снижения самооценки: «я задет до самой своей сути», «я\r\nни к чему не годен, я ничто, я полностью бесполезен», «я чувствую это обесценение, эту бесполезность, даже если другие так не думают обо\r\nмне»	Рак кости 
192	конфликт невозможности "укусить": невозможность бороться, спорить, удерживать ситуацию под контролем, обладать удерживать что-то \r\n#message\r\nhttps://www.youtube.com/watch?v=jHD353zrOWQ&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=69 	Кариес 
21	не могу переварить "дерьмовую" ситуацию, сильная подавленная злость	рак толстого кишечника
93	1. конфликт самообесценивания - "моя жизнь недостаточно хороша"                                                                         \r\n 2. ощущение беспомощности в отношении поврежденной части тела	Атеросклероз
106	неприятие собственной женственности, негармоничные отношения с мамой	Чрезмерное менструальное кровотечение
118	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества\r\n4. страх принятия чего-то нового - проявление упорства в своих убеждениях «Я не верю, что положение может улучшиться, я держусь за старое».	Гломерулонефрит
131	конфликт страха или опасений за будущее в целом - «Что со мной будет?» 	Мания преследования (паранойя), зрительные галлюцинации
144	1. сильный конфликт - не могу переварить (принять) что-либо                                                                                     2. Конфликт нехватки желаемого + несправедливость.\r\n#message \r\nhttps://www.youtube.com/watch?v=35rKcwzOtoo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229&t=3s	Рак двенадцатиперстной кишки 
11	опасность вторжения на мою территорию, не могу принять это , сильное раздражение, обида. 	язва желудка
12	конфликт расставания который ассоциирован с аллергеном. Либо сильный испуг ассоциированный с аллергеном.	аллергия 
14	подавленный  старый гнев по отношению к  близким с ощущением бессилия и несправедливости, застревание в этих чувствах.	неспецифический язвенный колит 
16	конфликт сомообесценивания, невыносимые обстоятельства, люди (терпеть не могу кого-то)\r\n#message\r\nhttps://youtu.be/6dcuNFZgjOo	ревматоидный полиартрит
18	Не могу избавиться от старой давнешней проблемы.  У меня "геморрой" с этим или с  собой. Конфликт идентичности. кто я для отца, матери...?	геморрой
19	не могу расстаться с кем-то или чем-то очень важным. Также территориальный конфликт идентичности - ктоя на этой территории?	запор
20	я не хочу, чтобы меня контролироваали , ппротест против брака, переживание о бывших взаимоотношениях, неосознаваемое  желание жить в них	аменорея
156	1. Конфликт сложного расставания.\r\n2. Конфликт загрязнения: дерма.\r\n3. Конфликт самообесценивания.  Вера в то, что ничего никогда не изменится\r\n#message \r\nhttps://www.youtube.com/watch?v=VXmo3WiwiGo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=247	Склеродермия 
168	1. Конфликт страха, опасения чего-то близкого\r\n2. Отсутствие желания видеть кого-то или что-то за рамками своего небольшого, недоступного другим пространства 	Близорукость (миопия)
181	1. гиперответственность в сочетании с разочарованием в жизни; разочарование в работе или семейных отношениях;\r\n2. ощущение, что жизнь лишила выбора — например, в работе или в личной жизни; отсутствие возможности изменить свою судьбу: «не могу больше ходить на эту работу, совсем не люблю то, что я там делаю», но «изменить ничего не могу, другой работы у меня нет»;\r\nили «не могу больше жить с этой женщиной (мужчиной), не люблю её, она (он) меня бесит»;\r\n3. глухое раздражение от повседневной рабочей рутины или подавленная злость на жизненные обстоятельства;	Кальцификация позвоночника (болезнь Бехтерева, анкилозирующий пондилоартрит)
193	Невозможность бороться, спорить, удерживать ситуацию под контролем, обладать удерживать что-то 	Пародонтоз
22	не могу переварить ситуацию с аспектом голода.	рак тонкого кишечника
24	я взвалил (взвалила) на себя  тяжелую ношу, моя жизнь невыносима, гнятущие обстоятельства	болезнь бехтерева
26	1. конфликт потери необходимого контакта , связи с близким и родным человеком\r\n2. крайне нежелательное общение с кем-либо	Нейродермит
27	1. конфликт разделения - потеря отношений с родным человеком / потеря уважения                                                2. конфликт самообесценивания - низкий уровень энергии и самооценки/ наличие крайне нежелательного общения\t\r\n#message\r\nhttps://youtu.be/D_W86MWEACw?t=459	Невралгия тройничного нерва
13	неспособность переварить отношение мамы ко мне, ситуацию с ощущением обреченности, беспомощности. Желание любви со стороны матери. \r\n#message\r\nhttps://youtu.be/fXerpLQawGE	синдром раздраженного кишечника
15	потеря значимого человека (без него как без воздуха)-развод родителей… страх удушья, страх того что творилось дома.\r\n#message\r\nhttps://youtu.be/PrW6WOXY0ps	бронхиальная астма
25	поиск решения неразрешенного конфликта, который не дает покоя даже ночью.\r\n#message\r\nhttps://youtu.be/9YR4wh6zF_I?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=550	Нарушение сна - инсомния
44	огромное желание забеременеть без возможности сделать это\r\n#message\r\nhttps://www.youtube.com/watch?v=B3j-j8PAWwE&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=188	Синдром поликистозных яичников (СПКЯ, поликистоз или склерокистоз яичников)
35	сильный конфликт самообесценивания, часто переданный по роду. У детей лейкемия выражается конфликтом «Я несу в себе недостаток самооценки своих родителей».\r\n#message\r\nhttps://youtu.be/G96o7Sg7Ju8?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=193	Лейкемия
45	1. сексуальный конфликт, связанный с мужчиной: конфликт женственности - ощущение, что ""мной как женщиной пренебрегают, я оскорблена""\r\n2. ощущение запятнанной сексуальной репутации - что скажут люди?\r\n3. Эмоциональный конфликт между бабушкой и внучкой, между мамой и дочерью.	Воспаление маточных труб 
28	"страх быть обездвиженным / отсутствие возможности или желания двигаться по жизни                                                                                                                                                                 Локализация\r\n•        Лицевая мускулатура: оказаться в дураках / стать посмешищем \r\n•        Мышцы плечевого пояса и спины: невозможность уклониться от кого-то или чего-то \r\n•        Сгибатели рук и ног: невозможность удержать, обнять, приблизить к себе кого-нибудь или что-нибудь \r\n•        Разгибатели рук и ног: невозможность избавиться, защититься, оттолкнуть что-либо или кого-либо\r\n•        Ноги: не найти выхода из создавшегося положения. Невозможность уйти, избежать чего-нибудь, успеть что-либо\r\n"	Инсульт
29	"1. конфликт потери необходимого контакта , связи с близким и родным человеком\r\n2. крайне нежелательное общение с кем-либо"	Нейродермит
30	у мужчин -  конфликт потери территории: потеря дома, работы, должности и т.д. \r\nу женщин - конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми	Боль в груди - стенокардия
31	1. сильный конфликт самообесценивания\r\n2. у мужчин чувство потери территории: потеря дома, работы, должности и т.д. \r\nу женщин конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми	Инфаркт миокарда
32	конфликт самообесценивания, связанный с сердцем - страх, что с сердцем что-то не так, вера в то, что сердце недостаточно сильное	Сужение митрального клапана
33	1. страх, что с сердцем что-то не так, вера в то, что сердце недостаточно сильное                                                   2. ощущение угнетенности, сильное нежелание выполнять обязанности на работе, по дому и т.д.                                                                                   3. тревога за свое будущее, тревога за личную жизнь\r\n#message\r\nhttps://youtu.be/6uztRhy0Elc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=314	Аритмия
34	1. недостаток любви, единства в семье \r\n2. конфликт сильного самообесценивания, связанный с предками\r\n#message\r\nhttps://youtu.be/YnfxAAymFBo?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=662	Анемия
60	недостаток качества сексуального контакта - "я расстроена, что не могу получить то, что хочу"	Половой герпес
36	накопление и удержание эмоциональных проблем, неразрешение конфликтов, проблема гиперконтроля\r\n#message\r\nhttps://youtu.be/n75EZtbReDc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=1360\r\n#message\r\nhttps://www.youtube.com/watch?v=PohsywNCw-c&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=229	Высокое кровяное давление - гипертония
37	1. конфликт самообесценивания - "моя жизнь недостаточно хороша"                                                                          \r\n2. ощущение беспомощности в отношении поврежденной части тела	Атеросклероз
38	территориальный конфликт в период восстановления, переживания за наследство, вторжение в личное пространство человека \r\n#message\r\nhttps://youtu.be/4d0Ti5d1grs?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=3303	Расширение участка аорты - аневризма аорты
39	1. обиды на мать, ощущение тяжелой женской доли, унаследование тяжести жизни от матери,  груза ответственности \r\n2. ощущение брошенности и одиночества\r\n3. ограничение личной свободы\r\n#message\r\n1. https://youtu.be/nRXDrHUbEQA?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=90\r\n#message\r\n2. https://www.youtube.com/watch?v=u0wYuCiexOo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=225 	Варикозное расширение вен
40	1. обиды на мать, ощущение тяжелой женской доли, унаследование тяжести жизни от матери,  груза ответственности \r\n2. ощущение брошенности и одиночества\r\n3. ограничение личной свободы\r\n#message\r\n1. https://youtu.be/nRXDrHUbEQA?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=90\r\n#message\r\n2. https://www.youtube.com/watch?v=u0wYuCiexOo&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=225 	варикоз
41	1. потеря или страх потери любимых людей (ребенок, супруг, родитель, друг) из-за смерти, ухода, переезда, пропажи. \r\n2. возвращение мыслями к болезненному прошлому \r\n3. потеря чувства сексуальности, проблемы с детьми\r\n#message\r\nhttps://youtu.be/alUSAFKzwv4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG	Киста яичника
42	1. боль от измены, боль от факта рождения ребенка на стороне у партнера \r\n2. конфликт нежелательной беременности после аборта, самоосуждение за аборт\r\n3. психологический запрет на рождение ребенка во имя самореализации\r\n#message\r\nhttps://youtu.be/alUSAFKzwv4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG	Эндометриоз
43	конфликт тяжелой утраты - фактическая потеря (утрата) очень близкого человека или людей (ребенка, любимого человека или животного), потеря собственного дела, которое воспринималось как дитя. 	Рак яичника
58	1. сильный конфликт неощущениея себя мужественным, потеря собственной значимости как мужчины, самообесценивание \r\n2. беспокойство за потомство - дети, внуки \r\n3. неудовлетворение семейной жизнью	Рак простаты
46	1. конфликт невозможности забеременеть из-за отсутствия или невозможности полового контакта\r\n2. женский конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, осознание себя нежеланной, проблемы с детьми, \r\n3. сексуальный конфликт разделения - измена, расставание с партнером	Рак шейки матки 
48	1. ощущение одиночества, отсутствия востребованности на работе, в семье, страх за будущее, неосознанное нежелание человека жить                                                                                                                                                                                                2.сильный конфликт с существующим или воображаемым партнером	Рак матки
49	чувство стыда с ощущением загрязненности в интимной жизни, в мыслях	Генитальные бородавки (кондиломы) шейки матки
50	неприятие собственной женственности, негармоничные отношения с мамой	Чрезмерное менструальное кровотечение
51	1. страх непреднамеренной беременности, страх не выносить плод, чувство сожаления об отстутствии гармоничных отношений с мужчиной                                                                                                                                                           2. огромное желание забеременеть кем-то из предков без реализации желаемого\r\n#message\r\nhttps://www.youtube.com/watch?v=z8g4PIlpVMQ	Менструальная боль (менструальный дискомфорт, предменструальный синдром)
119	Внутренние переживания, которыми человек ни с кем не может поделиться, но и избавиться от них не может. 	Поликистоз почек
52	1. конфликт угрозы существования - ""все потеряно"" - страх потерять все - имущество, состояние;    2.психологическая неготовность принятия беременности и ребенка\r\n3. отсутствие перспектив, неуверенности в завтрашнем дне\r\n4. глубокие конфликты отвержения/брошенности - чувство изоляции, полного одиночества \r\n#message\r\nhttps://www.instagram.com/p/Bx9COjqlize/?utm_source=ig_web_copy_link 	Токсикозы при беременности 
53	нежелание рожать, неготовность к материнству, конфликт между родителями.  Страх, что плод не сможет быть точным повторением ребенка, который умер ранее\r\n#message\r\nhttps://youtu.be/iySEV0yQDro?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=465	Выкидыш, преждевременные роды
55	сильный конфликт утраты - потеря или страх потери любимых людей (ребенок, супруга, родитель, любимое животное) из-за смерти, ухода, переезда. 	Рак яичника
56	боязнь оказаться не на высоте во время интимных отношений, страх расстаться с кем-либо или чем-либо	Гидроцеле (водянка яичка) 
57	отчаянье мужчины по причине неспособности стать хорошим родителем, неуверенность в себе как в мужчине	Аденома простаты
61	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества	Рак почек
78	1. конфликт, связанный с потерей территории (работа, дом, семья) \r\n2. конфликт, связанный с обозначением личных границ \r\n3. конфликт, связанный с повторяющимися спорами, разногласиями, ссорами с кем-либо\r\n4. конфликт самообесценивания - низкая самооценка, чувство вины. Зависание на негативном впечатлении.\r\n#message\r\n1. https://www.youtube.com/watch?v=0EDBP76sfAY&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=22                \r\n#message\r\n2. https://www.youtube.com/watch?v=LAG5LkZYLAA&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=220 	Депрессия
62	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества\r\n4. страх принятия чего-то нового - проявление упорства в своих убеждениях «Я не верю, что положение может улучшиться, я держусь за старое».	Гломерулонефрит
63	Внутренние переживания, которыми человек ни с кем не может поделиться, но и избавиться от них не может. 	Поликистоз почек
64	1. конфликт угрозы существования - ощущение, что все потеряно; чувство, что деньги ""утекают"" сквозь пальцы, страх за себя (отсутствие заботы, ухода), отсутствие перспектив, неуверенность в завтрашнем дне\r\n\r\n2. конфликт беженца - ощущение себя не на своем месте, чужим\r\n\r\n3. конфликт отвержения/брошенности - чувство изолированности, одиночества, воспоминания об утонувших в роду	Острая почечная недостаточность, острый некротический нефроз (острая тубулопатия)
65	1. территориальный конфликт - неожиданное вторжение в личные границы человека - ""мои границы нарушены, потому что я их четко не обозначил""\r\n2. конфликт борьбы за выживание\r\n#message\r\nhttps://youtu.be/SQag5uK5YJU?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=2099	Камни в почках (мочекаменная болезнь), песок в почках
76	действия вопреки желаниям, конфликт страха и отвращения \r\n#message\r\nhttps://youtu.be/Og7yMTu3kxk?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=482	Навязчивые мысли
66	1. территориальный конфликт - неожиданное вторжение в личные границы человека - мои границы нарушены, потому что я их четко не обозначил \r\n2. конфликт безопасности внутри установленных личных границ	Рак мочевого пузыря
67	1. территориальный конфликт - потеря личного пространства (квартира, работа - "меня выживают")         \r\n2. у женщин - раздражение по поводу полового партнера\t\r\n#message\r\nhttps://www.youtube.com/watch?v=Y8t7hCtFo14&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=197	Цистит
169	Опасение чего-то очень далекого - страх за будущее	Дальнозоркость (гиперметропия)
68	1. компенсация тревоги взаимоотношений в семье, способ заявить о себе                                                                 \r\n2. конфликт, связанный с отцом - отца нет или он очень властный и ребенок его боится                                                            3. желание вернуться в утробу матери и быть защищенным\r\n#message\r\nhttps://youtu.be/NkcYbDnAh6M?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=1831	Недержание мочи у детей
69	1. Запрет восприятия реальности, происходящих событий - "мне не позволено видеть мир таким какой он есть"                                                          2. часто в фазе программирования или семейном дереве, конфликт, при котором реальность воспринимается очень болезненно, шоковые события в роду.\r\n#message\r\n1. https://www.youtube.com/watch?v=dDW1OJdW3Gc               \r\n#message\r\n2. https://www.youtube.com/watch?v=HnXO9TAqShs&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=200 \r\n	Шизофрения
70	эмоциональная травма, полученная в раннем детстве из-за конфликта родителей - чувство брошенности, расставания, нежелания жить \r\n#message\r\nhttps://youtu.be/LWMbcVOAmkc?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=2689	Суицидальные наклонности, постоянные мысли о смерти и о "жизни после смерти"
71	территориальный конфликт:\r\nу мужчин -  конфликт потери территории: потеря дома, работы, должности и т.д. \r\nу женщин -  конфликт потери территории с сексуальным аспектом, потеря чувства сексуальности, проблемы с детьми	Клаустрофобия
72	страх осуждения, невозможность занять свое место в жизни\r\n#message\r\nhttps://www.youtube.com/watch?v=Spuh4jkdkM0	Агорафобия
73	1. Активный конфликт с матерью, чувство соперничества                                                                                              2. Разногласия, недопонимания с родными людьми	Анорексия 
74	страх голода, недостатка пищи, недостаток чего-то необходимого, страх быть брошенным	Булимия 
75	конфликт страха или опасений за будущее в целом - «Что со мной будет?» 	Мания преследования (паранойя), зрительные галлюцинации
77	отсутствие следования предназначению, внутреннему призванию, ощущение бессмысленности жизни	Синдром эмоционального выгорания
79	1. душевный и эмоциональный конфликт, случившийся в глубоком детстве: мысли матери об аборте, конфликтные отношения с партнером во время беременности, тяжелые роды                                                                                                     2. психологические травмы, полученные кем-то из предков в роду\r\n#message\r\nhttps://youtu.be/edB--oPhFGU?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG	Панические атаки
80	Подавленное чувство угрозы жизни человека (выкидыш, мысли об аборте) в период беременности матери	Аэрофобия
81	неосознанное желание трансформировать свою жизнь, страх сделать выбор, способного повлиять на будущее\r\nСимптомы:\r\n•        кашель - отсутствие реализации желаемого, болезненное реагирование на неразрешенную ситуацию \r\n•        бронхит - нарушение личных границ человека, постоянное раздражение на окружающий мир\r\n•        пневмония - страх смерти, ощущение глубоких потрясений, угрожающих жизни\r\n•        потеря обоняния - пребывание в дурнопахнущей, неприятной ситуации, оставившей отпечаток на психике.\r\n#message\r\nhttps://www.instagram.com/tv/CQej_aMIXix/?utm_source=ig_web_copy_link    \r\n#message\r\nhttps://www.instagram.com/tv/CQoxqmTokKV/?utm_source=ig_web_copy_link https://www.youtube.com/watch?v=66KlO-Moop8 	COVID-19, коронавирус
59	1. конфликт самообесценивания - снижение самооценки, низкий уровень энергии, переживания по поводу потери детей в роду                                                                               2. психологический запрет на возможность иметь детей, связанный с конкурентным воспитанием (в моем стаде я не альфа самец)\r\n#message\r\nhttps://youtu.be/iX3-aeZzMU4?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&t=2017\r\n#message\r\nhttps://www.youtube.com/watch?v=4-ai6nLG01A&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=187\r\n#message\r\nhttps://www.youtube.com/watch?v=47qzgFDk55k&list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG&index=198	Мужское бесплодие
94	территориальный конфликт в период восстановления, переживания за наследство, вторжение в личное пространство человека \r\n#message \r\nhttps://youtu.be/4d0Ti5d1grs?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Расширение участка аорты - аневризма аорты
132	действия вопреки желаниям, конфликт страха и отвращения \r\n#message \r\nhttps://youtu.be/Og7yMTu3kxk?list=PLvvQng9TolQPXKtRxUfHtW3XyL3W5_4BG 	Навязчивые мысли
\.


--
-- Data for Name: tgclient; Type: TABLE DATA; Schema: public; Owner: tgbot
--

COPY public.tgclient (id, tg_id, status_id, first_name, last_name, username) FROM stdin;
11	609944851	1	Валентина	Николаевна	\N
12	1189218889	1	Татьяна	Яковлева	\N
13	721679488	1	Надежда	Маркова🧡	psy_markova_nadia
14	2011899667	1	Ольга	\N	\N
15	2016842719	1	Наталья	Корнышкина	\N
1	278565148	1	Lev	Verbitskiy	lverbitskiy
16	498369382	1	.	\N	\N
17	618036879	1	1	2	\N
18	1040278148	1	Оля	\N	\N
3	277570312	1	Eveniya	\N	\N
4	431225750	1	Артем	Толоконин	ArtemOlegovichTolokonin
5	709688236	1	Klavdiia	Guder	KlavdiiaG
6	1490440627	1	Elena Stefanovskaya	Elena Stefanovskaya	\N
7	403341805	1	Tatiana	Feldman	matana1
8	184563255	1	Butaeva	Polina	butaeva_polina
20	420226864	1	Юлия	\N	\N
9	454811911	1	Natalia	\N	\N
19	119578893	1	Валерия	Копирайтер-Маркетолог	valeriya_copywriting
2	318317550	1	Денис	Гром	gromdeni
10	1478902805	1	Виктория	\N	\N
21	205694915	1	Denis	Skripka	dskripka
\.


--
-- Name: adminuser_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.adminuser_id_seq', 1, true);


--
-- Name: answersstatistic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.answersstatistic_id_seq', 41, true);


--
-- Name: commands_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.commands_id_seq', 1, true);


--
-- Name: menu_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.menu_id_seq', 1, true);


--
-- Name: menubutton_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.menubutton_id_seq', 6, true);


--
-- Name: migratehistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.migratehistory_id_seq', 7, true);


--
-- Name: statuses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.statuses_id_seq', 1, true);


--
-- Name: textanswers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.textanswers_id_seq', 198, true);


--
-- Name: tgclient_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tgbot
--

SELECT pg_catalog.setval('public.tgclient_id_seq', 21, true);


--
-- Name: adminuser adminuser_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.adminuser
    ADD CONSTRAINT adminuser_pkey PRIMARY KEY (id);


--
-- Name: answersstatistic answersstatistic_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.answersstatistic
    ADD CONSTRAINT answersstatistic_pkey PRIMARY KEY (id);


--
-- Name: commands commands_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.commands
    ADD CONSTRAINT commands_pkey PRIMARY KEY (id);


--
-- Name: menu menu_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_pkey PRIMARY KEY (id);


--
-- Name: menubutton menubutton_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menubutton
    ADD CONSTRAINT menubutton_pkey PRIMARY KEY (id);


--
-- Name: migratehistory migratehistory_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.migratehistory
    ADD CONSTRAINT migratehistory_pkey PRIMARY KEY (id);


--
-- Name: statuses statuses_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.statuses
    ADD CONSTRAINT statuses_pkey PRIMARY KEY (id);


--
-- Name: textanswers textanswers_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.textanswers
    ADD CONSTRAINT textanswers_pkey PRIMARY KEY (id);


--
-- Name: tgclient tgclient_pkey; Type: CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.tgclient
    ADD CONSTRAINT tgclient_pkey PRIMARY KEY (id);


--
-- Name: commands_to_status_id; Type: INDEX; Schema: public; Owner: tgbot
--

CREATE INDEX commands_to_status_id ON public.commands USING btree (to_status_id);


--
-- Name: menu_status_id; Type: INDEX; Schema: public; Owner: tgbot
--

CREATE INDEX menu_status_id ON public.menu USING btree (status_id);


--
-- Name: menubutton_menu_id; Type: INDEX; Schema: public; Owner: tgbot
--

CREATE INDEX menubutton_menu_id ON public.menubutton USING btree (menu_id);


--
-- Name: menubutton_to_status_id; Type: INDEX; Schema: public; Owner: tgbot
--

CREATE INDEX menubutton_to_status_id ON public.menubutton USING btree (to_status_id);


--
-- Name: tgclient_status_id; Type: INDEX; Schema: public; Owner: tgbot
--

CREATE INDEX tgclient_status_id ON public.tgclient USING btree (status_id);


--
-- Name: commands commands_to_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.commands
    ADD CONSTRAINT commands_to_status_id_fkey FOREIGN KEY (to_status_id) REFERENCES public.statuses(id) ON DELETE CASCADE;


--
-- Name: menu menu_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menu
    ADD CONSTRAINT menu_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.statuses(id) ON DELETE CASCADE;


--
-- Name: menubutton menubutton_menu_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menubutton
    ADD CONSTRAINT menubutton_menu_id_fkey FOREIGN KEY (menu_id) REFERENCES public.menu(id) ON DELETE CASCADE;


--
-- Name: menubutton menubutton_to_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.menubutton
    ADD CONSTRAINT menubutton_to_status_id_fkey FOREIGN KEY (to_status_id) REFERENCES public.statuses(id) ON DELETE CASCADE;


--
-- Name: tgclient tgclient_status_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tgbot
--

ALTER TABLE ONLY public.tgclient
    ADD CONSTRAINT tgclient_status_id_fkey FOREIGN KEY (status_id) REFERENCES public.statuses(id);


--
-- PostgreSQL database dump complete
--

