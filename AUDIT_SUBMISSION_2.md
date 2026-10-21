# Submission #2 repository audit

Audit date: 2026-10-21 (Asia/Ho_Chi_Minh). Project: Smart E-Mobility Hub, BEE BRAVE, CO3001 HK261.

**Readiness: FAIL against the requested project acceptance gates. Advisory quality score: 61/100.** The required document categories exist, but stale rendered diagrams, unsupported implementation claims, and reproducible business logic defects prevent a clean handoff. This is an audit judgment, not a predicted instructor grade.

## 1. Authority and scoring

Primary course source: `../BTL_SoftwareEngineering_HK261_v1.pdf`, physical page 5, “Project Submission Detail”; page 6, “Generative AI using”; page 4, teamwork, meetings, submissions and demonstration. Repository layout source: `docs/report/submission_2/REPORT_SUBMISSION_2.pdf`, Appendix A.2, physical pages 63-64 (printed pages 62-63).

The six-page course PDF requires group UI mockups, individual Sequence and Activity diagrams, and optional State-chart diagrams for Submission #2. Architectural views and class/method design belong to Submission #3. It permits simulated IoT, hard-coded data, and no backend database. Transparent AI disclosure is mandatory; the final submission explicitly packages that statement.

**The supplied PDF contains no numeric grading weights, no 70% MoSCoW threshold, no 90% commitment, and no fixed six-lifeline/five-swimlane template.** Those are project/user acceptance criteria, not verified course rules. No separate LMS rubric was available. The course warns of deductions/rejection for misleading AI disclosure; the repository's claim of automatic zero for the entire course is not established by this PDF.

| Dimension | Advisory weight | Earned | Basis |
| --- | ---: | ---: | --- |
| Group UI design and navigation | 20 | 14 | Seven screenshots, screen flow and screen catalogs exist; some screens and behavior remain target design; narrow viewport evidence absent. |
| Individual Sequence design | 25 | 18 | 17 sources and PNGs, all authors represented; freshness, numbering, activations, naming and failure branches need repair. |
| Individual Activity design | 25 | 17 | 17 sources and PNGs; partitions exist, but requested layer semantics and branch termination are inconsistent. |
| Traceability, executable prototype and reproducibility | 20 | 6 | All seven routes exist and scoring/deepcopy work; major state, payment, simulation, mapping and runtime defects remain. |
| Governance and report integrity | 10 | 6 | AI statement, seven prompt directories and peer assignment exist; claims, evidence links and meeting records are incomplete. |
| **Total** | **100** | **61** | Weights were chosen for this audit, using the course deliverable categories plus the user's additional gates. |

State-chart bonus: present, but no numeric bonus awarded by this audit; assess after freshness, lifecycle and vocabulary repair. A directory's existence is a pass on structure, not proof of functional or academic correctness.

## 2. Scope, evidence and limitations

- Inspected repository file inventory, all ten application Python sources, requirements, system Draw.io source/generator, individual scenario IDs in Markdown and DOCX XML, all 46 PlantUML sources and embedded PNG source metadata, governance documents, report source and exported PDF, and helper script entry points/rewriting patterns.
- Parsed all ten `src/**/*.py` files successfully. SS4's defect is a **runtime API call error**, not a Python syntax error.
- Ran the actual scheduler and simulator and exercised actual SS1/SS2 functions with a small deterministic UI stub. The strict SS4 call probe rejects its invalid argument. These are isolated probes, **not Streamlit AppTest or browser end-to-end tests**.
- Rebuilt the report with `latexmk -xelatex`, with all outputs directed to `/tmp/emobility-audit/latex`. It completed successfully with 64 physical pages. Last XeLaTeX log contains 16 overfull and 16 underfull horizontal boxes (maximum overrun 40.78769 pt). The PDF conversion also reports a duplicate page destination and an unsupported ICC profile.
- Rasterized all 64 existing report pages into four contact sheets and inspected them, plus enlarged physical page 29/Figure 2.5 and all 11 state-chart PNGs. Reviewed complete course pages 5 and 6 visually and all six pages as extracted text. This is a layout audit, not a claim that every small glyph on every page has passed print-size review.
- Streamlit and Plotly are absent from both available Python runtimes. No actual Streamlit/browser run was completed. PlantUML executable/JAR was not found in the inspected local locations, so fresh PlantUML syntax/render-warning checks remain **NOT VERIFIED**. No yellow renderer warning was observed in inspected state-chart images; that does not certify every image as warning-free.
- Repository application sources, UML assets and report were not changed by this audit. Existing untracked `PLAN_FIX_SUBMISSION_2.md` was preserved. New outputs are the audit, `PLAN.md`, and evidence under `docs/audit/submission_2/`.

