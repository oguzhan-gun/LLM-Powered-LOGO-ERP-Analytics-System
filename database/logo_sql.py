#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:06:42 2026

@author: data
"""

import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("logo_tiger.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# ─────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────────

def rand_date(start_year=2022, end_year=2024):
    start = datetime(start_year, 1, 1)
    end   = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

def rand_amount(lo=100, hi=50000):
    return round(random.uniform(lo, hi), 2)


# ═══════════════════════════════════════════════════════════════════
# 1. TEMEL TANIMLAR
# ═══════════════════════════════════════════════════════════════════



# ── Ülkeler ──────────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_COUNTRY (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO L_COUNTRY VALUES (?,?,?)", [
    (1,"TR","Türkiye"),(2,"DE","Almanya"),(3,"US","Amerika Birleşik Devletleri"),
    (4,"FR","Fransa"),(5,"GB","Birleşik Krallık"),(6,"IT","İtalya"),
    (7,"NL","Hollanda"),(8,"BE","Belçika"),(9,"ES","İspanya"),
    (10,"PT","Portekiz"),(11,"PL","Polonya"),(12,"RU","Rusya"),
    (13,"CN","Çin"),(14,"JP","Japonya"),(15,"AE","Birleşik Arap Emirlikleri"),
    (16,"SA","Suudi Arabistan"),(17,"EG","Mısır"),(18,"GR","Yunanistan"),
    (19,"BG","Bulgaristan"),(20,"RO","Romanya"),(21,"HU","Macaristan"),
    (22,"CZ","Çek Cumhuriyeti"),(23,"SK","Slovakya"),(24,"AT","Avusturya"),
    (25,"CH","İsviçre"),
])

# ── Şehirler ─────────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_CITY (
    LOGICALREF INTEGER PRIMARY KEY,
    COUNTRYREF  INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (COUNTRYREF) REFERENCES L_COUNTRY(LOGICALREF)
)""")
cursor.executemany("INSERT INTO L_CITY VALUES (?,?,?,?)", [
    (1,1,"34","İstanbul"),(2,1,"06","Ankara"),(3,1,"35","İzmir"),
    (4,1,"16","Bursa"),(5,1,"01","Adana"),(6,1,"07","Antalya"),
    (7,1,"42","Konya"),(8,1,"41","Kocaeli"),(9,1,"10","Balıkesir"),
    (10,1,"45","Manisa"),(11,1,"33","Mersin"),(12,1,"27","Gaziantep"),
    (13,1,"38","Kayseri"),(14,1,"03","Afyon"),(15,1,"25","Erzurum"),
    (16,2,"BE","Berlin"),(17,2,"MU","Münih"),(18,3,"NY","New York"),
    (19,3,"LA","Los Angeles"),(20,4,"PA","Paris"),(21,5,"LO","Londra"),
    (22,6,"MI","Milano"),(23,7,"AM","Amsterdam"),(24,9,"MA","Madrid"),
    (25,13,"SH","Şangay"),
])

# ── Posta Kodları ─────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_POSTCODE (
    LOGICALREF INTEGER PRIMARY KEY,
    CITYREF     INTEGER,
    CODE        TEXT,
    FOREIGN KEY (CITYREF) REFERENCES L_CITY(LOGICALREF)
)""")
cursor.executemany("INSERT INTO L_POSTCODE VALUES (?,?,?)", [
    (i, ((i-1)%15)+1, f"{34000+i*37}") for i in range(1,26)
])

# ── Sevkiyat Firmaları ────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_SHPAGENT (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO L_SHPAGENT VALUES (?,?,?)", [
    (1,"AGT01","Aras Kargo"),(2,"AGT02","Yurtiçi Kargo"),(3,"AGT03","MNG Kargo"),
    (4,"AGT04","PTT Kargo"),(5,"AGT05","DHL"),(6,"AGT06","FedEx"),
    (7,"AGT07","UPS"),(8,"AGT08","TNT"),(9,"AGT09","Sürat Kargo"),
    (10,"AGT10","Horoz Lojistik"),(11,"AGT11","Borusan Lojistik"),
    (12,"AGT12","Omsan Lojistik"),(13,"AGT13","DB Schenker"),
    (14,"AGT14","Kuehne+Nagel"),(15,"AGT15","Panalpina"),
    (16,"AGT16","Ceva Logistics"),(17,"AGT17","XPO Logistics"),
    (18,"AGT18","DSV"),(19,"AGT19","Rhenus"),(20,"AGT20","Gefco"),
    (21,"AGT21","Aramex"),(22,"AGT22","DPD"),(23,"AGT23","GLS"),
    (24,"AGT24","Hermes"),(25,"AGT25","Géodis"),
])

# ── Sevkiyat Türleri ──────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_SHPTYPES (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO L_SHPTYPES VALUES (?,?,?)", [
    (1,"KAR","Kara Taşımacılığı"),(2,"HAV","Hava Taşımacılığı"),
    (3,"DEN","Deniz Taşımacılığı"),(4,"DEMİR","Demiryolu"),(5,"ÇKMOD","Çok Modlu"),
    (6,"EXP","Ekspres"),(7,"EKO","Ekonomik"),(8,"SOG","Soğuk Zincir"),
    (9,"AğIR","Ağır Yük"),(10,"HACİM","Hacimli Yük"),(11,"KONT","Konteyner"),
    (12,"PAL","Paletli"),(13,"DOKS","Doküman"),(14,"ÖZEL","Özel Kurye"),
    (15,"SAB","Sabit Güzergah"),(16,"BEL","Belirli Zaman"),(17,"GECE","Gece Teslimat"),
    (18,"AYNI","Aynı Gün"),(19,"ERT","Ertesi Gün"),(20,"IKI","İki Günlük"),
    (21,"HAFTA","Haftalık Sefer"),(22,"2HAFTA","İki Haftada Bir"),
    (23,"AYLIK","Aylık Sefer"),(24,"ÖZEL2","Özel Zamanlama"),(25,"KARMA","Karma Teslimat"),
])

# ── Ticari İşlem Grupları ─────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_TRADGRP (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO L_TRADGRP VALUES (?,?,?)", [
    (1,"TG01","Perakende Satış"),(2,"TG02","Toptan Satış"),(3,"TG03","İhracat"),
    (4,"TG04","İthalat"),(5,"TG05","Yurt İçi Alış"),(6,"TG06","Yurt Dışı Alış"),
    (7,"TG07","Konsinye"),(8,"TG08","Hizmet Satışı"),(9,"TG09","Hizmet Alışı"),
    (10,"TG10","Proje Satışı"),(11,"TG11","Abonelik"),(12,"TG12","Sözleşmeli Satış"),
    (13,"TG13","Spot Satış"),(14,"TG14","Üretim Satışı"),(15,"TG15","Numune"),
    (16,"TG16","İade Alış"),(17,"TG17","İade Satış"),(18,"TG18","Fire/Zayiat"),
    (19,"TG19","Devir"),(20,"TG20","Konsorsiyum"),(21,"TG21","Ortaklık"),
    (22,"TG22","Franchise"),(23,"TG23","Distribütörlük"),(24,"TG24","Acentelik"),
    (25,"TG25","Bayilik"),
])

# ── Kullanıcılar ──────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_GOUSERS (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    NAME        TEXT,
    ACTIVE      INTEGER DEFAULT 1
)""")
cursor.executemany("INSERT INTO L_GOUSERS VALUES (?,?,?,?)", [
    (1,"admin","Sistem Yöneticisi",1),(2,"user01","Ahmet Yılmaz",1),
    (3,"user02","Mehmet Demir",1),(4,"user03","Ayşe Kaya",1),
    (5,"user04","Fatma Çelik",1),(6,"user05","Ali Şahin",1),
    (7,"user06","Zeynep Arslan",1),(8,"user07","Mustafa Aydın",1),
    (9,"user08","Elif Öztürk",1),(10,"user09","Hüseyin Koç",1),
    (11,"user10","Hatice Erdoğan",1),(12,"user11","İbrahim Doğan",1),
    (13,"user12","Emine Şimşek",1),(14,"user13","Yusuf Yıldız",1),
    (15,"user14","Merve Güneş",1),(16,"user15","Emre Aktaş",0),
    (17,"user16","Seda Polat",1),(18,"user17","Burak Çakır",1),
    (19,"user18","Neslihan Bozkurt",1),(20,"user19","Oğuzhan Keskin",0),
    (21,"user20","Derya Gündüz",1),(22,"user21","Sercan Parlak",1),
    (23,"user22","Gizem Uysal",1),(24,"user23","Tolga Kaplan",1),
    (25,"user24","Pınar Tekin",1),
])

# ── Kuruluş Bilgileri ─────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_CAPIDEF (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    TYPE        INTEGER  -- 1=Ambar 2=İşyeri 3=Fabrika
)""")
cursor.executemany("INSERT INTO L_CAPIDEF VALUES (?,?,?,?)", [
    (1,"FAB01","Ana Fabrika",3),(2,"FAB02","Yan Fabrika",3),
    (3,"ISY01","İstanbul İşyeri",2),(4,"ISY02","Ankara İşyeri",2),
    (5,"ISY03","İzmir İşyeri",2),(6,"AMB01","Merkez Ambarı",1),
    (7,"AMB02","İkmal Ambarı",1),(8,"AMB03","Bitmiş Ürün Ambarı",1),
    (9,"AMB04","Hammadde Ambarı",1),(10,"AMB05","Yardımcı Malzeme Ambarı",1),
    (11,"AMB06","Fire/İmha Ambarı",1),(12,"AMB07","Karantina Ambarı",1),
    (13,"AMB08","Sevkiyat Bekleyen",1),(14,"AMB09","Müşteri İade Ambarı",1),
    (15,"AMB10","Konsinye Ambarı",1),(16,"ISY04","Bursa İşyeri",2),
    (17,"ISY05","Adana İşyeri",2),(18,"FAB03","Montaj Fabrikası",3),
    (19,"FAB04","Paketleme Ünitesi",3),(20,"AMB11","Soğuk Depo",1),
    (21,"AMB12","Dış Depo 1",1),(22,"AMB13","Dış Depo 2",1),
    (23,"ISY06","Antalya İşyeri",2),(24,"ISY07","Gaziantep İşyeri",2),
    (25,"AMB14","Geçici Depo",1),
])

# ── Döküman Numaralama Şablonları ─────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_LDOCNUM (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    PREFIX      TEXT,
    LASTNUMBER  INTEGER
)""")
cursor.executemany("INSERT INTO L_LDOCNUM VALUES (?,?,?,?,?)", [
    (1,"DN001","Fatura Numaralama","FAT",10500),
    (2,"DN002","Sipariş Numaralama","SIP",8420),
    (3,"DN003","İrsaliye Numaralama","IRS",9100),
    (4,"DN004","Çek Numaralama","CEK",3300),
    (5,"DN005","Senet Numaralama","SEN",1200),
    (6,"DN006","Kasa Fişi","KAS",5600),
    (7,"DN007","Banka Fişi","BNK",4800),
    (8,"DN008","Muhasebe Fişi","MUH",7200),
    (9,"DN009","Üretim Emri","URE",2100),
    (10,"DN010","Stok Fişi","STK",6300),
    (11,"DN011","Teklif Numaralama","TEK",1800),
    (12,"DN012","Sözleşme Numaralama","SOZ",940),
    (13,"DN013","Proforma Fatura","PRF",670),
    (14,"DN014","Gümrük Beyannamesi","GMR",520),
    (15,"DN015","İthalat Dosyası","ITH",310),
    (16,"DN016","İhracat Dosyası","IHR",285),
    (17,"DN017","Kalite Belgesi","KAL",1500),
    (18,"DN018","Numune Formu","NUM",430),
    (19,"DN019","İş Emri","ISE",3800),
    (20,"DN020","Bakım Emri","BAK",920),
    (21,"DN021","İade Faturası","IAD",760),
    (22,"DN022","Kredi Notu","KRD",380),
    (23,"DN023","Debit Notu","DEB",240),
    (24,"DN024","Konsinye Belgesi","KON",175),
    (25,"DN025","Transfer Fişi","TRF",2900),
])

