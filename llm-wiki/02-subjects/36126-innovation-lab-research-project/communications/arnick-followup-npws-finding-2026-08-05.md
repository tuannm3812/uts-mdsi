# Follow-Up: Reference-Dataset Comparison — 5 August 2026

**Status:** Drafted and ready to send once Dr Arnick responds to the 3 August brief — not yet sent.

Hi Arnick,

A follow-up to the findings brief from 3 August. Since then I reran the same feasibility pilot against a second, independently and explicitly licensed reference — NPWS Fire History — instead of the NSW RFS layer used in the first pilot, partly to check whether the reference dataset itself was driving the earlier result.

The two references give very different headline numbers: 17.1% buffered match against NSW RFS, versus 97.12% against NPWS. The reason is structural, not a sign that reliability has actually improved. NSW RFS records shorter, narrower incident boundaries, while NPWS records consolidated, whole-of-season fire-complex boundaries — two of the fourteen events (Kerry Ridge and Gospers Mountain) alone cover a large share of the entire study region and together account for about 98% of every match.

Read together, both pilots point to the same underlying problem from opposite directions: neither a narrow incident-level reference nor a broad complex-level reference currently lets us test point-in-time or event-level hotspot reliability in NSW. The narrow layer under-covers true fire extent and duration, so most hotspots go unmatched. The broad layer over-matches almost trivially, and leaves too few independent events — effectively 2 of 14 — to validate against.

I think this strengthens rather than changes the direction from the brief: a reliability audit with explicit held-out, split-complex validation, rather than a single match-rate number as the headline result.

Does this match your reading of the two references, or is there a NSW fire-event source at a granularity between these two that would make event-level validation more tractable?

One small correction from the 3 August brief: two citations had the wrong author attached — the semantic-explanations paper is Phan et al. (2022), not Manolakis et al., and the self-supervised temporal detection paper is Barco et al. (2024), not Barbastathis et al. The papers and findings themselves are unchanged, just the names.

Thanks,
Tuan
