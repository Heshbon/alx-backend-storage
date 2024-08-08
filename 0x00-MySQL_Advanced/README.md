# MySQL_Advanced

This project is designed to deepen my understanding of advanced SQL concepts using MySQL. I dive into essential areas such as indexing, stored procedures, triggers, views, and more. The goal is to enhance my database management skills and optimize query performance.

# Concepts to Explore

To excel in this project, I need to be familiar with the following concepts:

	+ Advanced SQL.

	+ Database Indexing.

	+ Stored Procedures.

	+ Triggers.

	+ Views.

	+ Functions and Operators.

# Tasks 📃.

# 0. We are all unique!

  + <u>[0-uniq_users.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/0-uniq_users.sql)</u>: SQL script that creates a table users.

  + Requirements:

	+ id, integer, never null, auto increment and primary key.

	+ email, string (255 characters), never null and unique.

	+ name, string (255 characters).

# 1. In and not out

  + <u>[1-country_users.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/1-country_users.sql)</u>: SQL script that creates a table users.

  + Requirements:

	+ id, integer, never null, auto increment and primary key.

	+ email, string (255 characters), never null and unique.

	+ name, string (255 characters).

	+ country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US).

# 2. Best band ever!

  + <u>[2-fans.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/2-fans.sql)</u>: SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.

# 3. Old school band

  + <u>[3-glam_rock.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/3-glam_rock.sql)</u>: SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

# 4. Buy buy buy

  + <u>[4-store.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/4-store.sql)</u>: SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

# 5. Email validation to sent

  + <u>[5-valid_email.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/5-valid_email.sql)</u>: SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

#  6. Add bonus

  + <u>[6-bonus.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/6-bonus.sql)</u>: SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

# 7. Average score

  + <u>[7-average_score.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/7-average_score.sql)</u>: SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

# 8. Optimize simple search

  + <u>[8-index_my_names.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/8-index_my_names.sql)</u>: SQL script that creates an index idx_name_first on the table names and the first letter of name.

# 9. Optimize search and score

  + <u>[9-index_name_score.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/9-index_name_score.sql)</u>: SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

# 10. Safe divide

  + <u>[10-div.sql(https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/10-div.sql)</u>: SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

# 11. No table for a meeting

  + <u>[11-need_meeting.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/11-need_meeting.sql)</u>: SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

# 12. Average weighted score

  + <u>[100-average_weighted_score.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/100-average_weighted_score.sql)</u>: SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

# 13. Average weighted score for all!

  + <u>[101-average_weighted_score.sql](https://github.com/Heshbon/alx-backend-storage/blob/master/0x00-MySQL_Advanced/101-average_weighted_score.sql)</u>: SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
