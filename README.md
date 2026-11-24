# Sarkari Alert PWA starter

This is a mobile-friendly installable PWA starter with Gujarati, Hindi and English headings, job search and filters, saved jobs, an Admin Panel form, and an optional JSON feed importer.

## Important limitations
- Admin entries and saved jobs live only in the current browser's local storage. They are not shared between devices and there is no secure admin login.
- Automatic updates are not connected to government websites. Configure a trusted HTTPS JSON feed that permits browser CORS access. The app does not scrape government sites.
- Push notifications, shared database, scheduled imports, and secure authentication are not included yet.
- Verify every vacancy on the official recruitment website before applying.

## Publish
Upload this folder to an HTTPS static host. Open the hosted URL in Android Chrome and choose Install app / Add to Home screen. Service workers require HTTPS or localhost.
