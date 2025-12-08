#!/bin/bash
# Sync resume data from private backend to public website
# Run this after updating data/resume.json with new achievements

echo "Syncing resume data to public website..."

cp data/resume.json assets/data/resume.json
cp data/resume_profiles.json assets/data/resume_profiles.json

echo "✅ Synced:"
echo "  data/resume.json → assets/data/resume.json"
echo "  data/resume_profiles.json → assets/data/resume_profiles.json"
echo ""
echo "Next steps:"
echo "  1. Review changes: git diff assets/data/"
echo "  2. Test locally: bundle exec jekyll serve"
echo "  3. Commit: git add assets/data/ && git commit -m 'Update public resume'"
echo "  4. Push: git push"
