# Commands to set up the workspace 

# INSTALL PYTHON PACAKAGES & CREATE REQUIREMENTS FILE

pip3 install flask
pip3 install flask-pymongo
pip3 install dnspython
# add other installers here
pip3 freeze > requirements.txt

# HEROKU SETUP

pip3 freeze > requirements.txt


DOMAIN NAMES

+=========
+DOMAINS
+heroku domains:add quooqle.com
+Configure your app's DNS provider to point to the DNS Target solid-jackal-5jx6z025cmd60xal08yiqlxp.herokudns.com.
+  For help, see https://devcenter.heroku.com/articles/custom-domains
+
+The domain quooqle.com has been enqueued for addition
+Run heroku domains:wait 'quooqle.com' to wait for completion
+Adding quooqle.com to ⬢ quotations-space... done
+
+---------
+
+heroku domains:add www.quooqle.com
+Configure your app's DNS provider to point to the DNS Target hidden-buttercup-gile9tz9kxqx2jc4kltvd2vs.herokudns.com.
+  For help, see https://devcenter.heroku.com/articles/custom-domains
+
+The domain www.quooqle.com has been enqueued for addition
+Run heroku domains:wait 'www.quooqle.com' to wait for completion
+Adding www.quooqle.com to ⬢ quotations-space... done
+
+
+
+heroku domains
+=== quotations-space Heroku Domain
+quotations-space.herokuapp.com
+
+=== quotations-space Custom Domains
+Domain Name     DNS Record Type DNS Target                                              
+quooqle.com     ALIAS or ANAME  solid-jackal-5jx6z025cmd60xal08yiqlxp.herokudns.com     
+www.quooqle.com CNAME           hidden-buttercup-gile9tz9kxqx2jc4kltvd2vs.herokudns.com 
+
+heroku domains:add quotations.space
+Configure your app's DNS provider to point to the DNS Target horizontal-garden-jl6n2484vdrnl78v0hzq81tn.herokudns.com.
+  For help, see https://devcenter.heroku.com/articles/custom-domains
+
+The domain quotations.space has been enqueued for addition
+Run heroku domains:wait 'quotations.space' to wait for completion
+Adding quotations.space to ⬢ quotations-space... done


heroku git:remote quotations-space
heroku domains:add 'quotations-space'
