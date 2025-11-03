# Personal Academic Website

A professional Jekyll-based website for showcasing research in computational materials science.

## Overview

This website is built using Jekyll and is designed to be hosted on GitHub Pages. It features:

- **Home Page**: Introduction and research overview
- **Research**: Detailed descriptions of research projects
- **Software**: Documentation of open-source software packages (TETB_GRAPHENE, BLG_model_builder)
- **Publications**: List of academic publications and presentations
- **CV**: Curriculum Vitae

## Local Development

### Prerequisites

- Ruby (version 2.7 or higher)
- RubyGems
- Bundler

### Setup

1. Clone this repository:
```bash
git clone https://github.com/dpalmer-anl/dpalmer-anl.github.io.git
cd dpalmer-anl.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Run the Jekyll server locally:
```bash
bundle exec jekyll serve
```

4. Open your browser and navigate to `http://localhost:4000`

### Making Changes

- Edit content in the `.md` files
- Modify layouts in `_layouts/`
- Update styles in `assets/css/style.scss`
- Add new pages by creating new `.md` files with proper front matter

## Deployment

This site is configured for GitHub Pages deployment:

1. Commit your changes:
```bash
git add .
git commit -m "Update website content"
```

2. Push to GitHub:
```bash
git push origin main
```

GitHub Pages will automatically build and deploy your site.

## Configuration

Edit `_config.yml` to update:
- Site title and description
- Your contact information
- Social media links (GitHub, LinkedIn, Google Scholar, ORCID)
- Navigation menu items

## Customization

### Adding a New Page

1. Create a new `.md` file (e.g., `teaching.md`)
2. Add front matter:
```yaml
---
layout: page
title: Teaching
permalink: /teaching/
---
```
3. Add the page to navigation in `_config.yml` under `header_pages`

### Updating Software Examples

Edit `software.md` to add or update information about your software projects. Include:
- Repository links
- Installation instructions
- Usage examples
- Documentation links

### Adding Publications

Update `publications.md` with your latest papers, presentations, and preprints. Organize by year or category.

## Project Structure

```
.
├── _config.yml           # Jekyll configuration
├── _includes/            # Reusable components (header, footer)
├── _layouts/             # Page layouts
├── assets/
│   └── css/
│       └── style.scss    # Custom styles
├── index.md              # Home page
├── research.md           # Research page
├── software.md           # Software projects
├── publications.md       # Publications list
├── cv.md                 # Curriculum Vitae
├── Gemfile               # Ruby dependencies
└── README.md             # This file
```

## Tips for Academic Websites

1. **Keep it Updated**: Regularly update publications and research highlights
2. **Professional Tone**: Maintain a professional but approachable writing style
3. **Code Examples**: Include code snippets for software documentation
4. **Contact Info**: Make it easy for collaborators to reach you
5. **Mobile-Friendly**: The site is responsive and works on all devices

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## License

Content: © 2024 Daniel Palmer. All rights reserved.

Code (HTML/CSS/Jekyll structure): MIT License

## Contact

For questions or suggestions about this website template, please open an issue on GitHub.

