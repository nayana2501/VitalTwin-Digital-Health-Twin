# VitalTwin — Personal Health Digital Twin

**Challenge:** Happiest Health Digital Twin Challenge 2026  
**Project type:** Healthcare / digital health proof-of-concept  
**Status:** Functional educational prototype

## 1. Team details
- Team name: [Add team name]
- Team members: [Add full names and roles]
- Contact: [Add team contact email]

## 2. College / incubator information
- Institution: [Add college / incubator]
- Department / program: [Add department]

## 3. Project title
**VitalTwin: An Explainable Personal Wellness Digital Twin**

## 4. Problem statement
People often see health and lifestyle indicators separately, making it difficult to explore how everyday habits interact. VitalTwin offers an interactive, explainable simulation that combines selected lifestyle and wellness inputs into a transparent personal digital-twin view.

## 5. Healthcare use case
A user can explore a fictional or self-entered wellness profile, inspect component scores, view an illustrative trend, and compare hypothetical habit changes. The prototype is intended for health education and discussion, not diagnosis, clinical risk prediction, or treatment decisions.

## 6. Technical stack
- Python
- Streamlit UI
- Pandas and NumPy for calculations and synthetic history
- Plotly for interactive charts
- Rule-based, interpretable scoring engine

## 7. AI/ML model or framework details
The current version uses a transparent weighted rule-based score rather than a trained clinical ML model. This is intentional: the project does not have a validated clinical dataset and should not imply medical accuracy. The component weights and score transformations are documented in `src/twin_engine.py`. Future work could evaluate a properly governed model on consented, representative, clinically reviewed data.

## 8. Demo video
Add an unlisted YouTube demo (15–20 minutes) and replace this placeholder:
- Demo link: [ADD UNLISTED YOUTUBE LINK]
- Suggested walkthrough: problem → user profile → twin dashboard → explainability → intervention sandbox → limitations and privacy.

## 9. Open-source license
This project is released under the MIT License. See `LICENSE`.

## 10. Architecture diagram
See `docs/architecture.pdf` and `docs/architecture.mmd`.

## 11. Presentation
See `docs/presentation.pdf`. Update team details and include genuine screenshots/results before submission.

## 12. Public accessibility
Ensure the GitHub repository is public and all linked documents/video are accessible without requesting permissions.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Repository structure
```text
app.py
src/twin_engine.py
data/sample_profiles.csv
docs/architecture.pdf
docs/architecture.mmd
docs/presentation.pdf
tests/test_twin_engine.py
requirements.txt
LICENSE
README.md
```

## Privacy, safety, and limitations
- Use fictional/sample values for demonstrations.
- No patient records or external health service integrations are included.
- No diagnosis, treatment advice, or clinical prediction is provided.
- Scores are illustrative and not validated against clinical outcomes.
- Do not use the score to make medication, emergency, or treatment decisions.
- Any future deployment involving real health data needs consent, security review, clinical governance, and applicable legal/privacy review.

## Roadmap
1. Add user-controlled, consent-based time-series imports.
2. Add uncertainty ranges and calibration only after appropriate validation.
3. Conduct usability testing with health professionals.
4. Add secure authentication and audited data storage only if required.
