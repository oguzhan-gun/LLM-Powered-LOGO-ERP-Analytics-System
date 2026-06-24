# LLM Destekli ERP Sorgulama ve Analitik Sistemi

ERP verilerine, analizlere ve raporlama süreçlerine doğal dil aracılığıyla erişim sağlamak amacıyla geliştirilmiş yapay zekâ destekli bir asistandır.

## Genel Bakış

Bu proje, kullanıcıların ERP sistemleriyle doğal dil kullanarak etkileşim kurmasını sağlayarak manuel veritabanı sorgulama ve karmaşık raporlama süreçlerine olan ihtiyacı azaltmayı amaçlamaktadır.

Sistem; Büyük Dil Modelleri (LLM), Retrieval-Augmented Generation (RAG) ve akıllı sorgu yönlendirme mekanizmalarını bir araya getirerek bağlama duyarlı yanıtlar, veri analizleri ve raporlar üretmektedir.

## Temel Özellikler

* Doğal Dilden SQL'e Dönüşüm (Natural Language to SQL)
* Niyet (Intent) Tabanlı Akıllı Sorgu Yönlendirme
* Retrieval-Augmented Generation (RAG)
* Çok Ajanlı (Multi-Agent) LLM Mimarisi
* Dinamik Raporlama ve Analitik
* Otomatik Grafik ve Görselleştirme Üretimi
* Bağlama Duyarlı ERP Veri Erişimi

## Sistem Mimarisi

Platform, aşağıdaki bileşenlerden oluşan hibrit bir erişim ve akıl yürütme mimarisi kullanmaktadır:

* Niyet Analizi (Intent Analysis)
* Bağlam Erişimi (Context Retrieval)
* Sorgu Doğrulama (Query Verification)
* Sorgu Üretimi (Query Generation)
* Yanıt Üretimi (Response Generation)
* Analitik ve Görselleştirme

## Kullanılan Teknolojiler

* Python
* Gemini 2.5 Flash-Lite
* Retrieval-Augmented Generation (RAG)
* BM25
* Vektör Gömme (Vector Embeddings)
* SQL Server
* Multi-Agent Sistemler
* Veri Görselleştirme

## Sonuçlar

* 500'den fazla ERP odaklı sorgu üzerinde değerlendirilmiştir.
* Test senaryolarında %95'in üzerinde tatmin edici yanıt başarısı elde edilmiştir.
* Ortalama yanıt süresi 3–5 saniye arasındadır.

## Not

Bu depo, projenin yalnızca genel bir özetini sunmaktadır. Detaylı uygulama mimarisi, iş kuralları, özel veri setleri ve şirkete özgü bileşenler güvenlik ve gizlilik gerekçeleriyle paylaşılmamaktadır.
