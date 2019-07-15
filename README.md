# Py Block Ip
This tools has propose blocks ip suspects, for this is necessary create list request suspect, for example wp-admin, or wp-content/plugins/portable-phpmyadmin/
this path is used for robots and cracker for attack website in wordpress our other cms.  
if you not 


## How use

Install this libary with comand


    pip install -r requirements
    
    
This library run is necessary run with root because Ip Tables, and you restart you server all rules  will be revoked
.
Its use is simple, you need pass this parameters ip, path, file_rules, file_ip_accept, if not pass file_rules this library
get file content paths deny, and if not pass file_ip_accept all ips was be blocked 


## Example applications
For show use this lib has one example api in tornado with run in containeir docker you use is easy
is neccessary import lib.

    from py_block_ip import protect_attack
And in class or function handle for responder you call function 

    protect_attack(ip=self.request.remote_ip, path=self.request.uri, file_rules='app/example_rules.txt')
Being parameter ip is ip access resouce, path is por example wp-admin/index.php for example, file_rules
is file in format txt content list path suspect for example  wp-admin/index.php or phpmyadmin/index.php?, this
path is used for boots for map possible vulnerabilities. Has also parameter subnet if you whether block one range ip specific.
If you not blocked determined ips you was pass 

For you run app example with docker you need build image with comando

    docker build -t pyblock:1.0 . 

And for run 

    docker run -p 3000:3000 --cap-add=NET_ADMIN pyblock:1.0

Is necessary parameter --cap-add=NET_ADMIN for run with root and is possible create rules in
iptables.

Access http://127.0.0.1:3000/ if success you as message success. If you try accesse one path not 
permitted  you  ip is blocked and return message ip blocked. 
Obs: By default the rules is deleted when linux restart this is characteristic Iptables.    