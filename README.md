📑 README for UI Repo (home-test-ui)
# 🎬 Home Test – AQA (UI Automation)

## 📌 Project Overview
This repository contains **UI automation tests** for Twitch using **Selenium + Pytest**.  
The test runs in **Chrome Mobile Emulator (Pixel 2)** to simulate mobile behavior.

---

## ⚙️ Setup Instructions

### 1. Clone repo
```bash
git clone [<your-ui-repo-url>](https://github.com/soundaryakella/sportygroup-ui-automation-soundarya-kella.git)
cd home-test-ui

2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

▶️ Running Tests
python -m pytest tests/ui/test_twitch_mobile.py -v


Generate HTML report:

python -m pytest tests/ui/test_twitch_mobile.py --html=report.html --self-contained-html -v -s

📱 Test Case – Twitch Flow

Steps automated:

Open Twitch in mobile emulator (Pixel 2).

Click the search icon.

Enter StarCraft II.

Scroll down twice.

Select the first streamer.

Handle modal/popup if it appears.

Wait until streamer page fully loads.

Capture a screenshot.

✅ Screenshot saved in the screenshots/ folder.


## 🎥 Demo (Test Run GIF)
![Twitch Test Demo](gifs/twitch_test.gif)
