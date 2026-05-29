# 🏥⚡ Crisis Medical Analyzer

**A 100% Offline Edge-Computing Medical Continuity System for Crisis Situations**

Crisis Medical Analyzer is a fully **offline, edge-computing healthcare application** designed to maintain **clinical workflow continuity during hospital grid power failures, internet blackouts, or emergency situations**.

Healthcare staff can use available **power-managed devices** (laptops, tablets, or mobile phones) connected through a **local isolated Wi-Fi hotspot** to capture photos of **handwritten patient charts**.

Using **Gemma 4 E2B running locally inside LM Studio**, the system instantly:

* 📝 **Transcribes handwritten medical notes**
* 🚨 **Performs clinical triage**
* 📊 **Extracts strict structured JSON medical data**
* 🔒 **Operates with zero cloud dependency**

This ensures **privacy, resilience, and uninterrupted medical workflows** even in disconnected environments.

---

# 🚀 Key Features

* ✅ **100% Offline Processing**
* ✅ **Zero Internet Dependency**
* ✅ **Handwritten Medical Chart OCR**
* ✅ **AI-Based Clinical Summarization**
* ✅ **Critical Risk Flag Detection**
* ✅ **Structured JSON Extraction**
* ✅ **Emergency LAN-Based Device Access**
* ✅ **Local OpenAI-Compatible API using LM Studio**

---

# 🛠️ Tech Stack

| Component        | Technology        |
| ---------------- | ----------------- |
| Backend          | Flask             |
| AI Model         | Gemma 4 E2B       |
| Model Runtime    | LM Studio         |
| Image Processing | Pillow            |
| API Interface    | OpenAI Python SDK |
| Frontend         | HTML              |

---

# 📦 Prerequisites & Installation

## 1. Install Python Dependencies

Install required packages:

```bash
pip install flask openai pillow
```

---

## 2. Project Folder Structure

Create your project folder using the following architecture:

```plaintext
medical_app/
│
├── app.py              # Flask server orchestration logic
│
└── templates/
    └── index.html      # Independent web dashboard
```

---

# 🧠 Setting Up LM Studio Local Server

Follow these steps to configure the **offline inference engine**.

## Step 1: Launch LM Studio

Open **LM Studio** on your primary workstation.

---

## Step 2: Download Gemma 4 E2B

1. Navigate to the **Search** tab on the left sidebar.
2. Search for:

```plaintext
Gemma 4 E2B
```

3. Download the **multimodal / vision variant** of the model.

This downloads all model files locally to your machine.

---

## Step 3: Open Local Server

Navigate to the **Local Server** tab
(identified by the `<->` icon in the sidebar).

---

## Step 4: Load the Model

At the top-center model dropdown:

Select:

```plaintext
Gemma 4 E2B
```

LM Studio will load the model into execution memory.

---

## Step 5: Configure Server Settings

Verify the following settings:

| Setting | Value   |
| ------- | ------- |
| Port    | `1234`  |
| CORS    | Enabled |

> Enable **CORS** if multiple local devices or terminals will connect to the server.

---

## Step 6: Start the Server

Click the green:

```plaintext
Start Server
```

button.

If successful, LM Studio will expose an **OpenAI-compatible local endpoint**:

```plaintext
http://localhost:1234
```

---

# 💻 Running the Application

## Step 1: Navigate to Project Directory

```bash
cd medical_app
```

---

## Step 2: Start Flask Server

```bash
python app.py
```

---

## Step 3: Open the Web Dashboard

Visit:

```plaintext
http://127.0.0.1:5000
```

---

# 📡 Emergency Deployment (LAN Mode)

For emergency hospital deployment where multiple staff devices need access:

Instead of `localhost`, use your workstation’s **LAN IP address**.

Example:

```plaintext
http://192.168.1.45:5000
```

This allows:

* 📱 Mobile phones
* 💻 Laptops
* 📟 Tablets
* 🖥️ Local emergency terminals

to access the platform over an **isolated local Wi-Fi network**.

---

# 📊 Standardized JSON Response Contract

The AI backend is constrained to return responses in the following strict schema:

```json
{
    "extracted_text": "Complete transcribed string matching the uploaded handwritten note.",
    "summary": "Brief clinical case overview.",
    "critical_flags": "High-risk warnings, vital parameter anomalies, or urgent alerts.",
    "action_items": "Recommended backup interventions or standard emergency protocols."
}
```

---

# 🔒 Privacy & Security

Since all inference happens **entirely on-device**:

* No patient data leaves the hospital network
* No cloud processing involved
* HIPAA/privacy-friendly architecture
* Suitable for emergency offline environments

---

# 🌍 Use Cases

* Hospital power failures
* Internet blackouts
* Disaster relief camps
* Rural medical centers
* Military field hospitals
* Temporary emergency clinics

---

# 🏁 Future Enhancements

* Multi-language medical handwriting support
* Patient risk scoring
* Offline patient history tracking
* LAN-wide multi-user synchronization
* Medical dashboard analytics
* Voice-assisted emergency triage

---

## 👨‍⚕️ Built for Crisis Resilience

**When the cloud fails, healthcare should not.**
