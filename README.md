# Mark Schulz - Professional Website

A professional marketing and advertising portfolio website built with Jekyll and hosted on GitHub Pages.

## Quick Start

### Local Development

1. **Install Jekyll and dependencies:**
   ```bash
   gem install bundler jekyll
   bundle install
   ```

2. **Run the site locally:**
   ```bash
   bundle exec jekyll serve
   ```

3. **View in browser:**
   Open [http://localhost:4000](http://localhost:4000)

## Deployment to GitHub Pages

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `markschulz` (or `yourusername.github.io` for a user site)
3. Set to **Public**
4. Don't initialize with README (we already have one)

### Step 2: Push Your Site

```bash
cd /home/kryphion/coding/markschulz
git init
git add .
git commit -m "Initial commit - professional website"
git branch -M main
git remote add origin https://github.com/yourusername/markschulz.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under **Source**, select **Deploy from a branch**
4. Select **main** branch and **/ (root)** folder
5. Click **Save**

Your site will be live at `https://yourusername.github.io/markschulz/` in a few minutes!

### Step 4: Configure Custom Domain (Optional)

1. Purchase your domain (e.g., markschulz.com) from a registrar
2. Add DNS records at your registrar:
   ```
   Type: A
   Name: @
   Value: 185.199.108.153

   Type: A
   Name: @
   Value: 185.199.109.153

   Type: A
   Name: @
   Value: 185.199.110.153

   Type: A
   Name: @
   Value: 185.199.111.153

   Type: CNAME
   Name: www
   Value: yourusername.github.io
   ```

3. Create a file named `CNAME` in your repository root:
   ```bash
   echo "markschulz.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push
   ```

4. In GitHub Settings → Pages, add your custom domain
5. Enable **Enforce HTTPS** (after DNS propagates, 24-48 hours)

## Customization Checklist

### Essential Updates

- [ ] **_config.yml** - Update all personal information
  - [ ] Title, email, description
  - [ ] Author information
  - [ ] LinkedIn username
  - [ ] URL (your custom domain)

- [ ] **about.md** - Replace placeholder content
  - [ ] Professional background story
  - [ ] Complete work history
  - [ ] Education and certifications
  - [ ] Add actual resume PDF to `/assets/files/resume.pdf`

- [ ] **index.md** - Customize homepage
  - [ ] Update introduction
  - [ ] Tailor expertise areas to your experience

- [ ] **contact.md** - Set up contact form
  - [ ] Sign up at [Formspree.io](https://formspree.io/)
  - [ ] Replace `YOUR_FORM_ID` with actual form ID
  - [ ] Update LinkedIn and email links

- [ ] **Portfolio Items**
  - [ ] Delete example file: `_portfolio/example-campaign.md`
  - [ ] Add your actual case studies in `_portfolio/`

- [ ] **Blog Posts**
  - [ ] Delete example post: `_posts/2024-01-01-welcome-to-my-blog.md`
  - [ ] Add your articles (or leave empty until ready)

### Optional Enhancements

- [ ] **Analytics** - Uncomment Google Analytics in `_includes/custom-head.html`
- [ ] **Colors/Branding** - Customize CSS variables in `assets/css/custom.css`
- [ ] **Favicon** - Add your favicon files to root directory
- [ ] **Social Images** - Add og:image meta tags for social sharing

## Adding Content

### New Portfolio Item

Create a file in `_portfolio/` with this format:

```markdown
---
layout: portfolio-item
title: "Project Name"
client: Client Name
industry: Industry
date: 2024-01-15
excerpt: "Brief description for portfolio page"
---

# Project Name

Your case study content here...
```

### New Blog Post

Create a file in `_posts/` with format `YYYY-MM-DD-title.md`:

```markdown
---
layout: post
title: "Your Post Title"
date: 2024-01-15 10:00:00 -0500
categories: marketing strategy
excerpt: "Brief excerpt for blog listing"
---

Your blog post content here...
```

## LinkedIn Cross-Posting Setup

Your site includes an RSS feed at `/feed.xml` for automated LinkedIn posting:

1. **Option 1: Zapier (Recommended)**
   - Sign up at [Zapier.com](https://zapier.com)
   - Create new Zap: RSS → LinkedIn
   - RSS Feed URL: `https://yoursite.com/feed.xml`
   - Connect your LinkedIn account
   - Configure posting format

2. **Option 2: Buffer**
   - Sign up at [Buffer.com](https://buffer.com)
   - Add RSS feed under "Content" → "RSS Feeds"
   - Configure LinkedIn posting schedule

3. **Option 3: IFTTT**
   - Create applet: RSS Feed → LinkedIn
   - Similar setup to Zapier

## Privacy & Security Best Practices

✅ **Do Include:**
- Professional email
- City/State location
- LinkedIn profile
- Work history and achievements
- Professional portfolio samples

❌ **Don't Include:**
- Full home address
- Personal phone number (use Google Voice if needed)
- Full birthdate
- Social Security Number or other sensitive IDs
- Personal/family information

## Maintenance

### Updating Content

1. Edit files locally
2. Test with `bundle exec jekyll serve`
3. Commit and push to GitHub
4. Site auto-rebuilds in 1-2 minutes

### Updating Dependencies

```bash
bundle update
git add Gemfile.lock
git commit -m "Update dependencies"
git push
```

## Troubleshooting

**Site not showing changes?**
- Wait 2-3 minutes for GitHub to rebuild
- Check GitHub Actions tab for build errors
- Clear browser cache

**Custom domain not working?**
- DNS can take 24-48 hours to propagate
- Verify DNS records at your registrar
- Check GitHub Pages settings

**Contact form not working?**
- Verify Formspree form ID is correct
- Check Formspree dashboard for submissions
- Test form submission logged out

## Support

- **Jekyll Documentation:** [jekyllrb.com](https://jekyllrb.com)
- **GitHub Pages:** [docs.github.com/pages](https://docs.github.com/en/pages)
- **Formspree:** [help.formspree.io](https://help.formspree.io)

## License

This is a personal website. All content is copyright Mark Schulz unless otherwise noted.
