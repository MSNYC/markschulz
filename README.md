# Mark Schulz - Professional Portfolio

A single-page interactive portfolio and resume website for pharmaceutical marketing professional Mark Schulz. Built with Jekyll and hosted on GitHub Pages.

**Live Site:** [markschulz.me](https://markschulz.me)

## Features

- **Interactive Resume Builder**: Visitors can select pre-built profiles (Brand Management, Strategic Planning, Customer Experience) or create custom filtered resumes by choosing specific focus areas
- **Dynamic Content Filtering**: JavaScript-powered resume filtering based on therapeutic areas, audiences, and skills
- **Responsive Design**: Mobile-first design with modern card layouts and smooth animations
- **Privacy-Focused**: No tracking or analytics - visitor privacy is respected
- **Contact Form**: Integrated Formspree contact form for inquiries

## Tech Stack

- **Static Site Generator**: Jekyll 4.3+
- **Hosting**: GitHub Pages
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Interactivity**: Vanilla JavaScript (no frameworks)
- **Form Handling**: Formspree
- **Theme Base**: Minima (heavily customized)

## Project Structure

```
├── _includes/          # Reusable components (header, footer, head)
├── _layouts/           # Page layouts
├── assets/
│   ├── css/           # Custom stylesheets
│   ├── js/            # Resume builder JavaScript
│   └── data/          # Resume data (JSON)
├── resume/            # Pre-built profile pages
├── index.md           # Main single-page site
└── _config.yml        # Jekyll configuration
```

## Local Development

### Prerequisites

- Ruby 2.7+ (macOS comes with Ruby)
- Bundler and Jekyll gems

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/markschulz.git
   cd markschulz
   ```

2. **Install dependencies:**
   ```bash
   gem install bundler jekyll
   bundle install
   ```

3. **Run local server:**
   ```bash
   bundle exec jekyll serve
   ```

4. **View in browser:**
   Open [http://localhost:4000](http://localhost:4000)

## Content Updates

### Updating Resume Data

Resume content is stored in `assets/data/resume.json`. To update:

1. Edit `assets/data/resume.json` with new achievements, skills, or experience
2. Test locally with `bundle exec jekyll serve`
3. Commit and push to GitHub
4. Site auto-deploys in 2-3 minutes

### Modifying Styles

- **Main styles**: `assets/css/custom.css`
- **Resume builder**: `assets/css/resume-builder.css`
- **Executive resume**: `assets/css/resume-executive.css`

CSS uses custom properties (CSS variables) for consistent theming:
- `--accent-cyan`: Primary accent color
- `--bg-primary`, `--bg-secondary`: Background colors
- `--text-bright`, `--text-secondary`: Text colors

## Deployment

This site deploys automatically via GitHub Pages when changes are pushed to the `main` branch.

### Custom Domain Setup

The site uses a custom domain (`markschulz.me`). DNS configuration:

**A Records** (point to GitHub Pages):
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

**CNAME Record**:
- Name: `www`
- Value: `yourusername.github.io`

**In Repository**:
- Create `CNAME` file in root with domain name
- Enable "Enforce HTTPS" in GitHub Pages settings

## Privacy & Security

✅ **Public Information:**
- Professional work history and achievements
- City/State location (New York, NY)
- LinkedIn profile link

❌ **Private Information (NOT included):**
- Personal email address
- Phone number
- Home address
- Any sensitive personal data

**Contact Methods:**
- LinkedIn: [linkedin.com/in/mschulz](https://linkedin.com/in/mschulz)
- Contact form powered by Formspree

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Maintenance

### Updating Dependencies

```bash
bundle update
git add Gemfile.lock
git commit -m "Update dependencies"
git push
```

### Troubleshooting

**Site not updating after push?**
- GitHub Pages takes 2-3 minutes to rebuild
- Check GitHub Actions tab for build errors
- Clear browser cache

**Contact form not working?**
- Verify Formspree form ID is correct in `index.md`
- Check Formspree dashboard for submissions
- Ensure form action URL is `https://formspree.io/f/mwpgnrjn`

## License

All content is © 2025 Mark Schulz. Code structure may be used as reference for educational purposes.

## Built With

This site was developed with assistance from [Claude Code](https://claude.com/claude-code), demonstrating AI-assisted web development workflows.
