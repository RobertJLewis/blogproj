# Testing Documentation

This document explains how the **Gaming Blog App** was tested. It includes validation, automated and manual testing, and notes on bugs and improvements.

---

## Contents
- [Validation Testing](#validation-testing)  
  - [W3C Validator](#w3c-validator)  
  - [W3C CSS Validator](#w3c-css-validator)  
  - [JavaScript Validator](#javascript-validator)  
  - [Python Validator](#python-validator)  
- [Lighthouse](#lighthouse)  
- [Manual Testing](#manual-testing)  
  - [Full Testing](#full-testing)  
  - [Browser Compatibility](#browser-compatibility)  
  - [Responsiveness](#responsiveness)  
  - [Accessibility](#accessibility)  
  - [Testing User Stories](#testing-user-stories)  
  - [Features Testing](#features-testing)  
  - [Manual Features Testing](#manual-features-testing)  
- [Solved Issues & Bugs](#solved-issues--bugs)  
- [Known Issues & Bugs](#known-issues--bugs)  
- [Conclusion](#conclusion)  

---

## Validation Testing

### W3C Validator
The HTML for the app was checked using the [W3C Markup Validator](https://validator.w3.org/). All pages were tested to ensure proper syntax and no critical errors. Any issues found were fixed immediately to maintain clean markup.  

### W3C CSS Validator
The CSS was checked using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Stylesheets were validated to ensure there were no errors or broken rules, keeping the design consistent across browsers.

### JavaScript Validator
All JavaScript code was tested using online linters and browser developer tools. This ensured there were no syntax errors or runtime issues affecting CRUD operations, login/logout, or other interactive features.

### Python Validator
Backend Python code (if applicable, e.g., for APIs or server-side scripts) was checked using linters such as `pylint` and `flake8` to ensure clean code and catch any logical or syntax issues.

---

## Lighthouse
Google Chrome’s Lighthouse tool was used to test:

- **Performance:** Pages load quickly and actions respond promptly.  
- **Accessibility:** Verified keyboard navigation, color contrast, and ARIA labels.  
- **Best Practices:** Checked HTTPS, secure practices, and absence of JS errors.  
- **SEO:** Verified meta tags, headings, and content descriptions.

Goal: Performance score ≥ 90, Accessibility score ≥ 90, and no major best practice issues.

<img src="/testing/profilepage_lighthouse_scores.png">
<img src="/testing/feedpage_lighthouse_scores.png">
<img src="/testing/aboutpage_lighthouse_scores.png">
<img src="/testing/loginpage_lighthouse_scores.png">


---

## Manual Testing

### Full Testing
This part covers the manual testing I did to make sure the **Gaming Blog App** works properly across all main user interactions, devices, and screen sizes. I focused on things like form validation, navigation, responsiveness, and general usability. Each feature was tested step by step to catch any layout, logic, or access problems.

I also got extra feedback by having friends and family try the app on different devices and browsers to make sure the experience felt smooth and consistent everywhere.


### Browser Compatibility
I tested the app on several browsers to check for any compatibility issues:

- **Safari**  
- **Chrome**  
- **Firefox**  
- **Bing**  
- **Edge**  

Everything worked as expected on all of these, with no broken links, layout issues, or missing features.

### Responsiveness
I tested the app on a range of devices including desktop computers, tablets, and mobile phones to make sure it adapts well to different screen sizes. The layout adjusted properly on all devices, with no overlapping elements or broken formatting. Text, images, and buttons stayed readable and easy to interact with, ensuring a smooth user experience whether someone is browsing on a large monitor or a small smartphone. I also checked that interactive elements like forms and navigation menus were fully usable on touch screens and that scrolling and resizing didn’t break the design.


### Accessibility
I checked the app to make sure it is accessible to all users. This included testing keyboard navigation to ensure that all buttons, links, and forms can be used without a mouse. I also checked screen reader support to make sure content is read out correctly for visually impaired users. In addition, I tested color contrast and readability across the app to make sure text is clear and easy to see for everyone. The goal was to make the app usable and inclusive for all types of users.

### Testing User Stories
- Users can sign up, log in, and log out correctly.  
    <img src="/testing/login_button.png">
    <img src="/testing/logout_button.png">

- Users can create a post and see it in the feed.  
    <img src="/testing/creating_post.png">
    <img src="/testing/post_created.png">

- Users can edit or delete their own posts.  
    <img src="/testing/update_delete_post.png">
    <img src="/testing/updating_post.png">


### Features Testing
- CRUD functionality works without errors.  
- Error messages show for empty or invalid form submissions.  
- Navigation links and buttons perform as expected.
    <img src="/testing/error_message.png">


### Manual Features Testing
- Manually tested each form, button, and link throughout the app to ensure they work as expected. This included creating new posts, editing existing posts, and deleting posts, as well as interacting with the comment section.  
- Confirmed that updates to posts and comments are saved immediately and correctly reflected in the user interface, and that deletions remove content without leaving any broken elements or errors.  
- Tested edge cases such as submitting empty or invalid form inputs, entering overly long text, or leaving required fields blank to ensure the app handles errors gracefully and displays appropriate messages to the user.  
- Verified access control by attempting actions as different users, ensuring that only authorized users can edit or delete their own posts and comments. Unauthorized attempts were properly blocked and displayed relevant error messages.  
- Checked that all interactive elements (buttons, links, and navigation menus) respond correctly on both desktop and mobile devices, ensuring the app remains functional and user-friendly across different screen sizes and input methods.  

---

## Solved Issues & Bugs
During the development of the Gaming Blog App, several issues and bugs were encountered and resolved to improve functionality, usability, and user experience:

- **Broken navigation links:** Some links in the navigation menu were pointing to incorrect URLs or missing entirely. These were fixed so that all pages can be accessed smoothly from the menu.  
- **Login/logout session issues:** Initially, users were able to access protected pages even after logging out due to session handling problems. This was resolved by properly managing user sessions and restricting access to authenticated users only.  
- **CSS layout inconsistencies:** On mobile devices, certain elements like the post feed, buttons, and forms were misaligned or overflowing. Adjustments to CSS and media queries fixed these layout issues and made the app fully responsive.  
- **Form validation errors:** The blog creation and comment forms sometimes allowed empty submissions or invalid input, which caused server errors. Validation was added both on the frontend and backend to ensure only valid data is submitted.  
- **Profile image errors:** Pages would crash if a user didn’t have a profile image uploaded. This was fixed by adding conditional checks in the templates and using a default image when needed.  
- **CRUD operation bugs:** During testing, editing or deleting posts sometimes failed due to missing IDs or permission issues. These were corrected by checking object ownership and ensuring proper URL parameters were used.  
- **Comment handling issues:** Initially, comments did not always display immediately after submission, or the comment form would break for unauthorized users. These issues were fixed by adjusting the form handling and template rendering.  
- **Template rendering errors:** Occasionally, template logic caused errors when objects were missing certain attributes, such as when trying to access `.url` on an empty image field. Conditional statements were added to handle these cases safely.  

Overall, these fixes helped ensure the app is more stable, user-friendly, and works consistently across devices and browsers.

---

## Known Issues & Bugs
While the Gaming Blog App is fully functional and stable, there are a few minor issues that have been identified and may be addressed in future updates:

- **Performance delays on large posts:** Very long blog posts with lots of content or images can cause slight delays when loading the post page. While this does not break functionality, it may affect user experience on slower devices or connections. Optimisations such as lazy loading images and paginating content could improve performance in future updates.  
- **Older browser compatibility:** Some older browser versions, particularly Internet Explorer, do not fully support certain modern CSS features used in the app. This can result in minor layout inconsistencies, such as misaligned buttons or overlapping text. The app functions correctly in modern browsers like Chrome, Firefox, and Safari, but older browsers may not display it perfectly.  
- **Media and image handling:** Occasionally, very large image files uploaded to posts can slightly increase page load times. Implementing automatic image resizing or compression could help reduce this in the future.  
- **Edge case validation:** While most form validation works correctly, extremely unusual inputs (e.g., very long strings or special characters) may not always render perfectly or could require additional backend sanitisation.  
- **Accessibility improvements:** Although basic accessibility features are implemented, there is room for improvement with ARIA labels and keyboard navigation for certain dynamic components to make the app fully WCAG-compliant.  

These known issues do not affect the core functionality of the app but are areas that can be improved over time to provide an even smoother and more inclusive user experience.

---

## Conclusion
The Gaming Blog App has undergone extensive testing using a combination of validation tools, automated tests, and thorough manual testing to ensure it functions as intended. All core features, including CRUD operations for posts and comments, login and logout functionality, and user authentication, have been carefully checked and confirmed to work correctly.  

Manual testing helped verify that the user interface is intuitive and that navigation, forms, and interactive elements respond as expected across different devices and screen sizes. Browser compatibility tests confirmed that the app performs consistently on modern browsers like Chrome, Firefox, and Safari, while responsiveness checks ensured a smooth experience on desktops, tablets, and mobile devices. Accessibility testing demonstrated that the app supports keyboard navigation, screen readers, and appropriate color contrast, making it more inclusive for all users.  

Validation tools such as the W3C HTML/CSS validators, JavaScript linters, and Lighthouse audits confirmed that the code is clean, error-free, and adheres to best practices. Automated tests verified the reliability of core features and reduced the risk of introducing bugs during development.  

During the development and testing process, several issues were identified and resolved, including session handling, CSS layout inconsistencies, form validation errors, and profile image handling. Known minor issues, such as performance delays on very large posts and compatibility limitations with older browsers, have been documented and planned for future improvements.  

Overall, the app provides a reliable, user-friendly, and functional blogging experience. The thorough testing process ensures that users can confidently create, read, update, and delete posts, as well as interact with comments, all within a responsive and accessible environment. Future updates will continue to address remaining issues, optimise performance, and enhance the overall user experience.
