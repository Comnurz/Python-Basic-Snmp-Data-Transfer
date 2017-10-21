This development by Python3.

If you need another information for your Ubuntu os please look "oidlist.md" .


Please install "pysnmp" python library before use.
pysnmp to download write this command in your terminal: pip3 install pysnmp


If you cant get system information with use snmp, try your snmpd.conf file add following command:
view systemonly included .1.3.6.1.4.1.2021.9.1.8.1     //stated oid to let
rocommunity public default -V systemonly               //stated oids is public
