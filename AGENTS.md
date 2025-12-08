# Repository Guidelines

## Project Structure & Module Organization
- Root Jekyll config lives in `_config.yml`; global includes sit in `_includes/` and layouts in `_layouts/`.
- Content pages (e.g., `index.md`, `about.md`, `contact.md`, `blog.md`, `portfolio.md`) reference layouts via front matter; blog posts go in `_posts/` and portfolio items in `_portfolio/`.
- Static assets live under `assets/` (`css/`, `js/`, images/files); data-driven content can use `data/` YAML/JSON files.
- Documentation and marketing collateral are under `docs/` and `resume/`; generated site output (if any) should stay out of version control.

## Build, Test, and Development Commands
- `bundle install` — install Ruby gems defined for the site.
- `bundle exec jekyll serve` — run the site locally at `http://localhost:4000`; use `--livereload` for live refresh during edits.
- `bundle exec jekyll build` — produce the static site in `_site/` for manual inspection or deployment previews.
- `bundle update` — refresh gem versions; commit `Gemfile.lock` with the update.

## Coding Style & Naming Conventions
- Prefer 2-space indentation for HTML/Liquid/Markdown snippets; keep YAML front matter compact with consistent key order.
- Use kebab-case for file names in `_posts/` (`YYYY-MM-DD-title.md`) and `_portfolio/` (`client-or-project-name.md`).
- Keep Liquid logic minimal inside pages; extract repeated fragments to `_includes/` and reuse.
- CSS lives in `assets/css/`; favor small, purposeful overrides over large rewrites to retain maintainability.

## Testing Guidelines
- No automated test harness is present; validate changes by running `bundle exec jekyll serve` and manually reviewing affected pages.
- Check generated HTML for broken links, missing assets, and layout regressions across desktop and mobile.
- Before publishing, run `bundle exec jekyll build` to ensure the site compiles cleanly without warnings.

## Commit & Pull Request Guidelines
- Follow concise, present-tense commit messages (`add hero copy`, `tune portfolio layout`); group related edits together.
- PRs should include: a brief summary of the change, links to any relevant issues/tasks, screenshots or GIFs for visual updates, and steps to reproduce or verify.
- Keep diffs focused; separate content updates from structural or styling changes when possible for easier review.

## Security & Configuration Tips
- Do not commit secrets or form IDs; keep `.env`-style values local and inject via `_config.yml` overrides per environment if needed.
- When adding third-party scripts or analytics, place them in `_includes/` and document their purpose to aid future maintenance.
