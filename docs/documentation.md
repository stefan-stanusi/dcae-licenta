# DCAE Website


## 0. Assumption

In this document, we'll assume that the website lives in /var/www/dcae
If the website's files are in other location, please remember to modify the paths referenced here accordingly.

The set of files in /var/www/dcae will be called "the project". It is an internal name used by Django. When creating a website with Django, you'll begin with the command
```
django-admin startproject foo
```

The website's modules will be called "apps" ("app" for singular) or "applications" ("application" for singular). This is also an internal name used by Django, e.g.
```
django-admin startapp bar
```
or
```
./manage.py startapp bar
```

We'll assume that the database is called dcae and its user is the dcae role.


## 1. The Project's Structure

* Project's root (/var/www/dcae)
	* /app - Python code, website's modules
		- /about - The About page
		- /announcements - The news articles
		- /appconf - Third-party app, required for the thumbnail processing
		- /courses - Department's courses
		- /datatrans - Translations
		- /export - Third-partyy app for exporting data from the admin interface
		- /fts - Third-party (slightly modified) app for full-text search
		- /homepage - The homepage
		- /imagekilt - Third-party app (slightly modified) for thumbnail processing (its original name was **imagekit** ; it was renamed to prevent possible name clashes).
		- /labs - Department's labs
		- /master - Department's master programmes
		- /members - Member profiles and translation forms available in the public facing part of the website
		- /menu - The website's menu
		- /object_tools - Third-party app providing support for manipulations of the inbuilt admin pages
		- /pagination - Third-party app (slightly modified) for paginating the news archive pages
		- /partners - Department's partners for the master programmes
		- /projects - Department's research projects
		- /publications - Publications by the Department's members
		- /reversion - Third-party app keeping track of objects' modifications and allowing data recovery or rollbacks to previous versions of the information
		- /rooms - Department's rooms (associated with courses, labs or members)
		- /search - Website's search
		- /singletons - Utility for data models allowing only a unique object (the menu, the homepage info, the about page info)
		- /utils - Small utilities (a menu for the admin interface, functions used for downloading external images)
	* /docs - Documentation files
	* /empty - Document root in the Apache config
	* /logs - Log files
	* /res - Static resources and templates
		- /media - Stores files uploaded by users or copied from external sources
		- /static - Static files
		- /templates - Template files

The project's structure aims to separate the executable files from the static components. The Python code lives in the /app directory. The static components (the "resources") live in the /res directory.

## 2. The Database Structure

* dcae
	* about_about - Stores the info for the About page
	* announcements_announcement - Stores the announcements (news)
	* auth_group - Stores the website's groups
	* auth_group_permissions - Maps permissions to groups
	* auth_permission - Stores permissions for project's apps
	* auth_user - Stores website's users
	* auth_user_groups - Maps users to groups
	* auth_user_user_permissions - Maps permissions to users
	* courses_course - Stores department's courses
	* courses_course_coordinators - Maps courses to members who coordinate them
	* courses_course_people - Maps courses to memebers who attend them
	* courses_course_r - Maps courses to rooms
	* datatrans_fieldwordcount - Stores wordcounts for fields to be translated
	* datatrans_keyvalue - Stores translations for fields registered for translation
	* datatrans_modelwordcount - Stores wordcounts for models registered for translation
	* django_admin_log - Stores info about who created/edited/deleted what (with timestamps)
	* django_content_type - Stores references (name, label, model) for the content types defined by various apps
	* django_flatpage - Stores data about generic pages added to the website
	* django_flatpage_sites - Maps generic pages to websites
	* django_session - Stores session data
	* django_site - Stores the sites managed by the project
	* homepage_info - Stores homepage info
	* labs_laboratory - Stores info about the department's labs
	* labs_laboratory_coordinators - Maps labs to members who coordinate them
	* labs_laboratory_people - Maps labs to members who attend them
	* labs_laboratory_r - Maps labs to rooms
	* master_programme - Stores info about the master programmes
	* master_programme_partners - Maps master programmes to partners
	* members_member - Stores info about the department's members
	* members_member_coord_bachelor - Maps members to other members (their bachelor coordinators)
	* members_member_coord_msc - Maps members to other members (their MSc coordinators)
	* members_member_coord_phd - Maps members to other members (their PhD coordinators)
	* members_member_coordinator
	* members_member_rm
	* members_role
	* menu_menu
	* menu_menuitem
	* partners_partner
	* projects_project
	* projects_project_coordinators
	* projects_project_people
	* publications_genre
	* publications_publication
	* publications_publication_authors
	* reversion_revision
	* reversion_version
	* rooms_room
	* south_migrationhistory

Note: If you see italics in the list above, just ignore them

The table names follow the pattern **application-name_model-name**
