# Prog_Team_Website
README authored by Chance Loveday. Contributions by Chance Loveday, Kylind Reagan, Jorge Estrada-Martinez, Kyle Haywood, Matt Hurst, and Jessica Mohr.

A collaborative project for Maryville College CSC marketing and use in competition preparation. Please glance through this README to understand the goals and contents of this project.

## Purpose
To provide CSC/The Programming Team with database functionality to keep track of competition practice problems and student data as well as promote the organization to the college and public. The core functionality components of the problem bank tool are as follows.
* Provide an official webpage for individuals interested in joining the Programming Team or just CSC.
* Communicate the structure of the organization as both a student club and a competitive student team.
* Highlight current members and any notable achievements. Give a transparent look into the Programming Team and the intriguing world of computer science.
* Have a feature to contact programming.team@my.maryvillecollege.edu via the website.
* Share a collection of resources for various computer science subfields.

# Table of Contents

1. [Getting Started](#getting-started)
2. [Problem Bank](#problem-bank) - A database tool to be utilized during Programming Team practice; this will be separate from the mainstream website as a private version or standalone tool
    * Problem Table
    * Category Table
    * Solved Problems
    * Student Profiler
3. [Home Page](#home)
    * Calendar
    * Competitions
    * Socials
5. [About](#about)
    * Gallery
    * Mission
    * Advisor Blurb
    * Student Blurbs
6. [Major](#major)
7. [Problems](#problems)
   * Community Practice Problems
8. [Resources](#resources)
9. [Contact Us](#contact-us)
    * Contact Form
    * Club Email Communication
10. [Acknowledgements](#acknowledgememts)

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
The custom logo, designed by a Design student, takes the user to the Home Page.

1. [__Calendar__]: A feature implemented via Google Calendar that allows viewers to view upcoming events, such as Meet Maryvilles and Programming Team practices.
2. [__Competitions__]: Three buttons are linked to the testing sites visited most often by the Programming Team. Contest details should be found on the linked pages.
3. [__Socials__]: Include an icon linked to the Programming Team Facebook page. Twitter and Instagram accounts are under construction.

## About
A page that should inform the public about CSC both as a competition team and as a student organization. Team achievements, student spotlights, and competition information are provided on this page.

1. [__Gallery__]: The top of the About page cycles through images of club trips and events. Images and captions (unused) are stored in lists and implemented in JavaScript.
2. [__Mission__]: 

Mission Statement as seen on the club constitution: The mission is to promote computer science and technical learning among computer science and non-computer science majors alike in the Maryville College community and provide meaningful experiences to individuals seeking a career relating to computer programming.

3. [__Advisor Blurb__]: A short blurb provided by Dr. Johnson about her outlook on teaching computer science.
4. [__Student Blurbs__]: An assortment of blurbs from current students about their respective experiences. Any CSC member is welcome to provide a blurb and picture to be listed on the website. Five to six student spotlights are optimal. Arrows implemented in JavaScript switch between the respective name, picture, and blurb of each student.

## Major
This is an optional section intended to clarify the path of a computer science major. Instead of linking to the paradigm, this page should explain what a computer science major has to offer. Buttons lead directly to the major's paradigm and the major's page on the Maryville College website. Q&A is also listed toward the bottom to answer some common questions students or parents may have.

## Problems
A page that provides practice problems for the general public to try. Kattis and UVA problems of varying difficulties and categories are listed.
* __Community Practice Problems__: Fifteen to twenty problems, varying from easy to hard, are included in a formatted table. The problem's name, category, judge platform, difficulty, and link are provided.

## Resources
A collection of resources for areas including, computer science, competitive programming, software engineering/development, data science, web development, cybersecurity, ethical hacking, and artificial intelligence. Websites, online software, self-learning resources, MC alumni, and custom YouTube playlists can all be found here.

## Contact Us
A form that contacts the Programming Team email with the contact's information.
* __Contact Form Implementation__: The form requires a valid name, email, phone number, and message (at least 5-10 characters) from the sender. Only members linked to the team email will receive such messages. Security measures should be implemented to prevent phishing.

## Acknowledgements
* Home: Written by Chance and Kylind
* About: Written primarily by Chance; contributions by Jorge and all individuals who provided blurbs
* Major: Written by Samir; revisions and additions by Chance
* Problems: Written by Kylind; problems provided by Kattis and UVA Judge (from Kylind, Chance, and Barbara Johnson)
* Resources: Written and organized by Kylind; minor styling by Chance
* Contact: Written and implemented by Jorge and Chance
Logo designed by MC Design Major Cierra Hudson
