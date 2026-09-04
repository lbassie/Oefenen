# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Wat dit is

Leerproject om Claude Code en GitHub te oefenen: een getallen-gokspel (1-100,
raden met "hoger/lager" hints), in twee onafhankelijke implementaties die
dezelfde spellogica delen maar niet dezelfde code:

- `gokspel.py` — terminal/CLI versie (stdlib only, geen dependencies).
- `index.html` — losstaande browserversie (vanilla JS, geen build step), met
  een winst-animatie (canvas confetti, CSS-ballonnen, Web Audio jingle).

## Commands

```bash
python gokspel.py      # speel de terminalversie
python -m unittest     # run tests (test_gokspel.py)
```

`index.html` heeft geen build/serve-stap: direct openen in een browser is genoeg.

## Architecture

- `gokspel.py` bevat de complete spellus (input-loop, vergelijking, output) in
  één functie `speel()`. `test_gokspel.py` test de vergelijkingslogica los via
  een losstaande `vergelijk()`-helper, niet door `speel()` aan te roepen —
  omdat die laatste blocking `input()` gebruikt.
- `index.html` herimplementeert dezelfde spellogica in JavaScript (geen
  gedeelde code met `gokspel.py`); wijzigingen aan de spelregels moeten in
  beide bestanden apart doorgevoerd worden.
