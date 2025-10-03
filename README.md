# Introduction:
### Project Milestone 3: for Code Institute Full-Stack Development Program: Django Framework
This project demonstrates the implementation of the Django framework with Python on the back end to deliver an intuitive, interactive blog-sharing platform. The application adopts a Reddit-style structure, enabling users to register, authenticate, and manage their accounts seamlessly. Within the platform, users can create, edit, and delete blog posts, as well as engage with others by posting comments and liking & disliking content.

Comprehensive CRUD (Create, Read, Update, Delete) functionality has been implemented for user accounts, blog posts, and comments, ensuring that users retain full control over their contributions and may update or remove their content at any time. An integrated admin panel provides moderation capabilities and allows users to submit support requests or feature suggestions directly through the platform.



## Table of Contents
1. [Introduction](#introduction)  
2. [Strategy Plane](#strategy-plane)  
   - [Project Goals](#project-goals)  
   - [Target Audience](#target-audience)  
   - [Key Features](#key-features)  
3. [Scope Plane](#scope-plane)  
   - [Feature Planning](#feature-planning)  
4. [Structure Plane](#structure-plane)  
   - [User Stories](#user-stories)  
5. [Database Schema](#database-schema)  
6. [Skeleton Plane (Wireframes)](#skeleton-plane-wireframes)  
   - [Wireframes](#wireframes)  
7. [Surface Plane (UI Design)](#surface-plane-ui-design)  
   - [Colour Scheme](#colour-scheme)  
   - [Typography](#typography)  
   - [Imagery](#imagery)  
8. [Features](#features)  
   - [Blog Feed](#blog-feed)  
   - [Personalised User Dashboard](#personalised-user-dashboard)  
   - [Post Creation & Management](#post-creation--management)  
   - [Commenting & Likes](#commenting--likes)  
   - [Search and Filtering](#search-and-filtering)  
   - [Error Pages](#error-pages)  
   - [Footer](#footer)  
9. [Website Pages](#website-pages)  
   - [Home Page (Feed)](#home-page-feed)  
   - [Create Post Page](#create-post-page)  
   - [Login & Logout Pages](#login--logout-pages)  
   - [Register Page](#register-page)  
   - [Profile Page](#profile-page)  
   - [Error Pages](#error-pages-1)  
10. [Development Process](#development-process)  
    - [Iterative Development](#iterative-development)  
11. [Future Implementations](#future-implementations)  
12. [Accessibility](#accessibility)  
13. [Deployment & Local Development](#deployment--local-development)  
    - [Deployment](#deployment)  
    - [Preparation for Deployment in VS Code](#preparation-for-deployment-in-vs-code-with-postgresql-on-aws)  
    - [Generating a Secure SECRET_KEY & Configuring DEBUG Settings](#generating-a-secure-secret_key--configuring-debug-settings)  
    - [Local Development](#local-development)  
      - [How to Fork](#how-to-fork)  
      - [How to Clone](#how-to-clone)  
14. [Technologies Used](#technologies-used)  
    - [Languages](#languages)  
    - [Frameworks, Libraries & Tools](#frameworks-libraries--tools)  
    - [Design & Visuals](#design--visuals)  
    - [Development & Deployment](#development--deployment)  
15. [Testing & Accessibility Tools](#testing--accessibility-tools)  
16. [Credits & Inspiration](#credits--inspiration)  
    - [Content](#content)  
    - [Media](#media)  
    - [Acknowledgments](#acknowledgments)

## Strategy Plane
### Project Goals
Threadly is a community-driven gaming blog platform designed for gamers, content creators, and enthusiasts. It enables users to sign up, log in, and share posts on a wide range of gaming topics, from reviews and tips to news and discussions. Users can create, edit, and delete their posts, interact with others through comments and likes, and browse content organised by date posted.

The platform replaces the limitations of static gaming blogs with a dynamic, mobile-responsive, and user-friendly interface. Whether at home, at an event, or on the go, users can easily read, contribute to, and engage with the latest gaming content.

As the gaming industry continues to expand, tools like Threadly empower players and creators to connect, share insights, and build communities in a modern, cloud-based environment. Developed as part of a Level 5 Web Application Development course, the project focuses on usability, clean design, and practical functionality to deliver a polished gaming blog experience.

### Target Audience
Threadly is designed for:
  - 🎮 **Gamers** – Share reviews, tips, and gaming news with a like-minded community  
  - 📝 **Content creators** – Post and manage your own gaming-related articles and updates  
  - 📱 **Mobile users** – Access and contribute to the platform on the go  
  - 🤝 **Community members** – Comment, like, and engage with posts from other users  

### Key Features
  - 📝 **User-generated content** – Create, edit, and manage your own gaming posts  
  - 💬 **Community interaction** – Comment on and like posts to engage with others  
  - 🛠️ **Full CRUD functionality** – Add, view, update, or remove your content at any time  
  - 🔐 **Secure authentication** – Personalised accounts with registration, login, and logout  
  - 📱 **Responsive UI** – Optimised for smartphones, tablets, and desktops  



## Scope Plane
### Feature Planning
The Threadly project has been carefully planned to prioritise core functionality for the minimum viable product (MVP) while identifying additional features for future development. Features are categorised as **must-haves**, **should-haves**, and **could-haves** based on their importance and viability.

The MVP focuses on essential functionality for all users, including viewing the public landing page, registering for an account, logging in and out, managing sessions, creating, editing, and deleting posts, commenting on and liking posts, and accessing a responsive, mobile-first interface. Admin users also have access to the Django admin panel for moderation and content management.

Should-have features include filtering and sorting posts by category or date, searching posts by title, author, or keywords, and updating personal account profiles. Could-have features for future iterations include social media login/signup, bookmarking favourite posts, viewing analytics dashboards, and enhanced customisation options.

By defining the scope in this way, Threadly ensures a clear focus on delivering a seamless user experience while allowing room for expansion and additional functionality in later versions.



## Structure Plane
### User Stories
The Threadly platform has been designed around clear user stories to guide the structure and functionality of the app. These stories ensure the site meets the needs of different user types, including guests, registered users, admins, and mobile users.

**Guest users** can browse public posts and featured content to understand what the platform offers before registering. They see clear prompts to sign up or log in, making it easy to get started.  

**Registered users** can create an account, log in, and access their dashboard. They can add, edit, and delete posts, upload images to enhance their content, and engage with other users through comments and likes. Additional features include searching, filtering, and sorting posts to quickly find content, rating posts to track favourites, and managing their account details, such as updating their display name or profile information. 

**Admins** have access to a dedicated Django admin panel to manage users and content efficiently. They can edit or delete any posts, review user-submitted content to ensure the platform remains appropriate, and manage posts directly from the admin interface.  

**Mobile users** can access Threadly on smartphones and tablets, allowing them to read, create, and update posts while on the go. Image uploads and post creation are optimised for mobile, enabling a seamless experience across devices.  

Finally, all users are provided with friendly, informative error pages (e.g., 404 or 500) and see their most recent posts first in their dashboard, ensuring clarity, accessibility, and a smooth user experience.



## Database Schema
Threadly uses a relational database (PostgreSQL) to provide structured and reliable storage, with support for referential integrity, ideal for managing user accounts, posts, comments, and likes.

The MVP initially focused on a **Post** model linked to Django’s built-in **User** model. Each post stores core information such as title, content, category, creation date, and an optional image. This setup enabled rapid prototyping, full CRUD functionality, and integration with the Django admin panel.

During development, it became clear that additional granularity was needed to support user interactions such as comments and likes. To address this, dedicated **Comment** and **Like** models were introduced. Each comment is linked to a post and its author, while likes are linked to both the user and the post, establishing clear one-to-many relationships. This structure improves data accuracy, scalability, and the ability to extend functionality in the future, such as filtering posts, sorting by popularity, or displaying user interactions at the post level.

The schema follows relational database best practices, reducing redundancy, maintaining clarity, and supporting future enhancements to Threadly’s interactive features.



## Skeleton Plane
### Wireframes
The initial wireframes for Threadly were created using **Adobe Illustrator** to plan the layout, structure, and user flow of the gaming blog platform. Wireframes were designed for **mobile, tablet, and desktop** screens to ensure a fully responsive and accessible experience across all devices.

These wireframes established the information hierarchy and guided the user journey, covering key views such as the homepage, dashboard, post creation and management pages, and error pages. They provided a visual blueprint throughout development, helping to determine the placement of navigation, search, filter, and CRUD elements with a **mobile-first approach**.


    - inset image here 
    - insert image here
    



## Surface Plane
### Colour Scheme
The Threadly colour palette draws inspiration from vibrant gaming aesthetics, combining **blue and pink tones** to create a modern, energetic, and immersive feel. The scheme balances clarity and readability with playful accents, reflecting the dynamic world of gaming and community interaction.

The main colours for the site are:
  - **(Gaming Blue)** – Used for headings, buttons, and hyperlinks. This bright blue adds a bold, confident tone while maintaining clarity and consistency across the interface.  
  - **(Pixel Pink)** – Applied to call-to-actions, badges, and hover states, this vibrant pink introduces energy and highlights key interactive elements.  
  - **(Smoke White)** – Utilised for the footer, navigation, and text on light backgrounds. It provides contrast, grounding the interface and ensuring readability.  
  - **(Background Grey)** – A soft, neutral background colour that keeps the focus on content and enhances the visibility of the primary accents.  
  - **(Foreground White)** – Used for text, icons, and forms on coloured or dark backgrounds, ensuring clean, crisp readability across all devices.  

These colours are defined as **CSS variables** for consistent application throughout the platform, resulting in a cohesive and visually engaging aesthetic that complements Threadly’s focus on gaming and community engagement.





### Typography
Threadly uses **Google Fonts** to ensure high-quality, accessible typography across all devices and browsers. Fonts are imported using CSS `@import`, with appropriate fallbacks for maximum compatibility.

  - **Headings (h1, h2, h3):** The font **Poppins** was selected for all headings due to its geometric, modern style. Its clean lines and contemporary design make headlines stand out, giving the site a polished, distinctive visual identity while remaining highly legible.  
  - **Paragraphs and body text:** **Poppins** is also used for body copy, maintaining consistency while providing excellent readability at various sizes. Its friendly, modern tone complements the gaming-inspired colour palette, creating a cohesive and user-friendly reading experience throughout the site.  
  - **Icons and UI elements:** The **Font Awesome** library supports the interface with scalable, recognisable icons. These icons are stylistically aligned with Poppins, enhancing usability by providing clear visual cues for actions, navigation, and social interactions.  

Together, this typographic approach balances style and readability, contributing to Threadly’s modern, vibrant, and accessible gaming blog design.



### Imagery
All images used in Threadly were sourced from a variety of online platforms and are **not intended for commercial use**. The visuals were selected to reflect gaming culture and to enhance the immersive experience of the blog.  

Example images used for posts, banners, and thumbnails are intended to demonstrate how the platform displays content and populate the interface in a realistic way. These images provide context for the layout and functionality, helping users visualise their own posts and interactions within the platform.  

Overall, the imagery is clean, bold, and culturally relevant to gaming, reinforcing Threadly’s purpose as a community-driven, interactive blog for gamers.



## Features
Threadly is a full-stack web application designed to provide gamers and content creators with a dynamic, community-driven blog platform. The site delivers an engaging and intuitive experience with the following key features:

  - **Blog Feed** – A continuously updated feed where users can browse posts from the community. 
  - **Personalised User Dashboard** – Each registered user has a personalised view of their posts.
  - **Post Creation & Management** – Users can create, edit, and delete their posts with rich content.
  - **Commenting & Likes** – Engage with the community by commenting on posts and liking content to encourage interaction.  
  - **Custom 404 & 500 Error Pages** – Friendly, branded error pages guide users when something goes wrong.  

### Additional Features
  - **Responsive Design** – All pages are fully responsive, working seamlessly across mobile, tablet, and desktop devices.  
  - **Favicon** – A custom favicon is displayed in the browser tab for brand identity.  
  - **Defensive Programming** – Permission checks ensure only authorised users can perform sensitive actions. Admin-level tasks, such as editing or deleting system-wide content, are restricted to superusers. Unauthorized access attempts redirect users to the login page, improving security and user experience.  

### Footer
The footer appears consistently across all pages to support navigation, brand presence, and accessibility. It includes:
  - **Social Links** – Accessible icons linking to the site’s social media profiles.  
  - **Quick Links** – Direct access to key pages such as Home and Register (dynamically showing Dashboard when logged in).
  
The layout is fully responsive, ensuring usability and accessibility across all devices.





## Website Pages
### Home Page (Feed)
The Home Page serves as the main feed, displaying posts from all users in a dynamic, interactive stream.

**What it does:**
  - Shows posts from the community, including text and tags.
  - Allows users to comment on and like posts.
  - Highlights trending or recent posts for easy discovery.

**User Benefits:**
  - Keeps users engaged with fresh content.
  - Encourages interaction and community participation.
  - Provides a clear overview of recent activity and popular posts.

**Interactive Elements:**
  - Commenting system for user engagement.
  - Like buttons for posts.
  - Responsive layout for mobile, tablet, and desktop users.

---

### Create Post Page
The Create Post page allows users to publish new content to the platform.

**What it does:**
  - Provides a form for adding a title, body text, and tags.
  - Supports inline validation to ensure required fields are completed correctly.

**User Benefits:**
  - Enables users to contribute to the community easily.
  - Allows content creation without unnecessary page reloads.
  - Ensures posts are complete and properly formatted.

**Interactive Elements:**
  - Dynamic form fields for text and images.
  - Real-time validation feedback.
  - Submit button to publish the post directly to the feed.

---

### Login & Logout Pages
These pages handle user authentication and session management.

**What it does:**
  - Login page allows registered users to access their account.
  - Logout option securely ends the session.

**User Benefits:**
  - Provides secure access to personalised dashboards.
  - Protects user accounts and content.
  - Simplifies returning to the platform safely.

---

### Register Page
The Register page allows new users to create an account.

**What it does:**
  - Collects basic information like username, email, password, and optional profile image.
  - Includes form validation to prevent incomplete or invalid submissions.

**User Benefits:**
  - Enables new users to join the Threadly community.
  - Ensures accurate account creation and security.
  - Prepares users for personalised interaction with the platform.


---

### Profile Page
The Profile page is a personalised space where users can manage their account and content.

**What it does:**
  - Displays the user’s information and profile image.
  - Allows updates to username, email, password, and profile image.
  - Shows the user’s posts with options to edit or delete them.

**User Benefits:**
  - Gives users control over their personal data and content.
  - Encourages engagement and ownership of posts.
  - Provides a clear, user-friendly interface for account management.

**Interactive Elements:**
  - Editable profile form fields.
  - Upload button for profile images.
  - Links to edit or delete posts created by the user.


### Error Pages
Threadly includes custom error pages to provide a friendly, branded experience whenever something goes wrong. The 400 page handles malformed or invalid requests, the 403 page addresses attempts to access restricted content, the 404 page manages broken or incorrect links, and the 500 page responds to unexpected server errors. Each page features gaming-themed illustrations and clear calls-to-action, guiding users back to the homepage while maintaining visual consistency and brand identity. These pages reduce confusion, preserve trust, and ensure a polished user experience even in error scenarios.



## Development Process
Threadly was developed using an iterative, feature-driven approach:

  - Planned the site structure, wireframes (created in Adobe), and database schema.
  - Set up the Django project with a connected PostgreSQL database.
  - Implemented user authentication with Django Allauth.
  - Developed core CRUD functionality for posts, comments, and user profiles.
  - Built dynamic filtering, search, and personalised blog feed features.
  - Focused on accessibility, responsive design, and a clean UI.
  - Completed manual and automated testing, final documentation, and deployed to Heroku.
  - Version control was managed using Git and GitHub, with regular, descriptive commits to track progress and maintain a clear development history.


## Future Implementations
To expand Threadly’s functionality and improve the user experience, the following features are being considered for future development:

  - **Dark & Light Mode (Manual & Auto Toggle)** – Allow users to switch between light and dark themes, with an option to respect device system preferences.
  - **Advanced Post Filtering & Tagging** – Introduce filtering by game genre, tags, popularity, or post date to improve discoverability.
  - **Social Media Sign-In Options** – Offer Google, Facebook, or Apple login for quicker onboarding.
  - **Public Profile Sharing** – Let users create shareable public profiles to showcase their posts and interactions.
  - **Post Bookmarking & Favorites** – Enable users to save or highlight posts for easy reference later.
  - **Media Previews** – Embed images, GIFs, or video clips in posts for richer content presentation.
  - **Community Comments & Reactions** – Add enhanced commenting, reactions, or mini-discussions to posts.
  - **Notifications & Alerts** – Implement opt-in notifications for replies, new posts, or trending content.
  - **Bulk Post Management** – Allow users to manage multiple posts at once, including editing or deleting content.
  - **Profile Customisation** – Offer additional options for avatars, banners, or bio enhancements.
  - **Content Export & Backup** – Enable exporting posts or user data for personal backup or offline reference.
  - **Gamification & Leaderboards** – Reward active contributors with badges, points, or leaderboards to boost engagement.
These enhancements aim to make Threadly a more interactive, engaging, and personalised platform for the gaming community.



## Accessibility
Accessibility has been a central focus throughout the development of Threadly. Measures implemented to ensure the platform is inclusive and user-friendly include:
  - Using semantic HTML5 elements to improve structure and navigation for assistive technologies.
  - Providing descriptive alt text for all meaningful images, including user avatars, post images, and banners.
  - Applying ARIA labels to interactive elements such as icon-only buttons, links, and form controls for screen reader clarity.
  - Maintaining strong colour contrast across the UI, particularly in key areas like buttons, links, and navigation (see Colour Scheme).
  - Ensuring visible focus states and full keyboard navigability for all interactive components.
Accessibility was evaluated using Lighthouse, WAVE, and manual testing in Chrome DevTools, ensuring Threadly is usable and accessible for a wide range of users.


### Deployment & Local Development  
Deployment  The Vinyl Crate project is deployed using Heroku, with Amazon RDS PostgreSQL for the live database and Cloudinary for media file storage. Create the Live Database While sqlite3 was used for local development, this is not suitable for production. Instead, a free-tier PostgreSQL database from Amazon AWS was used for deployment.
  1. Sign in to your Amazon RDS Console and click Create Database.
  2. Select Standard Create, choose PostgreSQL, and select the Free tier template.
  3. Set a unique DB instance identifier, master username, and password.
  4. In the connectivity section, enable public access and ensure security group rules allow inbound connections from your IP.
  5. Launch the database and wait for the instance to become available.
  6. Once ready, copy the Endpoint and construct your DATABASE_URL in the following format: postgres://username:password@hostname:5432/dbname
