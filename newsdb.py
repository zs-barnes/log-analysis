#!/usr/bin/env python
import psycopg2


def main():

    db = psycopg2.connect(dbname='news')
    popular_articles(db)
    popular_authors(db)
    request_errors(db)
    db.close()


def popular_articles(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT title, views
        FROM articles, topthree
        WHERE articles.slug = topthree.substring
        ORDER BY views DESC ;
        """)
    results = cursor.fetchall()
    print('\nTop three articles:')
    for result in results:
        print "  ", result[0], "-", result[1], "views"

    cursor.close()


def popular_authors(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT name, sum( views ) AS views
        FROM authors, articles, topeight
        WHERE articles.slug = topeight.substring
        AND authors.id = articles.author
        GROUP BY name
        ORDER BY views DESC ;
        """)
    results = cursor.fetchall()
    print("\nMost popular authors:")
    for result in results:
        print "  ", result[0], "-", result[1], "views"
    cursor.close()


def request_errors(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT date, round(errors/accessed::numeric, 3)* 100
        AS error_percentage
        FROM a_e
        WHERE round(errors/accessed::numeric, 3) * 100 >= 1.0;
        """)
    results = cursor.fetchall()
    print("\nDays where errors are over 1%:")
    for result in results:
        print "  ", result[0], "-", result[1], "%"
    cursor.close()

if __name__ == '__main__':
    main()
