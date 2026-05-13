# 📚 BookStream-AI
**The Ultimate Pipeline for Intelligent Book Summarization & Formatting**

BookStream-AI is a suite of Python tools designed to handle the full lifecycle of digital book processing—from size optimization to AI-driven synthesis and professional document styling.

---

## 🏗️ System Components

The project consists of three core modules working in harmony:

### 1. 📂 PDF Optimizer (Compressor)
- **Purpose:** Reduces the footprint of high-resolution textbooks for faster API uploads.
- **Tech:** Utilizes `PyMuPDF` and image compression algorithms.
- **Goal:** Ensure large medical or technical books fit within Google File API limits without losing text clarity.

### 2. 🤖 AI Summarization Engine (Gemini API)
- **Purpose:** Acts as a "Subject Matter Expert" to analyze and distill content.
- **Features:** 
    - **Context-Aware:** Processes chunks of 30-50 pages as a single cohesive unit.
    - **Safety-First:** Hardened prompts to bypass safety filters in clinical/sensitive topics.
    - **High-Yield Output:** Focuses on diagnostic criteria, management, and key definitions.

### 3. 🎨 Document Architect (Styler & Merger)
- **Purpose:** Transforms raw AI text into a "Study-Ready" Microsoft Word document.
- **Design Logic:**
    - **Visual Comfort:** Implements a specialized color palette: 
        - Primary Headers: `RGB(31, 58, 86)` (Quiet Deep Blue).
        - Body Text: `RGB(87, 101, 116)` (Soft Slate Grey).
    - **Annotation Layout:** Sets a **2.5-inch right margin** specifically for manual note-taking.
    - **Structure:** Automatically parses bold terms and nested bullet points.

---
##2. Install Dependencies:
###pip install google-generativeai python-docx PyMuPDF docxcompose

3. **Configure API:**
   Add your Google Gemini API Key to your environment variables or `config.py`.

---

## 🚀 Execution Flow

1. **Compress:** Run `compressorbooks.py` to prepare your PDF.
2. **Summarize:** Run `books.py` to generate the AI content.


## 🎨 Visual Identity
| Element | Hex Code | RGB | Purpose |
| :--- | :--- | :--- | :--- |
| **Headers** | `#1F3A56` | (31, 58, 86) | High Focus |
| **Content** | `#576574` | (87, 101, 116) | Eye-Strain Reduction |

---
*Created by Ahmed El-dabea.*

