"""Prevent count-only validation from accepting the defects found in review."""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("submission_validator", ROOT / "scripts/validate_submission_2.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


@pytest.mark.parametrize("defect", ["wrong_id", "wrong_fr_meaning", "wrong_test", "inflated_coverage"])
def test_validator_rejects_traceability_regressions_with_unchanged_counts(defect):
    data = json.loads((ROOT / "docs/traceability/submission_2.json").read_text())
    assert validator.check_manifest(data)[0]
    if defect == "wrong_id":
        data["user_stories"]["US-07b"] = data["user_stories"].pop("US-05b")
    elif defect == "wrong_fr_meaning":
        data["functional_requirements"]["FR-03"]["description"] = "Trả xe SS1"
    elif defect == "wrong_test":
        data["user_stories"]["US-24b"]["test_id"] = "test_rerouting_that_does_not_exist"
    else:
        data["moscow_summary"]["overall_coverage_pct"] = 100
    assert not validator.check_manifest(data)[0]
