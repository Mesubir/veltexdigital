# Google SEO Starter Guide & Ranking Standards (Veltex Digital Blueprint)

This master instruction guide is compiled directly from [Google's Official SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) and Google Search Central best practices. All blog posts, landing pages, and service pages created for **Veltex Digital** (Full-Service Digital Marketing Agency across all industries) must strictly adhere to these rules.

---

## 1. Content Depth, Multi-Industry Scope, LSI Keywords & Keyword Density Rules

* **Multi-Industry Agency Scope**:
  * Veltex Digital serves **all commercial sectors**: E-commerce / D2C, B2B Lead Generation, Real Estate, Local Businesses & Services, Professional Services, Technology/SaaS, Education, and Healthcare.
  * Articles must provide universal, multi-industry growth frameworks, actionable step-by-step checklists, ROI models, and case strategies.

* **Comprehensive Content Depth & Mandatory 10 Google FAQs**:
  * Every blog article MUST include a dedicated **10-Question FAQ Section** answering the top 10 most searched questions on Google related to that topic (derived from Google Search SERP "People Also Ask" and high-volume queries).
  * Every FAQ section MUST include matching `FAQPage` Schema.org JSON-LD markup containing all 10 questions and answers.

* **Keyword Density Control (< 2.0%)**:
  * Primary Focus Keyword density must strictly remain **under 2.0%** of total word count.
  * Prevent keyword stuffing at all costs. Primary terms must flow naturally within headings and context.

* **LSI (Latent Semantic Indexing) & Semantic Entities**:
  * Enrich content using relevant LSI keywords, contextual synonyms, and related entity terms (e.g., *customer acquisition cost, conversion rate optimization, Google Map Pack 3-pack, local SEO citation consistency, lead generation funnel, return on ad spend ROAS, organic domain authority, B2B sales pipeline, e-commerce checkout optimization*).
  * Use LSI terms naturally across H2/H3 subheadings and bullet points.

* **Helpful Content & E-E-A-T**:
  * Write primarily for **people**, providing original insight, real benchmarks, and clear actionable takeaways.
  * Clearly display author/publisher credentials (`Veltex Digital Growth Team`).

---

## 2. Page & On-Page Structure Specifications

### A. Title Tags (`<title>`)
* **Length**: Between 50 and 60 characters to avoid truncation in Google Search SERP snippets.
* **Format**: `[Primary Focus Keyword / Page Topic] | Veltex Digital`
* **Rule**: Every single page must have a unique, highly descriptive title tag.

### B. Meta Descriptions (`<meta name="description">`)
* **Length**: Between 140 and 155 characters.
* **Purpose**: Summarize the page accurately with a compelling call-to-action to increase organic Click-Through-Rate (CTR).

### C. Canonical Tags (`<link rel="canonical">`)
* Every page must specify its full self-referencing absolute canonical URL:
  ```html
  <link rel="canonical" href="https://veltexdigital.in/blog/articles/target-page.html" />
  ```

### D. Semantic HTML Hierarchy
* **`<h1>` Tag**: Exactly ONE `<h1>` per page containing the primary topic.
* **`<h2>` Tags**: Major sub-topics outlining the main logical sections.
* **`<h3>` Tags**: Supporting details, checklists, and LSI sub-topics.
* **Rule**: Never skip heading levels. Do not use heading tags purely for font size styling.

### E. Internal Linking & Anchor Text
* **Descriptive Anchor Text**: Never use generic anchor text like "click here", "read more", or "link".
* **Contextual Anchor Text**: Use specific entity keywords, e.g., `<a href="/delhi/seo-agency.html">Delhi SEO agency growth solutions</a>`.
* **Internal Network**: Every blog article must link contextually to relevant service landing pages and parent hub pages.

### F. Image SEO Optimization
* **Filenames**: Use hyphen-separated descriptive filenames (e.g., `delhi-digital-marketing-agency-growth.jpg`).
* **Alt Attributes**: Provide meaningful, descriptive `alt` text for every image.

### G. Structured Data (Schema.org JSON-LD)
* **Blog Posts**: Implement `BlogPosting` or `Article` schema with publisher, author, headline, datePublished, and mainEntity.
* **FAQ Sections**: Implement `FAQPage` schema for accordion Q&A content containing all 10 questions and answers.
* **Service Pages**: Implement `Service` and `Organization` / `LocalBusiness` schema tags.

---

## 3. Web Design & Technical Page Experience

* **Theme Consistency**: Deep Navy (`#050511`), Glassmorphism (`rgba(255, 255, 255, 0.03)`), Neon Blue (`#00f3ff`), Neon Purple (`#bc13fe`), and Outfit typography.
* **Mobile-First Layout**: Fluid layouts using Tailwind CSS. All interactive elements must be touch-friendly on mobile devices.
* **Fast Page Load**: Light DOM overhead, CDN-hosted assets, zero render-blocking heavy scripts.
