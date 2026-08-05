# Teams Message to Dr Arnick — 3 August 2026

Hi Arnick, I’ve completed an initial literature scan and a public-data feasibility pilot for the NSW active-fire monitoring topic. I tested 19,849 DEA hotspots against 14 NSW Fire History events from the January 2020 Greater Blue Mountains period. After applying sensor-specific positional tolerances, 17.1% matched a recorded fire polygon and time window.

The main finding is that public access is feasible, but the reference labels are the limitation: final fire boundaries do not represent point-in-time active-fire truth, so the remaining observations cannot automatically be labelled as false alarms. The pilot also showed that confidence values differ across sensors and algorithms, and that repeated observations from one large event can cause leakage under random train/test splitting.

I’m therefore considering a reference-data and sensor-confidence reliability audit as the initial contribution, using confirmed-event, unresolved, and confirmed-non-fire classes with held-out-event and future-period evaluation. Would this be a suitable starting direction, or do you know of an archived incident or verified point-in-time active-fire source that could help resolve the unmatched class?

I’ve attached a short findings brief with the proposed next stage. Thank you.