# ── Günlük Döviz Kurları ──────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_DAILYEXCHANGES (
    LOGICALREF INTEGER PRIMARY KEY,
    DATE_        TEXT,
    CURTYPE     INTEGER,  -- 1=USD 2=EUR 3=GBP vb.
    BUYRATE     REAL,
    SELLRATE    REAL
)""")
rows = []
ref = 1
for days_ago in range(25):
    d = (datetime(2024,12,31) - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    rows.append((ref, d, 1, round(random.uniform(31,33),4), round(random.uniform(31.1,33.2),4))); ref+=1
    rows.append((ref, d, 2, round(random.uniform(34,36),4), round(random.uniform(34.1,36.2),4))); ref+=1
    if ref > 25:
        break
cursor.executemany("INSERT INTO L_DAILYEXCHANGES VALUES (?,?,?,?,?)", rows[:25])

# ── Network Kontrolü ──────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS L_NET (
    LOGICALREF INTEGER PRIMARY KEY,
    USERREF     INTEGER,
    FIRMNR      INTEGER,
    PERIODNR    INTEGER,
    LOGINDATE   TEXT,
    FOREIGN KEY (USERREF) REFERENCES L_GOUSERS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO L_NET VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), 1, 2024, rand_date(2024,2024)) for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 2. CARİ HESAPLAR
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLCARD (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,

    CREATEDDATE TEXT,
    ACTIVE      INTEGER,

    CITYREF     INTEGER,
    COUNTRYREF  INTEGER,

    TAXNR       TEXT,
    TAXOFFICE   TEXT,
    EMAILADDR   TEXT,

    PAYMENTREF  INTEGER,

    SPECODE     TEXT,
    SPECODE2    TEXT,
    SPECODE3    TEXT,
    SPECODE4    TEXT,
    SPECODE5    TEXT,

    FOREIGN KEY (CITYREF)    REFERENCES L_CITY(LOGICALREF),
    FOREIGN KEY (COUNTRYREF) REFERENCES L_COUNTRY(LOGICALREF)
)""")

clcard_data = [
    (1,"C001","Ahmet Mobilya Ltd.",rand_date(2024,2025),1,1,1,"1234567890","Kadıköy","ahmet@ahmetmobilya.com.tr",1,"SC001",None,None,None,None),
    (2,"C002","Mehmet Tekstil A.Ş.",rand_date(2024,2025),1,2,1,"2345678901","Çankaya","info@mehmettekstil.com",2,"SC002",None,None,None,None),
    (3,"C003","Ayşe Gıda Ticaret",rand_date(2024,2025),1,3,1,"3456789012","Bornova","ayse@aysegida.com",1,"SC003",None,None,None,None),
    (4,"C004","XYZ Holding A.Ş.",rand_date(2024,2025),1,1,1,"4567890123","Şişli","info@xyzholding.com",3,"SC004",None,None,None,None),
    (5,"C005","Delta Elektronik Ltd.",rand_date(2024,2025),1,4,1,"5678901234","Nilüfer","delta@deltaelektronik.com",1,"SC005",None,None,None,None),

    (6,"C006","Gamma Makina A.Ş.",rand_date(2024,2025),1,5,1,"6789012345","Seyhan","gamma@gammamakina.com",2,None,None,None,None,None),
    (7,"C007","Beta İnşaat Ticaret",rand_date(2024,2025),1,6,1,"7890123456","Muratpaşa","beta@betainsaat.com",1,None,None,None,None,None),
    (8,"C008","NoSales Corp.",rand_date(2024,2025),1,7,1,"8901234567","İzmit","ns@nosales.com",1,None,None,None,None,None),
    (9,"C009","EdgeCase Sanayi Ltd.",rand_date(2024,2025),1,8,1,"9012345678","Altıeylül","edge@edgecase.com.tr",2,None,None,None,None,None),
    (10,"C010","HighFreq Teknoloji A.Ş.",rand_date(2024,2025),1,9,1,"0123456789","Yunusemre","hf@highfreq.com.tr",3,None,None,None,None,None),

    (11,"C011","Alfa Tarım Ltd.",rand_date(2024,2025),1,10,1,"1122334455","Şehzadeler","alfa@alfatarım.com",1,None,None,None,None,None),
    (12,"C012","Sigma Kimya A.Ş.",rand_date(2024,2025),1,11,1,"2233445566","Toroslar","sigma@sigmakimya.com",2,None,None,None,None,None),
    (13,"C013","Omega Plastik Ltd.",rand_date(2024,2025),1,12,1,"3344556677","Şahinbey","omega@omegaplastik.com",1,None,None,None,None,None),
    (14,"C014","Zeta Ambalaj A.Ş.",rand_date(2024,2025),1,13,1,"4455667788","Melikgazi","zeta@zetaambalaj.com",1,None,None,None,None,None),
    (15,"C015","Theta Lojistik Ltd.",rand_date(2024,2025),1,14,1,"5566778899","Kaçıkören","theta@thetalojistik.com",2,None,None,None,None,None),

    (16,"C016","Kappa Metal A.Ş.",rand_date(2024,2025),1,1,1,"6677889900","Beşiktaş","kappa@kappametal.com",3,None,None,None,None,None),
    (17,"C017","Lambda Enerji Ltd.",rand_date(2024,2025),1,2,1,"7788990011","Çankaya","lambda@lambdaenerji.com",1,None,None,None,None,None),
    (18,"C018","Mu Yazılım A.Ş.",rand_date(2024,2025),1,3,1,"8899001122","Konak","mu@muyazilim.com",2,None,None,None,None,None),
    (19,"C019","Nu Danışmanlık Ltd.",rand_date(2024,2025),1,1,1,"9900112233","Fatih","nu@nudanismanlik.com",1,None,None,None,None,None),
    (20,"C020","Xi Reklam A.Ş.",rand_date(2024,2025),1,2,1,"0011223344","Yenimahalle","xi@xireklam.com",3,None,None,None,None,None),

    (21,"C021","Pi Güvenlik Ltd.",rand_date(2024,2025),1,4,1,"1023456789","Osmangazi","pi@pigüvenlik.com",1,None,None,None,None,None),
    (22,"C022","Rho Medikal A.Ş.",rand_date(2024,2025),1,6,1,"2034567890","Muratpaşa","rho@rhomedikal.com",2,None,None,None,None,None),
    (23,"C023","Tau Otomotiv Ltd.",rand_date(2024,2025),1,8,1,"3045678901","İzmit","tau@tauotomotiv.com",1,None,None,None,None,None),
    (24,"C024","Upsilon Tarih A.Ş.",rand_date(2024,2025),1,1,1,"4056789012","Sarıyer","ups@upsilontarih.com",3,None,None,None,None,None),
    (25,"C025","Phi Finans Ltd.",rand_date(2024,2025),1,2,1,"5067890123","Çankaya","phi@phifinans.com",2,None,None,None,None,None),
]

cursor.executemany(
    "INSERT INTO LG_CLCARD VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
    clcard_data
)
# ── Cari Hesap İstihbarat Bilgileri ──────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLINTEL (
    LOGICALREF  INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    FOUNDYEAR   INTEGER,
    EMPLCOUNT   INTEGER,
    ANNUALTURN  REAL,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CLINTEL VALUES (?,?,?,?,?)", [
    (i, i, random.randint(1980,2015), random.randint(5,500), rand_amount(500000,50000000))
    for i in range(1,26)
])

# ── Cari Hesap Fişleri ────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLFICHE (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    FICHENO     TEXT,
    DATE_       TEXT,
    TOTAL       REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CLFICHE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), f"CLF{i:05}", rand_date(), rand_amount(), random.randint(1,9))
    for i in range(1,26)
])

# ── Cari Hesap Hareketleri ────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLFLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    FICHEREF    INTEGER,
    CLIENTREF   INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (FICHEREF)  REFERENCES LG_CLFICHE(LOGICALREF),
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CLFLINE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_date(), rand_amount(), random.randint(1,9))
    for i in range(1,26)
])

# ── Cari Hesap Aylık Toplamları ───────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLTOTFIL (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    DEBIT       REAL,
    CREDIT      REAL,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CLTOTFIL VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])

# ── Cari Hesap Risk Tabloları ─────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CLRNUMS (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    RISKLIMIT   REAL,
    CURRENTRISK REAL,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CLRNUMS VALUES (?,?,?,?)", [
    (i, i, rand_amount(50000,500000), rand_amount(0,500000)) for i in range(1,26)
])

# ── Sevkiyat Adresleri ────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SHIPINFO (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    ADDRESS     TEXT,
    CITYREF     INTEGER,
    POSTCODE    TEXT,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF),
    FOREIGN KEY (CITYREF)   REFERENCES L_CITY(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SHIPINFO VALUES (?,?,?,?,?)", [
    (i, i, f"Örnek Mah. {i}. Sokak No:{i*3}", random.randint(1,15), f"{34000+i*37}")
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 3. MALZEME / STOK
# ═══════════════════════════════════════════════════════════════════

# ── Özellik Kodları ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CHARCODE (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_CHARCODE VALUES (?,?,?)", [
    (1,"RENK","Renk"),(2,"OLCU","Ölçü"),(3,"AGIRLK","Ağırlık"),(4,"MARKA","Marka"),
    (5,"MODEL","Model"),(6,"MALZME","Malzeme Tipi"),(7,"SINIF","Sınıf"),
    (8,"CERT","Sertifikasyon"),(9,"VOLTAJ","Voltaj"),(10,"AMPER","Amper"),
    (11,"FREKANS","Frekans"),(12,"IP","IP Koruma Sınıfı"),(13,"SICAKLIK","Sıcaklık"),
    (14,"BASINC","Basınç"),(15,"HIZ","Devir/Hız"),(16,"KAPASITE","Kapasite"),
    (17,"UZUNLUK","Uzunluk"),(18,"GENISLIK","Genişlik"),(19,"YUKSEKLIK","Yükseklik"),
    (20,"HACIM","Hacim"),(21,"TERMAL","Termal İletkenlik"),(22,"SERTLIK","Sertlik"),
    (23,"CEKME","Çekme Mukavemeti"),(24,"UZAMA","Uzama %"),(25,"YOGUNLUK","Yoğunluk"),
])

