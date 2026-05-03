💽 SILICON_PULSE_v1.0
SSD Wear-Leveling Simulator (Educator Edition)
📌 Overview

SILICON_PULSE_v1.0 is an interactive, web-based educational application designed to visualize how modern SSDs work internally. It simulates key concepts such as wear-leveling, garbage collection, block lifecycle, and Write Amplification Factor (WAF) using an intuitive and visually rich interface.

The project transforms complex storage system concepts into a real-time, interactive learning experience using block-level visualization and scenario-based simulation.

🎯 Features
🔹 1200-Block Interactive Grid – Visual representation of NAND flash memory
🔹 Wear Distribution Heatmap – Color-coded block wear levels
🔹 Write Amplification (WAF) Visualization
🔹 Static vs Dynamic Wear-Leveling (UI-based)
🔹 Scenario Presets (Data Center, Office, Streaming, Stress Test)
🔹 Block Inspector Panel – View block state, cycles, and details
🔹 Faulty Block Simulation
🔹 Educational Resources & Glossary
🔹 Modern Dark UI (Tailwind CSS)
🧠 Purpose

This project is built to help:

Students understand SSD internals visually
Educators demonstrate storage concepts interactively
Enthusiasts explore low-level storage behavior
🏗️ Tech Stack
Frontend: React 19, Vite 8
Styling: Tailwind CSS v4
Routing: React Router DOM v7
Icons: Lucide React, Material Symbols
Utilities: clsx, tailwind-merge
Scripts: Python (HTML → JSX conversion)
📂 Project Structure
Paintball/  (internal codename)
│
├── index.html
├── package.json
├── vite.config.js
├── eslint.config.js
│
├── raw HTML prototypes
├── Python conversion scripts
│
├── src/ (to be generated)
│   ├── main.jsx
│   ├── App.jsx
│   └── pages/
│
└── dist/ (production build)
⚙️ Setup & Installation
1. Clone the repository
git clone https://github.com/your-username/silicon-pulse-ssd-simulator.git
cd silicon-pulse-ssd-simulator
2. Install dependencies
npm install
3. Generate React pages from HTML
python convert_all.py
4. Create missing core files

Manually create:

src/main.jsx
src/App.jsx
src/index.css
5. Fix Tailwind v4 issue ⚠️

Replace unsupported classes like:

bg-surface-container-high/60

with:

rgba(...) or valid Tailwind syntax

OR downgrade to Tailwind v3.

6. Run development server
npm run dev
7. Build project
npm run build
⚠️ Current Limitations
❌ No real SSD logic (UI-based simulation only)
❌ WAF is static (not calculated dynamically)
❌ Blocks are randomly generated
❌ Missing src/ in original ZIP (must be recreated)
❌ Tailwind v4 compatibility issue
🚀 Future Improvements
✅ Real wear-leveling algorithm implementation
✅ Dynamic WAF calculation
✅ Backend integration for data persistence
✅ Algorithm comparison mode
✅ Advanced analytics (IOPS, latency)
✅ Real SSD data integration
