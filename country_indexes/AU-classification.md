---
layout: default
---

# Australia / Oceania (AU) — Hybrid Cyber–Influence Incident Classification

This table classifies 4 incidents targeting Australian entities according to the cyber–influence taxonomy:
- **(1) Cyber-enabled influence** — cyber operations serving an influence goal (1a–1h)
- **(2) Influence-enabled cyber** — disinformation/deception enabling a cyber intrusion (2a–2h)
- **(3) Parallel cyber–influence** — simultaneous, independent cyber and influence operations by the same actor

The **% fit** column rates how well each incident fits its primary type, on a 0.0–1.0 scale:
- **1.0** — textbook fit (defining act of the sub-type clearly present).
- **0.7–0.9** — strong fit, partial or mixed on one element.
- **≤ 0.5** — capped here for Type-1 incidents without a real unauthorised intrusion or DDoS, and for Type-2 incidents lacking a tactically-connected subsequent intrusion or DDoS by the same actor.
- **Type-3** scored on whether the cyber and influence components are by the same threat actor and close in time.

<div id="fit-filter" style="margin:16px 0;padding:12px 16px;background:#f3f6fb;border:1px solid #d0d7de;border-radius:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
  <label for="fitSlider" style="font-weight:600;white-space:nowrap;">Min % fit:</label>
  <input type="range" id="fitSlider" min="0" max="1" step="0.1" value="0" style="width:200px;cursor:pointer;">
  <span id="fitValue" style="font-weight:600;min-width:2.5em;">≥ 0.0</span>
  <span id="fitCount" style="color:#555;font-size:0.9em;"></span>
  <button id="fitReset" style="padding:4px 10px;border:1px solid #d0d7de;border-radius:4px;cursor:pointer;background:#fff;font-size:0.9em;">Show all</button>
</div>

| ID | Incident title | Country / scope | Primary type | Secondary type(s) | Perpetrator (as described) | Main victim category | % fit |
|---|---|---|---|---|---|---|---|
| AU-1 | [Australia's regulatory response to misinformation as a national-security and critical-infrastructure issue](../all_incidents/AU-Australias-Regulatory-Response-to-Misinformation-as-a-National-Security-and-Critical-Infrastructure-Issue.md) | Australia | 1c – cyber-enabled CIB and platform-scale propaganda dissemination (treated by Australian policy as a critical-infrastructure threat) | — | Mixed/uncertain (multiple online actors including foreign state-sponsored disinformation actors) | Elections, public health, critical infrastructure, civil society | 0.3 |
| AU-2 | [China-linked online influence campaign targeting Australian domestic and foreign policy debates](../all_incidents/AU-China-Linked-Online-Influence-Campaign-Targeting-Australian-Domestic-and-Foreign-Policy-Debates.md) | Australia | 1c – cyber-enabled CIB using fake accounts with AI-generated profile images | 2e – AI-generated identities used in account creation | China/PRC-linked (per ASPI and Recorded Future) | Civil society, public opinion, policy debate | 0.5 |
| AU-3 | [Coordinated inauthentic behavior and electoral disinformation concerns around Australian democratic events](../all_incidents/AU-Coordinated-Inauthentic-Behavior-and-Electoral-Disinformation-Concerns-Around-Australian-Democratic-Events.md) | Australia (federal election and Voice referendum environments) | 1c – cyber-enabled CIB and platform manipulation around elections | — | Mixed/uncertain (not always publicly attributable; fake profiles and coordinated manipulation identified by platforms and researchers) | Elections, voters, referendum participants | 0.4 |
| AU-4 | [Cyber intrusion into Australian political parties and broader concerns about foreign election interference](../all_incidents/AU-Cyber-Intrusion-into-Australian-Political-Parties-and-Broader-Concerns-About-Foreign-Election-Interference.md) | Australia | 1b – hack-and-leak (latent / pre-positioning; treated in the national-security framing as a hack-and-leak risk environment) | 3 – parallel cyber-influence risk framing (intrusion situated within wider foreign-interference threat picture) | China/PRC-linked (sophisticated state actor; public commentary pointed to China though Australia did not publicly name at the time) | Political parties, parliament, elections | 0.6 |

## Continental observations

- Only four incidents are captured, reflecting both the smaller media footprint and Australia's relatively well-defended democratic information environment, but the typology is varied.
- **AU-2 is one of the cleanest examples in the entire dataset of 2e (AI-generated identities)** as a supporting layer to a Type-1c influence operation — useful illustrative material for a 2026 keynote on AI-enabled hybrid threats.
- **Policy framing is itself notable**: AU-1 captures Australia's elevation of misinformation to a *critical-infrastructure* risk, a useful data point for the keynote's question on how governments are responding.
- China-linked activity dominates explicitly attributed Australian cases.

<script>
(function () {
  function filterByFit() {
    var threshold = parseFloat(document.getElementById('fitSlider').value);
    document.getElementById('fitValue').textContent = '≥ ' + threshold.toFixed(1);
    var rows = document.querySelectorAll('table tbody tr');
    var visible = 0;
    rows.forEach(function (row) {
      var cells = row.querySelectorAll('td');
      var last = cells[cells.length - 1];
      var val = parseFloat(last ? last.textContent.trim() : '');
      var show = isNaN(val) || val >= threshold;
      row.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    document.getElementById('fitCount').textContent =
      visible + ' / ' + rows.length + ' shown';
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('fitSlider').addEventListener('input', filterByFit);
    document.getElementById('fitReset').addEventListener('click', function () {
      document.getElementById('fitSlider').value = 0;
      filterByFit();
    });
    filterByFit();
  });
})();
</script>
