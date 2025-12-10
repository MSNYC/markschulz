# Security & Privacy Configuration

**Last Updated:** 2025-12-10

This document explains what data is public vs private in this repository and GitHub Pages site.

---

## 🔒 PRIVATE (Never Published)

### Protected by `.gitignore` (Never in Git)
These files are **never committed** to GitHub:

- ✅ `.env` - API keys and secrets
- ✅ `data/raw_inputs/` - Old resumes, performance reviews, source PDFs
- ✅ `data/resume_backup_*.json` - Backup files
- ✅ `data/processed_files.json` - Processing metadata
- ✅ `data/assessments/` - Personality assessments (Myers-Briggs, FIRO-B)
- ✅ `__pycache__/`, `*.pyc` - Python cache files

**Status:** ✅ Not in repository, not accessible anywhere

---

### In GitHub Repository (Public)
These files **are in the public GitHub repo** (visible to anyone) but are **NOT published** to GitHub Pages website:

- 📄 `CLAUDE.md` - Development guidelines for AI-assisted coding
- 📄 `AGENTS.md` - Repository conventions and build commands
- 📄 `SECURITY.md` - This security documentation
- 📄 `README.md` - Repository documentation

**Status:** ⚠️ Public on GitHub, but NOT on markschulz.me website

**Note:** These files contain technical documentation about the site architecture and development workflow. They do not contain sensitive data, passwords, or private information.

---

### Protected by Jekyll `exclude` (In Git, But Not Published)
These files **are in GitHub** (public repo) but are **NOT published** to GitHub Pages:

- ✅ `data/` - Backend resume data and processing scripts
- ✅ `scripts/` - Resume manager and Python utilities
- ✅ `docs/` - Source documents and planning materials
- ✅ `output/` - Generated resume exports
- ✅ `.venv/` - Python virtual environment
- ✅ `*.py` - All Python files

**Status:** ⚠️ In public GitHub repo, but NOT on website

---

## 🌐 PUBLIC (Published to Website)

### Published by Jekyll to GitHub Pages
These files **are visible** on your public website:

- 📄 Website pages: `index.md`, `about.md`, etc.
- 📁 `_portfolio/` - Portfolio case studies
- 📁 `_posts/` - Blog posts
- 📁 `assets/` - CSS, JavaScript, images
- 📄 `resume-interactive.html` - Interactive resume page
- 📄 `assets/data/resume.json` - **PUBLIC resume data for interactive resume**
- 📄 `assets/data/resume_profiles.json` - Profile filtering configuration

**Status:** ✅ Publicly accessible (intended)

**Note:** The files in `assets/data/` are PUBLIC copies used by the interactive resume. They contain your professional achievements and are meant to be visible to website visitors. The private backend version in `data/` is excluded.

---

## 🎯 How Data is Used

### Backend Data (`data/resume.json`)
- **Location:** Excluded from Jekyll (private)
- **Used by:** Python extraction scripts and resume generators
- **Contains:** Full career history including all extracted achievements
- **Accessible:** Only in private GitHub repo (if repo is private)
- **Published:** ❌ NEVER published to website

### Public Data (`assets/data/resume.json`)
- **Location:** Published to website
- **Used by:** Interactive resume JavaScript
- **Contains:** Professional achievements you want to showcase
- **Accessible:** ✅ Public on your website
- **Published:** ✅ Anyone can view at https://yoursite.com/assets/data/resume.json

### Data Sync Workflow
When you want to update the public resume with new achievements:

```bash
# After running batch processor and reviewing data/resume.json:
cp data/resume.json assets/data/resume.json
cp data/resume_profiles.json assets/data/resume_profiles.json

# Commit and push
git add assets/data/
git commit -m "Update public resume data"
git push
```

**You control when the public data is updated!**

