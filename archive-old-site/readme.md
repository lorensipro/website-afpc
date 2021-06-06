# To read and play with the old joomla archive, ask for the DB then use this

# run docker for mysql
docker run -e MYSQL_ROOT_PASSWORD=1234 -v /large-4t/data/site-original-afpc/mysql:/var/lib/mysql --publish 3306:3306 --name mysqldb mysql:latest
:w

# example of mysql client
mysql -uroot -p1234 -h127.0.0.1 -P3306 afpc

# get the news in JSON
echo 'select JSON_ARRAYAGG(JSON_OBJECT("title",title, "catid", catid, "date", created, "alias", alias, "introtext", introtext)) from jos_content;' | mysql -uroot -p1234 -h127.0.0.1 -P3306 afpc --skip-column-names | sed 's/\\"/\"/g' | jq .

# get the original menus in JSON
echo 'select JSON_ARRAYAGG(JSON_OBJECT("menutype",menutype, "name", name, "alias", alias)) from jos_menu;' | mysql -uroot -p1234 -h127.0.0.1 -P3306 afpc --skip-column-names | sed 's/\\"/\"/g' | jq .

# For json, may be use sed 's/\\"/\"/g' to allow the json parser ro work correctly

# run phpmyadmin
docker run --link mysqldb:db -p 8081:80 phpmyadmin/phpmyadmin