# ── Özellik Değerleri ─────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CHARVAL (
    LOGICALREF INTEGER PRIMARY KEY,
    CHARREF     INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (CHARREF) REFERENCES LG_CHARCODE(LOGICALREF)
)""")
vals = [
    (1,1,"KIRMIZI","Kırmızı"),(2,1,"MAVI","Mavi"),(3,1,"YESIL","Yeşil"),
    (4,1,"SIYAH","Siyah"),(5,1,"BEYAZ","Beyaz"),
    (6,2,"S","Small"),(7,2,"M","Medium"),(8,2,"L","Large"),(9,2,"XL","X-Large"),(10,2,"XXL","XX-Large"),
    (11,3,"1KG","1 kg"),(12,3,"5KG","5 kg"),(13,3,"10KG","10 kg"),(14,3,"25KG","25 kg"),(15,3,"50KG","50 kg"),
    (16,4,"BOSCH","Bosch"),(17,4,"SIEMENS","Siemens"),(18,4,"ABB","ABB"),
    (19,4,"SCHNEIDER","Schneider"),(20,4,"LEGRAND","Legrand"),
    (21,5,"2024","Model 2024"),(22,5,"2023","Model 2023"),(23,5,"2022","Model 2022"),
    (24,5,"2021","Model 2021"),(25,5,"2020","Model 2020"),
]
cursor.executemany("INSERT INTO LG_CHARVAL VALUES (?,?,?,?)", vals)

# ── Birim Setleri ─────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_UNITSETF (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_UNITSETF VALUES (?,?,?)", [
    (1,"BS001","Ağırlık Birimi Seti"),(2,"BS002","Uzunluk Birimi Seti"),
    (3,"BS003","Hacim Birimi Seti"),(4,"BS004","Adet Birimi Seti"),
    (5,"BS005","Alan Birimi Seti"),(6,"BS006","Elektrik Birimi Seti"),
    (7,"BS007","Zaman Birimi Seti"),(8,"BS008","Isı Birimi Seti"),
    (9,"BS009","Basınç Birimi Seti"),(10,"BS010","Hız Birimi Seti"),
    (11,"BS011","Gıda Birimi Seti"),(12,"BS012","İlaç Birimi Seti"),
    (13,"BS013","Tekstil Birimi Seti"),(14,"BS014","Kimya Birimi Seti"),
    (15,"BS015","İnşaat Birimi Seti"),(16,"BS016","Ambalaj Birimi Seti"),
    (17,"BS017","Elektronik Birimi Seti"),(18,"BS018","Otomotiv Birimi Seti"),
    (19,"BS019","Tarım Birimi Seti"),(20,"BS020","Enerji Birimi Seti"),
    (21,"BS021","Demir Çelik Birimi Seti"),(22,"BS022","Plastik Birimi Seti"),
    (23,"BS023","Kağıt Birimi Seti"),(24,"BS024","Cam Birimi Seti"),
    (25,"BS025","Genel Birim Seti"),
])

# ── Birimler ──────────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_UNITSETL (
    LOGICALREF  INTEGER PRIMARY KEY,
    UNITSETREF  INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    MAINUNIT    INTEGER DEFAULT 0,
    FOREIGN KEY (UNITSETREF) REFERENCES LG_UNITSETF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_UNITSETL VALUES (?,?,?,?,?)", [
    (1,1,"KG","Kilogram",1),(2,1,"GR","Gram",0),(3,1,"TON","Ton",0),
    (4,2,"MT","Metre",1),(5,2,"CM","Santimetre",0),(6,2,"MM","Milimetre",0),
    (7,3,"LT","Litre",1),(8,3,"ML","Mililitre",0),(9,3,"M3","Metreküp",0),
    (10,4,"AD","Adet",1),(11,4,"KTN","Karton",0),(12,4,"KOL","Koli",0),
    (13,5,"M2","Metrekare",1),(14,5,"CM2","Santimetrekare",0),
    (15,6,"KW","Kilowatt",1),(16,6,"W","Watt",0),(17,6,"KWH","Kilowatt-saat",0),
    (18,7,"SA","Saat",1),(19,7,"DK","Dakika",0),(20,7,"SN","Saniye",0),
    (21,8,"C","Celsius",1),(22,8,"F","Fahrenheit",0),(23,8,"K","Kelvin",0),
    (24,11,"KG","Kilogram",1),(25,25,"AD","Adet",1),
])

# ── Birim Setleri Arası Çevrim Katsayıları ────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_UNITSETC (
    LOGICALREF  INTEGER PRIMARY KEY,
    UNITSETREF  INTEGER,
    FROMUNITREF INTEGER,
    TOUNITREF   INTEGER,
    CONVFACT    REAL,
    FOREIGN KEY (UNITSETREF)  REFERENCES LG_UNITSETF(LOGICALREF),
    FOREIGN KEY (FROMUNITREF) REFERENCES LG_UNITSETL(LOGICALREF),
    FOREIGN KEY (TOUNITREF)   REFERENCES LG_UNITSETL(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_UNITSETC VALUES (?,?,?,?,?)", [
    (1,1,1,2,1000),(2,1,1,3,0.001),(3,1,2,1,0.001),
    (4,2,4,5,100),(5,2,4,6,1000),(6,2,5,4,0.01),
    (7,3,7,8,1000),(8,3,7,9,0.001),(9,3,8,7,0.001),
    (10,4,10,11,12),(11,4,10,12,6),(12,4,11,10,0.0833),
    (13,5,13,14,10000),(14,5,14,13,0.0001),
    (15,6,15,16,1000),(16,6,16,15,0.001),(17,6,15,17,1),
    (18,7,18,19,60),(19,7,18,20,3600),(20,7,19,18,0.0167),
    (21,8,21,22,1.8),(22,8,21,23,273.15),(23,8,22,21,0.5556),
    (24,1,3,1,1000),(25,2,6,4,0.001),
])




# ── Malzemeler ────────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITEMS (
    LOGICALREF  INTEGER PRIMARY KEY,
    CODE        TEXT,
    NAME        TEXT,
    STGRPCODE   TEXT,
    UNITSETREF  INTEGER,
    CARDTYPE    INTEGER,
    SPECODE     TEXT,
    FOREIGN KEY (UNITSETREF) REFERENCES LG_UNITSETF(LOGICALREF)
)""")
items_data = [
    (1,"M001","Çelik Boru DN25 x 3mm","HAM",1,1,"SC001"),
    (2,"M002","Alüminyum Levha 2mm","HAM",1,1,"SC001"),
    (3,"M003","HDPE Boru 32mm","HAM",3,1,"SC002"),
    (4,"M004","Vida M6x20 Galvanizli","SAR",4,1,"SC001"),
    (5,"M005","Kompresör 5.5kW","MAK",4,1,"SC003"),
    (6,"M006","Elektrik Motoru 11kW","MAK",6,1,"SC003"),
    (7,"M007","Redüktör 1:10","MAK",4,1,"SC004"),
    (8,"M008","Rulman 6204","YED",4,1,"SC001"),
    (9,"M009","V-Kayış A45","YED",4,1,"SC002"),
    (10,"M010","Karton Kutu 40x30x20","AMB",4,1,"SC005"),
    (11,"M011","Shrink Film","AMB",1,1,"SC002"),
    (12,"M012","Polietilen Torba 60x80","AMB",4,1,"SC002"),
    (13,"M013","Trafo 100kVA","MAK",4,1,"SC003"),
    (14,"M014","Devre Kesici 63A","MAK",4,1,"SC003"),
    (15,"M015","Sensör PT100","ELK",4,1,"SC003"),
    (16,"M016","PLC Siemens S7","ELK",4,1,"SC003"),
    (17,"M017","Frekans İnvertörü 7.5kW","ELK",4,1,"SC003"),
    (18,"M018","Paslanmaz Çelik 304 Sac","HAM",1,1,"SC001"),
    (19,"M019","Bakır Kablo 4mm2 NYY","ELK",2,1,"SC003"),
    (20,"M020","Pnömatik Silindir ø63","PNM",4,1,"SC004"),
    (21,"M021","Hidrolik Pompa 250 bar","MAK",4,1,"SC004"),
    (22,"M022","Filtre Elemanı 10 mikron","YED",4,1,"SC004"),
    (23,"M023","O-Ring 50x3 EPDM","YED",4,1,"SC002"),
    (24,"M024","Yağlama Pompası","MAK",4,1,"SC004"),
    (25,"M025","Kontaktör 40A 380V","ELK",4,1,"SC003"),
]
cursor.executemany("INSERT INTO LG_ITEMS VALUES (?,?,?,?,?,?,?)", items_data)

# ── Malzeme-Birim Ataması ─────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMUNITA (
    LOGICALREF  INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    UNITSETREF  INTEGER,
    FOREIGN KEY (ITEMREF)    REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (UNITSETREF) REFERENCES LG_UNITSETF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMUNITA VALUES (?,?,?)", [
    (i, i, random.randint(1,5)) for i in range(1,26)
])

# ── Malzeme-Ambar Bilgileri ───────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_INVDEF (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    INVENREF    INTEGER,
    MINLEVEL    REAL,
    MAXLEVEL    REAL,
    SAFELEVEL   REAL,
    FOREIGN KEY (ITEMREF)   REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (INVENREF)  REFERENCES L_CAPIDEF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_INVDEF VALUES (?,?,?,?,?,?)", [
    (i, i, random.randint(6,14), random.uniform(10,50), random.uniform(500,2000), random.uniform(50,200))
    for i in range(1,26)
])

# ── Malzeme Alternatifleri ────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITEMSUBS (
    LOGICALREF  INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    SUBSITEMREF INTEGER,
    FACTOR      REAL DEFAULT 1,
    FOREIGN KEY (ITEMREF)     REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (SUBSITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
pairs = set()
rows = []
for ref in range(1,26):
    a = random.randint(1,25)
    b = random.randint(1,25)
    while b == a or (a,b) in pairs:
        b = random.randint(1,25)
    pairs.add((a,b))
    rows.append((ref, a, b, round(random.uniform(0.9,1.1),4)))
cursor.executemany("INSERT INTO LG_ITEMSUBS VALUES (?,?,?,?)", rows)

# ── Malzeme Özellik Ataması ───────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CHARASGN (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CHARREF     INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (CHARREF) REFERENCES LG_CHARCODE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CHARASGN VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,10)) for i in range(1,26)
])

# ── Malzeme-Özellik Değerleri ─────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SELCHVAL (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CHARVALREF  INTEGER,
    FOREIGN KEY (ITEMREF)    REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (CHARVALREF) REFERENCES LG_CHARVAL(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SELCHVAL VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

# ── Malzeme Hareketleri ───────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_STLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    STOCKREF    INTEGER,
    CLIENTREF   INTEGER,
    INVOICEREF  INTEGER,
    TRCODE      INTEGER,
    TOTAL       REAL,
    VATAMNT     REAL,
    AMOUNT      REAL,
    PRICE       REAL,
    DATE_       TEXT,
    
    CREATEDBY   INTEGER,
    
    FOREIGN KEY (STOCKREF)  REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF),
    FOREIGN KEY (CREATEDBY)  REFERENCES L_GOUSERS(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_STLINE VALUES (?,?,?,?,?,?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),
        random.randint(1,25),
        random.randint(1,25),
        random.choice([1,2,3,6,7,8]),
        rand_amount(),
        rand_amount(10,5000),
        round(random.uniform(1,500),2),
        round(random.uniform(5,2000),2),
        rand_date(),

        random.randint(1,25)   # CREATEDBY
    )
    for i in range(1,26)
])

# ── Stok Fişleri ──────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_STFICHE (
    LOGICALREF INTEGER PRIMARY KEY,
    FICHENO     TEXT,
    DATE_       TEXT,
    TRCODE      INTEGER,
    CLIENTREF   INTEGER,
    TOTAL       REAL,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_STFICHE VALUES (?,?,?,?,?,?)", [
    (i, f"STF{i:05}", rand_date(), random.randint(1,9), random.randint(1,25), rand_amount())
    for i in range(1,26)
])

# ── Stok Yerleri ──────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_LOCATION (
    LOGICALREF INTEGER PRIMARY KEY,
    INVENREF    INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (INVENREF) REFERENCES L_CAPIDEF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_LOCATION VALUES (?,?,?,?)", [
    (i, random.randint(6,14), f"LOC{i:03}", f"Raf {chr(64+(i-1)%26+1)}-{i:02}")
    for i in range(1,26)
])

# ── Günlük Malzeme Ambar Toplamları ──────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_STINVTOT (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    INVENREF    INTEGER,
    DATE_       TEXT,
    ONHAND      REAL,
    FOREIGN KEY (ITEMREF)  REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (INVENREF) REFERENCES L_CAPIDEF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_STINVTOT VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(6,14), rand_date(), round(random.uniform(0,1000),2))
    for i in range(1,26)
])

# ── Malzeme Alış/Satış Aylık Toplamları ──────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_STINVENS (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    PURCHASE    REAL,
    SALES       REAL,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_STINVENS VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])

