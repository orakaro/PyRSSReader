## Setup heroku
```
wget http://ftp.ruby-lang.org/pub/ruby/1.8/ruby-1.8.7-p302.tar.gz
tar -zxvf ruby-1.8.7-p302.tar.gz
cd ruby-1.8.7-p302
./configure --with-openssl-dir=/usr/lib/openssl
make
make install

wget http://production.cf.rubygems.org/rubygems/rubygems-1.3.7.tgz
tar -zxvf rubygems-1.3.7.tgz
cd rubygems-1.3.7
ruby setup.rb config
ruby setup.rb setup
ruby setup.rb install

ruby -v
gem -v

```

##Sync with github and heroku
.git/config
```
[remote "all"]
        url = git@heroku.com:murmuring-depths-7423.git
        url = git@github.com:DTVD/PyRSSReader.git
[remote "github"]
        url = git@github.com:DTVD/PyRSSReader.git
 
```