Evidence: `diagram-inventory.json`, `png-provenance.json`, `probe-results.json`, `broken-links.json`, `latex-build.log`, and a SHA-256 baseline manifest in that evidence directory. Reproduce isolated probes from the repository root with `PYTHONDONTWRITEBYTECODE=1 python3 docs/audit/submission_2/reproduce-probes.py` (requires installed Pandas; uses a UI stub).

## 3. Deliverable inventory and UML gates

All seven subsystems already have exactly the four required child directories. **No missing-directory defect was found.** Counts are 17 Sequence + 17 Activity + 11 State-chart sources, each with a PNG, plus one local SS3 Use-case PlantUML source/PNG: 46 pairs total. Seven scenario Markdown documents contain 17 primary scenario definitions; seven DOCX files contain corresponding primary IDs. “14 scenarios” is legacy wording, not the actual primary scenario count. Do not confuse the 14 fields in a scenario template with the number of scenarios.

| UC | Sequence lifelines | Autonumber | Explicit activations | Activity lanes | Fork/join source |
| --- | ---: | --- | --- | ---: | --- |
| UC_SS1_01 | 6 | Yes | Yes | 5 | Yes |
| UC_SS1_02 | 6 | Yes | Yes | 5 | No |
| UC_SS1_03 | 6 | Yes | Yes | 4 | No |
| UC_SS2_01 | 4 | Yes | Yes | 3 | No |
| UC_SS2_02 | 6 | Yes | Yes | 5 | No |
| UC_SS2_03 | 6 | Yes | Yes | 5 | No |
| UC_SS2_04 | 8 | Yes | Yes | 6 | No |
| UC_SS3_01 | 5 | No | No | 3 | No |
| UC_SS3_02 | 6 | No | No | 3 | No |
| UC_SS4_01 | 6 | Yes | No | 2 | No |
| UC_SS4_02 | 7 | Yes | No | 2 | No |
| UC_SS5_01 | 5 | Yes | Yes | 5 | No |
| UC_SS5_02 | 6 | Yes | Yes | 6 | No |
| UC_SS6_01 | 5 | Yes | Yes | 5 | Yes |
| UC_SS6_02 | 4 | Yes | Yes | 3 | Yes |
| UC_SS7_01 | 7 | Yes | Yes | 6 | No |
| UC_SS7_02 | 6 | Yes | Yes | 5 | No |

Counts include actors and nested/indented declarations. Nine Sequence diagrams have six lifelines; only the three SS1 diagrams declare the exact requested actor/UI/SSO/state/wallet/IoT set. Fifteen have numbering and thirteen have explicit activation bars. Seven Activities have five lane names, but names/counts alone do not establish the five required responsibilities. SS5_01 uses its fifth lane for the scheduler, for example, rather than the wallet. Decisions exist in all 17 sources. Three Activities use forks; adding fake concurrency to the remaining sequential workflows would reduce modeling quality. Use explicit not-applicable notes for idle external layers and genuinely sequential work.

### PNG freshness

After removing the optional `@startuml` output name, trimming blank lines and line indentation, compare the current source with the first source block in PNG metadata: **26 match, 20 differ, zero lack metadata**. Three differences are punctuation-only; the others include substantive model, label, theme or styling changes. This is strong evidence of stale image generation, not a byte-for-byte renderer reproducibility claim.

Differing pairs:

- SS1: Activity 03, Sequence 03, EV State-chart.
- SS2: Activity 02, Sequence 02, Sequence 04 (time-range punctuation differences).
- SS3: all six Sequence/Activity/State-chart pairs; PNGs retain `aws-orange`, while current sources use `plain`.
- SS4: both Activities and State-chart 02.
- SS5: Activity 02, both Sequences, charging State-chart; affected PNG labels retain older unaccented text.
- SS6: Hub operational State-chart; exported image omits the newly added `GRID_OFFLINE` model.

The SS1 EV image omits `DISPATCHED` and `INCIDENT` present in its source/table. SS2 Sequence 02 and 04 PNGs are exactly 4096 px high: investigate renderer size limiting and missing lower content during regeneration. Enlarged Figure 2.5 is a tall diagram shrunk into a landscape page, leaving large side margins and text at impractical reading size.

## 4. Defect and gap matrix

