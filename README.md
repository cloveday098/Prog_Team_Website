# Prog_Team_Website
README authored by Chance Loveday. Contributions by Matt Hurst, Chance Loveday, and Kylind Reagan.

A collaborative project for Maryville College CSC marketing and use in competition preparation. Please glance through this README to understand the goals and contents of this project.

## Purpose
To provide CSC/The Programming Team with database functionality to keep track of competition practice problems and student data as well as promote the organization to the college and public. The core functionality components of the problem bank tool are as follows.
* Retrieve and display student information, including name, year, profile picture, and problems solved.
* Retrieve, add, edit, and delete problems from a living problem bank.
* Add and edit problem categories.
* Capability to associate solved problems with a student and vice versa; Capability to sort solved problems by student and by problem.

# Table of Contents

1. [Getting Started](#getting-started)
2. [Problem Bank](#problem-bank) - A database tool to be utilized during Programming Team practice; this will be separate from the mainstream website as a private version or standalone tool
    * Problem Table
    * Category Table
    * Solved Problems
    * Student Profiler
3. [Home Page](#home)
    * Header
    * Calendar
    * Socials
5. [About](#about)
    * Header
    * Advisor Blurb
    * Student Blurbs
    * Team Info
    * Styling
6. [Major](#major)
    * Four-Year Breakdown
7. [Contact Us](#contact-us)
    * Contact Form
    * Club Email Communication
8. [Problems](#problems)
   * Community Practice Problems

## Getting Started
If you are completely new to git or would like a refresher, look at the provided [tutorial](https://youtu.be/8JJ101D3knE?feature=shared) and [cheat sheet](education.github.com/git-cheat-sheet-education.pdf). This project will implement HTML, JavaScript, CSS/Bootstrap, and possibly PHP. If you are not familiar with any of these, online tutorials are readily available, and _W3 Schools_ is highly recommended. Milestones and tasks are available in the attached GitHub project; tasks will be updated here regularly.

## Problem Bank
This portion should be entirely separate from the rest of the project. A page that utilizes databases to record practice problems and student info

__Requirements__: Due to the sensitive needs of the database, the problem bank and associated tables should be restricted to members of the Programming Team. As a resolution, a login feature could be implemented, or this part could be a standalone tool. This section may warrant further discussion.

1. [__Problems__]: Displays problems of a certain category. Options to add, edit, and delete a problem should be included.
2. [__Categories__]: Displays the given categories. Options to add or edit categories should be included.
3. [__Solved Problems__]: Displays student names based on students who solved each problem.
4. [__Student Profiler__][Optional]: Implements a profile for each member, including name, class rank, profile picture, and problems solved. If a login feature is implemented, students should be able to view their statistics and submit requests to receive credit for solved problems. The advisor's account should have similar capabilities but be able to log solve problems, remove students, and serve as an administrator.

## Home
1. [__Header__]: Contains either a navbar or series of buttons that lead to the remaining pages, consisting of but not limited to the _About_, _Major_, _Contact_, _Problems_, and Maryville College Home pages. A custom logo will also reside at the top of this page.
2. [__Calendar__]: A feature that allows viewers to view upcoming events, events marked distinctly from the other dates.
3. [__Socials__]: Include links to email and the Facebook page.

## About
A page that should inform the public about CSC both as a competition team and as a student organization. Team achievements, student spotlights, and competition information are provided on this page.
1. [__Header__]: Consists of an image gallery that cycles through images of the Programming Team; Include a description of the Programming Team. The revised CSC Mission Statement should be provided on the Home page.

Mission Statement as seen on the club constitution: The mission is to promote computer science and technical learning among computer science and non-computer science majors alike in the Maryville College community and provide meaningful experiences to individuals seeking a career relating to computer programming.

2. [__Advisor Blurb__]: A short blurb provided by Dr. Johnson about her outlook on teaching computer science.
3. [__Student Blurbs__]: An assortment of blurbs from current students about their respective experiences; Any CSC member is welcome to provide a blurb and picture to be listed on the website. Five to six student spotlights are optimal, but a gallery (implemented using arrow buttons) might be efficient without overcrowding the page.
4. {__Team Info__]: Highlights notable programming contests.
5. [__Styling__]: Distinctive theme that blends with the overall color scheme and theme as well as group pictures.

## Major
This is an optional section intended to clarify the path of a computer science major. Instead of linking to the paradigm, this page should clearly indicate the required courses, their availabilities, and any suggested grouping of courses. This page can be as simple or as creative as desired.
* __Four-Year Breakdown__ (According to the incoming freshman class; courses are grouped by offering period and suggestions):
     1) First-Year
        * MTH 125
        * MTH 225
        * CSC 130
        * CSC 225
     2) Sophomore or Junior
        * CSC 231 or (MTH 232 & CSC 312)
        * CSC 220
        * CSC 250 (take early)
        * CSC 299
     3) Junior or Sophomore
        * CSC 260
        * CSC 319
        * CSC 349 (if no CSC 314)
        * MTH 321
     4) Senior
        * CSC 250 (unless taken earlier)
        * CSC 312
        * CSC 314 (if no CSC 349)
        * Senior Studies
        * CSC 381

## Contact Us
A form that contacts the Programming Team email with the contact's information.
* __Contact Form Implementation__: The form should require a valid name, email, phone number, and message (at least 5-10 characters) from the sender. Only members linked to the team email will receive such messages. Security measures should be implemented to prevent phishing.

## Problems
A page that provides sets of practice problems for the general public to try. Unless a custom online judge can be implemented, just use Kattis links.
