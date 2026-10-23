# bambu-gitops-example

> [!CAUTION]
> # 🛑 DON'T RUN YOUR PRINTER ON THESE SETTINGS.
> **THIS REPOSITORY CONTAINS SYNTHETIC TEST FIXTURES, NOT PRINTING RECIPES.**
> The values are made up for software tests. They have not been calibrated, safety-checked, or tested on any printer. **Do not import, copy, deploy, or use them to operate hardware.** Plastic is cheap. Replacing a toolhead is less entertaining.

This public repository is a **reference consumer and conformance-test fixture** for [bambu-gitops](https://github.com/bakeb7j0/bambu-gitops). It illustrates the desired-state configuration **schema**, not a safe configuration for a Bambu Lab printer.

## What this repo does

- Exercises a pinned version of the public engine in its own GitHub Actions CI.
- Provides a small synthetic instance with printer, process, filament, and calibration *shapes*.
- Demonstrates how a config repository consumes the engine's `validate` command.
- Includes negative test cases: missing profile, inheritance cycle, wrong nozzle and safety-review warnings.
- Publishes **no importable Bambu Studio preset files, no startup G-code, no connected device controls, and no real calibration measurements**.

## What this repo does NOT do

**It does not provide recommended temperatures, flow rates, speeds, fan settings, bed geometry, printer G-code, or K factors.** The figures are placeholders selected to exercise code. A green CI check means the documents comply with a **software contract**, **not** that a physical printer is safe to run with them.

Read [DO-NOT-PRINT.md](DO-NOT-PRINT.md) before copying anything. Yes, that filename is intentional.

## Try the validator (offline and read-only)

```bash
python3 -m pip install -e 'git+https://github.com/bakeb7j0/bambu-gitops.git@534e810801927896a7339994c1b5a9949ae0e392#egg=bambu-gitops'
bambu-gitops validate .
```

This command **reads JSON only**. It does not interact with Bambu Studio, printers, AMS, or Bambu Cloud.

## A not-remotely-subtle disclaimer

The examples are provided *as-is* under the license terms, with no warranty of safety, fitness for printing, or physical correctness. **Software validation is not mechanical, thermal or electrical validation.** See [LICENSE](LICENSE) and [SAFETY.md](SAFETY.md).

**TL;DR: You can use this to test software. You absolutely should not use this to test how fast a P1S can become an expensive paperweight.**
