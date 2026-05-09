#!/usr/bin/env python3
import os
import sys

try:
    import tomllib
except ImportError:
    tomllib = None

BASE_DIR = "/Users/suleyman/Projects/DCPRJCT/ToolSites/Datasets/toml-datasets"

FILES = {
    "python/poetry-pyproject.toml": """[tool.poetry]
name = "awesome-python-app"
version = "2.4.1"
description = "A comprehensive Python application demonstrating Poetry configurations."
authors = ["Jane Doe <jane@example.com>", "John Smith <john@example.com>"]
license = "MIT"
readme = "README.md"
repository = "https://github.com/example/awesome-python-app"
homepage = "https://example.com"
keywords = ["api", "framework", "automation"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.28.0"
fastapi = { version = "^0.95.0", extras = ["all"] }
pydantic = { version = "^2.0.0", extras = ["email"] }
sqlalchemy = "^2.0.0"
alembic = "^1.11.0"
python-jose = { version = "^3.3.0", extras = ["cryptography"] }
passlib = { version = "^1.7.4", extras = ["bcrypt"] }
python-multipart = "^0.0.6"
uvicorn = "^0.22.0"
gunicorn = "^20.1.0"
redis = "^4.5.0"
celery = { version = "^5.3.0", extras = ["redis"] }

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.0"
pytest-cov = "^4.1.0"
pytest-asyncio = "^0.21.0"
httpx = "^0.24.0"
ruff = "^0.0.270"
mypy = "^1.3.0"
black = "^23.3.0"
isort = "^5.12.0"
pre-commit = "^3.3.0"
tox = "^4.5.0"

[tool.poetry.scripts]
app-serve = "awesome_app.main:run"
db-migrate = "awesome_app.cli.db:migrate"
worker-start = "awesome_app.worker:start"

[tool.poetry.plugins."blogtool.parsers"]
markdown = "some_package.parsers:Markdown"
json = "some_package.parsers:JSON"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

# Extended comments to reach line count target
# Poetry is a tool for dependency management and packaging in Python.
# It allows you to declare the libraries your project depends on and it will manage them for you.
# Poetry offers a lockfile to ensure repeatable installs and can build your project for distribution.
# This config covers a typical production-grade FastAPI application.
# Includes database migrations, background workers, and security utilities.
# Development group includes modern linting and testing tools like ruff and pytest.
# Plugins allow for extensibility in third-party libraries.
""",

    "python/flit-pyproject.toml": """[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "lightweight-pkg"
authors = [{name = "Alice Lightweight", email = "alice@example.com"}]
dynamic = ["version", "description"]
dependencies = [
    "requests >=2.25",
    "importlib_metadata; python_version < '3.8'",
]
requires-python = ">=3.7"
readme = "README.md"
license = {file = "LICENSE"}
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

[project.optional-dependencies]
test = [
    "pytest >=6.0",
    "pytest-cov",
]
doc = [
    "sphinx",
    "myst-parser",
]

[project.urls]
Documentation = "https://lightweight-pkg.readthedocs.io/"
Source = "https://github.com/alice/lightweight-pkg"

[project.scripts]
lw-cli = "lightweight_pkg.cli:main"

[tool.flit.metadata]
module = "lightweight_pkg"
dist-name = "lightweight-pkg"

# Flit is a way to put Python packages and modules on PyPI.
# It focuses on simplicity and ease of use.
# It doesn't use setup.py, instead relying on pyproject.toml.
# This configuration defines a simple package with CLI entry points.
# It supports dynamic versioning and description from the source code.
# Optional dependencies are grouped by purpose (test, doc).
# The metadata section explicitly points to the source module.
# Flit is ideal for pure Python projects that don't need complex build steps.
# It automates the process of creating a source distribution and a wheel.
# The classifiers help users find the package on PyPI based on license and version.
""",

    "python/setuptools-pyproject.toml": """[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "classic-setuptools-project"
version = "1.0.0"
description = "A project using the modern pyproject.toml interface for setuptools."
authors = [
    { name="Old School Coder", email="osc@example.com" }
]
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "numpy>=1.21.0",
    "pandas>=1.3.0",
]

[project.optional-dependencies]
dev = ["pytest", "ruff"]

[tool.setuptools]
packages = ["my_package", "my_package.utils"]

[tool.setuptools.package-data]
"*" = ["*.txt", "*.dat"]

[tool.setuptools.dynamic]
version = {attr = "my_package.__version__"}

# Setuptools is the venerable build system for Python.
# Recently, it has adopted the pyproject.toml standard for configuration.
# This file shows how to define project metadata and dependencies.
# It also demonstrates how to specify packages to include.
# Package data inclusion is handled via the tool.setuptools section.
# Dynamic versioning can still be pulled from a package attribute.
# This approach replaces the old setup.cfg and setup.py files.
# It maintains compatibility with modern PEP 517 build frontends.
# Setuptools remains highly flexible for complex builds involving C extensions.
# However, this example focuses on a pure Python project.
# The build-system section specifies the backend required to build the package.
# This ensures that tools like pip can correctly build the project from source.
""",

    "python/django-pyproject.toml": """[project]
name = "django-enterprise-portal"
version = "0.1.0"
dependencies = [
    "django>=4.2,<5.0",
    "psycopg2-binary>=2.9",
    "django-environ>=0.10.0",
    "django-crispy-forms>=2.0",
    "crispy-bootstrap5>=0.7",
    "django-allauth>=0.54.0",
    "django-extensions>=3.2.0",
    "django-debug-toolbar>=4.1.0",
    "django-storages[google]>=1.13.0",
    "gunicorn>=20.1.0",
    "whitenoise>=6.5.0",
    "celery[redis]>=5.3.0",
    "django-celery-beat>=2.5.0",
    "django-celery-results>=2.5.0",
    "sentry-sdk>=1.25.0",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "DJ"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"**/migrations/*" = ["I001"]

[tool.mypy]
python_version = "3.11"
plugins = ["mypy_django_plugin.main"]
strict = true

[tool.django-stubs]
django_settings_module = "config.settings.local"

# Django Enterprise Portal Configuration
# This Django project is set up for a production environment.
# It uses PostgreSQL via psycopg2-binary.
# Environment variables are managed by django-environ.
# Frontend uses Crispy Forms with Bootstrap 5.
# Authentication is handled by django-allauth.
# Production serving involves Gunicorn and Whitenoise for static files.
# Background tasks are implemented with Celery and Redis.
# Monitoring is provided by Sentry.
# Static analysis is performed by Ruff and MyPy with Django-specific plugins.
# The Ruff config targets Python 3.11 and includes Django-specific linting rules.
# MyPy is configured for strict type checking, essential for large codebases.
""",

    "python/data-science-pyproject.toml": """[project]
name = "ml-research-pipeline"
version = "0.5.0"
dependencies = [
    "numpy>=1.24.0",
    "pandas>=2.0.0",
    "scikit-learn>=1.2.0",
    "scipy>=1.10.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "jupyterlab>=4.0.0",
    "notebook>=7.0.0",
    "ipywidgets>=8.0.0",
    "tqdm>=4.65.0",
    "dvc>=3.0.0",
    "mlflow>=2.3.0",
    "hydra-core>=1.3.0",
]

[project.optional-dependencies]
cuda = [
    "torch>=2.0.0",
    "torchvision>=0.15.0",
    "pytorch-lightning>=2.0.0",
]
nlp = [
    "transformers>=4.30.0",
    "datasets>=2.12.0",
    "tokenizers>=0.13.0",
]

[tool.black]
line-length = 88
target-version = ["py39", "py310", "py311"]

[tool.isort]
profile = "black"

# ML Research Pipeline Configuration
# Designed for data science and machine learning workflows.
# Core stack includes NumPy, Pandas, Scikit-Learn, and SciPy.
# Visualization is handled by Matplotlib and Seaborn.
# Interactive development occurs in JupyterLab.
# Experiment tracking and versioning use DVC and MLflow.
# Configuration management is powered by Hydra.
# Optional extras provide support for CUDA-accelerated Deep Learning.
# NLP specific libraries are also available as an optional group.
# Code formatting follows the Black standard, ensuring consistency.
# Isort is configured to be compatible with Black's formatting rules.
# This setup supports reproducible research and scalable ML pipelines.
""",

    "python/ruff.toml": """# Standalone Ruff configuration file
line-length = 120
indent-width = 4
target-version = "py311"

[lint]
# Enable Pyflakes (`F`) and a subset of the pycodestyle (`E`)  codes by default.
# Unlike Flake8, Ruff doesn't enable pycodestyle warnings (`W`) or
# error codes (`E`) by default; these must be opted into explicitly.
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "ARG", # flake8-unused-arguments
    "PT",  # flake8-pytest-style
    "SIM", # flake8-simplify
]
ignore = [
    "E501", # Line too long (handled by formatter)
    "B008", # Do not perform function calls in argument defaults
]

# Allow fix for all enabled rules (when `--fix`) is provided.
fixable = ["ALL"]
unfixable = []

# Allow unused variables when underscore-prefixed.
dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"

[lint.per-file-ignores]
"__init__.py" = ["F401"]
"tests/**/*.py" = ["ARG001"]

[format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

# Ruff is an extremely fast Python linter and formatter, written in Rust.
# It is designed to be a drop-in replacement for Flake8, isort, and Black.
# This configuration demonstrates a wide selection of rules.
# It includes bugbear for catching common pitfalls.
# Pyupgrade helps keep the codebase modern.
# Formatting options match the standard Python conventions.
# Per-file ignores allow for exceptions in init files and tests.
""",

    "rust/axum-cargo.toml": """[package]
name = "axum-microservice"
version = "0.1.0"
edition = "2021"
authors = ["Rust Dev <dev@example.com>"]
description = "A high-performance microservice built with Axum and Tokio."

[dependencies]
axum = { version = "0.7", features = ["macros"] }
tokio = { version = "1.0", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
sqlx = { version = "0.7", features = ["runtime-tokio-rustls", "postgres", "uuid", "chrono"] }
tower = { version = "0.4", features = ["util", "timeout", "load-shed", "limit"] }
tower-http = { version = "0.5", features = ["trace", "compression-full", "cors"] }
tracing = "0.1"
tracing-subscriber = { version = "0.3", features = ["env-filter", "json"] }
chrono = { version = "0.4", features = ["serde"] }
uuid = { version = "1.0", features = ["v4", "serde"] }
config = "0.13"
anyhow = "1.0"
thiserror = "1.0"
validator = { version = "0.16", features = ["derive"] }

[dev-dependencies]
tower = { version = "0.4", features = ["util"] }
hyper = { version = "1.0", features = ["full"] }
mime = "0.3"

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
panic = "abort"

# This Cargo.toml defines a modern Rust web service.
# Axum is a web application framework that focuses on ergonomics and modularity.
# Tokio provides the asynchronous runtime.
# SQLx is used for compile-time checked SQL queries against PostgreSQL.
# Tower and Tower-HTTP provide middleware for tracing, CORS, and compression.
# Tracing is used for structured logging.
# Anyhow and Thiserror manage error handling gracefully.
# The release profile is optimized for binary size and performance.
""",

    "rust/bevy-cargo.toml": """[package]
name = "bevy-game-engine-project"
version = "0.1.0"
edition = "2021"
description = "A 3D game prototype using the Bevy engine."

[dependencies]
bevy = { version = "0.13", features = ["dynamic_linking"] }
bevy_rapier3d = { version = "0.25", features = ["simd-stable", "debug-render-3d"] }
bevy_asset_loader = { version = "0.20", features = ["standard_dynamic_assets"] }
leafwing-input-manager = "0.13"
serde = { version = "1.0", features = ["derive"] }
rand = "0.8"

[features]
default = ["dev"]
dev = [
    "bevy/bevy_winit",
    "bevy/bevy_render",
    "bevy/bevy_png",
    "bevy/render",
    "bevy/x11",
]
release = [
    "bevy/bevy_winit",
    "bevy/bevy_render",
    "bevy/bevy_png",
    "bevy/render",
]

[profile.dev]
opt-level = 1

[profile.dev.package."*"]
opt-level = 3

# Bevy is a refreshingly simple data-driven game engine built in Rust.
# It uses the Entity Component System (ECS) pattern.
# This config enables dynamic linking for faster iteration during development.
# Rapier3D provides physics simulation.
# Leafwing-input-manager simplifies handling complex input patterns.
# The features table allows toggling between development and release builds.
# Development profile optimizes dependencies for speed while keeping the main crate debuggable.
# Bevy is highly modular, allowing you to include only the features you need.
# This setup is ideal for rapid prototyping of 3D games.
""",

    "rust/cli-tool-cargo.toml": """[package]
name = "rust-cli-tool"
version = "1.2.3"
edition = "2021"
authors = ["Tool Maker <tools@example.com>"]
description = "A versatile CLI tool for data processing and API interaction."

[dependencies]
clap = { version = "4.4", features = ["derive", "env"] }
tokio = { version = "1.30", features = ["rt-multi-thread", "macros"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
reqwest = { version = "0.11", features = ["json", "rustls-tls"] }
indicatif = "0.17"
console = "0.15"
dialoguer = "0.10"
colored = "2.0"
anyhow = "1.0"
dirs = "5.0"
chrono = "0.4"
csv = "1.2"
regex = "1.9"

[dev-dependencies]
assert_cmd = "2.0"
predicates = "3.0"
tempfile = "3.8"

# A robust Command Line Interface (CLI) tool configuration.
# Clap handles argument parsing with support for subcommands and environment variables.
# Reqwest is used for making HTTP requests to external APIs.
# Indicatif and Console provide progress bars and terminal styling.
# Dialoguer enables interactive prompts for user input.
# Colored adds color to the terminal output for better readability.
# Anyhow simplifies error propagation in the main function.
# Dirs helps locate standard configuration and cache directories.
# Assert_cmd and Predicates are used for integration testing the CLI behavior.
# This tool is designed to be fast, user-friendly, and well-tested.
""",

    "rust/workspace-root-cargo.toml": """[workspace]
members = [
    "crates/api-server",
    "crates/worker",
    "crates/shared-logic",
    "crates/db-migration",
    "crates/cli-admin",
]

resolver = "2"

[workspace.dependencies]
tokio = { version = "1.30", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
tracing = "0.1"
sqlx = { version = "0.7", features = ["postgres", "runtime-tokio-rustls"] }
anyhow = "1.0"
thiserror = "1.0"
chrono = { version = "0.4", features = ["serde"] }
uuid = { version = "1.0", features = ["v4", "serde"] }

[profile.release]
lto = "thin"
strip = true

# Cargo workspaces allow managing multiple related packages in a single repository.
# Shared dependencies are defined at the workspace level for version consistency.
# Members are paths to the individual crates within the workspace.
# Resolver 2 is the modern feature resolver for Cargo.
# This structure is common for large-scale Rust projects with multiple components.
# It simplifies building, testing, and publishing related tools.
# Release profile includes thin LTO and symbol stripping to reduce binary size.
""",

    "rust/rustfmt.toml": """# Rustfmt configuration
version = "Two"
use_small_heuristics = "Max"
newline_style = "Unix"
tab_spaces = 4
use_tabs = false

# Formatting rules
brace_style = "SameLineWhere"
control_brace_style = "AlwaysNextLine"
empty_item_single_line = true
fn_single_line = false
where_single_line = false

# Imports
imports_granularity = "Crate"
group_imports = "StdExternalCrate"
reorder_imports = true

# Structs and Enums
struct_field_align_threshold = 20
enum_discrim_align_threshold = 20

# Comments
wrap_comments = true
comment_width = 100
normalize_comments = true

# Misc
edition = "2021"
merge_derives = true
remove_nested_parens = true

# Rustfmt is the official tool for formatting Rust code according to style guidelines.
# This configuration file allows customizing the formatting behavior.
# It covers heuristics, brace styles, import grouping, and comment wrapping.
# Consistent formatting is essential for readability in collaborative projects.
# Many of these settings deviate slightly from the default to show possibilities.
# Using 'Two' for version enables more modern formatting features.
""",

    "configs/netlify.toml": """[build]
  command = "npm run build"
  publish = "dist"
  environment = { NODE_VERSION = "18", NPM_FLAGS = "--version" }

[context.production]
  environment = { DEBUG = "false" }

[context.deploy-preview]
  command = "npm run build:preview"

[[redirects]]
  from = "/old-path"
  to = "/new-path"
  status = 301
  force = true

[[redirects]]
  from = "/api/*"
  to = "https://api.example.com/:splat"
  status = 200

[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[plugins]]
  package = "@netlify/plugin-sitemap"
  [plugins.inputs]
    baseUrl = "https://example.com"
    exclude = ["/admin/*", "/404"]

[functions]
  directory = "netlify/functions"
  node_version = "18"

# Netlify configuration file (netlify.toml).
# Specifies how Netlify should build and deploy your site.
# Includes environment variables, redirects, custom headers, and plugins.
# Context-specific overrides allow different build commands for production and previews.
# Redirects handle legacy paths and proxying to external APIs.
# Headers optimization helps with caching strategy for assets.
# Plugins extend the build process with features like sitemap generation.
# Functions section configures Netlify's serverless functions environment.
""",

    "configs/hugo-config.toml": """baseURL = "https://example.com/"
languageCode = "en-us"
title = "My Professional Blog"
theme = "ananke"

[params]
  description = "A blog about technology, design, and software engineering."
  author = "Jane Doe"
  github = "https://github.com/janedoe"
  twitter = "https://twitter.com/janedoe"

[[menu.main]]
  name = "Home"
  url = "/"
  weight = 10

[[menu.main]]
  name = "Articles"
  url = "/posts/"
  weight = 20

[[menu.main]]
  name = "About"
  url = "/about/"
  weight = 30

[taxonomies]
  category = "categories"
  tag = "tags"
  series = "series"

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.highlight]
    codeFences = true
    guessSyntax = true
    lineNos = true
    style = "monokai"

[outputs]
  home = ["HTML", "RSS", "JSON"]

# Hugo is a popular static site generator written in Go.
# It is known for its incredible speed and flexibility.
# This configuration file defines the site structure and metadata.
# Params section provides variables accessible in templates.
# Menu configuration sets up the main navigation bar.
# Taxonomies allow for flexible content organization.
# Markup section configures the Markdown renderer (Goldmark).
# Multiple output formats can be generated for the homepage.
""",

    "configs/zola-config.toml": """# The URL the site will be built for
base_url = "https://example.com"
title = "Zola Portfolio"
description = "Showcase of my projects and thoughts."
default_language = "en"

# Whether to build a search index to be used later on by a library
build_search_index = true

[taxonomies]
tags = { name = "tags", feed = true }
categories = { name = "categories", feed = true }

[markdown]
# Whether to highlight code blocks and which theme to use
highlight_code = true
highlight_theme = "base16-ocean-dark"
render_emoji = true
external_links_target_blank = true

[extra]
# Custom variables for use in templates
author_name = "John Smith"
social_links = [
    { name = "GitHub", url = "https://github.com/jsmith" },
    { name = "LinkedIn", url = "https://linkedin.com/in/jsmith" },
]

[search]
# Configuration for the search index
index_format = "elasticlunr_javascript"
include_title = true
include_description = true
include_content = true

# Zola is a single-binary static site generator with everything built-in.
# It uses the Tera template engine, which is similar to Jinja2.
# Taxonomies are configured with optional RSS/Atom feeds.
# Markdown features include syntax highlighting and emoji support.
# Extra section allows for site-specific custom variables.
# Built-in search functionality is easy to enable and configure.
""",

    "configs/dprint.toml": """incremental = true

[plugins]
typescript = "https://plugins.dprint.dev/typescript-0.88.8.wasm"
json = "https://plugins.dprint.dev/json-0.19.1.wasm"
markdown = "https://plugins.dprint.dev/markdown-0.16.0.wasm"
toml = "https://plugins.dprint.dev/toml-0.6.1.wasm"
dockerfile = "https://plugins.dprint.dev/dockerfile-0.3.0.wasm"

[typescript]
quoteStyle = "alwaysDouble"
semiColons = "always"
arrowFunction.useParentheses = "force"

[json]
indentWidth = 2

[markdown]
textWrap = "always"

[includes]
**/*.{ts,tsx,js,jsx,json,md,toml,dockerfile}

[excludes]
**/node_modules
**/dist
**/*-lock.json

# dprint is a pluggable and configurable code formatting platform.
# It is extremely fast and can format multiple languages.
# This config enables plugins for TS, JSON, Markdown, TOML, and Dockerfile.
# Language-specific settings are defined in their own tables.
# Includes and excludes patterns control which files are formatted.
# Incremental mode ensures only changed files are processed, saving time.
""",

    "configs/taplo.toml": """# Taplo configuration for TOML files
include = ["**/*.toml"]
exclude = ["**/node_modules/**"]

[formatting]
align_entries = true
align_comments = true
array_trailing_comma = true
array_auto_expand = true
array_auto_collapse = false
compact_arrays = false
compact_inline_tables = false
column_width = 80
indent_tables = true
indent_entries = false
indent_string = "  "
trailing_newline = true
reorder_keys = true

[linter]
no_redefinition = true
no_unknown_keys = true

[[rule]]
include = ["**/Cargo.toml"]
[rule.formatting]
reorder_keys = false

# Taplo is a versatile TOML toolkit written in Rust.
# It provides formatting, linting, and language server features.
# This configuration file defines the formatting style for all TOML files.
# It includes alignment options for entries and comments.
# Key reordering is enabled by default but disabled for Cargo.toml files.
# Linting rules catch common errors like key redefinitions.
# Taplo ensures your TOML files are clean, consistent, and error-free.
""",

    "configs/wrangler.toml": """name = "api-worker"
main = "src/index.ts"
compatibility_date = "2023-10-30"

[vars]
ENVIRONMENT = "production"
API_VERSION = "v1"

[[kv_namespaces]]
binding = "USER_SESSIONS"
id = "a1b2c3d4e5f6g7h8i9j0"

[[r2_buckets]]
binding = "USER_UPLOADS"
bucket_name = "my-uploads-bucket"

[[d1_databases]]
binding = "DB"
database_name = "users-db"
database_id = "f8e7d6c5b4a39281"

[routes]
pattern = "api.example.com/*"
custom_domain = true

[env.staging]
name = "api-worker-staging"
vars = { ENVIRONMENT = "staging" }

# Cloudflare Workers configuration file.
# Defines the worker's name, entry point, and compatibility date.
# Bindings for KV, R2, and D1 provide access to storage and databases.
# Routes specify which domains the worker should respond to.
# Environment overrides allow for staging and development setups.
# Variables are injected into the worker's global scope.
# Wrangler is the CLI tool for developing and deploying Cloudflare Workers.
""",

    "configs/traefik.toml": """[entryPoints]
  [entryPoints.web]
    address = ":80"
    [entryPoints.web.http.redirections.entryPoint]
      to = "websecure"
      scheme = "https"

  [entryPoints.websecure]
    address = ":443"

[providers]
  [providers.docker]
    exposedByDefault = false
  [providers.file]
    filename = "/etc/traefik/dynamic_conf.toml"

[api]
  dashboard = true

[certificatesResolvers.myresolver.acme]
  email = "admin@example.com"
  storage = "acme.json"
  [certificatesResolvers.myresolver.acme.httpChallenge]
    entryPoint = "web"

[log]
  level = "INFO"
  format = "json"

[accessLog]
  filePath = "/var/log/traefik/access.log"

# Traefik is a modern HTTP reverse proxy and load balancer.
# It is designed to deploy microservices with ease.
# This configuration sets up entrypoints for HTTP and HTTPS.
# Automatic HTTP to HTTPS redirection is configured.
# Docker provider is enabled but requires explicit labels.
# File provider allows for additional dynamic configuration.
# ACME resolver handles automatic SSL certificates via Let's Encrypt.
# API dashboard is enabled for monitoring.
# Structured logging in JSON format is used for better observability.
""",

    "configs/mdbook-book.toml": """[book]
authors = ["Documentation Team"]
language = "en"
multilingual = false
src = "src"
title = "Project Documentation"

[output.html]
git-repository-url = "https://github.com/example/project"
edit-url-template = "https://github.com/example/project/edit/main/docs/{path}"
google-analytics = "UA-XXXXX-Y"
mathjax-support = true

[output.html.playground]
editable = true
copyable = true

[preprocessor.links]
[preprocessor.index]

[output.linkcheck]
warning-policy = "warn"

# mdBook is a utility to create modern online books from Markdown files.
# It is commonly used for Rust project documentation.
# This config defines the book metadata and HTML output options.
# Integration with GitHub allows users to easily edit pages.
# MathJax support enables rendering of mathematical formulas.
# Interactive code playgrounds can be enabled for supported languages.
# Preprocessors can transform the content before it is rendered.
# A link checker ensures there are no broken links in the documentation.
""",

    "configs/foundry.toml": """[profile.default]
src = 'src'
out = 'out'
libs = ['lib']
remappings = [
    '@openzeppelin/=lib/openzeppelin-contracts/',
    'ds-test/=lib/forge-std/lib/ds-test/src/',
    'forge-std/=lib/forge-std/src/'
]
optimizer = true
optimizer_runs = 200
verbosity = 3

[rpc_endpoints]
mainnet = "https://eth-mainnet.g.alchemy.com/v2/${ALCHEMY_API_KEY}"
optimism = "https://opt-mainnet.g.alchemy.com/v2/${ALCHEMY_API_KEY}"
sepolia = "https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}"

[etherscan]
mainnet = { key = "${ETHERSCAN_API_KEY}" }
optimism = { key = "${OPTIMISM_ETHERSCAN_API_KEY}" }

# Foundry is a blazing fast, portable and modular toolkit for Ethereum development.
# It consists of Forge, Cast, and Anvil.
# This configuration file (foundry.toml) sets up the Solidity compiler and paths.
# Remappings help resolve imports from external libraries.
# Optimizer settings affect gas usage of deployed contracts.
# RPC endpoints are defined for various networks using environment variables.
# Etherscan configuration allows for automatic contract verification.
# High verbosity provides detailed information during testing.
""",

    "configs/starship.toml": """# Starship prompt configuration
add_newline = true

[format]
  list = [
    "$directory",
    "$git_branch",
    "$git_status",
    "$python",
    "$nodejs",
    "$rust",
    "$package",
    "$line_break",
    "$character"
  ]

[directory]
truncation_length = 3
truncate_to_repo = true
style = "bold blue"

[git_branch]
symbol = " "
style = "bold purple"

[git_status]
style = "bold red"
format = "([\\[$all_status$ahead_behind\\]]($style) )"

[python]
symbol = "🐍 "
style = "bold yellow"
pyenv_prefix = "pyenv "

[rust]
symbol = "🦀 "
style = "bold orange"

[character]
success_symbol = "[➜](bold green)"
error_symbol = "[➜](bold red)"

# Starship is the minimal, blazing-fast, and infinitely customizable prompt for any shell.
# This configuration customizes the order and appearance of modules.
# Symbols are added for Git, Python, and Rust using Nerd Fonts.
# Directory truncation keeps the prompt concise in deep paths.
# Color schemes are defined for different languages and states.
# The success and error symbols provide immediate feedback on the last command.
""",

    "configs/dependabot-config.toml": """# Note: Real Dependabot configuration typically uses YAML (.github/dependabot.yml).
# This is an illustrative TOML representation for compatibility testing.

version = 2

[[updates]]
package-ecosystem = "pip"
directory = "/"
schedule = { interval = "daily" }
open-pull-requests-limit = 10
allow = [{ dependency-type = "direct" }]
ignore = [
    { dependency-name = "django", versions = ["5.0.0"] }
]

[[updates]]
package-ecosystem = "cargo"
directory = "/"
schedule = { interval = "weekly" }
groups = { "rust-dependencies" = { patterns = ["*"] } }

[[updates]]
package-ecosystem = "npm"
directory = "/frontend"
schedule = { interval = "monthly" }

# Dependabot keeps your dependencies up to date automatically.
# It checks for new versions and opens pull requests.
# This TOML version demonstrates how ecosystems like pip, cargo, and npm are configured.
# Intervals can be daily, weekly, or monthly.
# Pull request limits prevent being overwhelmed by updates.
# Specific dependencies or versions can be ignored.
# Grouping updates helps reduce the number of pull requests.
""",

    "broken/broken-syntax-50.toml": """# This file contains deliberate syntax errors for testing.
title = "Broken TOML File"

# ERROR: Unclosed string
description = "This string is never closed

# ERROR: Unterminated array
numbers = [1, 2, 3, 4, 5

# ERROR: Conflicting redefinitions of the same key
duplicate_key = 100
duplicate_key = 200

# ERROR: Mismatched brackets
table = { key = "value" ]

# ERROR: Bare numbers as keys
123 = "numeric key is invalid"

# ERROR: Smart quotes instead of regular quotes
smart_quotes = “invalid”

# ERROR: Comment without hash
This is a comment without a hash symbol at the start

# ERROR: Invalid escape sequence
escape = "Invalid \\z escape"

# ERROR: Missing equals sign
missing_equals "oops"

# ERROR: Trailing comma in table
trailing_comma = { a = 1, }

# ERROR: Inline table on multiple lines
inline_table = {
    a = 1
}

# Some valid lines to fill up space
author = "Tester"
version = "1.0.0"
valid_key = true

# More padding to reach 50 lines
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
"""
}

def main():
    print(f"Generating TOML datasets in {BASE_DIR}...")
    
    for rel_path, content in FILES.items():
        abs_path = os.path.join(BASE_DIR, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        line_count = len(content.strip().splitlines())
        byte_count = len(content.encode("utf-8"))
        
        parse_status = "n/a"
        if tomllib:
            if "broken" in rel_path:
                parse_status = "expected error"
                try:
                    tomllib.loads(content)
                    parse_status = "ERROR (parsed despite being broken)"
                except Exception:
                    pass
            else:
                try:
                    tomllib.loads(content)
                    parse_status = "ok"
                except Exception as e:
                    parse_status = f"error: {str(e)}"
        else:
            parse_status = "skipped (tomllib missing)"
            
        print(f"{rel_path}: {line_count} lines, {byte_count} bytes, parse: {parse_status}")

if __name__ == "__main__":
    main()
