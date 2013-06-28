##Ref
https://devcenter.heroku.com/articles/python
<br>
https://devcenter.heroku.com/articles/custom-domains
<br>
http://flask.pocoo.org/docs/tutorial/

##Sync with github
.git/config
```
[remote "all"]
        url = git@heroku.com:intense-plains-3420.git
        url = git@github.com:DTVD/heroku.git
[remote "github"]
        url = git@github.com:DTVD/heroku.git
```

##Domain

### heroku
```
heroku domains:clear
heroku domains:add www.vunhatminh.com
host www.vunhatminh.com
```

### onamae.com
https://www.onamae.com/navi/domain.html
```
*.vunhatminh.com
CNAME
intense-plains-3420.herokuapp.com
```


www.vunhatminh.com/users/login
