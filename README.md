# Py Block Ip
This tools has propose blocks ip suspects, for this is necessary create list request suspect, for example wp-admin, or wp-content/plugins/portable-phpmyadmin/
this path is used for robots and cracker for attack website in wordpress our other cms.  

## How use

Install this libary with comand


    pip install -r requirements.txt
    
    
## Configuration 
For configure run command 

    python3 -m py_block_ip --config  --paths_deny you_file_rules.txt --ip_accept you_file_content_ip_not_blocked.txt --log filelog.log

Being required only paths_deny if you not pass ip_accept all ips try access path is blocked
and you not pass --log the  logs will be saved in /var/log/pyblock_logs.log


This library run is necessary run with root because Ip Tables, and you restart you server all rules  will be revoked by default.
Its use is simple, you need import function protect_attack and call in you code.

    from py_block_ip import protect_attack
    protect_attack(ip="< ip access you applications>",
                  path="path request before domain for example wp-admin/admin.php",
                  file_rules='file in format txt content paths suspects',
                  ip_accept="list ip access allow resource ex: ['127.0.0.1'] optional",
                  subnet="optional if you not pass subnet by default block only ip specific is blocked for firewall ex: '0/24'")

pass this parameters ip, path, file_rules, file_ip_accept, if not pass file_rules this library
get file content paths deny, and if not pass file_ip_accept all ips was be blocked 


## Example applications
For show use this lib has one example api in tornado with run in containeir docker you use is easy
is necessary import lib.
  
For you run app example with docker you need build image with comando

    docker build -t pyblock:last . 

And for run 

    docker run -p 3000:3000 --cap-add=NET_ADMIN pyblock:last

Is necessary parameter --cap-add=NET_ADMIN for run with root and is possible create rules in
iptables.

Access http://127.0.0.1:3000/ if success you as message success. If you try accesse one path not 
permitted  you  ip is blocked and return message ip blocked. 
Obs: By default the rules is deleted when linux restart this is characteristic Iptables. 

You can submit pull requests and issues for discussion. However I only consider merging tested code.
##LICENCE
The MIT License (MIT)

Copyright (c) 2019 Fabiano Teichmann <fabiano at teichmann dot net>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.   