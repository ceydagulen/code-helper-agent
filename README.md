# 🧠 Code Helper Agent

Bir Python kod tabanını okuyup **RAG (Retrieval-Augmented Generation)** ile analiz eden, komut satırından çalışan yapay zeka kod asistanı.

Projenin klasörünü verirsiniz; ajan kodu parçalara ayırır, vektör veritabanına indeksler ve ardından kod hakkında sorduğunuz soruları — hatalar, iyileştirme önerileri, okunabilirlik, performans ve bakım kolaylığı — **ilgili kod parçalarını bağlam olarak kullanarak** yanıtlar.

---

## ✨ Özellikler

- **Kod tabanı yükleme** — Verilen klasördeki tüm `.py` dosyaları alt klasörlerle birlikte taranır
- **Akıllı parçalama (chunking)** — `RecursiveCharacterTextSplitter` ile 800 karakterlik, 100 karakter örtüşmeli parçalar
- **Vektör arama** — OpenAI embedding'leri + FAISS ile her soruya en ilgili 4 kod parçası bulunur
- **Kıdemli mühendis bakışı** — Sistem prompt'u; sorunları açıkça anlatmaya ve dosyaları baştan yazmak yerine hedefli iyileştirme önermeye odaklanır
- **Etkileşimli CLI** — İndeksleme bir kez yapılır, ardından istediğiniz kadar soru sorabilirsiniz
- **Kaynak takibi** — Her parça, geldiği dosyanın yolunu metadata olarak taşır

---

## 🏗️ Mimari

```
Kod klasörü
   │
   ▼
repo_loader.py   →  .py dosyalarını okur  ({path, content})
   │
   ▼
chunker.py       →  800 karakter / 100 örtüşme ile parçalar
   │
   ▼
embeddings.py    →  OpenAI Embeddings + FAISS vektör deposu
   │
   ▼
agent.py         →  Retriever (k=4) → Prompt → GPT-4o-mini → Yanıt
   │
   ▼
main.py          →  Komut satırı soru-cevap döngüsü
```

---

## 🛠️ Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Dil | Python 3.10+ |
| LLM orkestrasyonu | LangChain (LCEL zinciri) |
| LLM | OpenAI GPT-4o-mini (temperature = 0) |
| Embedding | OpenAI Embeddings |
| Vektör veritabanı | FAISS (CPU) |
| Metin bölme | LangChain Text Splitters |
| Ortam değişkenleri | python-dotenv |

---

## 🚀 Kurulum

**1. Projeyi klonlayın**
```bash
git clone https://github.com/ceydagulen/code-helper-agent.git
cd code-helper-agent
```

**2. Sanal ortam oluşturun ve bağımlılıkları yükleyin**
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. API anahtarını ayarlayın**

Proje klasöründe bir `.env` dosyası oluşturun:
```env
OPENAI_API_KEY=sk-...
```

---

## ▶️ Kullanım

Analiz etmek istediğiniz projenin **bilgisayarınızdaki klasör yolunu** verin:

```bash
python main.py --repo /path/to/your/project
```

Bir GitHub projesini analiz etmek için önce klonlayın:
```bash
git clone https://github.com/kullanici/proje.git
python main.py --repo ./proje
```

### Örnek oturum

```
🚀 Code Helper Agent started

📥 Loading repository:
   ./proje

✂️  Chunking code...

🧠 Building embeddings (this may take a minute)...

✅ Ready! Ask questions about the code.
Type 'exit' or 'quit' to stop.

❓ > Veritabanı bağlantısı nerede kuruluyor, bir sorun var mı?
❓ > Bu projede tekrar eden kod var mı?
❓ > main.py'nin okunabilirliğini nasıl artırabilirim?
❓ > exit

👋 Bye!
```

---

## 📁 Proje Yapısı

```
code-helper-agent/
├── main.py           # CLI giriş noktası ve soru-cevap döngüsü
├── repo_loader.py    # Klasördeki .py dosyalarını okur
├── chunker.py        # Kodu örtüşmeli parçalara böler
├── embeddings.py     # Embedding'leri üretir, FAISS indeksini kurar
├── agent.py          # Retriever + prompt + LLM zinciri
├── prompts.py        # Sistem prompt'u
└── requirements.txt
```

---

## 🔭 Geliştirme Fikirleri

- GitHub URL'sinden doğrudan klonlama
- Python dışındaki diller için destek (`.js`, `.java`, `.ts` …)
- FAISS indeksini diske kaydedip tekrar kullanma
- Yanıtlarda kaynak dosya yollarını gösterme
- Sohbet geçmişi (çok turlu bağlam)

---

## 👩‍💻 Geliştirici

**Ceyda Gülen** — Bilgisayar Mühendisliği, Bursa Teknik Üniversitesi
[GitHub](https://github.com/ceydagulen)