Paths below are relative to `smart-emobility-hub/`; line numbers refer to the audited baseline. High = blocks a committed workflow, corrupts domain/accounting state or materially misrepresents evidence. Medium = incomplete design, traceability or demonstrability. Low = maintainability/presentation drift.

| ID | Subsystem / file | Issue and evidence | Severity | Recommended fix |
| --- | --- | --- | --- | --- |
| D01 | SS4 `src/components/dispatch_incident.py:92-94` | Nested `st.text_area(dispatch_reason=st.text_area(...))` uses an unsupported keyword and no outer label. Strict call probe raises TypeError. | High | Replace with one labeled `text_area`; smoke-test actual SS4 navigation. |
| D02 | SS6 `sim_demand.py:146-200`; SS7 `sim_infrastructure.py:132-206` | Apply button exists only inside the Run-button branch. Its click reruns the script after Run has become false; preview is also only a local variable. | High | Persist preview/log/plan/version in session state; render and handle Apply outside Run; reject stale/repeated apply. |
| D03 | SS1 `student_booking.py:237-249,424-464` | No booking expiry enforcement. A booking dated 2000 was accepted by PIN and separately cancelled with the full 50,000 refund. `NO_SHOW_FEE` is unused. | High | Store deadline; process expiry once, before pickup/cancel, charging 10,000 and refunding 40,000. |
| D04 | SS1 `student_booking.py:237-246,343-361` | Pickup never frees an origin slot. A same-Hub return changed free slots from 15 to 14. In-use vehicles stay in the origin list and inflate physical inventory. | High | Model outside-Hub location after pickup; release origin once and consume destination once; conserve capacity. |
| D05 | SS1 `student_booking.py:363-375` | Fees beyond funds are clipped with `max(0, ...)`, then booking marked COMPLETED. Probe billed 270,000 from only 51,000 available+held, silently losing 219,000. | High | Atomic settlement; retain explicit debt or reject settlement according to documented policy; never discard liabilities. |
| D06 | SS2 `personal_ev.py:117-146`; SS1 filtering | Repeated placement appends the same personal EV to Hub inventory twice; no active reservation/ownership guard. Personal EV status stays registered, and parked private EVs become rentable/dispatchable through shared lists. | High | Unique IDs, ownership and reservation records; restrict shared rental/dispatch to shared fleet; prevent duplicate placement. |
| D07 | SS2 `personal_ev.py`; requirements FR-03b/05b/15b | No scheduled time window, check-in/out, parking/energy tariffs, combined wallet settlement or personal EV invoice despite “Implemented” claims. | High | Implement deterministic mock lifecycle and billing; show all four UC screens; label external gate hardware simulated. |
| D08 | SS5 `src/core/scheduler.py`, `smart_charging.py` | Scoring/FIFO exists, but no power-cap allocator, kW configuration, physical start/finish, energy accounting, 90/100% notifications, 15-minute grace or overstay fee. | High | Add resource-bound sessions, cap enforcement and idempotent fee events; connect to SS2/SS7. |
| D09 | SS5 `smart_charging.py:33-48`; scheduler add/remove | Queue seeded only once; predicate excludes reserved vehicles before testing whether they are reserved, so booking-priority seed is always false. Duplicate/unknown IDs accepted; completion only removes queue rows. | High | Reconcile queue from state changes; deduplicate and validate requests; bind booking flags and resource transitions. |
| D10 | SS7 `src/core/simulator.py:110-145` | Failure count is capped by free ports; fully busy ports cannot fail. Probe with two busy ports and two requested failures left both vehicles CHARGING. No per-port ERROR or Hub OFFLINE field is written. | High | Track physical port identities/busy/offline states and affected sessions; derive availability and Hub power separately. |
| D11 | SS7 `sim_infrastructure.py:79-104` | Toggle recovery adds the requested outage delta even if the prior decrement was clamped. With available=5,total=12: set down=12 gives 0; restore down=0 gives 12, inventing 7 free ports. Busy use is conflated with failure. | High | Derive counts from port records; restore only failed ports; preserve occupied sessions and prior state. |
| D12 | SS7 `sim_infrastructure.py:165-205`; SS1 `student_booking.py:288-308` | Infrastructure suggestion ranks free-port count, ignores parking/online/distance, and never moves vehicles. SS1 only offers a manual dropdown for a full Hub: no offline trigger, reservation transfer, one-click button, fee pause or 15-minute allowance. | High | Shared routing planner and atomic apply; reserve a destination, preserve deposit and apply allowance once. |
| D13 | SS4 `dispatch_incident.py:103-125` | No destination capacity guard; clamping can move multiple vehicles into a full Hub. DISPATCHED never completes. Form Hub changes can leave the vehicle selector stale until submission. | High | Reactive selection, revalidation on submit, all-or-nothing transfer, and receipt/completion transition. |
| D14 | SS3 `hub_monitor.py:195-196`; SS4 `dispatch_incident.py:50` | Yellow threshold is >60%; requirements say >=70% yellow, >=85% red; report/decision D6 says >85% red. KTX A 62.5% is yellow in code despite report's normal label. No periodic refresh, revenue, IoT alerts or full-Hub lock. | Medium | Centralize thresholds, honor frozen requirement boundaries, add honest mock refresh/alerts and revenue views. |
| D15 | `src/app.py:30-85,102-111`; NFR-10/11/12 | Student initialized only on visiting SS1; all roles can enter all pages; no mock role gate or wallet audit ledger. Empty logs are automatically reseeded. | Medium | Central state initializer, explicit mock identity/role selector, role guards, append-only ledger, seed only on missing keys. |
| D16 | `src/data/mock_hubs.json`, all mutating modules | Lowercase parked/charging/reserved contradict UPPER_CASE storage contract. Sparse vehicle/charger lists do not explain occupied background capacity. JSON seed load itself is correct and session-persistent only. | High | Typed state vocabulary and migration; explicitly model background mock loads; validate conservation after every command. Do not require a database. |
| D17 | All diagram PNGs; evidence `png-provenance.json` | 20/46 rendered assets differ from current source; changelog's fully resolved claims are contradicted by embedded source and report images. | High | Render from canonical sources with one recorded renderer version and output/source hash manifest; rebuild report afterward. |
| D18 | Sequence sources SS2-SS7 | Eight diagrams have a non-six lifeline count; six-count diagrams outside SS1 also use other responsibilities. SS3 lacks autonumber and activations; SS4 lacks activations. | Medium | Adopt requested six role groups with explicit idle-layer notes; preserve necessary collaborator details in messages/notes. Do not invent SSO/wallet traffic. |
| D19 | Activity sources SS1-SS7 | Only seven have five named lanes; several merge UI/control/IoT or introduce extra actor/subsystem lanes. SS1_02 reroute branch terminates before rejoining return/settlement. | Medium | Five responsibility lanes, actionable guarded branches and convergence; retain forks only for real independent work. |
| D20 | State-chart SS3/SS4 and shared references | CamelCase state aliases, PARKED/AVAILABLE synonyms and display-only uppercase mappings violate shared storage vocabulary. Session, port, vehicle and Hub states are mixed. | Medium | Document separate entity state machines; convert technical aliases to UPPER_CASE; make relevant tables and code match the same revision. |
| D21 | SS5 Sequence 01; SS6 diagrams | SS5 still updates state after a “cannot allocate” branch; SS6 labels nonexistent demand_simulation.py/demand_forecast.py; forecast says round/DataFrame while core uses int/list and UI creates DataFrame. | Medium | Repair branch exit guards and precise return contracts; rename lifelines to actual files/functions; preserve supported formula. |
| D22 | System `docs/diagrams/system/smartEhub.drawio`, generator | `uc_ss3_02` means device management and overload uses 03; SS5_02 means power-cap config instead of overstay; SS6/7 are generic sim nodes. Primary 17 UC IDs/names do not match detailed scenarios. | High | Establish canonical 17-UC catalog, repair Draw.io and generator together, retain helper UCs as explicitly subordinate. |
| D23 | `docs/requirements-analysis.md:119-180` | FR matrix has 23 rows/30 US declarations, but US-07 and US-12 are absent from FR mappings. UC table assigns rental pickup/return names to SS2_01/02, misses primary rows SS2_03/04, and has only 15 actual rows while claiming 17. All 44 relative links are broken (14 unique targets). | High | Complete explicit US->FR->scenario->both diagrams->code->test mapping; correct IDs and moved paths; label missing behavior honestly. |
| D24 | Submission #2 report §§1.2/1.5.3/1.6.2; OPEN_QUESTIONS/CHANGELOG | 90% is inferred from planning weights, with no accepted feature denominator. Report claims implemented overstay/one-click notifications and current PDF fixes not supported by code/assets. D2 cites nonexistent calculate_priority_score; actual method is _calculate_priority. | High | Compute coverage from acceptance evidence; distinguish implemented/mock/target design; correct resolved/open status. |
| D25 | Report Figures 2.5/2.7/3.5/3.9 and UML sizes | Tall diagrams are shrunk in landscape; Sequence 02/04 SS2 hit 4096 px height. Seven UI screenshots at small scale do not demonstrate secondary workflows or 375px responsiveness. | Medium | Split by interaction phase; render vectors/high resolution; capture real desktop/narrow screens and review final print-size pages. |
| D26 | Report LaTeX/build | Compiles but has 16 overfull and 16 underfull boxes, duplicate page destination and ICC warnings. A compilation pass is not a clean-layout pass. | Medium | Repair widths/headings/cover anchors; normalize image profiles; render final PDF and review pages/references. |
| D27 | `docs/ai-statement.md`, report Appendix A | Disclosure exists but concerns mainly Sprint 1 and code; no explicit updated account of Submission #2 diagrams/report/audit. It references absent prompt_history_antigravity.txt. Report only lists statement path in tree. | Medium | Add truthful current tool/scope/contribution disclosure to repo and PDF; link real logs; distinguish planned human review from completed review. |
| D28 | `docs/tasks-assignment.md`, meeting minutes | Assignment/review plan exists, but no completed Submission #2 peer evaluation evidence. All-100% contribution table is not demonstrated evaluation; template still says 14 UCs. Only Meeting_01 exists; README advertises missing 02/03. | Medium | Update 17-UC ownership and pending reviewer sign-offs; link actual records; do not fabricate meetings, marks or signatures. |
| D29 | `requirements.txt`, README; helper scripts | Streamlit >=1.28 and Pandas >=2.0 allow versions lacking current APIs such as DataFrame Styler.map; screenshot scripts require undeclared Selenium, use fragile indexes/fixed waits, and rewrite scripts can restore stale report claims. | Medium | Separate runtime/dev dependencies and record tested lock; fail screenshot capture on app errors; retire or guard historical rewrite scripts. |
| D30 | README, docs/README, helper paths | Clone URL is placeholder, docs index links missing compliance-check.md/diagrams/README.md, parse_drawio.py hard-codes a stale BTL_1 absolute directory. | Low | Fix local links and actual repository URL; derive paths from source/repo root; document reproducible local commands. |
| D31 | UML clean-render gate | No local PlantUML renderer found; current sources have not been freshly parsed/rendered by this audit. Zero-warning claim cannot be certified. | Medium | Install/select a recorded stable renderer when executing plan, check all sources and inspect all generated images; do not equate ordinary yellow UML notes with warnings. |
| D32 | SS5 `Usecase scenario/UC_SS5_DuongDangKhoa.md:144-177`, matching DOCX; SS2 tariff story/scenario | SS5 scenario retains a weighted SoC/wait/urgency/off-peak formula unlike the verified additive scheduler/report formula. US-09 requests hourly parking, while SS2 scenario quotes 5,000 per visit. These are unresolved specification differences. | Medium | Record an explicit policy decision; update both scenario formats, code and diagrams together. Preserve existing tariff evidence and do not silently count conflicting acceptance criteria as satisfied. |

