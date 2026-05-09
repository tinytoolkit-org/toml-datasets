# Contributing to toml-datasets

Thanks for considering a contribution. This repo collects realistic, idiomatic TOML configuration files across the Python, Rust, static-site, formatter, cloud, and tooling ecosystems. We especially welcome **anonymized real-world configs** — they're far more useful for parser tests and learning than handcrafted toy examples.

## Before you open a PR

1. **Open an issue first** if you're proposing a new ecosystem or non-trivial config, so we can agree on scope and licensing.
2. If contributing a real-world config, **strip secrets, tokens, hostnames, and user-identifying paths** before submitting.

## File conventions

- **Naming:** kebab-case describing the tool/framework, e.g. `poetry-pyproject.toml`, `wrangler.toml`, `axum-cargo.toml`. Use `*-broken.toml` for intentionally malformed examples.
- **Format:** **TOML 1.0 strict**. Every file in `python/`, `rust/`, `configs/` must parse cleanly with `tomllib` (Python 3.11+) or any TOML 1.0 parser.
- **Folders:**
  - `python/` — pyproject.toml variants and standalone Python tool configs
  - `rust/` — Cargo.toml variants and standalone Rust tool configs
  - `configs/` — everything else (static sites, formatters, cloud, tooling)
  - `broken/` — deliberately malformed for validator testing
  - `generators/` — Python script that writes the handcrafted strings to disk

## Required CATALOG.md entry

```
### <filename>
- **Category:** python | rust | configs | broken
- **Configures:** <tool/framework name + brief context>
- **Lines:** <int>
- **Features demonstrated:** dotted-keys | arrays-of-tables | mixed-types | inline-tables | …
- **Source:** handcrafted | abstracted-from-real-project (anonymized)
- **Suggested tool:** https://tomlkit.org/<route>
- **License:** CC0-1.0
```

## PR checklist

- [ ] Filename follows convention
- [ ] File parses with `python3 -c "import tomllib; tomllib.loads(open('path').read())"` (broken/ exempted)
- [ ] No secrets, hostnames, real usernames, or production paths
- [ ] CATALOG.md updated
- [ ] README.md catalog table updated
- [ ] Tone matches existing entries — practical, not promotional

## What we particularly want

- Less-represented ecosystems: Hugo themes, Jekyll-via-TOML, Foundry, Anchor (Solana), etc.
- Edge-case TOML 1.0 features: nested arrays of tables, multi-line literal strings with backslashes, bare keys with hyphens
- Realistic broken configurations seen in the wild (anonymized)

## Out of scope

- Files containing real secrets, tokens, or proprietary URLs
- Non-TOML 1.0 dialects unless clearly labelled
