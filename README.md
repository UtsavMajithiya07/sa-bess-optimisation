\# Battery storage optimisation in South Australia's NEM



How much value can a grid-scale battery capture from energy arbitrage in South Australia, and how does that depend on duration, cycling limits and forecast quality?



\## Data



5-minute dispatch prices (energy and FCAS) for the SA1 region from January 2019 to September 2026, downloaded from AEMO's public archive with NEMOSIS (https://github.com/UNSW-CEEM/NEMOSIS). Non-intervention prices only, nominal $/MWh.



Note: the NEM moved to five-minute settlement on 1 October 2021. Before then, energy was settled on 30-minute trading prices.



\## Reproduce



&#x20;   python -m venv .venv

&#x20;   .venv\\Scripts\\activate

&#x20;   pip install -r requirements.txt

&#x20;   python src/download\_prices.py



\## Status



Work in progress. Paper target: December 2026.

