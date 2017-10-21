from urllib.request import Request,urlopen

from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('public'),
    cmdgen.UdpTransportTarget(('localhost', 161)),
    '1.3.6.1.4.1.2021.10.1.3.1', #CPU 1 minute load
    '1.3.6.1.2.1.1.1',           #System Description
    '1.3.6.1.4.1.2021.4.6',      #total RAM used
    '1.3.6.1.4.1.2021.9.1.8.1',  #Path where the disk is mounted
)
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
            )
        )
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                request = Request('URL',data=val.prettyPrint()) #send data
