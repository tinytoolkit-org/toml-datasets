# toml-datasets

Real-world TOML configuration files across the Python, Rust, static-site, formatter, cloud, and tooling ecosystems. For parser tests, IDE schema validation, and learning the spec by reading actual configs.

Pairs with **[tomlkit.org](https://tomlkit.org)** — drop any file from this repo into a tool there and it's processed in your browser tab. Nothing uploaded.

License: [CC0 1.0](LICENSE) — no rights reserved.

## Sister repos

- [jsonl-datasets](https://github.com/tinytoolkit-org/jsonl-datasets) → [jsonlkit.com](https://jsonlkit.com)
- [csv-datasets](https://github.com/tinytoolkit-org/csv-datasets) → [csvkit.org](https://csvkit.org)
- [geojson-datasets](https://github.com/tinytoolkit-org/geojson-datasets) → [geojsonkit.org](https://geojsonkit.org)

## What's in here

- **`python/`** — pyproject variants (Poetry, Flit, Setuptools, Django, data science) plus standalone tool configs (Ruff)
- **`rust/`** — Cargo manifests (Axum, Bevy, CLI, monorepo, workspace) plus rustfmt
- **`configs/`** — static-site (Hugo, Zola, mdBook), formatters (dprint, taplo), cloud (Netlify, Wrangler, Traefik), tooling (Foundry, Starship, Dependabot-illustrative)
- **`broken/`** — deliberately malformed files for validator testing
- **`generators/`** — Python script that writes every config to disk; running it again is idempotent

For TOML, "lots of lines per file" isn't really a thing — real configs are 30–300 lines. This repo prioritises **breadth** instead: 28+ different ecosystems represented.

## Catalog

| File | Lines | Size | What it configures | Open in |
| --- | ---: | ---: | --- | --- |
| `python/pyproject.toml` | 44 | 0.9 KB | Standard pyproject (Hatchling backend, Ruff, pytest) | [/toml-to-json](https://tomlkit.org/toml-to-json) |
| `python/poetry-pyproject.toml` | 59 | 2.1 KB | Poetry-managed project with deps, dev-deps, scripts | [/toml-validator](https://tomlkit.org/toml-validator) |
| `python/flit-pyproject.toml` | 51 | 1.6 KB | Flit-backend pyproject | [/toml-validator](https://tomlkit.org/toml-validator) |
| `python/setuptools-pyproject.toml` | 42 | 1.5 KB | Minimal setuptools backend | [/toml-validator](https://tomlkit.org/toml-validator) |
| `python/django-pyproject.toml` | 52 | 1.6 KB | Django project with extras (postgres, redis, celery) | [/toml-validator](https://tomlkit.org/toml-validator) |
| `python/data-science-pyproject.toml` | 50 | 1.4 KB | pandas / numpy / jupyter / matplotlib stack | [/toml-validator](https://tomlkit.org/toml-validator) |
| `python/complex-pyproject.toml` | 121 | 1.8 KB | Bigger pyproject with more tool tables | [/toml-formatter](https://tomlkit.org/toml-formatter) |
| `python/ruff.toml` | 50 | 1.6 KB | Standalone Ruff config (rules, line-length, per-file-ignores) | [/toml-validator](https://tomlkit.org/toml-validator) |
| `rust/cargo.toml` | 37 | 0.9 KB | Basic Cargo manifest | [/toml-to-json](https://tomlkit.org/toml-to-json) |
| `rust/axum-cargo.toml` | 43 | 1.6 KB | Axum web service deps (tokio, tower, serde, sqlx) | [/toml-validator](https://tomlkit.org/toml-validator) |
| `rust/bevy-cargo.toml` | 45 | 1.4 KB | Bevy game engine with feature flags | [/toml-to-json](https://tomlkit.org/toml-to-json) |
| `rust/cli-tool-cargo.toml` | 38 | 1.4 KB | clap + tokio + serde + reqwest CLI | [/toml-validator](https://tomlkit.org/toml-validator) |
| `rust/workspace-root-cargo.toml` | 33 | 1.1 KB | Cargo workspace root with members | [/toml-validator](https://tomlkit.org/toml-validator) |
| `rust/monorepo-cargo.toml` | 129 | 2.5 KB | Larger workspace example | [/toml-validator](https://tomlkit.org/toml-validator) |
| `rust/rustfmt.toml` | 39 | 1.1 KB | Rust formatter config | [/toml-formatter](https://tomlkit.org/toml-formatter) |
| `configs/netlify.toml` | 45 | 1.3 KB | Netlify build, redirects, headers, plugins, contexts | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/wrangler.toml` | 36 | 0.9 KB | Cloudflare Workers (R2, KV, D1, routes, vars) | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/hugo-config.toml` | 52 | 1.3 KB | Hugo site config (params, menus, taxonomies) | [/toml-to-yaml](https://tomlkit.org/toml-to-yaml) |
| `configs/zola-config.toml` | 41 | 1.3 KB | Zola static site config | [/toml-to-yaml](https://tomlkit.org/toml-to-yaml) |
| `configs/mdbook-book.toml` | 31 | 1.0 KB | mdBook book.toml | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/dprint.toml` | 32 | 0.9 KB | dprint multi-language formatter config | [/toml-formatter](https://tomlkit.org/toml-formatter) |
| `configs/taplo.toml` | 35 | 1.0 KB | Taplo TOML formatter / linter config | [/toml-formatter](https://tomlkit.org/toml-formatter) |
| `configs/traefik.toml` | 41 | 1.1 KB | Traefik reverse proxy (entryPoints, routers, services, middleware) | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/foundry.toml` | 30 | 1.1 KB | Solidity / Foundry config | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/starship.toml` | 48 | 1.1 KB | Starship prompt config | [/toml-validator](https://tomlkit.org/toml-validator) |
| `configs/dependabot-config.toml` | 33 | 1.1 KB | Illustrative Dependabot-style config (real Dependabot uses YAML) | [/toml-to-yaml](https://tomlkit.org/toml-to-yaml) |
| `configs/config-mixed.toml` | 57 | 1.2 KB | Dotted keys, multi-line strings, datetimes, mixed numbers | [/toml-formatter](https://tomlkit.org/toml-formatter) |
| `broken/broken-syntax-50.toml` | 63 | 1.0 KB | 50 lines, 8–12 deliberate syntax errors with `# ERROR:` annotations | [/toml-validator](https://tomlkit.org/toml-validator) |
| `broken/broken-mixed-300.toml` | 318 | 5.0 KB | 300-line file with mixed syntax + type errors | [/toml-validator](https://tomlkit.org/toml-validator) |

Every file in `python/`, `rust/`, `configs/` parses cleanly under TOML 1.0 (Python `tomllib`). Files in `broken/` do not — that's the point.

## Open in tomlkit.org

Drop a file onto the relevant page:

- [/toml-formatter](https://tomlkit.org/toml-formatter) — canonical spacing and table layout
- [/toml-validator](https://tomlkit.org/toml-validator) — line-and-column error reporting
- [/toml-to-json](https://tomlkit.org/toml-to-json), [/toml-to-yaml](https://tomlkit.org/toml-to-yaml) — round-trip converters
- [/json-to-toml](https://tomlkit.org/json-to-toml), [/yaml-to-toml](https://tomlkit.org/yaml-to-toml) — back the other way

## Generators

```bash
python3 generators/make_datasets.py
```

Idempotent — re-running it overwrites every file with the same content. Stdlib only.

## Ecosystem coverage

- **Python:** Poetry, Flit, Setuptools, Hatchling, Django stack, data-science stack, Ruff
- **Rust:** Cargo (basic, Axum, Bevy, CLI, workspace), rustfmt
- **Static sites:** Hugo, Zola, mdBook
- **Formatters:** dprint, taplo, rustfmt
- **Cloud / infra:** Netlify, Cloudflare Wrangler, Traefik
- **Tooling:** Foundry, Starship, Dependabot-illustrative

## What this is good for

- Testing TOML 1.0 parsers
- IDE schema validation testbed
- Reading idiomatic configs to learn the spec by example
- Formatter golden-file fixtures
- Validator stress tests (`broken/`)

## Contributing

Issues and PRs welcome — anonymized real-world configs especially. See [CONTRIBUTING.md](CONTRIBUTING.md). Strip secrets / hostnames / production paths before submitting.

## License

CC0 1.0 Universal — see [LICENSE](LICENSE). All configs are illustrative.

---

Built alongside [tomlkit.org](https://tomlkit.org).