# ── Malzeme Seri/Lot Bilgileri ────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SERILOTN (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CODE        TEXT,
    LOTNO       TEXT,
    EXPDATE     TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SERILOTN VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), f"SER{i:05}", f"LOT{random.randint(1000,9999)}", rand_date(2024,2026))
    for i in range(1,26)
])

# ── Seri/Lot Hareketleri ──────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SLTRANS (
    LOGICALREF INTEGER PRIMARY KEY,
    SLNREF      INTEGER,
    STLINEREF   INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    FOREIGN KEY (SLNREF)    REFERENCES LG_SERILOTN(LOGICALREF),
    FOREIGN KEY (STLINEREF) REFERENCES LG_STLINE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SLTRANS VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_date(), round(random.uniform(1,100),2))
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 4. FATURALAR & SİPARİŞLER
# ═══════════════════════════════════════════════════════════════════

# ── Ödeme Planları ────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PAYPLANS (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    INSTALLMENT INTEGER
)""")
cursor.executemany("INSERT INTO LG_PAYPLANS VALUES (?,?,?,?)", [
    (1,"PP001","Peşin",1),(2,"PP002","2 Taksit",2),(3,"PP003","3 Taksit",3),
    (4,"PP004","4 Taksit",4),(5,"PP005","6 Taksit",6),(6,"PP006","9 Taksit",9),
    (7,"PP007","12 Taksit",12),(8,"PP008","18 Taksit",18),(9,"PP009","24 Taksit",24),
    (10,"PP010","36 Taksit",36),(11,"PP011","Aylık Ödeme",12),(12,"PP012","Çeyreklik",4),
    (13,"PP013","Yarı Yıllık",2),(14,"PP014","Yıllık",1),(15,"PP015","Proje Ödemesi",5),
    (16,"PP016","Avans+3 Taksit",4),(17,"PP017","Avans+6 Taksit",7),
    (18,"PP018","50-50",2),(19,"PP019","30-30-40",3),(20,"PP020","10-90",2),
    (21,"PP021","Haftalık",52),(22,"PP022","15 Günlük",24),(23,"PP023","60 Günde Bir",6),
    (24,"PP024","90 Günde Bir",4),(25,"PP025","Özel Plan",0),
])

# ── Ödeme Plan Satırları ──────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PAYLINES (
    LOGICALREF  INTEGER PRIMARY KEY,
    PAYPLANREF     INTEGER,
    LINENUM     INTEGER,
    DUEDAY     INTEGER,
    RATE        REAL,
    FOREIGN KEY (PAYPLANREF) REFERENCES LG_PAYPLANS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PAYLINES VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), (i-1)%6+1, random.randint(0,180), round(random.uniform(10,100),2))
    for i in range(1,26)
])

# ── Ödeme/Tahsilat Hareketleri ────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PAYTRANS (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    TRCODE      INTEGER,
    STATUS      INTEGER,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_PAYTRANS VALUES (?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),
        rand_date(),
        rand_amount(),
        random.randint(1,4),
        random.randint(0,1)  # 0=open/unpaid, 1=paid/closed
    )
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_INVOICE (
    LOGICALREF  INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    FICHENO     TEXT,
    DATE_       TEXT,
    NETTOTAL    REAL,
    VATAMNT     REAL,
    GROSSTOTAL  REAL,
    TRCODE      INTEGER,
    
    PAYPLANREF  INTEGER,
    
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF),
    FOREIGN KEY (PAYPLANREF) REFERENCES LG_PAYPLANS(LOGICALREF)
)""")
invoice_data = []
for i in range(1,26):
    net   = rand_amount(500,100000)
    vat   = round(net*0.2, 2)
    gross = round(net+vat, 2)
    invoice_data.append((i, random.randint(1,25), f"FAT{i:05}", rand_date(),
                         net, vat, gross, random.choice([1,2,3,4,7,8]),
                         random.randint(1,25)   # PAYPLANREF
                         ))
cursor.executemany("INSERT INTO LG_INVOICE VALUES (?,?,?,?,?,?,?,?,?)", invoice_data)

# ── Sipariş Fişleri ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ORFICHE (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    FICHENO     TEXT,
    DATE_       TEXT,
    TOTAL       REAL,
    STATUS      INTEGER,

    SHIPADDR    TEXT,
    SHPAGENTREF INTEGER,
    SHPTYPEREF  INTEGER,

    FOREIGN KEY (CLIENTREF)   REFERENCES LG_CLCARD(LOGICALREF),
    FOREIGN KEY (SHPAGENTREF) REFERENCES L_SHPAGENT(LOGICALREF),
    FOREIGN KEY (SHPTYPEREF)  REFERENCES L_SHPTYPES(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_ORFICHE VALUES (?,?,?,?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),
        f"SIP{i:05}",
        rand_date(),
        rand_amount(),
        random.randint(0,3),

        random.choice([
            "İstanbul Depo",
            "Ankara Şube",
            "İzmir Lojistik Merkezi",
            "Bursa Fabrika",
            "Antalya Bölge Deposu"
        ]),

        random.randint(1,25),  # SHPAGENTREF
        random.randint(1,25)   # SHPTYPEREF
    )
    for i in range(1,26)
])

# ── Sipariş Hareketleri ───────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ORFLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    FICHEREF    INTEGER,
    STOCKREF    INTEGER,
    AMOUNT      REAL,
    PRICE       REAL,
    TOTAL       REAL,
    FOREIGN KEY (FICHEREF)  REFERENCES LG_ORFICHE(LOGICALREF),
    FOREIGN KEY (STOCKREF)  REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ORFLINE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25),
     round(random.uniform(1,500),2), round(random.uniform(10,5000),2), rand_amount())
    for i in range(1,26)
])

# ── Müstahsil Faturası ────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRODUCER (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    FICHENO     TEXT,
    DATE_       TEXT,
    TOTAL       REAL,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PRODUCER VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), f"MST{i:05}", rand_date(), rand_amount())
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 5. FİYATLAR & KOŞULLAR
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRCLIST (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    ITEMREF     INTEGER,
    PRICE       REAL,
    CURRENCY    INTEGER,
    BEGDATE     TEXT,
    ENDDATE     TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PRCLIST VALUES (?,?,?,?,?,?,?,?)", [
    (i, f"PL{i:03}", f"Fiyat Listesi {i}", random.randint(1,25),
     round(random.uniform(10,5000),2), random.randint(1,3),
     rand_date(2024,2024), rand_date(2025,2025))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ASCOND (
    LOGICALREF  INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    DISCRATE    REAL,
    PAYDAYS     INTEGER
)""")
cursor.executemany("INSERT INTO LG_ASCOND VALUES (?,?,?,?,?)", [
    (1,"AC001","Nakit Peşin",5.0,0),(2,"AC002","30 Gün Vadeli",0.0,30),
    (3,"AC003","60 Gün Vadeli",0.0,60),(4,"AC004","90 Gün Vadeli",0.0,90),
    (5,"AC005","Peşin+%3 İndirim",3.0,0),(6,"AC006","14 Gün %1 İndirim",1.0,14),
    (7,"AC007","120 Gün Vadeli",0.0,120),(8,"AC008","Konsinye",0.0,0),
    (9,"AC009","Havale+%2",2.0,0),(10,"AC010","Taksitli 12 Ay",0.0,360),
    (11,"AC011","Sipariş Avansı %50",0.0,30),(12,"AC012","Letter of Credit",0.0,45),
    (13,"AC013","Akreditif",0.0,60),(14,"AC014","Vadeli Çek",0.0,90),
    (15,"AC015","Banka Havalesi",0.0,0),(16,"AC016","Kredi Kartı",0.0,0),
    (17,"AC017","%5 Masraf Dahil",0.0,30),(18,"AC018","Özel Anlaşma",0.0,0),
    (19,"AC019","İhracat Ödeme",0.0,45),(20,"AC020","Avans %30 Kalan 60 Gün",0.0,60),
    (21,"AC021","2/10 Net 30",2.0,10),(22,"AC022","1/15 Net 45",1.0,15),
    (23,"AC023","EOM-30",0.0,30),(24,"AC024","Spot Fiyat",0.0,0),
    (25,"AC025","Uzun Vadeli 180 Gün",0.0,180),
])

# ── İndirim/Masraf Kartları ────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_DECARDS (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    CARDTYPE    INTEGER,
    RATE        REAL
)""")
cursor.executemany("INSERT INTO LG_DECARDS VALUES (?,?,?,?,?)", [
    (1,"D001","Genel İndirim",1,5.0),(2,"D002","Miktar İndirimi",1,10.0),
    (3,"D003","Promosyon İndirimi",1,15.0),(4,"D004","Sezon İndirimi",1,20.0),
    (5,"D005","Sadakat İndirimi",1,8.0),(6,"D006","Nakit İndirimi",1,3.0),
    (7,"D007","Kampanya İndirimi",1,12.0),(8,"D008","Sipariş İndirimi",1,7.0),
    (9,"M001","Nakliye Masrafı",2,0.0),(10,"M002","Sigorta Masrafı",2,0.0),
    (11,"M003","Ambalaj Masrafı",2,0.0),(12,"M004","Gümrük Masrafı",2,0.0),
    (13,"M005","Elleçleme Masrafı",2,0.0),(14,"M006","Depolama Masrafı",2,0.0),
    (15,"M007","Montaj Masrafı",2,0.0),(16,"M008","Test Masrafı",2,0.0),
    (17,"M009","Belgelendirme",2,0.0),(18,"M010","Danışmanlık",2,0.0),
    (19,"D009","VIP Müşteri",1,25.0),(20,"D010","Yeni Müşteri",1,2.0),
    (21,"D011","Yıl Sonu İndirimi",1,30.0),(22,"D012","İhracat İndirimi",1,5.0),
    (23,"M011","Akreditif Masrafı",2,0.0),(24,"M012","Kur Farkı Karşılığı",2,0.0),
    (25,"D013","Kombine İndirim",1,18.0),
])