### Interactive Resume (`resume-interactive.html`)
- **Location:** Published to website
- **Fetches data from:** `assets/data/resume.json` at runtime
- **Privacy:** Shows only what's in `assets/data/resume.json`
- **Filtering:** Uses tags from `assets/data/resume_profiles.json` to filter by role

---

## 🔍 Verification Steps

### 1. Check what's in Git:
```bash
git ls-files | grep -E "(data|scripts|docs)"
```

### 2. Check what's excluded from Jekyll:
```bash
grep -A 20 "^exclude:" _config.yml
```

### 3. Check what's gitignored:
```bash
cat .gitignore
```

### 4. Verify website build doesn't include sensitive data:
```bash
bundle exec jekyll build
ls -la _site/data/  # Should return "No such file or directory"
ls -la _site/scripts/  # Should return "No such file or directory"
```

---

## ⚠️ Important Notes

### GitHub Repository Visibility
- **Current:** Private repository
- **When public:** Only files not in `.gitignore` will be visible
- **Recommendation:** Keep repo private OR audit all committed files before making public

### GitHub Pages
- **Publishes from:** `_site/` directory (Jekyll build output)
- **Excludes:** Everything in Jekyll's `exclude` list
- **Safety:** Even if repo is public, excluded files won't be on the website

### Data Workflow
```
Source Docs (raw_inputs/)
  ↓ [gitignored - never in Git]
Python Scripts Process
  ↓ [in Git but excluded from Jekyll]
data/resume.json Updated
  ↓ [in Git but excluded from Jekyll]
Manual Curation
  ↓
resume-interactive.html
  ↓ [published to website]
Public Website
```

---

## 🛡️ Security Checklist

Before making repository public:
- [ ] Verify `.env` is gitignored
- [ ] Verify `data/raw_inputs/` is gitignored
- [ ] Check `git log` for any accidentally committed secrets
- [ ] Review all committed files: `git ls-files`
- [ ] Build Jekyll site and verify `_site/` doesn't contain sensitive data
- [ ] Test GitHub Pages preview before going live

Before publishing to GitHub Pages:
- [ ] Review `_config.yml` exclude list
- [ ] Build site locally: `bundle exec jekyll serve`
- [ ] Check `_site/` directory for any sensitive files
- [ ] Verify interactive resume only shows intended data
- [ ] Test all public pages in incognito browser

---

## 📞 If You Find Exposed Data

If you discover sensitive data is accessible:

1. **Immediate:** Take site offline (disable GitHub Pages in repo settings)
2. **Fix:** Add files to `exclude` in `_config.yml`
3. **Verify:** Rebuild and check `_site/` directory
4. **Republish:** Re-enable GitHub Pages
5. **Audit:** Review commit history for leaked secrets

---

## 🔐 Summary

**TRULY PRIVATE (Never in Git):**
- ✅ API keys (`.env`)
- ✅ Source documents (`data/raw_inputs/`)
- ✅ Personal assessments
- ✅ Backup files

**IN PUBLIC GITHUB REPO (But Not on Website):**
- ⚠️ Development documentation (`CLAUDE.md`, `AGENTS.md`, `SECURITY.md`)
- ⚠️ Backend data (`data/resume.json`, Python scripts)
- ⚠️ Repository guidelines and architecture docs

**PUBLIC ON WEBSITE (markschulz.me):**
- ✅ Website pages and blog posts
- ✅ Portfolio case studies
- ✅ Interactive resume (`assets/data/resume.json` - curated data only)
- ✅ CSS, JavaScript, images

**Protection layers:**
1. `.gitignore` - keeps sensitive files (API keys, source docs) out of Git entirely
2. Jekyll `exclude` - keeps backend files out of published website
3. Public repo - development files visible on GitHub but not on your site
4. Manual curation - you control what goes in the public interactive resume

**Bottom line:**
- Your source documents, API keys, and assessments are **never** in Git
- Your backend development files are in the public GitHub repo (technical docs only)
- Only curated resume data appears on markschulz.me
- No sensitive personal information is publicly accessible
