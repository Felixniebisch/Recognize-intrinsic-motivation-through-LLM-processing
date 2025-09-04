# 🧠 Recognizing Intrinsic Motivation through LLM Processing

This repository contains the code and prompt logic for a research project investigating whether large language models (LLMs), such as GPT-4, can accurately predict **intrinsic motivation** based on open-ended, free-text descriptions of participants’ primary activities. Predictions are evaluated against scores from the validated **Intrinsic Motivation Inventory (IMI)**, grounding the project in **Self-Determination Theory** (Ryan & Deci, 2000).

---

## 📌 Overview

- **Language model:** GPT-4-turbo via OpenAI API
- **Task:** Predict Likert-scale subscale scores (1–7) for IMI dimensions
- **Method:** Prompt engineering + chain-of-thought style scoring
- **Comparison:** LLM scores vs. ground-truth self-reports (IMI questionnaire)
- **Key metrics:** Spearman's ρ, MAE, non-linear prediction bias

---

## 🧾 Project Structure

| File | Purpose |
|------|---------|
| `PoC - main script.py` | Main control script: loops over participants, prompts GPT-4, saves predictions |
| `initialization_prompt.py` | Sets up initialization/system prompt using LangGPT-style multilevel design |
| `compute_averages.py` | Aggregates responses and applies scoring logic |
| `reversed_scales.py` | Handles subscale items that are reverse-coded |
| `PydanticClasses.py` | Provides structured data validation for responses |

---

## 🧪 Installation

This project uses Python 3.11+. Install required packages via:

```bash
pip install openai pandas numpy scipy statsmodels pydantic python-dotenv
