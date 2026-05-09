# TOML Datasets

![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg) [Try it in tomlkit.org →](https://tomlkit.org) ![Spec: TOML 1.0](https://img.shields.io/badge/Spec-TOML%201.0-blue.svg)

A curated collection of real-world and synthetic TOML configuration files for testing and research.

## Why this exists

TOML examples found online are often either too trivial (like a three-line hello-world `Cargo.toml`) or are buried deep within complex open-source repositories, making them difficult to find and collect. Developers learning the nuances of the TOML 1.0 spec, building high-performance parsers, or testing IDE schema integrations benefit from having a single, well-organized catalogue of examples.

This repository covers a wide range of ecosystems including Python packaging, Rust project structures, static site generators, formatters, and cloud infrastructure. These datasets are designed to run alongside the browser-only tools at tomlkit.org, allowing users to format, validate, or convert their configurations without ever needing to upload data to a server.

## Folder structure

- `python/`: Project manifests and tool settings for the Python ecosystem.
- `rust/`: Cargo manifests and workspace configurations.
- `configs/`: General-purpose tool and cloud provider configuration files.
- `broken/`: Intentionally malformed files for testing parser error handling.
- `generators/`: Scripts used to generate or modify the dataset collection.

Note that for TOML, "lots of lines per file" is unusual. Real-world configuration files typically range from 30 to 300 lines. Consequently, this collection prioritizes breadth—offering 28+ different ecosystem-specific configurations—over the massive single-file size found in other data formats.

## Catalog

| File | Lines | Size | What it configures | Suggested tool |
| :--- | :--- | :--- | :--- | :--- |
| `python/complex-pyproject.toml` | 121 | 1.8 KB | Advanced Python configuration | [To JSON](/toml-to-json) |
| `python/data-science-pyproject.toml` | 50 | 1.4 KB | Data science environment | [To JSON](/toml-to-json) |
| `python/django-pyproject.toml` | 52 | 1.6 KB | Django project metadata | [To JSON](/toml-to-json) |
| `python/flit-pyproject.toml` | 51 | 1.6 KB | Flit packaging config | [To JSON](/toml-to-json) |
| `python/poetry-pyproject.toml` | 59 | 2.1 KB | Poetry dependency manager | [To JSON](/toml-to-json) |
| `python/pyproject.toml` | 44 | 0.9 KB | Standard Python project | [To JSON](/toml-to-json) |
| `python/ruff.toml` | 50 | 1.6 KB | Ruff linter settings | [Formatter](/toml-formatter) |
| `python/setuptools-pyproject.toml` | 42 | 1.5 KB | Setuptools configuration | [To JSON](/toml-to-json) |
| `rust/axum-cargo.toml` | 43 | 1.6 KB | Axum web framework | [To YAML](/toml-to-yaml) |
| `rust/bevy-cargo.toml` | 45 | 1.4 KB | Bevy game engine | [To YAML](/toml-to-yaml) |
| `rust/cargo.toml` | 37 | 0.9 KB | Basic Cargo manifest | [To YAML](/toml-to-yaml) |
| `rust/cli-tool-cargo.toml` | 38 | 1.4 KB | CLI application manifest | [To YAML](/toml-to-yaml) |
| `rust/monorepo-cargo.toml` | 129 | 2.5 KB | Complex monorepo structure | [To YAML](/toml-to-yaml) |
| `rust/rustfmt.toml` | 39 | 1.1 KB | Rust code formatting | [Formatter](/toml-formatter) |
| `rust/workspace-root-cargo.toml` | 33 | 1.1 KB | Cargo workspace root | [To YAML](/toml-to-yaml) |
| `configs/config-mixed.toml` | 57 | 1.2 KB | Mixed key/table styles | [Formatter](/toml-formatter) |
| `configs/dependabot-config.toml` | 33 | 1.1 KB | Dependabot updates | [Formatter](/toml-formatter) |
| `configs/dprint.toml` | 32 | 0.9 KB | dprint formatter config | [Formatter](/toml-formatter) |
| `configs/foundry.toml` | 30 | 1.1 KB | Ethereum development | [Formatter](/toml-formatter) |
| `configs/hugo-config.toml` | 52 | 1.3 KB | Hugo static site | [Formatter](/toml-formatter) |
| `configs/mdbook-book.toml` | 31 | 1.0 KB | mdBook documentation | [Formatter](/toml-formatter) |
| `configs/netlify.toml` | 45 | 1.3 KB | Netlify deployment | [Formatter](/toml-formatter) |
| `configs/starship.toml` | 48 | 1.1 KB | Starship shell prompt | [Formatter](/toml-formatter) |
| `configs/taplo.toml` | 35 | 1.0 KB | Taplo TOML language tool | [Formatter](/toml-formatter) |
| `configs/traefik.toml` | 41 | 1.2 KB | Traefik proxy config | [Formatter](/toml-formatter) |
| `configs/wrangler.toml` | 36 | 0.9 KB | Cloudflare Workers | [Formatter](/toml-formatter) |
| `configs/zola-config.toml` | 41 | 1.3 KB | Zola static site | [Formatter](/toml-formatter) |
| `broken/broken-mixed-300.toml` | 318 | 5.0 KB | Mixed syntax errors | [Validator](/toml-validator) |
| `broken/broken-syntax-50.toml` | 63 | 1.0 KB | Invalid TOML syntax | [Validator](/toml-validator) |

## Open in tomlkit.org

To work with these files in your browser, drag and drop any `.toml` file from this repository directly into the tools at [tomlkit.org](https://tomlkit.org). All processing happens locally; your data never leaves your machine.

Available routes:
- `/toml-formatter`: Cleanup and prettify TOML.
- `/toml-validator`: Check for syntax and specification errors.
- `/toml-to-json`: Convert TOML configurations for JSON-based systems.
- `/toml-to-yaml`: Convert TOML to YAML manifests.
- `/json-to-toml`: Migrate JSON configs to TOML.
- `/yaml-to-toml`: Migrate YAML configs to TOML.

## What this is good for

- **Parser tests**: Comprehensive test cases for validating TOML parser compliance.
- **TOML 1.0 spec coverage**: Examples using nested tables, arrays of tables, and various date formats.
- **IDE schema validation**: Testbed for validating IDE plugins and schema integrations.
- **Documentation by example**: Reference templates for writing idiomatic `pyproject.toml` or `Cargo.toml` files.
- **Formatter golden files**: Benchmark files for verifying output consistency in code formatters.
- **Learning**: Learn the TOML specification by reading real-world configuration patterns.

## Ecosystem coverage

- **Python**: Poetry, Flit, Setuptools, Django, data-science, Ruff.
- **Rust**: Cargo, Axum, Bevy, CLI, workspace, rustfmt.
- **Static sites**: Hugo, Zola, mdBook.
- **Formatters**: dprint, taplo, rustfmt.
- **Cloud**: Netlify, Cloudflare Wrangler, Traefik.
- **Tooling**: Foundry, Starship, Dependabot-illustrative.

## Generators

The `generators/make_datasets.py` script writes most of these handcrafted strings to disk. Running this script is idempotent and ensures that the collection remains consistent across updates.

## Sister repos

- [jsonl-datasets](https://github.com/tinytoolkit-org/jsonl-datasets)
- [csv-datasets](https://github.com/tinytoolkit-org/csv-datasets)
- [geojson-datasets](https://github.com/tinytoolkit-org/geojson-datasets)

## Contributing

We welcome contributions from the community. If you have an anonymized real-world configuration file from an ecosystem not yet represented, please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit a pull request.

## License

This dataset is licensed under the [CC0 1.0 Universal](LICENSE) license. All configuration files provided are illustrative and have been anonymized to ensure no real secrets, private production hosts, or sensitive credentials are included.

---
Built alongside [tomlkit.org](https://tomlkit.org).
