# Resume Data - Single Source of Truth

## Master Files

These are the ONLY two files that should exist in this directory:

- **resume.json** - Your complete resume database (master copy)
- **resume_profiles.json** - Profile definitions for interactive filtering

## Important Notes

1. **No backups should be committed** - All backup files are gitignored
2. **This is the public version** - Contains sanitized contact info (no real phone/email)
3. **Version control via Git** - Use git history if you need to see old versions
4. **Single source of truth** - The website reads from these files directly

## Making Updates

To update your resume:

1. Edit `resume.json` directly
2. Test locally: `bundle exec jekyll serve`
3. Commit and push to GitHub
4. Site auto-deploys in 2-3 minutes

## Version History

Current version: 2.2.0 (2025-12-08)
- Updated AI/ML references to AI (accurate representation)
- Streamlined custom select checkboxes to 11 focused options
- Added epilepsy tags to BANZEL achievements