# ── Promosyon Kartları ────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRCARDS (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    BEGDATE     TEXT,
    ENDDATE     TEXT,
    DISCRATE    REAL
)""")
cursor.executemany("INSERT INTO LG_PRCARDS VALUES (?,?,?,?,?,?)", [
    (i, f"PR{i:03}", f"Promosyon {i}", rand_date(2024,2024), rand_date(2025,2025),
     round(random.uniform(1,30),1))
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 6. KASA & BANKA
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_KSCARD (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    NAME  TEXT,
    CURRENCY    INTEGER
)""")
cursor.executemany("INSERT INTO LG_KSCARD VALUES (?,?,?,?)", [
    (1,"KAS01","TL Ana Kasası",1),(2,"KAS02","USD Kasası",2),
    (3,"KAS03","EUR Kasası",3),(4,"KAS04","İstanbul Kasası",1),
    (5,"KAS05","Ankara Kasası",1),(6,"KAS06","İzmir Kasası",1),
    (7,"KAS07","Bursa Kasası",1),(8,"KAS08","Adana Kasası",1),
    (9,"KAS09","Antalya Kasası",1),(10,"KAS10","Merkez Kasası",1),
    (11,"KAS11","GBP Kasası",4),(12,"KAS12","CHF Kasası",5),
    (13,"KAS13","SAR Kasası",6),(14,"KAS14","AED Kasası",7),
    (15,"KAS15","Yedek Kasası",1),(16,"KAS16","Mağaza Kasası",1),
    (17,"KAS17","Online Kasa",1),(18,"KAS18","POS Kasası",1),
    (19,"KAS19","Proje Kasası 1",1),(20,"KAS20","Proje Kasası 2",1),
    (21,"KAS21","Seyahat Kasası",2),(22,"KAS22","Temsil Kasası",1),
    (23,"KAS23","Avans Kasası",1),(24,"KAS24","Tahsilat Kasası",1),
    (25,"KAS25","Diğer Kasalar",1),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_KSLINES (
    LOGICALREF INTEGER PRIMARY KEY,
    CARDREF     INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (CARDREF) REFERENCES LG_KSCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_KSLINES VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), rand_date(), rand_amount(), random.randint(1,4))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CSHTOTS (
    LOGICALREF INTEGER PRIMARY KEY,
    CARDREF     INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    DEBIT       REAL,
    CREDIT      REAL,
    FOREIGN KEY (CARDREF) REFERENCES LG_KSCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CSHTOTS VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BNCARD (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    BANKNAME    TEXT
)""")
cursor.executemany("INSERT INTO LG_BNCARD VALUES (?,?,?,?)", [
    (1,"BNK01","Ziraat Bankası Merkez","Ziraat Bankası"),
    (2,"BNK02","İş Bankası İstanbul","İş Bankası"),
    (3,"BNK03","Garanti BBVA Ankara","Garanti BBVA"),
    (4,"BNK04","Akbank İzmir","Akbank"),
    (5,"BNK05","Yapı Kredi Bursa","Yapı Kredi"),
    (6,"BNK06","Halkbank Adana","Halkbank"),
    (7,"BNK07","VakıfBank Antalya","VakıfBank"),
    (8,"BNK08","Denizbank Konya","Denizbank"),
    (9,"BNK09","TEB Kocaeli","TEB"),
    (10,"BNK10","ING Bank İstanbul","ING Bank"),
    (11,"BNK11","QNB Finansbank","QNB Finansbank"),
    (12,"BNK12","HSBC Türkiye","HSBC"),
    (13,"BNK13","Şekerbank","Şekerbank"),
    (14,"BNK14","Odeabank","Odeabank"),
    (15,"BNK15","Türkiye Finans","Türkiye Finans"),
    (16,"BNK16","Kuveyt Türk","Kuveyt Türk"),
    (17,"BNK17","Albaraka Türk","Albaraka Türk"),
    (18,"BNK18","Burgan Bank","Burgan Bank"),
    (19,"BNK19","ICBC Turkey","ICBC"),
    (20,"BNK20","Fibabanka","Fibabanka"),
    (21,"BNK21","Türkiye Kalkınma Bankası","TKB"),
    (22,"BNK22","Eximbank","Eximbank"),
    (23,"BNK23","Citibank Türkiye","Citibank"),
    (24,"BNK24","Deutsche Bank TR","Deutsche Bank"),
    (25,"BNK25","BNP Paribas TR","BNP Paribas"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BANKACC (
    LOGICALREF INTEGER PRIMARY KEY,
    BANKREF     INTEGER,
    CODE        TEXT,
    IBAN        TEXT,
    CURRENCY    INTEGER,
    FOREIGN KEY (BANKREF) REFERENCES LG_BNCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BANKACC VALUES (?,?,?,?,?)", [
    (i, i, f"ACC{i:03}", f"TR{random.randint(10,99)}{random.randint(1000000000,9999999999)}{random.randint(10000000,99999999)}", random.randint(1,3))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BNFICHE (
    LOGICALREF INTEGER PRIMARY KEY,
    BANKACCREF  INTEGER,
    FICHENO     TEXT,
    DATE_       TEXT,
    TOTAL       REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (BANKACCREF) REFERENCES LG_BANKACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BNFICHE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), f"BNF{i:05}", rand_date(), rand_amount(), random.randint(1,4))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BNFLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    FICHEREF    INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (FICHEREF) REFERENCES LG_BNFICHE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BNFLINE VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), rand_date(), rand_amount(), random.randint(1,4))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BNTOTFIL (
    LOGICALREF  INTEGER PRIMARY KEY,
    BANKACCREF  INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    DEBIT       REAL,
    CREDIT      REAL,
    FOREIGN KEY (BANKACCREF) REFERENCES LG_BANKACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BNTOTFIL VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 7. ÇEK / SENET
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CSCARD (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    CLIENTREF   INTEGER,
    AMOUNT      REAL,
    DUEDATE     TEXT,
    CSTYPE      INTEGER,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_CSCARD VALUES (?,?,?,?,?,?)", [
    (
        i,
        f"CS{i:05}",
        random.randint(1,25),
        rand_amount(500,50000),
        rand_date(2024,2025),
        random.randint(1,2)
    )
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CSROLL (
    LOGICALREF INTEGER PRIMARY KEY,
    FICHENO     TEXT,
    DATE_       TEXT,
    TOTAL       REAL
)""")

cursor.executemany("INSERT INTO LG_CSROLL VALUES (?,?,?,?)", [
    (
        i,
        f"CSR{i:05}",
        rand_date(),
        rand_amount(1000,100000)
    )
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CSTRANS (
    LOGICALREF  INTEGER PRIMARY KEY,
    CARDREF     INTEGER,
    CSROLLREF   INTEGER,
    DATE_       TEXT,
    AMOUNT      REAL,
    TRCODE      INTEGER,
    FOREIGN KEY (CARDREF) REFERENCES LG_CSCARD(LOGICALREF),
    FOREIGN KEY (CSROLLREF) REFERENCES LG_CSROLL(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_CSTRANS VALUES (?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),   # CARDREF
        random.randint(1,25),   # CSROLLREF
        rand_date(),
        rand_amount(),
        random.randint(1,6)
    )
    for i in range(1,26)
])

# ═══════════════════════════════════════════════════════════════════
# 8. MUHASEBE
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMUHACC (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    PARENTCODE  TEXT,
    ACCTYPE     INTEGER
)""")
cursor.executemany("INSERT INTO LG_EMUHACC VALUES (?,?,?,?,?)", [
    (1,"100","Kasa",None,1),(2,"102","Bankalar",None,1),
    (3,"120","Alıcılar",None,1),(4,"121","Alacak Senetleri",None,1),
    (5,"150","İlk Madde ve Malzeme","15",1),(6,"152","Mamuller","15",1),
    (7,"153","Ticari Mallar","15",1),(8,"180","Gelecek Aylara Ait Giderler",None,1),
    (9,"191","İndirilecek KDV",None,1),(10,"200","Arazi ve Arsalar","20",2),
    (11,"252","Binalar","25",2),(12,"253","Tesis, Makine, Cihazlar","25",2),
    (13,"255","Demirbaşlar","25",2),(14,"257","Birikmiş Amortismanlar","25",2),
    (15,"300","Banka Kredileri",None,3),(16,"320","Satıcılar",None,3),
    (17,"321","Borç Senetleri",None,3),(18,"360","Ödenecek Vergi",None,3),
    (19,"391","Hesaplanan KDV",None,3),(20,"400","Banka Kredileri (Uzun)","40",3),
    (21,"500","Sermaye",None,4),(22,"590","Dönem Net Karı",None,4),
    (23,"600","Yurt İçi Satışlar",None,5),(24,"620","Satılan Ticari Mallar",None,5),
    (25,"770","Genel Yönetim Giderleri",None,6),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMFICHE (
    LOGICALREF INTEGER PRIMARY KEY,
    FICHENO     TEXT,
    DATE_       TEXT,
    TRCODE      INTEGER,
    DESCRIPTION TEXT
)""")
cursor.executemany("INSERT INTO LG_EMFICHE VALUES (?,?,?,?,?)", [
    (i, f"MUH{i:05}", rand_date(), random.randint(1,7),
     random.choice(["Tahsilat","Ödeme","Satış","Alış","Gider","Devir","Kapanış"]))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMFLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    FICHEREF    INTEGER,
    ACCREF      INTEGER,
    DEBIT       REAL,
    CREDIT      REAL,
    DATE_       TEXT,
    FOREIGN KEY (FICHEREF) REFERENCES LG_EMFICHE(LOGICALREF),
    FOREIGN KEY (ACCREF)   REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_EMFLINE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_amount(), rand_amount(), rand_date())
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMUHTOT (
    LOGICALREF INTEGER PRIMARY KEY,
    ACCREF      INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    DEBIT       REAL,
    CREDIT      REAL,
    FOREIGN KEY (ACCREF) REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_EMUHTOT VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ACCCODES (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    ACCREF      INTEGER,
    TRCODE      INTEGER,
    FOREIGN KEY (ACCREF) REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ACCCODES VALUES (?,?,?,?)", [
    (i, f"ENT{i:03}", random.randint(1,25), random.randint(1,9))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_CRDACREF (
    LOGICALREF INTEGER PRIMARY KEY,
    CLIENTREF   INTEGER,
    ACCREF      INTEGER,
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF),
    FOREIGN KEY (ACCREF)    REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_CRDACREF VALUES (?,?,?)", [
    (i, i, random.randint(1,25)) for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 9. HİZMET KARTLARI
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SRVCARD (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    PRICE       REAL,
    VATRATE     REAL
)""")
cursor.executemany("INSERT INTO LG_SRVCARD VALUES (?,?,?,?,?)", [
    (1,"HZ001","Montaj Hizmeti",500,20),(2,"HZ002","Bakım Hizmeti",350,20),
    (3,"HZ003","Tamir Hizmeti",420,20),(4,"HZ004","Teknik Destek",200,20),
    (5,"HZ005","Yazılım Geliştirme",1500,20),(6,"HZ006","Danışmanlık",800,20),
    (7,"HZ007","Eğitim Hizmeti",600,20),(8,"HZ008","Proje Yönetimi",1200,20),
    (9,"HZ009","Tasarım Hizmeti",900,20),(10,"HZ010","Test ve Kalibrasyon",450,20),
    (11,"HZ011","Kurulum Hizmeti",700,20),(12,"HZ012","Devreye Alma",650,20),
    (13,"HZ013","Periyodik Bakım",300,20),(14,"HZ014","Acil Müdahale",1000,20),
    (15,"HZ015","Uzaktan Destek",150,20),(16,"HZ016","Saha Hizmeti",550,20),
    (17,"HZ017","Nakliye Hizmeti",400,20),(18,"HZ018","Depolama Hizmeti",250,20),
    (19,"HZ019","Kalite Kontrol",350,20),(20,"HZ020","Sertifikasyon",800,20),
    (21,"HZ021","AR-GE Hizmeti",2000,20),(22,"HZ022","Lisanslama",500,20),
    (23,"HZ023","Abonelik Hizmeti",200,20),(24,"HZ024","Sigorta Hizmeti",300,20),
    (25,"HZ025","Finans Danışmanlığı",1000,20),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SRVUNITA (
    LOGICALREF INTEGER PRIMARY KEY,
    SRVREF      INTEGER,
    UNITSETREF  INTEGER,
    FOREIGN KEY (SRVREF)     REFERENCES LG_SRVCARD(LOGICALREF),
    FOREIGN KEY (UNITSETREF) REFERENCES LG_UNITSETF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SRVUNITA VALUES (?,?,?)", [
    (i, i, random.randint(4,7)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SRVNUMS (
    LOGICALREF INTEGER PRIMARY KEY,
    SRVREF      INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    QUANTITY    REAL,
    TOTAL       REAL,
    FOREIGN KEY (SRVREF) REFERENCES LG_SRVCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SRVNUMS VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024,
     round(random.uniform(1,50),1), rand_amount())
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SRVTOT (
    LOGICALREF INTEGER PRIMARY KEY,
    SRVREF      INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    PURCHASE    REAL,
    SALES       REAL,
    FOREIGN KEY (SRVREF) REFERENCES LG_SRVCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SRVTOT VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024, rand_amount(), rand_amount())
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 10. SATIŞ YÖNETİMİ
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SLSMAN (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_SLSMAN VALUES (?,?,?)", [
    (1,"SE001","Ahmet Yılmaz"),(2,"SE002","Mehmet Demir"),(3,"SE003","Ayşe Kaya"),
    (4,"SE004","Fatma Çelik"),(5,"SE005","Ali Şahin"),(6,"SE006","Zeynep Arslan"),
    (7,"SE007","Mustafa Aydın"),(8,"SE008","Elif Öztürk"),(9,"SE009","Hüseyin Koç"),
    (10,"SE010","Hatice Erdoğan"),(11,"SE011","İbrahim Doğan"),(12,"SE012","Emine Şimşek"),
    (13,"SE013","Yusuf Yıldız"),(14,"SE014","Merve Güneş"),(15,"SE015","Emre Aktaş"),
    (16,"SE016","Seda Polat"),(17,"SE017","Burak Çakır"),(18,"SE018","Neslihan Bozkurt"),
    (19,"SE019","Oğuzhan Keskin"),(20,"SE020","Derya Gündüz"),(21,"SE021","Sercan Parlak"),
    (22,"SE022","Gizem Uysal"),(23,"SE023","Tolga Kaplan"),(24,"SE024","Pınar Tekin"),
    (25,"SE025","Kadir Yılmaz"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SLSCLREL (
    LOGICALREF INTEGER PRIMARY KEY,
    SLSMANREF   INTEGER,
    CLIENTREF   INTEGER,
    FOREIGN KEY (SLSMANREF) REFERENCES LG_SLSMAN(LOGICALREF),
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SLSCLREL VALUES (?,?,?)", [
    (i, random.randint(1,25), i) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_TARGETS (
    LOGICALREF INTEGER PRIMARY KEY,
    SLSMANREF   INTEGER,
    YEAR_       INTEGER,
    MONTH_      INTEGER,
    TARGET      REAL,
    ACTUAL      REAL,
    FOREIGN KEY (SLSMANREF) REFERENCES LG_SLSMAN(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_TARGETS VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), 2024, random.randint(1,12),
     rand_amount(50000,500000), rand_amount(30000,500000))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ROUTE (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    SLSMANREF   INTEGER,
    FOREIGN KEY (SLSMANREF) REFERENCES LG_SLSMAN(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ROUTE VALUES (?,?,?,?)", [
    (i, f"ROT{i:03}", f"Rota {i} - Güzergah", random.randint(1,25))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ROUTETRS (
    LOGICALREF INTEGER PRIMARY KEY,
    ROUTEREF    INTEGER,
    CLIENTREF   INTEGER,
    VISITDAY    INTEGER,
    FOREIGN KEY (ROUTEREF)  REFERENCES LG_ROUTE(LOGICALREF),
    FOREIGN KEY (CLIENTREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ROUTETRS VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), random.randint(1,7))
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 11. ÇALIŞANLAR
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMPGROUP (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_EMPGROUP VALUES (?,?,?)", [
    (1,"EG01","Üretim"),(2,"EG02","Kalite"),(3,"EG03","Lojistik"),(4,"EG04","Satış"),
    (5,"EG05","Muhasebe"),(6,"EG06","İnsan Kaynakları"),(7,"EG07","Bilgi İşlem"),
    (8,"EG08","Bakım"),(9,"EG09","Ar-Ge"),(10,"EG10","Yönetim"),
    (11,"EG11","Pazarlama"),(12,"EG12","Satın Alma"),(13,"EG13","İdari İşler"),
    (14,"EG14","Güvenlik"),(15,"EG15","Temizlik"),(16,"EG16","Teknik Servis"),
    (17,"EG17","Proje"),(18,"EG18","İhracat"),(19,"EG19","İthalat"),
    (20,"EG20","Depo"),(21,"EG21","Sevkiyat"),(22,"EG22","Tahsilat"),
    (23,"EG23","Eğitim"),(24,"EG24","Hukuk"),(25,"EG25","Danışman"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMPLOYEE (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    NAME        TEXT,
    SURNAME     TEXT,
    STARTDATE   TEXT,
    GROUPREF    INTEGER,
    FOREIGN KEY (GROUPREF) REFERENCES LG_EMPGROUP(LOGICALREF)
)""")
names = [
    ("Ahmet","Yılmaz"),("Mehmet","Demir"),("Ayşe","Kaya"),("Fatma","Çelik"),
    ("Ali","Şahin"),("Zeynep","Arslan"),("Mustafa","Aydın"),("Elif","Öztürk"),
    ("Hüseyin","Koç"),("Hatice","Erdoğan"),("İbrahim","Doğan"),("Emine","Şimşek"),
    ("Yusuf","Yıldız"),("Merve","Güneş"),("Emre","Aktaş"),("Seda","Polat"),
    ("Burak","Çakır"),("Neslihan","Bozkurt"),("Oğuzhan","Keskin"),("Derya","Gündüz"),
    ("Sercan","Parlak"),("Gizem","Uysal"),("Tolga","Kaplan"),("Pınar","Tekin"),
    ("Kadir","Yılmaz"),
]
cursor.executemany("INSERT INTO LG_EMPLOYEE VALUES (?,?,?,?,?,?)", [
    (i+1, f"EMP{i+1:03}", names[i][0], names[i][1],
     rand_date(2015,2022), random.randint(1,25))
    for i in range(25)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMGRPASS (
    LOGICALREF INTEGER PRIMARY KEY,
    EMPREF      INTEGER,
    GROUPREF    INTEGER,
    FOREIGN KEY (EMPREF)   REFERENCES LG_EMPLOYEE(LOGICALREF),
    FOREIGN KEY (GROUPREF) REFERENCES LG_EMPGROUP(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_EMGRPASS VALUES (?,?,?)", [
    (i, i, random.randint(1,25)) for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 12. ÜRETİM
# ═══════════════════════════════════════════════════════════════════

# ── Operasyonlar ──────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_OPERTION (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    STDTIME     REAL
)""")
cursor.executemany("INSERT INTO LG_OPERTION VALUES (?,?,?,?)", [
    (1,"OP001","Kesme",15.0),(2,"OP002","Bükme",20.0),(3,"OP003","Kaynak",45.0),
    (4,"OP004","Delme",10.0),(5,"OP005","Tornalama",30.0),(6,"OP006","Frezeleme",35.0),
    (7,"OP007","Taşlama",25.0),(8,"OP008","Boyama",60.0),(9,"OP009","Kumlama",40.0),
    (10,"OP010","Montaj",90.0),(11,"OP011","Test",30.0),(12,"OP012","Paketleme",15.0),
    (13,"OP013","Isıl İşlem",120.0),(14,"OP014","Galvaniz",60.0),
    (15,"OP015","Kaplama",45.0),(16,"OP016","Dövme",30.0),(17,"OP017","Döküm",90.0),
    (18,"OP018","Enjeksiyon",20.0),(19,"OP019","Ekstrüzyon",25.0),
    (20,"OP020","Laminasyon",35.0),(21,"OP021","Kalite Kontrol",20.0),
    (22,"OP022","Sevk Hazırlama",10.0),(23,"OP023","Etiketleme",5.0),
    (24,"OP024","Depolama",10.0),(25,"OP025","Stok Sayımı",30.0),
])

# ── İş İstasyonları ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WORKSTAT (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    CAPACITY    REAL
)""")
cursor.executemany("INSERT INTO LG_WORKSTAT VALUES (?,?,?,?)", [
    (1,"WS001","CNC Torna",480.0),(2,"WS002","CNC Freze",480.0),
    (3,"WS003","Lazer Kesim",480.0),(4,"WS004","Pres",480.0),
    (5,"WS005","Kaynak Hücresi 1",480.0),(6,"WS006","Kaynak Hücresi 2",480.0),
    (7,"WS007","Montaj Bandı 1",480.0),(8,"WS008","Montaj Bandı 2",480.0),
    (9,"WS009","Boya Hattı",480.0),(10,"WS010","Paketleme Hattı",480.0),
    (11,"WS011","Test Laboratuvarı",480.0),(12,"WS012","Kalite Birimi",480.0),
    (13,"WS013","Isıl İşlem Fırını",240.0),(14,"WS014","Galvaniz Hattı",240.0),
    (15,"WS015","Enjeksiyon Makinesi",480.0),(16,"WS016","Ekstrüzyon Hattı",480.0),
    (17,"WS017","Vibrasyon Testi",480.0),(18,"WS018","Basınç Testi",480.0),
    (19,"WS019","Elektrik Testi",480.0),(20,"WS020","Sevkiyat Birimi",480.0),
    (21,"WS021","Otomasyon Hattı",480.0),(22,"WS022","Robot Kaynak",480.0),
    (23,"WS023","Koordinat Ölçüm",240.0),(24,"WS024","Spektrometre",120.0),
    (25,"WS025","3D Baskı",480.0),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSGRPF (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_WSGRPF VALUES (?,?,?)", [
    (1,"WSG01","Metal İşleme"),(2,"WSG02","Kaynak"),(3,"WSG03","Montaj"),
    (4,"WSG04","Yüzey İşleme"),(5,"WSG05","Test ve Kalite"),(6,"WSG06","Plastik"),
    (7,"WSG07","Elektronik"),(8,"WSG08","Paketleme"),(9,"WSG09","Isıl İşlem"),
    (10,"WSG10","Otomasyon"),(11,"WSG11","CNC İşleme"),(12,"WSG12","Döküm"),
    (13,"WSG13","Presler"),(14,"WSG14","Lazer İşleme"),(15,"WSG15","Boya Hattı"),
    (16,"WSG16","Sevkiyat"),(17,"WSG17","Depo"),(18,"WSG18","Ar-Ge"),
    (19,"WSG19","Pilot Üretim"),(20,"WSG20","Yedek Kapasite"),
    (21,"WSG21","Genel İmalat"),(22,"WSG22","Özel Makineler"),
    (23,"WSG23","El Aletleri"),(24,"WSG24","Ölçüm"),(25,"WSG25","3D Üretim"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSGRPASS (
    LOGICALREF  INTEGER PRIMARY KEY,
    WSREF       INTEGER,
    WSGRPREF    INTEGER,
    FOREIGN KEY (WSREF)    REFERENCES LG_WORKSTAT(LOGICALREF),
    FOREIGN KEY (WSGRPREF) REFERENCES LG_WSGRPF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_WSGRPASS VALUES (?,?,?)", [
    (i, i, random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSCHCODE (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_WSCHCODE VALUES (?,?,?)", [
    (1,"WSC01","Tezgah Tipi"),(2,"WSC02","Eksen Sayısı"),(3,"WSC03","Tabla Boyutu"),
    (4,"WSC04","Spindle Hızı"),(5,"WSC05","Besleme Hızı"),(6,"WSC06","Tolerans"),
    (7,"WSC07","Hassasiyet"),(8,"WSC08","Enerji Tüketimi"),(9,"WSC09","Ağırlık"),
    (10,"WSC10","Üretici Marka"),(11,"WSC11","Üretim Yılı"),(12,"WSC12","Son Bakım"),
    (13,"WSC13","Çalışma Süresi"),(14,"WSC14","OEE Skoru"),(15,"WSC15","MTBF"),
    (16,"WSC16","MTTR"),(17,"WSC17","Maks. Yük"),(18,"WSC18","Sıcaklık Aralığı"),
    (19,"WSC19","Yağ Tipi"),(20,"WSC20","Koruyucu Sınıf"),
    (21,"WSC21","Gürültü Seviyesi"),(22,"WSC22","Titreşim Seviyesi"),
    (23,"WSC23","Soğutma Tipi"),(24,"WSC24","Kontrol Sistemi"),(25,"WSC25","Yazılım"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSCHVAL (
    LOGICALREF INTEGER PRIMARY KEY,
    WSCODEREF   INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (WSCODEREF) REFERENCES LG_WSCHCODE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_WSCHVAL VALUES (?,?,?,?)", [
    (i, random.randint(1,25), f"WSCV{i:03}", f"Özellik Değeri {i}")
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSATTASG (
    LOGICALREF INTEGER PRIMARY KEY,
    WSREF       INTEGER,
    WSCODEREF   INTEGER,
    FOREIGN KEY (WSREF)     REFERENCES LG_WORKSTAT(LOGICALREF),
    FOREIGN KEY (WSCODEREF) REFERENCES LG_WSCHCODE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_WSATTASG VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_WSATTVAS (
    LOGICALREF INTEGER PRIMARY KEY,
    WSREF       INTEGER,
    WSCHVALREF  INTEGER,
    FOREIGN KEY (WSREF)      REFERENCES LG_WORKSTAT(LOGICALREF),
    FOREIGN KEY (WSCHVALREF) REFERENCES LG_WSCHVAL(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_WSATTVAS VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMWSDEF (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    WSREF       INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (WSREF)   REFERENCES LG_WORKSTAT(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMWSDEF VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMWSTOT (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    WSREF       INTEGER,
    DATE_       TEXT,
    QUANTITY    REAL,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (WSREF)   REFERENCES LG_WORKSTAT(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMWSTOT VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_date(), round(random.uniform(1,1000),2))
    for i in range(1,26)
])

# ── Ürün Reçeteleri ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BOMASTER (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BOMASTER VALUES (?,?,?,?)", [
    (i, i, f"BOM{i:03}", f"Reçete {i}") for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BOMREVSN (
    LOGICALREF INTEGER PRIMARY KEY,
    BOMREF      INTEGER,
    REVISION    TEXT,
    DATE_       TEXT,
    FOREIGN KEY (BOMREF) REFERENCES LG_BOMASTER(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BOMREVSN VALUES (?,?,?,?)", [
    (i, random.randint(1,25), f"REV{i:02}", rand_date())
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_BOMLINE (
    LOGICALREF INTEGER PRIMARY KEY,
    BOMREF      INTEGER,
    ITEMREF     INTEGER,
    AMOUNT      REAL,
    UNITREF     INTEGER,
    FOREIGN KEY (BOMREF)   REFERENCES LG_BOMASTER(LOGICALREF),
    FOREIGN KEY (ITEMREF)  REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (UNITREF)  REFERENCES LG_UNITSETL(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_BOMLINE VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25),
     round(random.uniform(0.1,100),3), random.randint(1,10))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMBOMAS (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    BOMREF      INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (BOMREF)  REFERENCES LG_BOMASTER(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMBOMAS VALUES (?,?,?)", [
    (i, i, i) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_COPRDBOM (
    LOGICALREF  INTEGER PRIMARY KEY,
    BOMREF      INTEGER,
    COPRODUCTREF INTEGER,
    AMOUNT      REAL,
    FOREIGN KEY (BOMREF)       REFERENCES LG_BOMASTER(LOGICALREF),
    FOREIGN KEY (COPRODUCTREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_COPRDBOM VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), round(random.uniform(0.01,10),3))
    for i in range(1,26)
])

# ── Üretim Rotaları ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ROUTING (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ROUTING VALUES (?,?,?,?)", [
    (i, i, f"RNG{i:03}", f"Rota {i}") for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_RTNGLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    ROUTINGREF  INTEGER,
    OPERTNREF   INTEGER,
    WSREF       INTEGER,
    SEQNO       INTEGER,
    SETUPTIME   REAL,
    RUNTIME     REAL,
    FOREIGN KEY (ROUTINGREF) REFERENCES LG_ROUTING(LOGICALREF),
    FOREIGN KEY (OPERTNREF)  REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (WSREF)      REFERENCES LG_WORKSTAT(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_RTNGLINE VALUES (?,?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), random.randint(1,25),
     i%10+1, round(random.uniform(5,60),1), round(random.uniform(10,120),1))
    for i in range(1,26)
])

# ── Üretim Emirleri ───────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRODORD (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    ORDNO       TEXT,
    PLANDATE    TEXT,
    DUEDATE     TEXT,
    AMOUNT      REAL,
    STATUS      INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PRODORD VALUES (?,?,?,?,?,?,?)", [
    (i, random.randint(1,25), f"UEM{i:05}", rand_date(),
     rand_date(2024,2025), round(random.uniform(10,500),1), random.randint(0,4))
    for i in range(1,26)
])

# ── İş Emirleri ───────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_DISPLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    PRODORDREF  INTEGER,
    WSREF       INTEGER,
    OPERTNREF   INTEGER,
    PLANDATE    TEXT,
    STATUS      INTEGER,
    FOREIGN KEY (PRODORDREF) REFERENCES LG_PRODORD(LOGICALREF),
    FOREIGN KEY (WSREF)      REFERENCES LG_WORKSTAT(LOGICALREF),
    FOREIGN KEY (OPERTNREF)  REFERENCES LG_OPERTION(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_DISPLINE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), random.randint(1,25),
     rand_date(), random.randint(0,3))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_OCCUPATN (
    LOGICALREF  INTEGER PRIMARY KEY,
    WSREF       INTEGER,
    PRODORDREF  INTEGER,
    DATE_       TEXT,
    USEDTIME    REAL,
    FOREIGN KEY (WSREF)      REFERENCES LG_WORKSTAT(LOGICALREF),
    FOREIGN KEY (PRODORDREF) REFERENCES LG_PRODORD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_OCCUPATN VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_date(), round(random.uniform(0.5,8),1))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PEGGING (
    LOGICALREF  INTEGER PRIMARY KEY,
    PRODORDREF  INTEGER,
    SALESORDREF INTEGER,
    AMOUNT      REAL,
    FOREIGN KEY (PRODORDREF)  REFERENCES LG_PRODORD(LOGICALREF),
    FOREIGN KEY (SALESORDREF) REFERENCES LG_ORFICHE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PEGGING VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), round(random.uniform(1,100),2))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_OPRTREQ (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    ITEMREF     INTEGER,
    AMOUNT      REAL,
    FOREIGN KEY (OPERTNREF) REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (ITEMREF)   REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_OPRTREQ VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), round(random.uniform(0.1,10),3))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_TOOLREQ (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    DEFINITION  TEXT,
    QUANTITY    INTEGER,
    FOREIGN KEY (OPERTNREF) REFERENCES LG_OPERTION(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_TOOLREQ VALUES (?,?,?,?)", [
    (i, random.randint(1,25), f"Alet/Takım {i}", random.randint(1,5))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_LABORREQ (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    EMPGROUPREF INTEGER,
    QUANTITY    INTEGER,
    FOREIGN KEY (OPERTNREF)   REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (EMPGROUPREF) REFERENCES LG_EMPGROUP(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_LABORREQ VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), random.randint(1,5))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_LNOPASGN (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    ITEMREF     INTEGER,
    FOREIGN KEY (OPERTNREF) REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (ITEMREF)   REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_LNOPASGN VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRVOPASG (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    PRVOPRTNREF INTEGER,
    FOREIGN KEY (OPERTNREF)   REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (PRVOPRTNREF) REFERENCES LG_OPERTION(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PRVOPASG VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_OPATTASG (
    LOGICALREF  INTEGER PRIMARY KEY,
    OPERTNREF   INTEGER,
    WSCODEREF   INTEGER,
    FOREIGN KEY (OPERTNREF)  REFERENCES LG_OPERTION(LOGICALREF),
    FOREIGN KEY (WSCODEREF)  REFERENCES LG_WSCHCODE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_OPATTASG VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PRDCOST (
    LOGICALREF  INTEGER PRIMARY KEY,
    PRODORDREF  INTEGER,
    MONTH_      INTEGER,
    YEAR_       INTEGER,
    MATERIALCOST REAL,
    LABORCOST   REAL,
    OVERHEAD    REAL,
    FOREIGN KEY (PRODORDREF) REFERENCES LG_PRODORD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_PRDCOST VALUES (?,?,?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,12), 2024,
     rand_amount(), rand_amount(100,5000), rand_amount(50,3000))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ENGCLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    CODE        TEXT,
    ITEMREF     INTEGER,
    BOMREF      INTEGER,
    DATE_       TEXT,
    DESCRIPTION TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (BOMREF)  REFERENCES LG_BOMASTER(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ENGCLINE VALUES (?,?,?,?,?,?)", [
    (i, f"ECR{i:04}", random.randint(1,25), random.randint(1,25),
     rand_date(), f"Mühendislik değişikliği {i} açıklaması")
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMFACTP (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    FACREF      INTEGER,
    LEADTIME    INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (FACREF)  REFERENCES L_CAPIDEF(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMFACTP VALUES (?,?,?,?)", [
    (i, i, random.randint(1,3), random.randint(1,30)) for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 13. KALİTE KONTROL
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_QCSET (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_QCSET VALUES (?,?,?)", [
    (1,"QC001","Girdi Kalite Kontrol"),(2,"QC002","Süreç Kalite Kontrol"),
    (3,"QC003","Final Kalite Kontrol"),(4,"QC004","Müşteri Ret Analizi"),
    (5,"QC005","Tedarikçi Değerlendirme"),(6,"QC006","Boyut Kontrol"),
    (7,"QC007","Yüzey Kontrol"),(8,"QC008","Malzeme Test Seti"),
    (9,"QC009","Fonksiyon Test Seti"),(10,"QC010","Güvenlik Test Seti"),
    (11,"QC011","Paket Kontrol"),(12,"QC012","Etiket Kontrol"),
    (13,"QC013","Sertifika Kontrol"),(14,"QC014","Isıl İşlem Kontrol"),
    (15,"QC015","Kaynak Kontrol"),(16,"QC016","Elektrik Test Seti"),
    (17,"QC017","Mekanik Test Seti"),(18,"QC018","Kimyasal Analiz"),
    (19,"QC019","NDT Kontrol"),(20,"QC020","Çevresel Test"),
    (21,"QC021","Yorulma Testi"),(22,"QC022","Darbe Testi"),
    (23,"QC023","Korozyon Testi"),(24,"QC024","Sızdırmazlık Testi"),
    (25,"QC025","Titreşim Testi"),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_QCSLINE (
    LOGICALREF INTEGER PRIMARY KEY,
    QCSETREF    INTEGER,
    CODE        TEXT,
    DEFINITION  TEXT,
    MINVAL      REAL,
    MAXVAL      REAL,
    FOREIGN KEY (QCSETREF) REFERENCES LG_QCSET(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_QCSLINE VALUES (?,?,?,?,?,?)", [
    (i, random.randint(1,25), f"QCSL{i:03}", f"Kontrol Kriteri {i}",
     round(random.uniform(0,50),2), round(random.uniform(50,100),2))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_QCLVAL (
    LOGICALREF  INTEGER PRIMARY KEY,
    QCSLINEREF  INTEGER,
    MEASUREDVAL REAL,
    RESULT      INTEGER,
    FOREIGN KEY (QCSLINEREF) REFERENCES LG_QCSLINE(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_QCLVAL VALUES (?,?,?,?)", [
    (i, random.randint(1,25), round(random.uniform(0,100),3), random.randint(0,1))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SLQCASGN (
    LOGICALREF INTEGER PRIMARY KEY,
    STLINEREF   INTEGER,
    QCSETREF    INTEGER,
    DATE_       TEXT,
    RESULT      INTEGER,
    FOREIGN KEY (STLINEREF) REFERENCES LG_STLINE(LOGICALREF),
    FOREIGN KEY (QCSETREF)  REFERENCES LG_QCSET(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SLQCASGN VALUES (?,?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), rand_date(), random.randint(0,1))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_QASGN (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    QCSETREF    INTEGER,
    FOREIGN KEY (ITEMREF)  REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (QCSETREF) REFERENCES LG_QCSET(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_QASGN VALUES (?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25)) for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 14. SABİT KIYMETLER
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_FAREGIST (
    LOGICALREF  INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    PURCHDATE   TEXT,
    PURCHCOST   REAL,
    USEFULLIFE  INTEGER
)""")
cursor.executemany("INSERT INTO LG_FAREGIST VALUES (?,?,?,?,?,?)", [
    (1,"SK001","CNC Tornalama Merkezi",rand_date(2018,2022),rand_amount(50000,500000),10),
    (2,"SK002","CNC Frezeleme Merkezi",rand_date(2019,2022),rand_amount(50000,500000),10),
    (3,"SK003","Lazer Kesim Makinesi",rand_date(2020,2023),rand_amount(100000,800000),10),
    (4,"SK004","Hidrolik Pres 200T",rand_date(2017,2021),rand_amount(80000,400000),15),
    (5,"SK005","Robot Kaynak Hücresi",rand_date(2021,2023),rand_amount(150000,600000),10),
    (6,"SK006","Boya Fırını",rand_date(2018,2022),rand_amount(40000,200000),15),
    (7,"SK007","Koordinat Ölçüm Makinesi",rand_date(2020,2023),rand_amount(60000,300000),10),
    (8,"SK008","Isıl İşlem Fırını",rand_date(2016,2020),rand_amount(30000,150000),20),
    (9,"SK009","Kompresör 132kW",rand_date(2019,2022),rand_amount(20000,80000),10),
    (10,"SK010","Forklift 3T",rand_date(2020,2023),rand_amount(15000,60000),5),
    (11,"SK011","Çatılı Alan A Blok",rand_date(2010,2015),rand_amount(500000,5000000),50),
    (12,"SK012","Çatılı Alan B Blok",rand_date(2012,2016),rand_amount(300000,3000000),50),
    (13,"SK013","İdari Bina",rand_date(2008,2012),rand_amount(1000000,8000000),50),
    (14,"SK014","Depo Binası",rand_date(2015,2019),rand_amount(200000,2000000),50),
    (15,"SK015","Arazi",rand_date(2005,2010),rand_amount(1000000,10000000),0),
    (16,"SK016","Ofis Mobilyası",rand_date(2020,2023),rand_amount(5000,50000),5),
    (17,"SK017","Sunucu Sistemi",rand_date(2021,2023),rand_amount(30000,150000),5),
    (18,"SK018","ERP Yazılımı",rand_date(2022,2023),rand_amount(50000,300000),5),
    (19,"SK019","Araç - Kamyon",rand_date(2019,2022),rand_amount(30000,200000),5),
    (20,"SK020","Araç - Binek",rand_date(2021,2023),rand_amount(20000,100000),5),
    (21,"SK021","Spektrometre",rand_date(2020,2023),rand_amount(40000,200000),10),
    (22,"SK022","3D Yazıcı",rand_date(2022,2023),rand_amount(10000,80000),5),
    (23,"SK023","Solar Panel Sistemi",rand_date(2022,2023),rand_amount(100000,500000),25),
    (24,"SK024","Güç Jeneratörü",rand_date(2019,2022),rand_amount(30000,150000),10),
    (25,"SK025","Havalandırma Sistemi",rand_date(2018,2022),rand_amount(15000,100000),15),
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_FAYEAR (
    LOGICALREF  INTEGER PRIMARY KEY,
    FAREF       INTEGER,
    YEAR_       INTEGER,
    DEPRAMOUNT  REAL,
    NETVALUE    REAL,
    FOREIGN KEY (FAREF) REFERENCES LG_FAREGIST(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_FAYEAR VALUES (?,?,?,?,?)", [
    (i, i, 2024, rand_amount(1000,50000), rand_amount(10000,400000))
    for i in range(1,26)
])


# ═══════════════════════════════════════════════════════════════════
# 15. DAĞITIM & ÖZEL KODLAR & DİĞER
# ═══════════════════════════════════════════════════════════════════

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_DISTTEMP (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_DISTTEMP VALUES (?,?,?)", [
    (i, f"DT{i:03}", f"Dağıtım Şablonu {i}") for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_DISTLINE (
    LOGICALREF  INTEGER PRIMARY KEY,
    DISTREF     INTEGER,
    ACCREF      INTEGER,
    RATE        REAL,
    FOREIGN KEY (DISTREF) REFERENCES LG_DISTTEMP(LOGICALREF),
    FOREIGN KEY (ACCREF)  REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_DISTLINE VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), round(random.uniform(1,100),2))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SPECODES (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    CODETYPE    INTEGER
)""")
cursor.executemany("INSERT INTO LG_SPECODES VALUES (?,?,?,?)", [
    (i, f"SC{i:03}", f"Özel Kod {i}", random.randint(1,5))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_SUPPASGN (
    LOGICALREF  INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    SUPPLIERREF INTEGER,
    LEADTIME    INTEGER,
    FOREIGN KEY (ITEMREF)     REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (SUPPLIERREF) REFERENCES LG_CLCARD(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_SUPPASGN VALUES (?,?,?,?)", [
    (i, i, random.randint(1,25), random.randint(1,30)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ITMCLSAS (
    LOGICALREF INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    CLASSCODE   TEXT,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_ITMCLSAS VALUES (?,?,?)", [
    (i, i, f"CLS{random.randint(100,999)}") for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_TRGPAR (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    VALUE_      TEXT
)""")
cursor.executemany("INSERT INTO LG_TRGPAR VALUES (?,?,?,?)", [
    (i, f"TRG{i:03}", f"Trigger Parametresi {i}", str(random.randint(0,1)))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_LOGREP (
    LOGICALREF INTEGER PRIMARY KEY,
    USERREF     INTEGER,
    DATE_       TEXT,
    ACTION      TEXT,
    TABLENAME   TEXT,
    STATUS      INTEGER,
    DESCRIPTION TEXT,
    FOREIGN KEY (USERREF) REFERENCES L_GOUSERS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_LOGREP VALUES (?,?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),
        rand_date(),
        random.choice(["INSERT","UPDATE","DELETE","SELECT"]),
        random.choice(["LG_CLCARD","LG_ITEMS","LG_INVOICE","LG_STLINE","LG_ORFICHE"]),
        random.choice([0,0,0,1]),   # 1 = başarısız
        random.choice([
            "İşlem başarılı",
            "Yetki hatası",
            "Veri doğrulama hatası",
            "Kayıt bulunamadı",
            "Transaction rollback"
        ])
    )
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_ERRORLOG (
    LOGICALREF INTEGER PRIMARY KEY,
    USERREF     INTEGER,
    DATE_       TEXT,
    MODULE      TEXT,
    ERRLEVEL    INTEGER,
    ERRMESSAGE  TEXT,
    FOREIGN KEY (USERREF) REFERENCES L_GOUSERS(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_ERRORLOG VALUES (?,?,?,?,?,?)", [
    (
        i,
        random.randint(1,25),
        rand_date(),
        random.choice([
            "Muhasebe",
            "Cari",
            "Stok",
            "Satış",
            "Üretim"
        ]),
        random.randint(1,3),
        random.choice([
            "Yetki hatası",
            "Validation error",
            "Kayıt bulunamadı",
            "SQL timeout",
            "Transaction rollback"
        ])
    )
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_LNGEXCSETS (
    LOGICALREF INTEGER PRIMARY KEY,
    TABLENAME   TEXT,
    FIELDNAME   TEXT,
    RECREF      INTEGER,
    LANGCODE    TEXT,
    DEFINITION  TEXT
)""")
cursor.executemany("INSERT INTO LG_LNGEXCSETS VALUES (?,?,?,?,?,?)", [
    (i, random.choice(["LG_ITEMS","LG_CLCARD","LG_SRVCARD"]),
     "NAME", random.randint(1,25),
     random.choice(["EN","DE","FR","AR","RU"]),
     f"Translation {i}")
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EMCENTER (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    ACCREF      INTEGER,
    FOREIGN KEY (ACCREF) REFERENCES LG_EMUHACC(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_EMCENTER VALUES (?,?,?,?)", [
    (i, f"MC{i:03}", f"Masraf Merkezi {i}", random.randint(1,25))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_TRANSAC (
    LOGICALREF INTEGER PRIMARY KEY,
    FIRMNR      INTEGER,
    PERIODNR    INTEGER,
    STATUS      INTEGER
)""")
cursor.executemany("INSERT INTO LG_TRANSAC VALUES (?,?,?,?)", [
    (i, 1, 2024, random.randint(0,1)) for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_STCOMPLN (
    LOGICALREF  INTEGER PRIMARY KEY,
    ITEMREF     INTEGER,
    COMPITEMREF INTEGER,
    AMOUNT      REAL,
    FOREIGN KEY (ITEMREF)     REFERENCES LG_ITEMS(LOGICALREF),
    FOREIGN KEY (COMPITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")
cursor.executemany("INSERT INTO LG_STCOMPLN VALUES (?,?,?,?)", [
    (i, random.randint(1,25), random.randint(1,25), round(random.uniform(1,20),2))
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_PERDOC (
    LOGICALREF INTEGER PRIMARY KEY,
    RECREF      INTEGER,
    TABLENAME   TEXT,
    DOCPATH     TEXT
)""")
cursor.executemany("INSERT INTO LG_PERDOC VALUES (?,?,?,?)", [
    (i, random.randint(1,25),
     random.choice(["LG_ITEMS","LG_CLCARD","LG_FAREGIST"]),
     f"/docs/doc_{i:04}.pdf")
    for i in range(1,26)
])

cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_FIRMDOC (
    LOGICALREF INTEGER PRIMARY KEY,
    CODE        TEXT,
    DEFINITION  TEXT,
    DOCPATH     TEXT
)""")
cursor.executemany("INSERT INTO LG_FIRMDOC VALUES (?,?,?,?)", [
    (i, f"FD{i:03}", f"Firma Dökümanı {i}", f"/firmadocs/fd_{i:04}.pdf")
    for i in range(1,26)
])

# ── Firma Bazlı Günlük Döviz Kurları ─────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS LG_EXCHANGE (
    LOGICALREF INTEGER PRIMARY KEY,
    FIRMNR      INTEGER,
    DATE_       TEXT,
    CURTYPE     INTEGER,
    BUYRATE     REAL,
    SELLRATE    REAL
)""")
cursor.executemany("INSERT INTO LG_EXCHANGE VALUES (?,?,?,?,?,?)", [
    (i, 1, rand_date(2024,2024), random.randint(1,3),
     round(random.uniform(30,37),4), round(random.uniform(30.1,37.2),4))
    for i in range(1,26)
])

# ── Maliyet Kapama / Costing ─────────────────────────────

cursor.execute("DROP TABLE IF EXISTS LG_PRDCOST")

cursor.execute("""
CREATE TABLE LG_PRDCOST (
    LOGICALREF INTEGER PRIMARY KEY,
    DATE_       TEXT,
    ITEMREF     INTEGER,
    COSTTYPE    INTEGER,
    TOTALCOST   REAL,
    AMOUNT      REAL,
    UNITCOST    REAL,
    PERIODNR    INTEGER,
    FOREIGN KEY (ITEMREF) REFERENCES LG_ITEMS(LOGICALREF)
)""")

cursor.executemany("INSERT INTO LG_PRDCOST VALUES (?,?,?,?,?,?,?,?)", [
    (
        i,
        rand_date(2022,2024),
        random.randint(1,25),
        random.randint(1,3),
        round(random.uniform(1000,50000),2),
        round(random.uniform(1,500),2),
        round(random.uniform(10,500),2),
        random.choice([202201,202202,202203,202301,202302,202303,202401,202402,202403])
    )
    for i in range(1,26)
])
# ─────────────────────────────────────────────
# KAYDET & KAPAT
# ─────────────────────────────────────────────
conn.commit()
conn.close()

print("✅ logo_tiger.db başarıyla oluşturuldu!")
print(f"   Toplam tablo sayısı: ~90")
print(f"   Her tabloda: 25 kayıt")