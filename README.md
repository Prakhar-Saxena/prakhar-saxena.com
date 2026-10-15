# prakhar-saxena.com

Personal website of Prakhar Saxena. It is a single static page (`index.html`) with no build step.

## Hosting

- **Host:** GitHub Pages, served from the `master` branch root of this repo.
- **Custom domain:** the `CNAME` file holds `prakhar-saxena.com`, so GitHub serves the site on that domain. Don't delete it.
- **HTTPS:** GitHub Pages provisions the certificate. Turn on "Enforce HTTPS" under *Settings → Pages* so plain `http://` visits redirect to `https://`.
- **Deploying:** push to `master`. GitHub Pages republishes in about a minute.

## DNS (GoDaddy)

The domain is registered with GoDaddy. Its DNS records point the apex domain and `www` at GitHub Pages,
following GitHub's guide to [managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
`www.prakhar-saxena.com` redirects to `prakhar-saxena.com`.

## Link previews

The `og:*` and `twitter:*` meta tags in `index.html` control the title, description, and image shown when the link is shared.
The preview image is `Prakhar Saxena - Profile Photograph - Square Cropped.jpg`, a square crop of the profile photograph centred on the face. After changing it, refresh cached previews with
[LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) or the
[Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/).

## Files

- `index.html`: the whole site
- `Prakhar Saxena - Profile Photograph.jpg`: avatar on the page
- `Prakhar Saxena - Profile Photograph - Square Cropped.jpg`: square link-preview image
- `Prakhar Saxena - Resume.pdf`: resume linked from the page
