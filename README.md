# Introduction:
### Project Milestone 3: for Code Institute Full-Stack Development Program: Django Framework
This project demonstrates the implementation of the Django framework with Python on the back end to deliver an intuitive, interactive blog-sharing platform. The application adopts a Reddit-style structure, enabling users to register, authenticate, and manage their accounts seamlessly. Within the platform, users can create, edit, and delete blog posts across multiple content categories, as well as engage with others by posting comments and liking content.

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


