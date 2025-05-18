# 🍽️ Barbeque Nation Virtual Booking Assistant — Formi Intern Assignment

## 📌 Overview

This is a voice+text conversational agent built using **Retell AI** + **Flask** that answers enquiries, takes bookings, and handles FAQs for **Barbeque Nation outlets in Delhi and Bangalore**.

The agent supports:
- 📍 Location-based outlet info
- 📅 New bookings (collects name, number, pax, date)
- ❓ FAQs (Jain food, halal, drinks, kulfi)
- 🕒 Outlet timings
- 🔁 Modify / Cancel bookings

---

## 🧠 Architecture

User → Retell AI (Multi-Prompt Agent)
→ State Machine (Prompt Templates)
→ Tool (get_branch_info) → Flask API → JSON KB (by outlet)


---

## 🗂️ Folder Structure

Barbeque-Nation-Voice-AI/
├── api/
│ └── main.py # Flask backend with /kb, /menu, /properties
├── kb/
│ ├── indiranagar.json
│ ├── koramangala.json
│ ├── jpnagar.json
│ ├── electronic_city.json
│ ├── counnaught.json
│ ├── unity_mall.json
│ ├── vasant_kunj.json
│ └── menu.json # Optional general menu info
├── states/
│ ├── collect_location.jinja
│ ├── collect_name_number.jinja
│ ├── collect_pax.jinja
│ ├── collect_date.jinja
│ ├── modify_booking.jinja
│ ├── faq_handler.jinja
│ ├── confirm_booking.jinja
│ └── outlet_info.jinja
├── post_call_logging/ # (Optional) logging via JSON or Sheets
│ └── logs.json
├── chatbot-frontend/ # (Optional) Web UI
│ └── index.html
├── README.md
└── requirements.txt


---

## ⚙️ Tech Stack

- 🐍 Python + Flask (API backend)
- 🧾 JSON knowledge base per outlet
- 🔁 Retell AI (multi-prompt agent)
- 🧠 Jinja2-based prompt templates
- (Optional) Google Sheets logging

---

## 🧾 API Endpoints

| Route                    | Description                            |
|--------------------------|----------------------------------------|
| `/kb/<location>`         | Returns structured JSON for outlet     |
| `/properties`            | Lists all available outlets            |
| `/menu` (optional)       | Returns global menu/FAQ content        |

---

## 🧠 Retell Agent States

| State Name            | Template Used           | Description                        |
|-----------------------|-------------------------|------------------------------------|
| `start`               | Static greeting         | Welcomes the user                  |
| `collect_location`    | collect_location.jinja  | Asks for city/outlet               |
| `collect_name_number` | collect_name_number.jinja | Collects & confirms contact info |
| `collect_pax`         | collect_entity.jinja    | Asks for number of guests          |
| `collect_date`        | collect_entity.jinja    | Collects booking date              |
| `confirm_booking`     | inform_property.jinja   | Confirms full booking              |
| `modify_booking`      | collect_entity.jinja    | Collects what user wants to change |
| `faq_handler`         | inform_property.jinja   | Answers menu & food FAQs           |
| `information_timings` | inform_property.jinja   | Gives outlet hours                 |
| `outlet_info`         | tool-based              | Answers PDR, valet, baby chair     |
| `fallback`            | Static fallback         | Handles invalid queries            |

---

## 🔗 Retell Agent Link

👉 [https://dashboard.retellai.com/agents/agent_54a381e1edc692c65e133c235b]

---

## 🧪 How to Run Locally

```bash
cd api
python main.py


Access at http://localhost:5000/kb/indiranagar

Test endpoints like /properties, /menu


---


- barbeque_nation_chatbot [https://dashboard.retellai.com/agents/agent_54a381e1edc692c65e133c235b]
- SOUMILI PAL with your Soumili Pal


