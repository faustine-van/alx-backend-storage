# 📖 alx-backend-storage.
It contains Mysql view, stored procedure and mysql triggers, etc

### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
```
### Tasks files
- 2-fans.sql: Import table dump: [metal_bands.sql.zip](https://github.com/faustine-van/alx-backend-storage/blob/master/0x00-MySQL_Advanced/dump_sql_files/metal_bands.sql)
### Reference

- [MySQL cheatsheet](https://devhints.io/mysql?utm_campaign=ALX%20-%202023%20-%20SE%20Cohort%2013&utm_medium=email&_hsmi=81332650&_hsenc=p2ANqtz--BHD76ZQc9Rx9p3knO0x8PSKxVHSFpxWD1lXgScRTzZuTQ0qbDIPsD710X4CaIMxMl4K3MnfvEw0Chl8jZ6YNVLCMeVF0O_lXDA_DdQ5svkEnbBJM&utm_content=81332650&utm_source=hs_email)
- [MySQL Performance: How To Leverage MySQL Database Indexing.](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/?utm_campaign=ALX%20-%202023%20-%20SE%20Cohort%2013&utm_medium=email&_hsmi=81332650&_hsenc=p2ANqtz-8iHaGRBvYtRET1JHNU9BBuxvQvbj9L14xpr2kQzViaLIiTpi1flJvaDpnZSqIoGYEUwN4X2f0oQJkk_ld1ghCSY3zkPS5LFsgijz2Fg5NjsQTDeCU&utm_content=81332650&utm_source=hs_email)
- [ MySQL Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php?utm_campaign=ALX%20-%202023%20-%20SE%20Cohort%2013&utm_medium=email&_hsmi=81332650&_hsenc=p2ANqtz-9cSF7w5sFF2_wgMjlXvELtcHw8RuzM7ygMukt55nvsHCBdiBBy167WicwcR6FaryTQDNFWuL9ruBHTsQ48zrmLvg8tKvf3xG8NqKdZsgdAHgIyh7k&utm_content=81332650&utm_source=hs_email#google_vignette)
- [MySQL Views](https://www.w3resource.com/mysql/mysql-views.php?utm_campaign=ALX%20-%202023%20-%20SE%20Cohort%2013&utm_medium=email&_hsmi=81332650&_hsenc=p2ANqtz-_1XmezMoPiVNVqcHi_BVzIeARcsvvCsJdLT-sQ_URL5opIZY--DYYPj4gX5i75_UMrsFgBLoa0_QyITtiF2udEundjWksIKI7ge07SQCbVsJcJMXg&utm_content=81332650&utm_source=hs_email#google_vignette)
- [MySQL Triggers](https://www.w3resource.com/mysql/mysql-triggers.php#google_vignette)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
