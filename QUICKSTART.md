# Quick Start Guide

## For First-Time Setup

### 1. Personalize Your Site

Edit `_config.yml` and update:
```yaml
title: Dan Palmer
email: dpalmer3@illinois.edu
description: Materials Science PhD student at University of Illinois at Urbana-Champaign
url: "https://dpalmer-anl.github.io"

# Social links
github_username: dpalmer-anl
linkedin_username: daniel-palmer-6a8788170
scholar_userid: your-google-scholar-id
orcid: 0000-0002-2504-4195
```

### 2. Update Content

**Home Page** (`index.md`):
- Update your bio and research interests
- Add your affiliation
- Update contact information

**Research Page** (`research.md`):
- Fill in details about your research projects
- Add publication references
- Update collaboration information

**Software Page** (`software.md`):
- Update repository links
- Ensure installation instructions are accurate
- Add any additional software projects

**Publications Page** (`publications.md`):
- Add your actual publications
- Include DOIs and links
- Update conference presentations

**CV Page** (`cv.md`):
- Fill in your education details
- Add your research experience
- Update skills, awards, and teaching experience
- Upload a PDF version of your CV to `assets/` folder

### 3. Test Locally

```bash
# Install dependencies (first time only)
bundle install

# Run local server
bundle exec jekyll serve

# Open http://localhost:4000 in your browser
```

### 4. Deploy to GitHub Pages

```bash
# Make sure you're in a git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial website setup"

# Add remote (if not already added)
git remote add origin https://github.com/dpalmer-anl/dpalmer-anl.github.io.git

# Push to GitHub
git push -u origin main
```

### 5. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch
4. Click **Save**
5. Your site will be available at `https://dpalmer-anl.github.io`

## Common Tasks

### Adding a New Publication

Edit `publications.md`:
```markdown
### 2024

1. **Your Name**, Co-Author. "Paper Title"
   - *Journal Name*, Volume(Issue), Pages (Year)
   - [arXiv:xxxx.xxxxx](https://arxiv.org) | [DOI](https://doi.org/xx.xxxx)
```

### Adding a New Software Project

Edit `software.md` and add a new section:
```markdown
## Project Name

<div class="software-card">

### Description

Project description here...

#### Key Features
- Feature 1
- Feature 2

#### Installation
\```bash
pip install your-package
\```

</div>
```

### Updating Your Photo

1. Add your photo to `assets/images/` (e.g., `profile.jpg`)
2. Edit `index.md` and add:
```markdown
<img src="/assets/images/profile.jpg" alt="Your Name" style="width: 200px; border-radius: 50%;">
```

### Changing Colors

Edit `assets/css/style.scss`:
```scss
$primary-color: #0066cc;    // Main accent color
$secondary-color: #2c3e50;  // Headers and footer
$accent-color: #3498db;     // Links and highlights
```

## Troubleshooting

### Site Not Building?

Check GitHub Actions tab in your repository for build errors.

### Changes Not Showing?

1. Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
2. Wait a few minutes for GitHub Pages to rebuild
3. Check that you pushed your changes: `git push`

### Ruby Errors Locally?

```bash
# Update bundle
bundle update

# Clean and rebuild
bundle exec jekyll clean
bundle exec jekyll serve
```

## Next Steps

- Add a blog by creating `_posts/` directory
- Add more pages (teaching, outreach, etc.)
- Customize styling in `assets/css/style.scss`
- Add images to `assets/images/`
- Consider adding a custom domain

## Need Help?

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Help](https://docs.github.com/en/pages)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