## 5. User Story traceability audit seed

The correct graph is generally many-to-many: 30 stories, 23 FRs and 17 UCs cannot form a bijection. “1-to-1 traceability” is interpreted as an explicit, unambiguous evidence chain for **each** story, with shared artifacts allowed. This table supplies intended links, not certification of implementation. `PARTIAL` means some main-flow behavior exists; `MISSING` means the story's requested result is not implemented; `DEFECTIVE` means a concrete failing path is reproduced or established by code; `REVIEW` requires acceptance reconciliation.

| US | Existing / proposed FR link | Canonical UC(s) | Code evidence and current status |
| --- | --- | --- | --- |
| US-01 | FR-01 | SS1_01, SS1_02 | SS1 chooses/rents vehicles but lacks an independent shared parking reservation; PARTIAL. |
| US-02 | FR-01, FR-01b | SS1_01 | SS1 list/filter/tariff UI exists; user can lower SoC floor below committed threshold; PARTIAL. |
| US-03 | FR-01b | SS1_01, SS1_03 | Deposit lock exists; 15-minute expiry absent; DEFECTIVE. |
| US-03b | FR-01c | SS1_01 | PIN pickup exists, expired PIN accepted; QR is target design; DEFECTIVE. |
| US-04 | FR-01b | SS1_01, SS1_02 | Fixed mock voucher accepted/stored/applied; PARTIAL pending end-to-end acceptance. |
| US-05 | FR-02 | SS1_03 | Full refund works, including erroneously overdue cancellations; DEFECTIVE. |
| US-05b | FR-01c | SS1_02 | Return path exists, capacity/accounting defects; DEFECTIVE. |
| US-06 | FR-15b | SS1_02 | UI invoice exists without persistent settled ledger/distance data; PARTIAL. |
| US-07 | Extend FR-05 and FR-15b explicitly | SS3_01 | SS3 has no booking/revenue view; MISSING. Current FR table has no link. |
| US-08 | FR-03 | SS2_01 | Registration form exists; duplicate plate/ownership validation missing; PARTIAL. |
| US-09 | FR-05b; also FR-04 for reservation | SS2_02, SS2_04 | Immediate placement instead of advance time window; no parking tariff; PARTIAL. |
| US-10 | FR-04, FR-05b | SS2_02, SS2_04, SS5_01 | Immediate port consumption; no scheduled tariff/energy calculation; PARTIAL. |
| US-11 | FR-05b, FR-15b | SS2_04 | Combined private-EV payment/invoice absent; MISSING. |
| US-11b | FR-03b | SS2_03, SS2_04 | Check-in/check-out UI and commands absent; MISSING. |
| US-12 | Extend FR-04/FR-05b explicitly | SS2_02, SS2_04, SS5_02 | Current tariff/charging/payment inspection absent; MISSING. Current FR table has no link. |
| US-13 | FR-05 | SS3_01 | KPIs exist; revenue/automatic refresh missing; PARTIAL. |
| US-13b | FR-05c | SS3_02 | Partial >85% overload banner; 60% colors, no 100% block; DEFECTIVE. |
| US-14 | FR-06 | SS3_01, SS4_02 | No sensor error feed or active notification; MISSING. |
| US-15 | FR-07 | SS4_01 | Invalid text_area blocks page; destination guard absent; DEFECTIVE. |
| US-16 | FR-08 | SS4_02 | Incident log/status write exists, page blocker and no repair lifecycle; PARTIAL. |
| US-17 | FR-08 | SS4_02 | Session incident history exists but SS4 page blocks; PARTIAL. |
| US-18 | FR-09 | SS5_01 | Scoring/FIFO verified; tariffs, time pressure and allocation incomplete; PARTIAL. |
| US-19 | FR-10 | SS5_02 | No charged-complete event, user notification or energy receipt; MISSING. |
| US-19b | FR-10b | SS5_02 | No grace timer or overstay calculation; MISSING. |
| US-20 | FR-11 | SS5_01 | No power-cap configuration/enforcement; MISSING. |
| US-21 | FR-12 | SS6_01, SS6_02 | Preview/deepcopy exists; Apply broken, no revenue impact; DEFECTIVE. |
| US-22 | FR-13 | SS6_02 | Forecast/list/queue plots exist with 6-24 hours; random reruns not reproducible; PARTIAL. |
| US-23 | FR-14 | SS7_01 | Busy-port failure and restoration wrong; DEFECTIVE. |
| US-24 | FR-15 | SS7_01, SS7_02, SS4_01 | Suggestions exist; actual Apply/rerouting workflow absent/broken; DEFECTIVE. |
| US-24b | FR-15c | SS7_02, SS1_02 | Full-Hub top-two suggestions exist, but no automatic offline warning or one-click transfer; PARTIAL. |

UC abbreviations in this table prepend `UC_`: `SS1_01` means `UC_SS1_01`. For an implementation-ready manifest add actual scenario section anchors, the existing owner-specific Sequence/Activity paths from `diagram-inventory.json`, concrete Python functions, and executable acceptance test IDs for every row. Do not turn this seed into a false completion certificate.

## 6. Verified strengths and handoff

`src/app.py` loads seed JSON relative to its own location, once per session, and maps all seven components. All 17 primary UCs have diagram source/image pairs and named owners. Scheduler examples reproduce 177.5 at 5% SoC, 65.0 at 30%, and 125.0 at 30% with booking; FIFO tie sorting is implemented. Both simulator methods deepcopy baseline state. The report has Sections 1-4 and Appendix A and rebuilds locally. Governance artifacts exist; they need updated, accurate evidence.

Execute `PLAN.md` in dependency order: freeze evidence/catalog, repair state and workflows, reconcile design, regenerate assets, update disclosure/report, then run real app and visual acceptance. Do not rerun legacy bulk report-rewrite scripts as a repair shortcut. Do not mark an unrun gate passed.
