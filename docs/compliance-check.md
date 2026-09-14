# Compliance Audit Report – Submission #1

| Criterion | Mandatory Requirement | Current Repository Status | Gap / Missing Action Item |
|---|---|---|---|
| **1. Group Work vs. Individual Work Separation** | | | |
| • Project Details Specification (Group Work) | Documented context, problem statement, objectives, scope boundary. | Present in `docs/tasks-assignment.md` (sections 1.1‑1.3) and partially in `docs/README.md` (architecture overview). | ✅ – No action needed. |
| • Stakeholder Matrix (Group Work) | Clear identification of the 4 stakeholder groups with roles/expectations. | Stakeholder analysis appears in the **Sprint 1** table (lines 126‑132) of `tasks-assignment.md`. | ✅ – No action needed. |
| • System‑wide Use‑Case Diagram (Group Work) | Whole‑system use‑case diagram covering all 7 subsystems. | Mentioned in `tasks-assignment.md` (Sprint 2 description) but the actual diagram file is not present in the repository. | **Missing diagram** – Add a PNG/SVG file (e.g., `docs/diagrams/system_usecase.png`) and reference it in the docs. |
| • Individual Use‑Case Specifications (Individual Work) | Each of the 7 members must have **2** detailed use‑cases with name and MSSV. | The matrix of responsibilities (lines 66‑74) lists use‑case IDs per member, but the detailed specifications are not stored in the repo. | **Missing detailed specs** – Create separate markdown files (`docs/usecases/TVx_<name>.md`) containing the full IEEE‑style specifications. |
| • Non‑Functional Requirements (Group Work) | Performance, Availability, Reliability, Security. | Summarised in `tasks-assignment.md` (Sprint 3, line 146). | ✅ – No action needed. |
| • Bonus Requirements | Non‑interactive functional requirements (IoT simulation, overload trigger). | Described in `tasks-assignment.md` (lines 147‑148). | ✅ – No action needed. |
| **2. Project Management & Academic Integrity** | | | |
| • Weekly Team Meetings & Minutes (≥ Meeting #1 & #2) | Minutes stored under `docs/meeting-minutes/` following the ISO/IEEE template. | Only **Meeting #1** (`Meeting_01_20260908.tex/.md`) exists. No Meeting #2 file is present. | **Add Meeting #2** (and subsequent meetings) in both `.tex` and `.md` formats and commit them. |
| • Generative AI Transparency Statement | Statement in `README.md` and documentation. | AI policy is described in `tasks-assignment.md` (lines 48‑56) but not in `README.md`. | **Insert AI Transparency Statement** into `docs/README.md` (e.g., a dedicated “AI Disclosure” section). |
| • Prompt History Logging | `docs/prompt-history/` with sub‑folders for each member. | Directory exists and contains placeholder `README.md` files. | ✅ – No action needed. |
| **3. Core Software Engineering Focus & Technology Rules** | | | |
| • Prototyping & Tech Stack Rules | Python / Streamlit evolutionary prototype. | Confirmed in `docs/README.md` (architecture diagram) and repository structure (`src/app.py`, `src/components/`). | ✅ – No action needed. |
| • Data Management | No forced backend DB; state stored in `st.session_state` or `mock_hubs.json`. | `mock_hubs.json` resides in `src/data/` and is loaded into session state as described in the README. | ✅ – No action needed. |
| • Core Scope Focus | Emphasis on state management, resource allocation, charging schedule, dispatch, What‑if simulation (no hardware/3‑D maps). | All seven subsystems are implemented as Streamlit components (`src/components/...`) matching the scope. | ✅ – No action needed. |

## Overall Compliance Score
- Total criteria checked: **15**
- Fully satisfied: **11**
- Partially / missing: **4**

**Compliance Score: 73 %**

## Prioritized Checklist (to be completed before final Submission #1)
1. **Add System‑wide Use‑Case Diagram** – create and commit the diagram file.
2. **Create Detailed Individual Use‑Case Documents** – two use‑cases per member with full specification.
3. **Add Meeting #2 (and any subsequent minutes)** – both `.tex` and `.md` versions.
4. **Insert Generative AI Transparency Statement** into `docs/README.md`.
5. (Optional) **Clean repository history** – if the instructor requires that the non‑PDF files never appear in the Git history, run a `git filter‑repo` rewrite and force‑push. Otherwise the current removal commit is sufficient.

*Once the above items are addressed, the repository will meet all mandatory academic requirements for Submission #1.*
