# Logs Analysis
A program that performs multiple queries on a web service log using python and postgresql.

### Usage 
1) Clone the repository. 
2) Install VirtualBox
3) Install Vagrant
4) Download SQL news file and move it into the vagrant directory: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5) Move the newsdb.py file into the vagrant directory
>Use the terminal to CD into vagrant, then use the follwing commands to connect to the database: 
- `vagrant up`
- `vagrant ssh`
- `cd /vagrant`
- `psql -d news -f newsdata.sql`
- `psql news`
> In order for the queries to work, you will need to set up these views in the news database by copying these commands into the news shell:
>
` CREATE view topthree as SELECT substring(path from 10 for char_length(path)),  
COUNT(*) as views FROM log GROUP by path ORDER by views desc limit 3 offset 1;`

` CREATE view topeight as SELECT substring(path from 10 for char_length(path)),  
COUNT(*) as views FROM log GROUP by path ORDER by views desc limit 8 offset 1;`

`CREATE view errors as SELECT date(time), COUNT(*) as errors from log WHERE status = '404 NOT FOUND' GROUP by date ORDER by date;`

`CREATE view accessed as SELECT date(time), count(*) as views FROM log GROUP by date order by date;`

`CREATE view a_e as SELECT accessed.date, errors, accessed from errors, accessed where accessed.date = errors.date;`
6) Exit out of vagrant by pressing ctrl+d, then cd into news
7) Run `python newsdb.py`

### Liscense 
The MIT License

Copyright (c) 2010-2017 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.













  