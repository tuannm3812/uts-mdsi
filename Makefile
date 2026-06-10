PYTHON := python3
SCRIPT := scripts/audit_llm_wiki.py

.PHONY: quality quality-full audit normalize-raw

quality:
	$(PYTHON) $(SCRIPT) --no-manifest --strict

quality-full:
	$(PYTHON) $(SCRIPT) --strict

audit:
	$(PYTHON) $(SCRIPT) --json

normalize-raw:
	$(PYTHON) scripts/normalize_raw_filenames.py
