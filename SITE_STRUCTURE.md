# Website Structure Documentation

## Complete File Tree

```
dpalmer-anl.github.io/
│
├── _config.yml                 # Jekyll site configuration
├── Gemfile                     # Ruby dependencies
├── .gitignore                  # Git ignore rules
│
├── README.md                   # Project documentation
├── QUICKSTART.md               # Quick start guide
├── SITE_STRUCTURE.md           # This file
├── serve.sh                    # Local server script
│
├── _layouts/                   # Page layouts
│   ├── default.html            # Base layout with header/footer
│   ├── home.html               # Home page layout
│   └── page.html               # Standard page layout
│
├── _includes/                  # Reusable components
│   ├── header.html             # Site header with navigation
│   └── footer.html             # Site footer with links
│
├── assets/                     # Static assets
│   ├── css/
│   │   └── style.scss          # Custom CSS styles
│   └── images/                 # Images directory (add photos here)
│
└── Content Pages:
    ├── index.md                # Home page
    ├── research.md             # Research projects page
    ├── software.md             # Software documentation page
    ├── publications.md         # Publications list page
    ├── cv.md                   # Curriculum Vitae page
    └── 404.md                  # Error page
```

## Page Descriptions

### Core Configuration

**_config.yml**
- Site title, description, and URL
- Author information
- Social media links
- Navigation menu configuration
- Jekyll plugins and settings

**Gemfile**
- Ruby gem dependencies
- GitHub Pages gem for easy deployment
- Jekyll plugins (SEO, feed, sitemap)

### Layouts

**default.html**
- Base template for all pages
- Includes HTML structure, head section, header, and footer
- SEO tags and meta information

**home.html**
- Extends default layout
- Used for the main landing page

**page.html**
- Extends default layout
- Used for standard content pages
- Includes page title header

### Includes

**header.html**
- Site logo/title
- Navigation menu
- Mobile-responsive hamburger menu

**footer.html**
- Contact information
- Social media links
- Copyright notice
- Three-column layout

### Content Pages

**index.md** (Home Page)
- Professional introduction
- Research interests overview
- Recent highlights
- Contact information
- Uses `home` layout

**research.md**
- Detailed research project descriptions
- Total Energy Tight Binding for Graphene section
- Bilayer Graphene Model Development section
- Machine Learning applications
- Future research directions
- Uses `page` layout

**software.md**
- TETB_GRAPHENE package documentation
  - Features, installation, examples
  - GitHub links and citations
- BLG_model_builder package documentation
  - Parameter optimization details
  - Usage examples
  - Advanced features
- Related tools and utilities
- Uses `page` layout

**publications.md**
- Journal articles by year
- Conference presentations
- Posters
- Thesis information
- Software publications
- Citation metrics links
- Uses `page` layout

**cv.md**
- Education history
- Research experience
- Technical skills
- Publications (summary)
- Presentations
- Awards and honors
- Teaching experience
- Professional service
- Uses `page` layout

**404.md**
- Custom error page
- Helpful navigation links

### Styling

**assets/css/style.scss**
- Custom color scheme (blue/navy professional theme)
- Typography settings
- Responsive design (mobile-friendly)
- Component styles:
  - Header and navigation
  - Research project cards
  - Software documentation cards
  - Code blocks
  - Footer
  - CV-specific styles
- Print-friendly styles
- Mobile breakpoints

### Utility Files

**serve.sh**
- Bash script to run local development server
- Checks for Ruby and Bundler
- Installs dependencies
- Starts Jekyll with live reload

**.gitignore**
- Excludes build files
- Ignores system files
- Hides sensitive information

## Color Scheme

The site uses a professional academic color scheme:

- **Primary**: `#0066cc` (Blue) - Links, accents
- **Secondary**: `#2c3e50` (Dark gray-blue) - Headers, footer
- **Accent**: `#3498db` (Light blue) - Hover effects
- **Text**: `#333` (Dark gray)
- **Background**: White and light grays

## Key Features

### Responsive Design
- Mobile-first approach
- Hamburger menu for small screens
- Flexible grid layouts
- Touch-friendly buttons and links

### SEO Optimized
- Jekyll SEO plugin
- Proper meta tags
- Sitemap generation
- RSS feed

### Professional Academic Style
- Clean, modern design
- Easy-to-read typography
- Clear information hierarchy
- Research-focused content structure

### Developer-Friendly
- Well-commented code
- Modular architecture
- Easy to customize
- Clear documentation

## Customization Points

### Quick Customizations

1. **Colors**: Edit `assets/css/style.scss` variables
2. **Navigation**: Update `_config.yml` `header_pages`
3. **Social Links**: Edit `_config.yml` social media fields
4. **Content**: Edit individual `.md` files
5. **Footer**: Modify `_includes/footer.html`

### Adding Features

1. **Blog**: Create `_posts/` directory and add blog layout
2. **Projects Collection**: Configure in `_config.yml`
3. **Photo Gallery**: Add to `assets/images/` and create page
4. **Custom Domain**: Add `CNAME` file with your domain

## Development Workflow

1. **Edit Content**: Modify `.md` files
2. **Test Locally**: Run `./serve.sh` or `bundle exec jekyll serve`
3. **Preview**: Open http://localhost:4000
4. **Commit**: `git add . && git commit -m "Update"`
5. **Deploy**: `git push origin main`
6. **Live**: Changes appear at https://dpalmer-anl.github.io

## Browser Compatibility

Tested and compatible with:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Minimal JavaScript (only for mobile menu)
- Optimized CSS
- Fast static site generation
- GitHub Pages CDN delivery

## Accessibility

- Semantic HTML5
- ARIA labels where needed
- Keyboard navigation support
- High contrast text
- Screen reader friendly

## Future Enhancements

Consider adding:
- Blog functionality
- Project portfolio page
- Teaching materials section
- Interactive visualizations
- Contact form
- Search functionality
- Multi-language support

## Support and Resources

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)
- [Liquid Templating](https://shopify.github.io/liquid/)

---

*Last Updated: November 2024*

