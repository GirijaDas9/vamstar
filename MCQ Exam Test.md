## HTML

> Q1. What is the purpose of the `<track>` tag, and when should it be used?

- The `<track>` tag is used for specifying subtitles, captions, and other types of time-based text. It is typically applied as a child of the `<audio>` and `<video>` tag.

> Q2. What are the best examples of void elements?

- `<br><base><source>`

> Q3. In HTML5, which tag or tags embed a webpage inside of a webpage?

- `<iframe>`

> Q4. Where do `<header>` and `<footer>` tags typically occur?

- as children of `<body>, <article>, <aside>, <nav>, and <section>` tags

> Q5. What is the best way to apply bold styling to text?

-  `<strong>`

## CSS

> Q1. Among these selectors which selector has the highest specificity ranking for selecting the
anchor link element?

- `ul li a`

> Q2. Using an attribute selector, how would you select an `<a>` element with a "title" attribute?

- `a[title]{...}`

> Q3. What is the CSS selector for an `<a>` tag containing the title attribute?

- `a[title]`

> Q4. CSS grid and flexbox are now becoming a more popular way to create page layouts. However,
floats are still commonly used, especially when working with an older code base, or if you need to
support older browser version. What are two valid techniques used to clear floats?

- Use the "clearfix hack" on the floated element and add a float to the parent element.

> Q5. What element(s) do the following selectors match to?

- ```markdown
1. An element with an class of "nav"
2. A nav element
3. An element with a id of "nav"
```

## GIT

> Q1. How can you check your current git version?

- git --version

> Q2. What command lets you create a connection between a local and remote repository?

- git remote add origin

> Q3. Describe what these Git commands do to the commit history:

```bash
git reset --hard HEAD~5
git merge --squash HEAD@{1}
```

- The current branch's HEAD is reset back five commits, then prior commits are squashed
into a single commit

> Q4. Your current project has several branches; master, beta, and push-notifications.
You've just finished the notification feature in the push-notification branch, and you want to
commit it to beta branch. How can you accomplish this?

- Checkout the beta branch and run git merge push-notification

> Q5. Which of the following is true you when you use the following command?
`git add -A`

- All new and updated files are staged